import requests

class cli:
    def __init__(self,headers=None,cookies={}):
        self.headers = headers
        if self.headers == None:
            self.headers = {
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9'}
            
        self.cookies = cookies

    def get(self,url):
        """

        Get data from given url
        
        """
        res = requests.get(url, headers=self.headers, cookies=self.cookies)
        self.cookies = res.cookies.get_dict()
        return res
    def post(self,url,data):
        """

        Post given data to given url

        """
        res = requests.post(url, headers=self.headers, cookies=self.cookies,data=data)
        self.cookies = res.cookies.get_dict()
        return res

client = cli()

a = client.get('https://coursehero.com')

print(a.text)
