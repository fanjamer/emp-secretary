import discord
import asyncio

client = discord.Client()

prefix = "~"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='under development'))
    #await client.send_message(client.get_channel('175398479152021504'), 'EMP Secratary Ready to Work!') #this is the general chat
    await client.send_message(client.get_channel('321057345906147330'), 'DEBUG_TO_CODING_CHAT: EMP Secratary Ready to Work!') #this is the coding chat

@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith(prefix + 'sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith(prefix + 'admintest'):
    	for role in message.author.roles:
	    	if role.permissions.administrator:
	    		await client.send_message(message.channel, 'Success!')
	elif message.content.startswith(prefix + 'upgrade'):
		#CONTINUE HERE!!!

@client.event
async def on_member_join(member):
	newmem = member
	for server in client.servers:
		roles = server.roles
	for role in roles:
		if role.name == 'New Members':
			await client.add_roles(newmem, role)
	if member.top_role.name == "@everyone":
		#await client.send_message(client.get_channel('175398479152021504'), 'User ' + str(member) + ' has joined! Assigning New Member role.')
		await client.send_message(client.get_channel('321057345906147330'), 'User @' + str(member) + ' has joined! Assigning New Member role.')
		#await client.add_roles(member, roleToGive) #<@&>

client.run('MzIxMDUyMzYxMTc3MDM4ODU4.DBYfhA.LpH11j8CbOIZR810EHRigbf60JA')