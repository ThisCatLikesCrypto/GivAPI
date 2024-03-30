import requests
import datetime


#Gets current data
def getData(serial, api_key):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/system-data/latest"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Success
        data = response.json()['data']
    else:
        # Error
        data = {"error": response.status_code}
    
    return data

#Get data for a specific date
def getDate(serial, api_key, date):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "data-points/" + date
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


#Example use
if __name__ == "__main__":
    serial = "YOUR_SERIAL_HERE"
    api_key = "YOUR_KEY_HERE" # (needs api:inverter:read to function)
    print(getData(serial, api_key))
    print(getDate(serial, api_key, "2024-02-02"))