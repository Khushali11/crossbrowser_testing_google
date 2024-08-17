from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Define a function to run the test on a specific browser
def run_google_search_test(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()  # or specify path: webdriver.Chrome(executable_path='path/to/chromedriver')
    elif browser_name == "firefox":
        driver = webdriver.Firefox()  # or specify path: webdriver.Firefox(executable_path='path/to/geckodriver')
    elif browser_name == "edge":
        driver = webdriver.Edge()  # or specify path: webdriver.Edge(executable_path='path/to/msedgedriver')
    else:
        raise ValueError("Unsupported browser!")

    # Open Google
    driver.get("https://www.google.com")

    # Ensure the page title is correct
    assert "Google" in driver.title

    # Find the search box element
    search_box = driver.find_element(By.NAME, "q")

    # Enter a search query
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(2)

    # Check that results are displayed
    assert "Selenium" in driver.title

    # Optionally, you can print the first result title
    first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
    print(f"{browser_name}: First result title is '{first_result.text}'")

    # Close the browser
    driver.quit()


# Run the test in Chrome, Firefox, and Edge
for browser in ["chrome", "firefox", "edge"]:
    run_google_search_test(browser)
