import requests

#Gets current data, needs api:inverter to function
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
        try:
            data = response.json()['data']
        except:
            raise ValueError("The response does not have a 'data' component. Response: " + response.json())
    else:
        # Error
        data = {"error": response.status_code}
    
    return data

#Get all data for a specific date, in 5 minute intervals, needs api:inverter to function
def getDate(serial, api_key, date, page=1, per_page=1):
    params = {"page" : page, "per_page": per_page}
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/data-points/" + date
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Success
        try:
            data = response.json()['data']
        except:
            raise ValueError("The response does not have a 'data' component. Response: " + response.json())
    else:
        # Error
        data = {"error": response.status_code}
    return data

#Get account data, needs needs api:account to function
def getAcc(api_key):
    url = 'https://api.givenergy.cloud/v1/account'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
        }

    response = requests.request('GET', url, headers=headers)
    if response.status_code == 200:
        # Success
        try:
            data = response.json()['data']
        except:
            data = ("Error: The response does not have a 'data' component. Response: " + response.json())
    else:
        # Error
        data = {"error": response.status_code}
    return data

#Example use
if __name__ == "__main__":
    serial = "YOUR_SERIAL_HERE"
    api_key = "YOUR_KEY_HERE"
    print(getData(serial, api_key))
    print(getDate(serial, api_key, "2024-02-02", 1))
    print(getAcc(api_key))