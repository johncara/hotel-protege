import openai
import os
import json
from dotenv import load_dotenv

# Load .env variables (optional, but helpful)
load_dotenv()

# Set your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Read the prompt
script_dir = os.path.dirname(os.path.abspath(__file__))
prompt_path = os.path.join(script_dir, 'prompt.json')
with open(prompt_path, 'r') as file:
    prompts = json.load(file)
prompt = prompts["story_prompt"]

# Send the request
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.8,
    max_tokens=500
)

# Extract and print the story
story = response.choices[0].message.content
print(story)