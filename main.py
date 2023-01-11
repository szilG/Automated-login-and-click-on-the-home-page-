from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_driver():
  # Set option to make browsing easier
  # create options using webdriver.ChromeOptions
  options = webdriver.ChromeOptions()
  # infobar may interfere with the script so disable it
  options.add_argument("disable-infobars")
  # start the browser as maximized.
  options.add_argument("start-maximized")
  # to avoid some issues that occur when you interact with a browser on a Linux computer
  options.add_argument("disable-dev-shm-usage")
  # disable browser security
  options.add_argument("no-sandbox")
  # to help selenium to avoid detection from the browser
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  

print(main())