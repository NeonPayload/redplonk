import requests
import socket
import sys

def internetdb(scan_item):
    try:
        print("[internetdb function] scan item " + scan_item)
        ip_address = socket.gethostbyname(scan_item)
        print(ip_address)
        response = requests.get(f"https://internetdb.shodan.io/{ip_address}").json()
        print(response)
        return response
   
    except:
       return 'No internetdb'