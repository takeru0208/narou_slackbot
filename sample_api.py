import requests
import pprint
from bs4 import BeautifulSoup
import sys
import datapackage
def main():
    slack_bot_url = 'https://hooks.slack.com/services/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'
    # response = requests.post(
    #     slack_bot_url,
    #     '{"text":"python_api_test"}'
    # )
    # pprint.pprint(response.text)

    narou_url = 'https://ncode.syosetu.com/n6680gx/'
    test_url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
    response = requests.get(
        test_url
    )
    headers
    print(response)
    response2 = requests.get(narou_url)
    print(response2)
    sys.exit()
    soup = BeautifulSoup(response.text, 'html.parser')
    elems = soup.find_all("a", class_="reference internal")
    for count, e in enumerate(elems):
        print(e.getText())
        if count > 10:
            break


if __name__ == '__main__':
    main()