from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://support.hpe.com/hpsc/wc/public/home"
url_form_post = "https://support.hpe.com/hpsc/wc/public/find"

options = Options()
options.headless = True

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
driver.get(url)

#
# You add additional form fields with the id of
# serialNumber1, serialNumber2, serialNumber3, etc.
# You can send up to 20 serial numbers at a time.
#
# Please note that HPE has a rate-limit that requries reCAPTHCA
#
# send_keys() is the serial number of the device
#
driver.find_element(By.ID, "serialNumber0").send_keys("111111")
driver.find_element(By.NAME, "submitButton").click()
text_data = driver.find_element(By.CLASS_NAME, "hpui-standard-table").text

# Raw data that needs to be parsed.
print(text_data)
