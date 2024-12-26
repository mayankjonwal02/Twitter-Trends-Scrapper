from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.common.exceptions import TimeoutException
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
import os
import zipfile
import time
import datetime
from DB.mongodb import add_trends
# ProxyMesh credentials
proxy_host = "us-ca.proxymesh.com"
proxy_port = 31280
proxy_username = "stark@33"
proxy_password = "8;X@Y4xaJ>^j;@p"
PROXY = f"http://{proxy_host}:{proxy_port}"

# Create a Proxy object
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = PROXY
proxy.ssl_proxy = PROXY
proxy.proxy_username = proxy_username
proxy.proxy_password = proxy_password

useragentarray = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
]

def get_trends():
    proxy_helper = SeleniumAuthenticatedProxy(proxy_url="http://{}:{}@{}:{}".format(proxy_username, proxy_password, proxy_host, proxy_port))
    options = webdriver.ChromeOptions()
    # adding argument to disable the AutomationControlled flag 
    options.add_argument("--disable-blink-features=AutomationControlled") 
    
    # exclude the collection of enable-automation switches 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    
    # turn-off userAutomationExtension 
    options.add_experimental_option("useAutomationExtension", False) 
    # proxy_helper.enrich_chrome_options(options)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    # for i in range(len(useragentarray)):
    #     # setting User Agent iteratively as Chrome 108 and 107
    #     driver.execute_cdp_cmd(
    #         "Network.setUserAgentOverride", {"userAgent": useragentarray[i]}
    #     )
    #     print(driver.execute_script("return navigator.userAgent;"))
    #     driver.get("https://httpbin.io/headers")
        # User credentials
    contact = '9625401776'  # Enter phone number, email, or username
    id = "jonwalmayank"
    password = 'mayjon1372'  # Enter password
    trends_json = {}

    



    try:
        # Open Twitter login page
        driver.get("https://www.google.com")
        # driver.get("https://x.com/i/flow/login")

        driver.maximize_window()
        time.sleep(10)
        driver.get("https://x.com/i/flow/login")
        time.sleep(5)
        # Perform login
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
        )
        email_input.send_keys(contact)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
        time.sleep(5)


        try:
            email_input_new = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
            )
            email_input_new.send_keys(contact)
            driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
            time.sleep(5)
        except TimeoutException:
            pass

        try:
            print("entered try loop")
            email_input_verify = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]'))
            )
            # email_input_verify = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]')
            if email_input_verify:
                print("email_input_verify exist in the page")
                email_input_verify.send_keys(id)
                time.sleep(5)
                driver.find_element(By.CSS_SELECTOR, 'button[data-testid="ocfEnterTextNextButton"]').click()
                time.sleep(5)
                password_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(By.CSS_SELECTOR, 'input[name="password"]')
                )
                password_input.send_keys(password)
                driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()
                time.sleep(5)
        except TimeoutException :
            print("email_input_verify does not exist in the page")

            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input'))
            )
            password_input.send_keys(password)
            driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred in try block : {e}")

        # Navigate to the trends page
        driver.get("https://x.com/explore/tabs/for-you")
        time.sleep(5)

        # Locate parent element
        parent_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Timeline: Explore"]'))
        )

        # Extract trends
        trends = []
        if parent_element:
            print("Parent element is present.")
            inner_elements = parent_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="cellInnerDiv"]')

            for inner_element in inner_elements[:5]:
                spans = inner_element.find_elements(By.TAG_NAME, 'span')
                if len(spans) > 1:  # Ensure the second span exists
                    trends.append(spans[1].text)
        else:
            print("Parent element is not present.")
            return trends_json

        # Add trends and timestamp to JSON
        for i, trend in enumerate(trends, start=1):
            trends_json[f"nameoftrend{i}"] = trend

        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        trends_json["date"] = current_date
        trends_json["time"] = current_time

    except Exception as e:
        print(f"An error occurred: {e}")
        return trends_json
    finally:
        driver.quit()

    return trends_json



