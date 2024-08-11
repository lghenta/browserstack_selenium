import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def is_mobile(driver):
    """
    Checks if the current browser is a mobile platform based on its capabilities.
    """
    browser_name = driver.capabilities.get('browserName', '').lower()
    platform_name = driver.capabilities.get('platformName', '').lower()
    return 'mobile' in browser_name or 'android' in platform_name or browser_name == 'samsung'

def safe_click(driver, element):
    """
    Attempts to click an element safely using different methods if necessary.
    """
    try:
        # Tries a regular click
        element.click()
    except:
        try:
            # Tries a JavaScript click
            driver.execute_script("arguments[0].click();", element)
        except:
            try:
                # Tries an ActionChains click
                ActionChains(driver).move_to_element(element).click().perform()
            except Exception as e:
                print(f"Failed to click element: {str(e)}")
                raise

def login(driver, test_data):
    """
    Performs the login operation on the website.
    """
    print(f"Navigated to: {driver.current_url}")

    try:
        # Locates and enters the username
        username_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "react-select-2-input"))
        )
        print("Username dropdown found")
        ActionChains(driver).move_to_element(username_dropdown).click()\
            .send_keys(test_data['username']).send_keys(Keys.ENTER).perform()
        print(f"Username '{test_data['username']}' entered")

        # Locates and enters the password
        password_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "react-select-3-input"))
        )
        print("Password dropdown found")
        ActionChains(driver).move_to_element(password_dropdown).click()\
            .send_keys(test_data['password']).send_keys(Keys.ENTER).perform()
        print("Password entered")

        # Locates and clicks the login button
        if not locate_and_click_login_button(driver):
            raise Exception("Unable to locate or click login button")

        # Waits for login to complete by checking the presence of an element username
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "username"))
        )
        print("Login successful")
    except Exception as e:
        print(f"Login failed: {str(e)}")
        raise

def locate_and_click_login_button(driver):
    """
    Locates and clicks the login button on the login page.
    """
    print("Attempting to locate and click the login button")
    try:
        # Waits for the login form to be present
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
        )
        print("Login form found")

        # Tries to find the login button by ID and clicks it
        try:
            button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "login-btn"))
            )
            print("Login button found using selector: ID login-btn")
            safe_click(driver, button)
            print("Login button clicked")
            return True
        except:
            print("Failed to locate or click login button")
            return False

    except Exception as e:
        print(f"An error occurred while trying to locate and click login button: {str(e)}")
        return False

def favorite_galaxy_s20_plus(driver):
    """
    Locates and favorites the Galaxy S20+ product 
    """
    try:
        print("Looking for Galaxy S20+")
        galaxy_s20_plus = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "11"))
        )
        print("Galaxy S20+ product located")

        # Locates the favorite icon for the Galaxy S20+
        favorite_icon = WebDriverWait(galaxy_s20_plus, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="11"]/div[1]/button'))
        )
        print("Galaxy S20+ favorite button located")

        # Clicks the favorite icon
        safe_click(driver, favorite_icon)
        print("Galaxy S20+ has been favorited.")

    except Exception as e:
        print(f"Failed to favorite Galaxy S20+: {str(e)}")
        raise

def verify_galaxy_s20_plus_in_favorites(driver):
    """
    Verifies that the Galaxy S20+ is listed in the favorites 
    """
    try:
        # Clicks on the favorites button
        favorites_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "favourites"))
        )
        safe_click(driver, favorites_button)
        print("Navigated to favorites page")

        # Verifies that Galaxy S20+ is present in the favorites list
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="11" and @class="shelf-item"]'))
        )
        print("Galaxy S20+ is listed in the favorites.")
    except Exception as e:
        print(f"Failed to verify Galaxy S20+ in favorites: {str(e)}")
        raise

def test_bstackdemo(driver, test_data):
    """
    Runs the full test for logging in, favoriting a product, and verifying it.
    """
    driver.get(test_data['url'])

    try:
        # Performs login
        login(driver, test_data)

        # Selects the Samsung option
        samsung_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Samsung']"))
        )
        print("Samsung option found")
        safe_click(driver, samsung_option)
        print("Samsung option clicked")

        # Favorites Galaxy S20+ and verifies it in the favorites list
        favorite_galaxy_s20_plus(driver)
        verify_galaxy_s20_plus_in_favorites(driver)
        print("Test completed successfully!")

    except Exception as e:
        print(f"Current URL: {driver.current_url}")
        pytest.fail(f"Test failed: {str(e)}")
