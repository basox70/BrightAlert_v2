import discord
from discord.ext import commands, tasks
from discord.flags import Intents

import os

from selenium.webdriver import Chrome, Edge, Firefox, ChromiumEdge, Ie
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

from utils import config, mail
from utils.logger import logger

cfg = config.Config()
mail = mail.Mail(cfg)

botIntents = Intents.default()
botIntents.guilds = True
botIntents.messages = True
botIntents.reactions = True
botIntents.message_content = True
botIntents.members = True

client = discord.Client(command_prefix=cfg.prefix,
    description="BrightAlert_v2",
    intents=botIntents,)

driver = None

def login(email, password):
    global driver
    driver.get('https://uottawa.brightspace.com/d2l/home')
    time.sleep(5)
    email_input = driver.find_element(value="i0116")
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    time.sleep(2)
    password_input = driver.find_element(value="password_input")
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    start = time.time()
    time.sleep(4)
    while time.time() - start < 61:
        logger.debug(time.time()-start)
        try:
            driver.find_element(value="idSIButton9").click()
            break
        except:
            pass
        if (time.time() - start) > 59:
            logger.debug("condition = false now cuz why not")
            return False
    return True


def alert():
    time.sleep(2)
    x = True
    while x:
        try:
            pyautogui.click('bell.png')
            x = False
        except:
            pass
    l = True
    while l:
        coords = pyautogui.locateOnScreen('scan.png', confidence = 0.5)
        if coords != None:
            logger.debug(coords)
            pyautogui.screenshot('img/scanned_notifs.png', region = coords)
            l = False


@client.event
async def on_message(message):
    # Ignore if message is from a bot or himself
    if message.author == client.user or message.author.bot:
        return
    if "!setup" in message.content[0:6] and len(message.content.split()) == 3 :
        global driver
        driver = ChromiumEdge()
        splitted_message = message.content.split()
        username = splitted_message[1]
        password = splitted_message[2]
        cond = login(username, password)
        logger.debug(cond)

        if cond:
            alert()
            await message.channel.send(file=discord.File('img/scanned_notifs.png'))
            os.remove('img/scanned_notifs.png')

        elif not cond:
            await message.channel.send(f"{message.author.mention} You have not authenticated in time! Please restart the process.")

    elif "!setup" in message.content and len(message.content.split()) != 3:
        await message.channel.send("`!setup` needs email and password ")

if __name__ == "__main__":
    logger.info(f"discord.py version: {discord.__version__}")
    logger.debug('BrightAlert bot is running!!')
    client.run(cfg.token)
