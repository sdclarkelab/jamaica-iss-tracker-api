import random
import time

import requests
from bs4 import BeautifulSoup as bS


def get_soup(url: str, timeout_retry_count: int = 0):
    """

    :param url:
    :param timeout_retry_count:
    :return:
    """
    soup = None

    for i in range(0, timeout_retry_count):
        response = _get_page_response(url)
        status_code = response.status_code

        if status_code == 200:
            #  Returns the page content to string using UTF-8
            content = response.text
            soup = _extract_dom(content)
            break

        delays = [7, 4, 6, 2, 10, 19]
        delay = random.choice(delays)
        time.sleep(delay)

    return soup


def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        lines = open(ua_file).read().splitlines()
        random_ua = random.choice(lines)
    except Exception as e:
        print(e)
    finally:
        return random_ua


def _get_page_response(url: str):
    headers = {
        'User-Agent': get_random_ua(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                  '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Referer': 'https://www.google.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1'
    }

    # Sends Get request to URL and returns a response
    page_response = requests.get(url, headers=headers)
    return page_response


def _extract_dom(response):
    parsed_data = bS(response, 'lxml')
    return parsed_data
