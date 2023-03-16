# visit https://beta.openai.com/ to get your own key
import openai
# My OpenAI Key
openai.api_key = "OPENAI_API_KEY"

response = openai.Completion.create(
  engine="davinci",
  prompt="人类如何才能开启太空旅行的时代呀？",
  max_tokens=500
)

print(response.choices[0].text)