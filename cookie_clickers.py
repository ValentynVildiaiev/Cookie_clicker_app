from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path ="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
)
language_eng = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
language_eng.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@id='bigCookie']"))
)
cookies = driver.find_element(By.XPATH, "//*[contains(text(),'Got it!')]")


cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"
driver.implicitly_wait(1000)
cookie = driver.find_element(By.ID,cookie_id)
product_available = "product unlocked enabled"
achievment_close = "framed close sidenote"

while True:
    
    driver.implicitly_wait(10)
    cookie = driver.find_element(By.ID,cookie_id).click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",",""))
    print(cookies_count)
    
    for num in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(num)).text.replace(",", "")
    
        if not product_price.isdigit():
            continue
    
        product_price = int(product_price)

        if cookies_count >= product_price:
            try:
                product = driver.find_element(By.ID, product_prefix + str(num))
                product.click()
                break
            except Exception as e:
                print(f"Error clicking product: {e}")

