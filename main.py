import openai
import os
from dotenv import load_dotenv

# Load .env variables (optional, but helpful)
load_dotenv()

# Set your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Define the prompt
prompt = "Tell me a story about a boy in a castle"

# Send the request
response = client.chat.completions.create(
    model="gpt-4.1",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.8,
    max_tokens=500
)

# Extract and print the story
story = response.choices[0].message.content
print(story)