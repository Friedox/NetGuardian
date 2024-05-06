import requests


async def perform_scan():
    # Send HTTP request to a web server and check for response status
    try:
        response = requests.get('http://example.com')
        if response.status_code == 200:
            return "Web server is up"
        else:
            return f"Unexpected status code: {response.status_code}"
    except requests.ConnectionError:
        return "Failed to connect to the web server"
