import os
import json
import openai
openai.organization = ORG_KEY
openai.api_key = API_KEY
models = openai.Model.list()
jsons = json.loads(str(models))
for i in range(len(jsons['data'])):
    print(jsons['data'][i]['id'])
input()
