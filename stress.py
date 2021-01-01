#!/usr/bin/python3
"""
    A web stressor to test your infrastructure
"""

from multiprocessing import Process
import requests

# send a request
def send_request(url):
    while True:
        requests.get(url)

if __name__ == "__main__":
    conn_pool = []
    url = input("what url do you want to send to: ")
    for i in range(10000):
        print(i)
        Process(target=send_request, args=(url,)).start()