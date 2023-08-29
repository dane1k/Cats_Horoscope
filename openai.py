import openai
import os
import sys

# API KEY
openai.api_key = os.environ.get('BOT_TELEGRAM_TOKEN_FOR_CODE', 'nothing')
if openai.api_key == 'nothing':
    sys.exit("API Key not accept")

# preporation for getting answers
prompt = "Can u make the funny forecast of zodiac signs in cat style with cat's emoji?"
response = openai.Completion.create(
    engine="davinci",  # model
    prompt=prompt,
    max_tokens=100  # max cound of tokens
)

# print request to chatpgt
generated_code = response.choices[0].text.strip()
print(generated_code)
