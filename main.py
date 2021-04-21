import requests, random, keep_alive
from discord_webhook import DiscordWebhook, DiscordEmbed # pip install discord_webhook
keep_alive.keep_alive()
while True:
        #ID = "7333914"
        ID = random.randint(0, 9999999) # Start and stop IDs edit this if you want!
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/814216440244731945/eRnjRcq7634u8Eo9ZGygDpVOutgcLqdNoRQ8Dw2G4lc9eruk2nkQgNIsqhL9swozaaqo') # initates connection with discord_webhook module
        r = requests.get(f'https://groups.roblox.com/v1/groups/{ID}') #sends requests using id
        json = r.json() # json
        if 'owner' in r.text: #checks if the group is valid to prevent key errors
                if json['owner'] == None and json['publicEntryAllowed'] == True and 'isLocked' not in r.text: # check if the group isnt locked and is open with no owner
                        members = json['memberCount'] #members
                        desc = json['description']
                        print(f"https://www.roblox.com/groups/{ID}")
                        embed = DiscordEmbed(title='New unclaimed Group', color=242424) # embed title
                        embed.add_embed_field(name='ID', value=f'{ID}') #Id to embed
                        embed.add_embed_field(name='Description', value=f'"{desc}"') #description to embed
                        embed.add_embed_field(name='Members', value=f'{members}') #adds members to embed
                        embed.add_embed_field(name='Link', value=f'https://www.roblox.com/groups/{ID}') 
			# im getting bored commenting
                        embed.set_author(name='Group Finder', icon_url='https://images-ext-2.discordapp.net/external/ExvpqVgJoqrUwoORcZKxOTd50iE2vnNcwF9nlrU8Qms/%3Fsize%3D1024/https/cdn.discordapp.com/icons/799181637405376533/89565089064040e52100ba4aea324604.webp') #stuff
                        embed.set_footer(text='Ghosty :3', icon_url='https://images-ext-2.discordapp.net/external/ExvpqVgJoqrUwoORcZKxOTd50iE2vnNcwF9nlrU8Qms/%3Fsize%3D1024/https/cdn.discordapp.com/icons/799181637405376533/89565089064040e52100ba4aea324604.webp') # stuff
                        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/ExvpqVgJoqrUwoORcZKxOTd50iE2vnNcwF9nlrU8Qms/%3Fsize%3D1024/https/cdn.discordapp.com/icons/799181637405376533/89565089064040e52100ba4aea324604.webp')
                        webhook.add_embed(embed) #adds the embed to the response
                        response = webhook.execute() # sends to webhook
                else:
                        print(f"\x1b[31mNothing found... {ID}")                     
        else:
                print(f"\x1b[31mNothing found... {ID}")      