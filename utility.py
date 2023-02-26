import requests

class Utility():
    def __init__(self):
        pass
    def is_internet_available(self):
        try:
            # try to send a request to Google's DNS server
            requests.get('https://www.google.com', timeout=5)
            return True
        except requests.ConnectionError:
            return False