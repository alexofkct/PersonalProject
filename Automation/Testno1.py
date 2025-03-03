from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pi
import os
import discord
from dotenv import load_dotenv
trigger=1
#driver location
Chromedriver_location='C:\\Users\\Rithik Sarvesh B\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python38\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe'
#URLs
Login_site='https://www.mycamu.co.in'
Timetable_site='https://www.mycamu.co.in/#/home/feed/timetable'
#Xpaths
username_xpath="//input[@name='username']"
password_xpath="//input[@name='password']"
Login_button_xpath='//*[@id="login_tab"]/div[1]/form/div[3]/button'
Timetable_xpath='//*[@id="Timetable"]'
Timetabl_xpath='//*[@id="Timetable"]/a/span[1]'
First_online_class='//*[@id="tdy_schdl"]/div[1]/div[5]/div[2]/a'
nline_class='//*[@id="tdy_schdl"]/div[1]/div[4]/div[2]/a'
#Alternatives
line_class="Attend Online Class"
#Login credentials
username='' #Enter the username here
password='' #Enter the password
#Channel ID
channel_id=  #Enter the Discord channel ID here
#Here comes the cool guy, Discord!
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')
client=discord.Client()
#Hail Selenium!
browser=webdriver.Chrome(Chromedriver_location)
browser.implicitly_wait(5)
browser.get(Login_site)
browser.maximize_window()
#Login
browser.find_element_by_xpath(username_xpath).send_keys(username)
browser.find_element_by_xpath(password_xpath).send_keys(password)
print("About to click Login")
browser.find_element_by_xpath(Login_button_xpath).click()
print("Logged in Successfully")
#Timetable
browser.implicitly_wait(5)
try:
    browser.find_element_by_xpath(Timetable_xpath).click()
finally:
    browser.find_element_by_xpath(Timetabl_xpath).click()
print("Hurray, We entered the timetable section")
'''
browser.get(Timetable_site) '''
try:
    Online_class=browser.find_element_by_xpath(First_online_class)
finally:
    Online_class=browser.find_element_by_link_text(line_class)
Online_class.click()
time.sleep(5)
#Redirecting to Microsoft Team call
pi.click(x=1164,y=334)
time.sleep(5)
pi.click(x=1578,y=908)
trigger=0
print("Voila! You are in, Sir")
@client.event
async def on_ready():
    if trigger==0:
        await client.get_channel(883618108424736782).send('Boss, I sneaked through your class in disguise. Have fun there!')
    else:
        await client.get_channel(channel_id).send('Boss, Sups here! We have a problem. I didnt make it. We need you ASAP')
client.run(TOKEN)
browser.quit()



