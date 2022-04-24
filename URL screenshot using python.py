import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# here i am using chrome version 1000 hence installed
# pip install chromedriver-binary==100.0.4896.60.0
# make sure to check chrome version to install right version

script_name = sys.argv[0]
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


try:
    # entere the URL here , whose screenshot needs to be taken
    url = r"https://www.geeksforgeeks.org/automate-whatsapp-messages-with-python-using-pywhatkit-module/"
    driver.get(url)

    # get the width of page
    page_width = driver.execute_script("return document.body.scrollWidth")

    # get the height og page
    page_height = driver.execute_script("return document.body.scrollHeight")

    # create image
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot("screenshot.png")
    driver.quit()
    print("Screenshot created !!")
except IndexError:
    print("Usage: %s URL" % script_name)
