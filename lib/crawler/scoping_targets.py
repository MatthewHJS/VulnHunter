from lib.crawler import crawler 
from urllib.parse import urljoin, urlparse
import re



def get_soup(url, COOKIES):
    return crawler.crawl_website(url, COOKIES)

def find_forms(soup, base_url):
    forms = []
    for form in soup.find_all('form'):
        action = form.get('action')
        method = form.get('method', 'get').lower()
        inputs = []
        for input_tag in form.find_all(['input', 'textarea', 'select']):
            input_type = input_tag.get('type', 'text')
            input_name = input_tag.get('name')
            inputs.append((input_type, input_name))
        forms.append((urljoin(base_url, action), method, inputs))
    return forms

def find_links(soup, base_url):
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '?' in href:
            links.append(urljoin(base_url, href))
    return links

def find_event_handlers(soup):
    event_handlers = []
    for tag in soup.find_all(True):
        for attr, value in tag.attrs.items():
            if attr.startswith('on'):
                event_handlers.append((tag.name, attr, value))
    return event_handlers

def find_csrf_tokens(soup):
    tokens = []
    for input_tag in soup.find_all('input', {'type': 'hidden'}):
        name = input_tag.get('name')
        if 'csrf' in name.lower() or 'token' in name.lower():
            tokens.append(name)
    return tokens

def analyze_page(url, COOKIES):
    soup = get_soup(url, COOKIES)
    if not soup:
        return

    print(f"\nAnalyzing URL: {url}\n")
    
    print("Forms:")
    forms = find_forms(soup, url)
    for action, method, inputs in forms:
        print(f"Action: {action}, Method: {method}")
        for input_type, input_name in inputs:
            print(f"  Input: type={input_type}, name={input_name}")

    print("\nLinks with query parameters:")
    links = find_links(soup, url)
    for link in links:
        print(link)

    print("\nElements with event handlers (potential XSS):")
    event_handlers = find_event_handlers(soup)
    for tag_name, attr, value in event_handlers:
        print(f"Tag: {tag_name}, Event: {attr}, Value: {value}")

    print("\nPotential CSRF tokens:")
    csrf_tokens = find_csrf_tokens(soup)
    for token in csrf_tokens:
        print(token)


