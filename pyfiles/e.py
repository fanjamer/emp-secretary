import discord
import asyncio

client = discord.Client()

versionNum = '0.8.29 [HOTFIX 1]'

prefix = "~"

requested = False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='under development'))
    #await client.send_message(client.get_channel('175398479152021504'), 'EMP Secratary Ready to Work!') #this is the general chat
    await client.send_message(client.get_channel('321057345906147330'), 'EMP Secratary Version ' + versionNum + ' Ready to Work!') #this is the coding chat

@client.event
async def on_message(message):
	roleFound=False
	if message.content.startswith(prefix + 'gaming'):
		roleFound=False
		roles = message.author.roles
		for role in roles:
			if role.name == 'Member':
				roleFound = True
		if roleFound:
			await client.send_message(message.channel, 'You have been upgraded: you now have the \'Player\' Role.')
			await client.add_roles(message.author, discord.utils.get(message.server.roles, name='Player'))
			await client.send_message(discord.utils.get(message.server.channels, id='291009126262374400'), message.author.mention + ' has been given the role: \'Player.\'')
	elif message.content == prefix + 'dj' and len(message.content) == 3:
		roleFound=False
		roles = message.author.roles
		for role in roles:
			if role.name == 'Member':
				roleFound = True
		if roleFound:
			await client.send_message(message.channel, 'You have requested the \'DJ\' Role. Server administrators will review your request.')
			await client.add_roles(message.author, discord.utils.get(message.server.roles, name='MRequest'))
			await client.send_message(discord.utils.get(message.server.channels, id='291009126262374400'), message.author.mention + ' has requested the role: \'DJ.\'')
			await client.send_message(discord.utils.get(message.server.channels, id='321045061888638976'), message.author.mention + ' has requested the role: \'DJ.\'' + \
				'\nTo accept this request, type ' + \
				'\'~djaccept <@mention>.\'\nTo deny ' + \
				'this request, type \'~djdeny <@mention>.\'')
	elif message.content.startswith(prefix + 'djaccept'):
		roleFound=False
		requested=False
		roles = message.author.roles
		for role in roles:
			if role.permissions.administrator:
				roleFound = True
		if roleFound:
			mentions = message.mentions
			roles = mentions[0].roles
			for role in roles:
				if role.name == 'MRequest':
					requested = True
					await client.remove_roles(mentions[0], role)
			if requested:
				await client.add_roles(mentions[0], discord.utils.get(mentions[0].server.roles, name='DJ'))
				await client.send_message(mentions[0], 'You have been given the role \'DJ\' on EMP.')
				await client.send_message(message.channel, str(mentions[0]) + ' Has been given \'DJ.\'')
	elif message.content.startswith(prefix + 'djdeny'):
		roleFound=False
		roles = message.author.roles
		for role in roles:
			if role.permissions.administrator:
				roleFound = True
		if roleFound:
			content = message.content
			content = content.split()
			contentLen = len(content) - 1
			mentions = message.mentions
			if contentLen >= 1 and contentLen <= 2:
				if contentLen == 1:
					roles = mentions[0].roles
					for role in roles:
						if role.name == 'MRequest':
							await client.remove_roles(mentions[0], role)
							await client.send_message(mentions[0], 'Your \'DJ\' request was denied on EMP.')
							await client.send_message(message.channel, 'DJ Request Denied.')

@client.event
async def on_member_join(member):
	await client.send_message(client.get_channel('321057345906147330'), 'User ' + member.mention + ' has joined! Welcome to The EMP Server!')

@client.event
async def on_member_update(before, after):
	try:
		if after.game.name == 'Overwatch':
			try:
				if before.game.name == 'Overwatch':
					print('nongame change member update ' + after)
			except AttributeError:
				await client.send_message(discord.utils.get(after.server.channels, id='303366926820835328'), after.mention + ' is playing Overwatch! :white_check_mark:')
	except AttributeError:
		print('non overwatch change')

	try:
		if after.game.name == 'League of Legends':
			try:
				if before.game.name == 'League of Legends':
					print('nongame change member update ' + after)
			except AttributeError:
				await client.send_message(discord.utils.get(after.server.channels, id='303606238157996033'), after.mention + ' is playing League of Legends! :white_check_mark:')
	except AttributeError:
		print('non league change')

	try:
		if before.nick != after.nick:
			await client.send_message(discord.utils.get(after.server.channels, id='291009126262374400'), before.nick + ' is now known as ' + after.mention + '.')
	except AttributeError:
		print('non nickname change')

client.run('MzIxMDUyMzYxMTc3MDM4ODU4.DBYfhA.LpH11j8CbOIZR810EHRigbf60JA')