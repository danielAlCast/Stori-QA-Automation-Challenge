from selenium import webdriver
import time
# Using Chrome browser
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Download the ChromeDriver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# Going to the page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print("Site Tittle " + driver.title)
print("URL: " + driver.current_url)

# Radio Button by css, select radio 2,3,1
driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[value='radio3']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[value='radio1']").click()
time.sleep(2)


# Suggestion class, write Me and select Mexico

driver.find_element(By.XPATH, "//input[@placeholder='Type to Select Countries']").send_keys("Me")
time.sleep(2)

countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
# print(len(countries))   length of countries with Me
# Finding Mexico in countries
for country in countries:
    if country.text == "Mexico":
        country.click()
        break
time.sleep(2)


# Dropdown, select option 2 and then 3

dropdown = Select( driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
time.sleep(2)
# dropdown.select_by_visible_text("Option2")
dropdown.select_by_value("option2")
time.sleep(2)
dropdown.select_by_value("option3")
time.sleep(2)

# Checkboxes, select option 1 and 2

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
# print(len(checkboxes))

for checkbox in checkboxes:
    value = checkbox.get_attribute("value")
    if value == "option1" or value == "option2":
        checkbox.click()
        assert checkbox.is_selected()
time.sleep(2)

# Alert example, type Stori Card, click alert and then ok

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Stori Card")
driver.find_element(By.XPATH, "//input[@value='Alert']").click()
# Saving alert message
alert = driver.switch_to.alert
print('Alert message is: '+alert.text)
time.sleep(2)
alert.accept()

# Print if Element Displayed Example is hidden or shown

isShown = driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()

if isShown:
    print("The Element Displayed Example is shown")
else:
    print("The Element Displayed Example is hidden")

time.sleep(2)
driver.close()








