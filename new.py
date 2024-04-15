import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_optinons = webdriver.ChromeOptions()
# Создание экземпляра веб-драйвера
chrome_optinons.add_argument('--headless')
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_optinons)
wait = WebDriverWait(driver, 10, poll_frequency=1)


# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

# Клик на кнопку, которая вызывает alert
BUTTON_1 = (By.XPATH, "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
time.sleep(3)

# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())
time.sleep(3)
# Переключение на alert
driver.switch_to.alert
time.sleep(3)