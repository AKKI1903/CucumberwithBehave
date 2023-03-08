import re
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("I am on the Registration page")
def openbrowser(context):
    context.options = webdriver.ChromeOptions()
    context.options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(options=context.options)
    context.driver.get("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
    expected_url = "https://www.way2automation.com/way2auto_jquery/registration.php#load_box"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Error: expected URL {expected_url}, but got {actual_url}"


@when("I enter all the valid details")
def enter_details(context):
    driver = context.driver

    # Enter first name
    first_name = driver.find_element(By.NAME, "name")
    first_name.send_keys("Chandler")
    if first_name.get_attribute("value"):
        print("First Name entered:", first_name.get_attribute("value"))
    else:
        print("First Name not entered")

    # Enter last name
    driver.find_element(By.CSS_SELECTOR, "#register_form > fieldset:nth-child(1) > p:nth-child(2) > input[type=text]").send_keys("Bing")

    # Select marital status
    driver.find_element(By.XPATH, "//label[contains(text(),'Single')]/input").click()

    # Select hobbies
    hobby_checkbox = driver.find_element(By.XPATH, "//label[contains(text(),'Dance')]/input")
    hobby_checkbox.click()
    if hobby_checkbox.is_selected():
        print("CheckBox has value")
    else:
        print("No Checkbox is selected. Please select one of the checkbox")

    # Select country, birthdate and phone
    for i in range(1, 4):
        select_element = driver.find_element(By.XPATH, f"//*[@id='register_form']/fieldset[5]/div[{i}]/select")
        select_element.find_element(By.XPATH, "//option[2]").click()

    phone_field = driver.find_element(By.NAME, "phone")
    phone_number = "8234567991"
    if re.match("^[0-9]+$", phone_number):
        phone_field.send_keys(phone_number)
    else:
        print("Invalid phone number. Please enter only digits.")

    # Enter username and email
    driver.find_element(By.NAME, "username").send_keys("abc123")

    email_field = driver.find_element(By.NAME, "email")
    email = "Bing@test.com"
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        email_field.send_keys(email)
    else:
        print("Invalid Email")

    # Upload photo
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys('/Users/ankushsharma/Downloads/photo.jpeg')

    # Enter about yourself
    driver.find_element(By.TAG_NAME, "textarea").send_keys("They not only help teams continually improve the quality of the software they create, but they also help teams do it more effectively.")

    # Enter password and confirm password
    password = "Abcd@123"
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password_field.get_attribute('value')):
        print("password does not meet requirement")

    c_password = driver.find_element(By.NAME, "c_password")
    c_password.send_keys(password)
    if password == c_password.get_attribute('value'):
        print("Password Matched")
    else:
        print("Password does not match")


@then("I click on Submit")
def submit(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
