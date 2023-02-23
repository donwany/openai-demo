import openai
from dotenv import dotenv_values
from flask import Flask, request, jsonify

config = dotenv_values(".env")

app = Flask(__name__)
openai.api_key = config['OPENAI_API_KEY']

# print(openai.Model.list())

model_name = "text-davinci-003"


def generate_response(prompt, model):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.6
    )
    return response.choices[0].text.strip()


def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url


def moderation(prompt):
    response = openai.Moderation.create(input=prompt)
    output = response["results"][0]
    return output


@app.route("/generate-text", methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']
    response = generate_response(prompt, model=model_name)
    return jsonify({"response": response})


@app.route("/generate-image", methods=['POST'])
def gen_image():
    data = request.get_json()
    prompt = data['prompt']
    response = generate_image(prompt)
    return jsonify({"response": response})


@app.route("/moderation", methods=['POST'])
def mode_api():
    data = request.get_json()
    results = moderation(data['input'])
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1957)
