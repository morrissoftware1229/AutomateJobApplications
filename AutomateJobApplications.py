#Importing necessary modules
import os
import pyautogui as gui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

#Importing this because location bar won't clear out using clear()
from selenium.webdriver.common.keys import Keys

#Initial Selenium setup
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Get input from user
#searchForThisValue = input("Please enter what you would want to search for on Indeed.com")
#locationToSearchIn = input("Please enter the location you would like to check in")
#pathToResume = input("Please enter absolute path to resume")
#remoteOption = input("Please enter 1 for remote or 0 for in-person")
#print(remoteOption)

#Navigates to Indeed.com
driver.get("https://www.indeed.com/")

#Maximizes the window
driver.maximize_window()

#Adds user input to occupational search field
searchWhatBar = driver.find_element(value='text-input-what')
searchWhatBar.send_keys('Accountant')

#Adds user input to location search field
searchWhereBar = driver.find_element(value="text-input-where")
searchWhereBar.send_keys(Keys.CONTROL + "a")
searchWhereBar.send_keys(Keys.DELETE)
searchWhereBar.send_keys('United States')

#Presses enter button
enterButton = driver.find_element(By.XPATH, "//button[@type='submit']")
enterButton.click()

#Sets jobs to remote if indicated by user
#if(remoteOption == 1):
    #remoteButton = Select(driver.find_element("filter-remotejob"))
    #remoteButton.select_by_visible_text("Remote")
    #remoteOption = driver.find_element("filter-remotejob-0")
    #remoteOption.click()
    #enterRemoteButton = driver.find_element(By.XPATH, "//button[@type='submit']")
    #enterRemoteButton.click()

