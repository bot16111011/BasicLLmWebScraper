import time
from bs4 import BeautifulSoup
from extra import *
# import selenium.webdriver as webdriver
# from selenium.webdriver.edge.service import Service

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
AUTH = "Enter your API key"
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

def scrape_website(website):
    print("Launching Edge Browser")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
    # driver_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"
    # options = webdriver.EdgeOptions()
    # driver = webdriver.Edge(service=Service(driver_path), options=options)

    # try:
    #     driver.get(website)
    #     print("Page loaded ....")
    #     html = driver.page_source 
    #     time.sleep(10)
    #     return html
    # finally:
    #     driver.quit()


    # wait = WebDriverWait(self.driver, 20) 
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["Script","style"]):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0,len(dom_content),max_length)
    ]