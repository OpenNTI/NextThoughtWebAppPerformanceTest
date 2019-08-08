import sys

#
# Ensure that minimal dependencies are installed
#
def environment_check():
    '''
    Makes sure we have selenium installed.
    :return: True if selenium is found.
    '''
    try:
        __import__('selenium')  # We do need selenium
        return True
    except ImportError:
        return False

#
# Useful methods translated from QA common into QA minimal
#
def min_login(wait_until=None):
    '''
    Login with optional delay
    :param wait_until: If the --delay parameter is used, we will fill in username and password but wait to press 'login'
    until an exact moment. This would let us have every box press 'login' at exactly 1:55, while no delay would
    have each box login as soon as they are able for a more spread-out load.
    :return:
    '''
    browser.get(url)

    handle_currently_logged_in_somewhere()
    min_wait_xpath("//div[contains(@class, 'mask')]", appear=False)

    # Check if they are already logged in elsewhere in case of message (which we expect if this is happening in bulk)
    min_wait_xpath("//input[@id='username']")

    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)

    min_wait_xpath("//button[contains(@id, 'submit')]", until_override=EC.element_to_be_clickable, wait=10)

    if wait_until:
        # We actually want to wait for a particular datetitme
        import time
        while datetime.now() < wait_until:
            timedelta = wait_until - datetime.now()
            diff = timedelta.total_seconds()
            if diff > 100:
                time.sleep(20)
            else:
                time.sleep(1)
        print('Pressing login at ' + datetime.now().strftime('%H:%M - %b %d, %Y'))

    browser.find_element_by_id("submit").send_keys(Keys.RETURN)
    min_wait_xpath("//div[contains(@class, 'x-mask')]", appear=False)

    # Wait for login to finish
    min_wait_xpath("//div[contains(@class, 'identity')]", wait=120)

def min_logout():
    '''
    Logout using the profile icon
    :return:
    '''
    min_wait_xpath("//div[@id='loading-mask']", appear=False, wait=120)

    if not check_already_logged_out():
        identity_icon = "//div[contains(@class, 'identity')]"
        min_wait_xpath(identity_icon)
        scroll_to_center(identity_icon)
        min_wait_xpath("//div[contains(@class, 'mask')", appear=False)
        min_click("//div[contains(@class, 'identity')]/div[@class='profile-pic']")
        min_click("//div[contains(@id, 'menuitem') and contains(.,'Sign Out')]")
        min_wait_xpath("//div[@id='loading-mask']", appear=False)

def check_already_logged_out():
    '''
    Check if we are arleady logged in
    :return: True if so, false if not
    '''
    try:
        identity_icon = "//div[contains(@class, 'identity')]"
        min_wait_xpath(identity_icon, wait=10)
        return False
    except TimeoutException:
        min_wait_xpath("//form[@id='login']", wait=10)
        return True

def handle_currently_logged_in_somewhere(login=False):
    '''
    Handles the situation when we see the 'already logged in' message
    :param login: Whether we should continue to logged in if that message appears.
    :return:
    '''
    try:
        min_wait_xpath("//div[@id='active-session-login' and @class='visible']", wait=3)
        if login:
            min_click("//button[@name='No']")
        else:
            min_click("//button[@name='Yes']")
        min_wait_xpath("//div[contains(@class, 'mask')]", appear=False)
    except TimeoutException as _:
        pass


def min_click(element):
    '''
    Click on either an element or xpath
    :param element: Element or xpath
    :return:
    '''
    if isinstance(element, basestring):
        min_wait_xpath(element)
        browser.find_element_by_xpath(element).click()
    else:
        element.click()

def scroll_to_center(element):
    '''
    Scroll the browser window such that :param element: is in the middle
    :param element: The element (or xpath) to scroll to
    :return:
    '''
    elm = element
    if isinstance(element, basestring):
        elm = browser.find_element_by_xpath(element)

    # {'block': \"center\"}
    browser.execute_script("arguments[0].scrollIntoView({'block': \"center\"});", elm)

def min_wait_xpath(xpath, appear=True, wait=30, until_override=None):
    """
    Waits for an element to appear or disappear depending on :param appear:
    :param xpath: The xpath to check
    :param appear: Wait for appear if True, disappear if False. Default True.
    :param wait: How long to wait; default 30 seconds.
    :param until_override: Overrides the EC check if specified.
    :return:
    """
    assert xpath is not None, 'xpath cannot be empty'
    until = EC.visibility_of_element_located if appear else EC.invisibility_of_element
    if until_override:
        until = until_override
    args = (By.XPATH, xpath)

    try:
        WebDriverWait(browser, wait).until(until(args), xpath + ' did ' + ('not' if appear else '') + ' appear')
    except Exception as e:
        raise

#
# Tests
#
def test_stress_login(datestart=None):
    min_login(datestart)
    min_logout()

    print('Execution finished!')
    browser.quit()

if __name__ == "__main__":
    if len(sys.argv) < 4 or '--help' in sys.argv:
        print('usage: python ' + sys.argv[0] + " <url> <username> <password> (--firefox | --chrome) [--headless] [--delay (time)]")
        print('--delay, if provided, must be of the form <hour>:<minute>-<month>/<day>/<year> e.g. 5:30-05/30/2019 is')
        print('5:30 on May 30th, 2019. --delay will make the test wait until (time) to actually press the login button')
        exit(0)

    if not environment_check():
        print('Selenium is not installed')
        exit(0)

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.keys import Keys

    url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    browser = None
    headless = False

    if '--firefox' in sys.argv:
        fp = webdriver.FirefoxOptions()
        if '--headless' in sys.argv:
            fp.headless = True
        else:
            fp.headless = False

        browser = webdriver.Firefox(options=fp)
    elif '--chrome' in sys.argv:
        fp = webdriver.ChromeOptions()
        if '--headless' in sys.argv:
            fp.headless = True
        else:
            fp.headless = False

        browser = webdriver.Chrome(options=fp)

    if not browser:
        print('Please specify either --firefox or --chrome')
        exit(0)

    browser.set_window_size(1536, 1024)

    date_start = None
    if '--delay' in sys.argv:
        index = 0
        for i in range(0, len(sys.argv)):
            if sys.argv[i] == '--delay':
                index = i + 1
                break
        from datetime import datetime
        date_start = datetime.strptime(sys.argv[index], "%H:%M-%m/%d/%Y")
        print('Will press login at ' + date_start.strftime('%H:%M - %b %d, %Y'))

    test_stress_login(date_start)