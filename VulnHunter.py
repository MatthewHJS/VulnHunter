from lib.visuals import banner
from lib.crawler import scoping_targets as st
from datetime import datetime
import time
from lib.visuals.bash_colors import color

COOKIES = 'security=low; PHPSESSID=cp9p9d6u4fq38ovmt28g4jk720' 
URL = 'http://127.0.0.1/vulnerabilities/sqli/'


def main():

    banner.printBanner()
    time.sleep(0.5)
    print(f"[*] Starting The Hunt @ {datetime.now().replace(microsecond=0)}\n")
    

    print(f'[{color.DARKCYAN}{datetime.now().time().replace(microsecond=0)}{color.END}]   Looking For Vulnerabilities')
    time.sleep(0.5)
    
    soup = st.get_soup(URL, COOKIES)
    forms = st.find_forms(soup, URL)
    if forms:
        for action, method, inputs in forms:
            print(f"Action: {action}, Method: {method}")
            for input_type, input_name in inputs:
                print(f"  Input: type={input_type}, name={input_name}")

    links = st.find_links(soup, URL)
    if links:
        print("\nLinks with query parameters:")
        for link in links:
            print(link)

    event_handlers = st.find_event_handlers(soup)
    if event_handlers:
        print("\nElements with event handlers (potential XSS):")
        for tag_name, attr, value in event_handlers:
            print(f"Tag: {tag_name}, Event: {attr}, Value: {value}")

    csrf_tokens = st.find_csrf_tokens(soup)
    if csrf_tokens:
        for token in csrf_tokens:
            print(token)


    return None




main()