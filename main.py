import discord
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import datetime
import time
#import requests
import pyautogui

token = 'ODA3NzA0MDYyMzg3OTQ1NTI0.YB73Bg.vbznQdeOwlfxLJBmdWKIFUa9Lj0'

client = discord.Client()

driver = webdriver.Chrome()

def login(email, password, condition):
	global driver
	driver.get('https://uottawa.brightspace.com/d2l/home')
	time.sleep(5)
	emailInput = driver.find_element_by_id("i0116")
	emailInput.send_keys(email)
	emailInput.send_keys(Keys.ENTER)
	time.sleep(5)
	passwordInput = driver.find_element_by_id("passwordInput")
	passwordInput.send_keys(password)
	time.sleep(2)
	passwordInput.send_keys(Keys.ENTER)
	start = time.time()
	time.sleep(4)
	while time.time() - start < 61:
		print(time.time()-start)
		try:
			driver.find_element_by_id("idSIButton9").click()
			break
		except:
			pass
		if (time.time() - start) > 59:
			condition = False
			print("condition = false now cuz why not")		
	return condition



	
def alert():
	global driver
	time.sleep(2)
	pyautogui.click('bell.png')
	coords = pyautogui.locateOnScreen('scan.png')
	pyautogui.screenshot('img/scan1.png', region = coords)





@client.event
async def on_message(message):
	server_id = client.get_guild(807703919768895529)
	if "!setup" in message.content and len(message.content.split()) == 3 :
		splitted_message = message.content.split()
		username = splitted_message[1]
		password = splitted_message[2]
		cond = True
		try:
			cond2 = login(username, password, cond)
			
		except:
			print("Something went wrong! Please restart the setup process.")
		alert()
	elif "!setup" not in message.content or len(message.content.split()) != 3 :
		message.channel.send("```The message format is incorrect```.")

	if cond2 == False:
		await message.channel.send(f"{message.author.mention} You have not authenticated in time! Please restart the process.")













print('BrightAlert bot is running!!')
client.run(token)