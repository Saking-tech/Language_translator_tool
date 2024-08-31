import openai
import time
apikey = "API_KEY"
# apikey = "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"
openai.organization = "org-49qwvNPbihsNA0wsH4N1acHi"
# openai.organization = "org-ryYSMabmTI392fgreFFbrH8k"
openai.api_key = apikey
model_engine = "gpt-4o-mini-2024-07-18"



time.sleep(3)
lang = "hindi"
text = "HI, I am a language translator tool"
prompt = f"Convert the \" {text} \" into {lang}"
response = openai.ChatCompletion.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[{
        "role":"user",
        "content": prompt}]
)
saves = response.choices[0].message.content
print(saves)
