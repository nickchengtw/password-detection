import requests

def call_api(username, password):
    url = 'https://api.example.com/login'  # Replace with the actual API endpoint URL
    
    payload = {
        'username': username,
        'password': password
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        # API call successful
        print("API call successful!")
        print("Response:", response.json())
    else:
        # API call failed
        print("API call failed. Status code:", response.status_code)

# Example usage
username = 'admin'
password = 'qwerty123'

call_api(username, password)
