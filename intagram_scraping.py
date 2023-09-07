import  instaloader
from requests import get
from json import loads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





driver = webdriver.Chrome()  # NOTE: FIREFOX EXAMPLE
driver.get("http://www.instagram.com")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
username.send_keys("Username")

password.clear()
password.send_keys("[password]")

Login_button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

profile_name ="anime"
instaloader.Instaloader().download_profile(profile_name,profile_pic_only=False)

url = 'https://instagram.com/<anime>'

params = { '__a': 1, '__d': 1 }

cookies = { 'sessionid': '<anime>' }


def on_success(response):
    profile_data_json = response.text
    parsed_data = loads(profile_data_json)

    print('User fullname:', parsed_data['graphql']['user']['full_name'])
    print('User bio:', parsed_data['graphql']['user']['biography'])



def on_error(response):
    # Printing the error if something went wrong
    print('Something went wrong')
    print('Error Code:', response.status_code)
    print('Reason:', response.reason)

response = get(url, params, cookies=cookies)

if response.status_code == 200:
    on_success(response)
else:
    on_error(response)



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Selenium webdriver
driver = webdriver.Chrome(executable_path='path_to_chrome.exe')  # Replace with the path to your Chrome webdriver executable

# Open Instagram and navigate to a specific post
post_url = 'https://www.instagram.com/p/anime/'
driver.get('anime')

# Wait for the page to load (you might need to adjust the sleep duration)
time.sleep(5)

# Scrape post views
try:
    post_views_element = driver.find_element(By.XPATH, '//span[@class="vcOH2"]/span')
    post_views = post_views_element.text
    print(f'Post Views: {post_views}')
except Exception as e:
    print('Unable to scrape post views:', e)

# Scrape hashtags
try:
    hashtags_elements = driver.find_elements(By.XPATH, '//a[@class="xil3i"]')
    hashtags = [element.text for element in hashtags_elements]
    print('Hashtags:', hashtags)
except Exception as e:
    print('Unable to scrape hashtags:', e)

# Close the browser
driver.quit()
