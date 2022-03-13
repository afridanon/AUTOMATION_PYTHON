#----------    RICHARD DANY    -----------#
#--------  Author :- SHAIK AFRID   -------# 
# ------    LANGUAGE :- PYTHON    --------#  
# ------  FRAMEWORK :- SELENIUM   --------#
# ------  USES :- WEB AUTOMATION  --------#
# --- DONT TRY TO STEEL MY CODE BITCH  ---# 

"""
Chrome Options For Browser Security
"""
import undetected_chromedriver as uc
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled");
options.add_argument("--disable-infobars");
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

"""

from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 10)
driver.maximize_window()
wait.until(EC.presence_of_element_located((By.XPATH, xpath_value))).send_keys(search_query)

"""