import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from lib.visuals.bash_colors import color

# Configuration for DVWA
LOGIN_URL = 'http://127.0.0.1/login.php'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

session = requests.Session()
session.headers.update(HEADERS)

def set_custom_cookies(cookie_string):
    cookies = {}
    for cookie in cookie_string.split(';'):
        key, value = cookie.strip().split('=', 1)
        cookies[key] = value
    session.cookies.update(cookies)

def crawl_website(url, COOKIES):

    set_custom_cookies(COOKIES)
    print(f'[{color.DARKCYAN}{datetime.now().time().replace(microsecond=0)}{color.END}]   Testing Connection To {color.BLUE}{url}{color.END}')
    time.sleep(0.5)
    try:
        response = session.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        print(f'[{color.DARKCYAN}{datetime.now().time().replace(microsecond=0)}{color.END}]   Connection Established')

        return soup

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


