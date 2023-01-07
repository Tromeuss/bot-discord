import discord


@bot.event
async def on_ready():
    print("ready !")

client = discord.Client()
COMMAND_PREFIX = "!"
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Traitez la commande envoyée par l'utilisateur ici
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content.startswith(COMMAND_PREFIX):
        return
    # Traitez la commande envoyée par l'utilisateur ici
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content.startswith(COMMAND_PREFIX):
        return
    command_and_args = message.content[len(COMMAND_PREFIX):].split(" ")
    command = command_and_args[0]
    args = command_and_args[1:]
    # Traitez la commande et les arguments ici
import requests

def send_request_to_my_api(command, args):
    api_url = "https://api.openai.com/v1/images/generations"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer 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"}
    data = '{"model": "image-alpha-001", "prompt": "' + command + ' ' + ' '.join(args) + '", "num_images":1, "size":"1024x1024", "response_format":"url"}'
    response = requests.post(api_url, headers=headers, data=data)
    return response.json()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content.startswith(COMMAND_PREFIX):
        return
    command_and_args = message.content[len(COMMAND_PREFIX):].split(" ")
    command = command_and_args[0]
    args = command_and_args[1:]
    api_response = send_request_to_my_api(command, args)
    if "data" in api_response:
        image_url = api_response["data"][0]["url"]
        image_data = requests.get(image_url).content
        channel = client.get_channel(GRXvmjnX)
        await channel.send_file(io.BytesIO(image_data), filename="image.jpg")



bot.run("MTA2MTQyNDUzNzQ3ODEyMzY3MQ.G_Hck9.VWxDhO3TLRV_JQowq9E9nIQBBEPxeXbHMIrXXk")