#Importing necessary modules
import os
import pyautogui as gui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

#Importing this because location bar won't clear out using clear()
from selenium.webdriver.common.keys import Keys

#Initial Selenium setup
options = Options()
options.add_experimental_option("detach", True)
#This will need to be updated for different users
options.add_argument("user-data-dir=C:\\Users\\morri\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Get input from user
#searchForThisValue = input("Please enter what you would want to search for on Indeed.com")
#locationToSearchIn = input("Please enter the location you would like to check in")
#pathToResume = input("Please enter absolute path to resume")
#remoteOption = input("Please enter 1 for remote or 0 for in-person")

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

#Signs into account
if(len(driver.find_elements(By.XPATH, "//a[contains(@href, 'https://secure.indeed.com/account/login')]")) > 0):
    signIn = driver.find_element(By.XPATH, "//a[contains(@href, 'https://secure.indeed.com/account/login')]")
    signIn.click()
    signIn.send_keys(Keys.SHIFT + Keys.TAB)
    signIn.send_keys(Keys.SHIFT + Keys.TAB)
    signIn.send_keys(Keys.SHIFT + Keys.TAB)
    signIn.send_keys(Keys.ENTER)

#Sets jobs to remote if indicated by user
remoteButton = driver.find_element(value="filter-remotejob")
remoteButton.click()
driver.implicitly_wait(2)
if(len(driver.find_elements(By.XPATH, "//a[@class='yosegi-FilterPill-dropdownListItemLink']")) > 0):
    action = ActionChains(driver)
    action.send_keys(Keys.ARROW_DOWN)
    action.send_keys(Keys.ENTER)
    action.perform()
else:
    remoteOption = driver.find_element(By.XPATH, "//label[@for='filter-remotejob-0']")
    remoteOption.click()
    enterRemoteButton = driver.find_element(By.XPATH, "//button[@form='filter-remotejob-menu']")
    enterRemoteButton.click()


#Filters by date
dateFilter = driver.find_element(By.XPATH, "//div[@class='jobsearch-DesktopSort']//span//a")
dateFilter.click()

#Selects first job
currentJobSelection = driver.find_element(By.XPATH, "//div[@class='job_seen_beacon']")
currentJobSelection.click()
driver.implicitly_wait(2)

#Stores information from position
jobDescription = driver.find_element(By.XPATH, "//div[@id='jobDescriptionText']")

#Clicks apply now button
driver.implicitly_wait(2)
indeedApplyButton = driver.find_element(By.XPATH, "//button[@id='indeedApplyButton']")
indeedApplyButton.click()

#ISSUE - Multiple tabs are opening when clicking apply now button

#Clicks the submit application button
submitApplicationButton = driver.find_elements(By.XPATH, "//button[@class='ia-continueButton']")
submitApplicationButton.click()