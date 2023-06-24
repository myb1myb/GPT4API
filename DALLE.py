import openai
openai.organization = ORG_KEY
openai.api_key = API_KEY
prompt = input("Introduction:")
response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
)
print(response)
image_url = response['data'][0]['url']
print(image_url)
