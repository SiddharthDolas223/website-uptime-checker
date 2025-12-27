import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {url} is UP and running!")
        else:
            print(f"⚠️ {url} returned status code {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"❌ {url} is DOWN or unreachable.")

if __name__ == "__main__":
    website = input("Enter website URL (example: https://google.com): ")
    check_website(website)
