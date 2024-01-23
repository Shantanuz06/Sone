import discord
import os
import openai
from keep_alive import keep_alive

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Set your Discord bot token and OpenAI API key
DISCORD_TOKEN = "MTE4NDUyMzQyMjUyMTM2NDYyMQ.GC99oD.Zl9y4DErH1aqWTGt3yV8_lODW7XLpDs1N2jjOE"
OPENAI_API_KEY = "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"
openai.api_key = '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'
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_message = message.content

    # Use OpenAI GPT-3 API to generate a response
    response = generate_openai_response(user_message)

    # Send the response back to the same channel
    await message.channel.send(response)

def generate_openai_response(user_message):
    # You can customize the prompt and other parameters based on your needs
    prompt = f"User: {user_message}\nBot:"

    # Call the OpenAI GPT-3 API to get a response
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose a different engine if needed
            prompt=prompt,
            max_tokens=100,  # Adjust the max_tokens parameter based on your desired response length
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the generated response from the API result
        generated_response = response['choices'][0]['text'].strip()

        return generated_response
    except Exception as e:
        return f"Error generating response: {str(e)}"
 
keep_alive()
client.run(DISCORD_TOKEN)
