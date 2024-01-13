import requests

def find_admin_panel(base_url):
    common_paths = ['/admin', '/login', '/dashboard', '/wp-admin']  # Add more paths if needed

    for path in common_paths:
        url = base_url + path
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[+] Found admin panel: {url}")
        else:
            print(f"[-] Not found: {url}")

# Replace 'https://odamlar.tv' with the actual URL you are testing
target_url = 'https://oxu.uz'
find_admin_panel(target_url)
