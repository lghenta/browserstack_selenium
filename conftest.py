import os
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def load_config():
    """
    Loads the configuration from 'config.yml' and overrides with environment variables if available.
    """
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Overrides credentials with environment variables if they exist
    config['browserstack']['username'] = os.environ.get(
        'BROWSERSTACK_USERNAME', config['browserstack']['username']
    )
    config['browserstack']['access_key'] = os.environ.get(
        'BROWSERSTACK_ACCESS_KEY', config['browserstack']['access_key']
    )
    
    return config

# Loads the configuration at module level so it's available for all fixtures
config = load_config()

@pytest.fixture(params=config['capabilities'])
def driver(request):
    """
    Pytest fixture  initializes and yields a Selenium WebDriver instance based on the provided capabilities.
    This fixture is parameterized to run tests across different capability sets defined in the configuration.
    """
    # Retrieves the current set of capabilities for this test iteration
    caps = request.param.copy()  # Uses copy to avoid mutating the original capabilities

    # Adds BrowserStack credentials to capabilities
    caps['browserstack.user'] = config['browserstack']['username']
    caps['browserstack.key'] = config['browserstack']['access_key']

    # Determines the appropriate WebDriver options based on the browser or device specified
    if 'device' in caps:
        # If testing on a mobile device, default to ChromeOptions.
        options = ChromeOptions()
    else:
        browser_name = caps.get('browser', '').lower()
        if browser_name == 'chrome':
            options = ChromeOptions()
        elif browser_name == 'firefox':
            options = FirefoxOptions()
        else:
            raise ValueError(f"Unsupported browser: {caps.get('browser')}")

    # Sets all capabilities into the WebDriver options
    for key, value in caps.items():
        options.set_capability(key, value)

    # Initializes the Remote WebDriver with the specified capabilities
    driver = webdriver.Remote(
        command_executor=config['browserstack_url'],
        options=options
    )

    # Sets an implicit wait time for the WebDriver
    driver.implicitly_wait(10)

    # Provides the driver to the test functions
    yield driver

    # Quits the WebDriver session after the test is complete
    driver.quit()

@pytest.fixture(scope='module')
def test_data():
    """
    Pytest fixture to provides test data from the configuration.

    :return: A dictionary containing test site data.
    """
    return config['test_site']
