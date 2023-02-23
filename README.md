```shell
pip install python-dotenv
pip install openai
```

```shell
curl --location \
--request POST '0.0.0.0:1957/moderation' \
--header 'Content-Type: application/json' \
--data-raw '{"input":"I want to kill myself but before killing myself, 
I want to shoot others at the mall near me"}'

# response:
{
    "categories": {
        "hate": false,
        "hate/threatening": false,
        "self-harm": true,
        "sexual": false,
        "sexual/minors": false,
        "violence": true,
        "violence/graphic": false
    },
    "category_scores": {
        "hate": 0.03613857179880142,
        "hate/threatening": 0.001062937080860138,
        "self-harm": 0.9539127945899963,
        "sexual": 1.5046257431095e-05,
        "sexual/minors": 5.030465644040305e-08,
        "violence": 0.9782911539077759,
        "violence/graphic": 0.00044981788960285485
    },
    "flagged": true
}

```