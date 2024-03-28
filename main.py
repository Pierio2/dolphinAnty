import requests
import json
from selenium import webdriver
def main():
    profile = 322438460
    url = f"http://localhost:3001/v1.0/browser_profiles/{profile}/start?automation=1"
    response = requests.request("GET", url)
    port = json.loads(response.content).get('automation').get('port')
    print(port)

    options = webdriver.ChromeOptions()
    options.debugger_address = f"127.0.0.1:{port}"
    browser = webdriver.Chrome(options=options)
    browser.get("https://rubexgroup.ru")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()