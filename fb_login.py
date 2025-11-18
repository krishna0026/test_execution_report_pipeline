from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def get_facebook_title():

    chrome_options = Options()
    chrome_options.add_argument("--headless")               # RUN HEADLESS is necessary for using selenium using git
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")


    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    title= driver.title
    driver.quit()
    return title

# print('Title: ', get_facebook_title() )
# This is to just check cod eis working fine or not