from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("I am on the Basic Form page")
def openbrowser(context):
    context.options = webdriver.ChromeOptions()
    context.options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(options=context.options)
    context.driver.get("https://dineshvelhal.github.io/testautomation-playground/forms.html?")


@when("I interact with all the basic forms")
def basic_controls(context):
    context.driver.find_element(By.ID, "exp").send_keys("5")
    exp_help = context.driver.find_element(By.ID, 'exp_help')
    assert exp_help.get_attribute('innerHTML') == '5'

    checkbox_java = context.driver.find_element(By.ID, 'check_java')
    checkbox_java.click()
    checkbox_python = context.driver.find_element(By.ID, 'check_python')
    checkbox_python.click()
    checkbox_validate = context.driver.find_element(By.ID, 'check_validate')
    selected_values = ""
    if checkbox_java.is_selected():
        selected_values += checkbox_java.get_attribute('value') + " "
    if checkbox_python.is_selected():
        selected_values += checkbox_python.get_attribute('value') + " "

    assert checkbox_validate.get_attribute('innerHTML') == selected_values.strip()
    radio_button = context.driver.find_element(By.ID, 'rad_protractor')
    radio_button.click()
    if radio_button.is_selected():
        selected_value = radio_button.get_attribute('value')
        span_value = context.driver.find_element(By.ID, 'rad_validate').get_attribute('innerHTML')
        assert selected_value == span_value

    context.driver.find_element(By.ID, "select_tool")
    list_item = context.driver.find_element(By.CSS_SELECTOR, "#select_tool > option:nth-child(3)")
    list_item.click()
    if list_item.is_selected():
        selected_value = list_item.get_attribute("value")
        select_tool_validate = context.driver.find_element(By.ID, "select_tool_validate").get_attribute('innerHTML')
        assert selected_value == select_tool_validate

    select_lang = context.driver.find_element(By.ID, "select_lang")
    jv_lang = context.driver.find_element(By.XPATH, "//*[@id='select_lang']/option[1]")
    jv_lang.click()
    py_lang = context.driver.find_element(By.XPATH, "//*[@id='select_lang']/option[2]")
    py_lang.click()
    language_validate = context.driver.find_element(By.ID, "select_lang_validate").get_attribute('innerHTML').split(',')
    select_values = [option.get_attribute('value') for option in
                     select_lang.find_elements(By.CSS_SELECTOR, "option:checked")]

    assert set(language_validate) == set(select_values)

    text_value = context.driver.find_element(By.TAG_NAME, "textarea")
    text_value.send_keys("Common text Area")
    text_area = context.driver.find_element(By.ID, "area_notes_validate")
    expected_value = text_value.get_attribute('value')
    assert text_area.get_attribute('innerHTML') == expected_value
    common_sense = context.driver.find_element(By.ID, 'common_sense')
    print(common_sense.get_attribute('placeholder'))

    context.driver.find_element(By.XPATH, "//label[@for='german']").click()
    context.driver.find_element(By.XPATH, "//label[@for='german']").click()
    german_validate = context.driver.find_element(By.ID, "german_validate")
    print("Speaks German :", german_validate.text)

    range_input = context.driver.find_element(By.ID, 'fluency')
    context.driver.execute_script(
        "arguments[0].value = '4'; arguments[0].dispatchEvent(new Event('change'))",
        range_input)
    current_value = range_input.get_attribute('value')
    span_element = context.driver.find_element(By.ID, 'fluency_validate').get_attribute('innerHTML')
    assert span_element == current_value, f" value {span_element}, but got {current_value}"

    context.driver.execute_script("window.scrollBy(0, 700)")
    context.driver.find_element(By.ID, "upload_cv").send_keys('/Users/ankushsharma/Documents/Docfile.docx')
    file_input = context.driver.find_element(By.ID, 'upload_files')
    file_input.send_keys('/Users/ankushsharma/Downloads/Krebsregistermeldung_OncoAssist_20230228_1529.xml')
    file_input.send_keys('/Users/ankushsharma/Downloads/Krebsregistermeldung_OncoAssist_20230228_1528.xml')
    validate_files = context.driver.find_element(By.ID, 'validate_files')
    uploaded_files = validate_files.text
    assert 'Krebsregistermeldung_OncoAssist_20230228_1529.xml' in uploaded_files
    assert 'Krebsregistermeldung_OncoAssist_20230228_1528.xml' in uploaded_files

    salary = context.driver.find_element(By.ID, 'salary')
    assert salary.get_attribute('placeholder') == 'You should not provide this'


@then("I click Submit on Form with Validation Form")
def validation_form(context):
    submit_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    city_field = context.driver.find_element(By.ID, "validationCustom03")
    state_field = context.driver.find_element(By.ID, "validationCustom04")
    zip_field = context.driver.find_element(By.ID, "validationCustom05")
    terms_checkbox = context.driver.find_element(By.ID, "invalidCheck")
    submit_button.click()

    # check if any of the required fields is empty
    invalid_fields = context.driver.find_elements(By.XPATH, "//input[@required and @value='']")
    if len(invalid_fields) > 0:
        print("Please fill in all the required fields.")

    city_field.send_keys("Hamburg")
    print(f"City field entered: {city_field.get_attribute('value') or 'not entered'}")

    print(f"State field entered: {state_field.get_attribute('value') or 'not entered'}")

    zip_field.send_keys("22457")
    print(f"Zip field entered: {zip_field.get_attribute('value') or 'not entered'}")

    if terms_checkbox.is_selected():
        print("Terms and conditions checkbox is selected.")
    else:
        print("Terms and conditions checkbox is not selected.")

    submit_button.click()


@step("Non English label and locator")
def non_english(context):
    # Interact with non-English label
    input_field = context.driver.find_element(By.ID, 'नाव')
    input_field.send_keys("My Name is ")
    checkbox_marathi = context.driver.find_element(By.ID, "मराठी")
    checkbox_marathi.click()
    checkbox_guj = context.driver.find_element(By.ID, "ગુજરાતી")
    checkbox_guj.click()
    checkbox_pun = context.driver.find_element(By.ID, "ਪੰਜਾਬੀ")
    checkbox_pun.click()
    checkbox_lan = context.driver.find_element(By.ID, "check_validate_non_english")
    selected_values = " "
    if checkbox_marathi.is_selected():
        selected_values += checkbox_marathi.get_attribute('value') + " "
    if checkbox_guj.is_selected():
        selected_values += checkbox_guj.get_attribute('value') + " "
    if checkbox_pun.is_selected():
        selected_values += checkbox_pun.get_attribute('value') + " "

    assert checkbox_lan.get_attribute('innerHTML') == selected_values.strip()
