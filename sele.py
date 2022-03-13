
#----------    RICHARD DANY    -----------#
#--------  Author :- SHAIK AFRID   -------# 
# ------    LANGUAGE :- PYTHON    --------#  
# ------  FRAMEWORK :- SELENIUM   --------#
# ------  USES :- WEB AUTOMATION  --------#
# --- DONT TRY TO STEEL MY CODE BITCH  ---# 
import undetected_chromedriver as uc   #PACKAGE
from selenium.webdriver.common.keys import Keys
import time  # FOR SLEEP   
from op import options  #IMPORT OPTIONS FROM ANOTHER FILE  
from securepass import INSTA_PASSWORD, INSTA_USERNAME   #SECURE PASSWORD WITH YOUR BLODDY TALENT
from securepass import FB_USERNAME,FB_PASSWORD  #IMPORT USERNAME AND PASSWORD
from user_name import INSTA_USERNAME     #IMPORT USERNAME
driver = uc.Chrome(options=options) #chrome
driver.get("https://www.instagram.com/") # LOAD WEBSITE
time.sleep(7)
USER_NAME = driver.find_element_by_name("username") #FIND USERNAME  INPUT FIELD
PASS_WORD = driver.find_element_by_name("password") #FIND PASSWORD INPUT FIELD
USER_NAME.send_keys(INSTA_USERNAME+"dany_") #SEND INSTA USERNAME
PASS_WORD.send_keys(INSTA_PASSWORD+"d") #SEND INSTA PASSWORD
# SUBMIT BUTTON For LOGGING IN
SUBMIT_BUTTON = driver.find_element_by_xpath("//button[@class = 'sqdOP  L3NKy   y3zKF     '][@type='submit'] ") 
SUBMIT_BUTTON.click()
time.sleep(5)
try:    # TRY FOR EXCEPTION ERROR
    # FIRST NOT NOW BUTTON
    NOT_NOW = driver.find_element_by_xpath("//button[@class = 'sqdOP yWX7d    y3zKF     '][@type='button']")
    NOT_NOW.click()
    time.sleep(5)
    # SECOND NOT NOW BUTTON
    NOT_NOW1 = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm '][@tabindex ='0']")
    NOT_NOW1.click()
    time.sleep(2)
    # SEARCH ID FOR MESSAGE
    SEARCH_BOX = driver.find_element_by_xpath("//input[@aria-label='Search Input'][@autocapitalize='none'][@class='XTCLo  d_djL  DljaH '][@placeholder='Search'][@type='text']")
    time.sleep(2)
    SEARCH_BOX.send_keys(INSTA_USERNAME)
    time.sleep(3)
    # DOUBLE ENTER FOR FIND
    SEARCH_BOX.send_keys(Keys.RETURN)
    SEARCH_BOX.send_keys(Keys.RETURN)
    time.sleep(2)
    # CLICK ON MESSAGE BUTTON
    MESSAGE_BUTTON = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    '][@type='button']").click()
    time.sleep(5)
    # MESSAGE INPUT BOX TYPE MSG
    MESSAGE_INPUTTEXT = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    time.sleep(2)
    MESSAGE_INPUTTEXT.send_keys("HEY I AM RICHARD !")
    time.sleep(2)
    MESSAGE_INPUTTEXT.send_keys(Keys.RETURN)


except:   # EXCEPT EXCEPTION FOR ERROR
    time.sleep(5)
    """

    NEED THIS CODE FOR
    FUCKING INTELLIGENCE FOR INSTAGRAM CODE 

    """
    FB_EMAIL = driver.find_element_by_id("email")    # FIND USERNAME TEXT FIELD
    FB_PASS = driver.find_element_by_id("pass")      # FIND PASSWORD TEXT FIELD
    FB_EMAIL.send_keys(FB_USERNAME)
    FB_PASS.send_keys(FB_PASSWORD)
    time.sleep(3)
    driver.find_element_by_id("loginbutton").click()
    time.sleep(5)
    # FIRST NOT NOW BUTTON
    NOT_NOW = driver.find_element_by_xpath("//button[@class = 'sqdOP yWX7d    y3zKF     '][@type='button']")
    NOT_NOW.click()
    time.sleep(5)
    # SECOND NOT NOW BUTTON
    NOT_NOW1 = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm '][@tabindex ='0']")
    NOT_NOW1.click()
    time.sleep(2)
    # SEARCH ID FOR MESSAGE
    SEARCH_BOX = driver.find_element_by_xpath("//input[@aria-label='Search Input'][@autocapitalize='none'][@class='XTCLo  d_djL  DljaH '][@placeholder='Search'][@type='text']")
    time.sleep(2)
    SEARCH_BOX.send_keys(INSTA_USERNAME)
    time.sleep(3)
    # DOUBLE ENTER FOR FIND
    SEARCH_BOX.send_keys(Keys.RETURN)
    SEARCH_BOX.send_keys(Keys.RETURN)
    time.sleep(2)
    # CLICK ON MESSAGE BUTTON
    MESSAGE_BUTTON = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    '][@type='button']").click()
    time.sleep(5)
    # MESSAGE INPUT BOX TYPE MSG
    MESSAGE_INPUTTEXT = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    time.sleep(2)
    # MESSAGE WHAT YOU WANT SEND
    MESSAGE_INPUTTEXT.send_keys("HEY I AM RICHARD !")
    time.sleep(2)
    # KEYBOARD ENTER KEY PRESS WITH THIS FUCKING CODE
    MESSAGE_INPUTTEXT.send_keys(Keys.RETURN)
