import requests
import bs4


def getCommonHeader():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    return header


def req(url, headers):
    resp = requests.get(url, headers)
    return resp



def test():
    url = "https://www.baidu.com"
    headers = getCommonHeader()
    resp = req(url, headers)
    print(resp.content.decode("utf-8"))


if __name__ == '__main__':
    test()
