import twitchio
from twitchio.ext import commands
import asyncio
import serial
import time
import re
import random
 
from threading import Semaphore


#enter access token here
#add custom cheer emote to list on line 37
access = ''
 



class Bot(commands.Bot):
 
    sema = Semaphore(1)
 
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        self.lock = asyncio.Lock()
        super().__init__(token=access, prefix='?', initial_channels=['keith282'])
 
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
 
    async def event_message(self, message):
        cheer_beginning = ['cheer', 'biblethump', 'cheerwhal', 'corgo', 'uni', 'showlove', 'party', 'seemsgood', 'pride', 'kappa', 'frankerz', 'heyguys', 'dansgame', 'elegiggle', 'trihard', 'kreygasm', '4head', 'swiftrage', 'notlikethis', 'failfish', 'vohiyo', 'pjsalt', 'mrdestructoid', 'bday', 'ripcheer', 'shamrock']

        #get the bit donations, and add up the amount of bits donated in the message
        words = message.content.lower()
        words = words.replace('\n', ' ')
        while("  " in words):
            words = words.replace("  ", " ")
        words = words.split(' ')
        cheer = 0
        for word in words:
            word_no_numbers = re.sub(r'\d+', '', word)
            if word_no_numbers in cheer_beginning:

                number_from_word = re.findall(r'\d+', word)
                if(len(number_from_word) == 0):
                    continue
                cheer_amount += int(number_from_word[0]) 
 
        await self.bitsDonated(cheer)
 
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