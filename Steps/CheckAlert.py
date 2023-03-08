from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("I am on the Alert page")
def openbrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.way2automation.com/way2auto_jquery/alert.php#load_box")


@then("I Click on the Alert Button")
def accept_alert(context):
    # Switch to Frame
    context.driver.switch_to.frame(context.driver.find_element(By.CSS_SELECTOR, ".demo-frame"))
    context.driver.find_element(By.CSS_SELECTOR, "body > button").click()
    # interact with alert window and close alert
    context.driver.switch_to.alert.accept()

