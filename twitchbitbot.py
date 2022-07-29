import twitchio
from twitchio.ext import commands
import asyncio
import serial
import time
import re
import random
 
from threading import Semaphore


#enter access token here
#modify custom emote on line 43
access = 'twitch_access_token'
 



class Bot(commands.Bot):
 
    sema = Semaphore(1)
 
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        self.lock = asyncio.Lock()
        super().__init__(token=access, prefix='?', initial_channels=['your_channel'])
 
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
 
    async def event_message(self, message):
        #this is called when a message is sent to the channel
        
        #get the bit donations, and add up the amount of bits donated in the message
        words = message.content.lower()
        m = sum([int(j) for i in re.finditer(r'\bcheer(\d+)\b', words) for j in i.groups() if j is not None])

        custom_emote = "usercheer"
        m += sum([int(j) for i in re.finditer(r'\b' + custom_emote + r'(\d+)\b', words) for j in i.groups() if j is not None])

        m += sum([int(j) for i in re.finditer(r'\bbiblethump(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bcheerwhal(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bcorgo(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\buni(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bshowlove(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bparty(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bseemsgood(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bpride(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bkappa(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bfrankerz(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bheyguys(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bdansgame(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\belegiggle(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\btrihard(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bkreygasm(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\b4head(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bswiftrage(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bnotlikethis(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bfailfish(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bvohiyo(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bpjsalt(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bmrdestructoid(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bbday(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bripcheer(\d+)\b', words) for j in i.groups() if j is not None])
        m += sum([int(j) for i in re.finditer(r'\bshamrock(\d+)\b', words) for j in i.groups() if j is not None])

        #send to function that does things on bit donations
        await self.bitsDonated(m)
 
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)
 
    async def bitsDonated(self, amount):
        cheer = amount
        if cheer < 1:
            return
        print(cheer)
 
        self.sema.acquire()
        try:
            if(cheer > 0):
                #do what you want here
                #cheer contains the number of bits donated
                #semaphore is used so that everything here is thread safe e.g. you can write to a COM port without issues
                pass
        finally:
            self.sema.release()
 
 
bot = Bot()
bot.run()