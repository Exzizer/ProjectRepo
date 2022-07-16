def selenium_test(user_id):
    from selenium import webdriver

    # Windows:
    from selenium.common import NoSuchElementException
    from selenium.webdriver import Keys
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome(executable_path="C:\\Users\\popov\\Downloads\\chromedriver_win32\\ChromeDriver.exe")

    driver.get("http://127.0.0.1:5001/users/get_user_data/"+user_id)

    try:
        element = driver.find_element(By.ID,'user')
        result = element.text
    except NoSuchElementException:
        element = driver.find_element(By.ID, 'error')
        result = element.text

    driver.quit()

    return result


selenium_test("19")
