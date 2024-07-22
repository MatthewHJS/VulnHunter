from lib.visuals import banner
from lib.crawler import scoping_targets


COOKIES = 'security=low; PHPSESSID=cp9p9d6u4fq38ovmt28g4jk720' 
URL = 'http://127.0.0.1/vulnerabilities/sqli/'


def main():

    banner.printBanner()

    scoping_targets.analyze_page(URL, COOKIES)




    return None




main()