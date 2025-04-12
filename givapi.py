import requests

"""
TODO: Add smart device data/requests and multiple-setting requests.
Also add engineer+ and company+ stuff but I likely will not do that.

Copyright Wilbur Williams <contact@wilburwilliams.uk> 2024. Licensed under GPL3.
If you can contribute to this please do so at https://github.com/ThisCatLikesCrypto/GivAPI

For documentation on the API please see https://beta.givenergy.cloud/docs/api/v1
This has been built for GivEnergy API version 1.22.0, and is for end-user accounts.
Nothing that requires higher account types is included.
"""

def get(api_key, url, params=None):
    """
    Main GET function.
    Sends a GET request with the required headers and optional params.
    Returns the 'data' key of the response JSON or an error code.
    """
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    if params is None:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200 or 201:
        data = response.json()['data']
    else:
        data = {"error": response.status_code}
    return data

def post(api_key, url, value=None):
    """
    Main POST function.
    Sends a POST request with a value payload if provided.
    Returns the 'data' key of the response JSON or an error.
    """
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    indata = {"value": value}

    if value is None:
        response = requests.post(url, headers=headers)
    else:
        response = requests.post(url, headers=headers, json=indata)

    if str(response.status_code).startswith("2"):
        try:
            data = response.json()['data']
            return data
        except:
            data = {"error": "Something went wrong. response.json() is " + response.json()}
    return {"error": response.status_code}

# GET functions

def getAcc(api_key):
    """Get account data. Requires scope: api:account."""
    url = 'https://api.givenergy.cloud/v1/account'
    return get(api_key, url)

def getData(serial, api_key):
    """Get current inverter data. Requires scope: api:inverter:read."""
    url = f"https://api.givenergy.cloud/v1/inverter/{serial}/system-data/latest"
    return get(api_key, url)

def getDate(serial, api_key, date):
    """Get inverter data for a specific date in 5-minute intervals. Requires scope: api:inverter."""
    url = f"https://api.givenergy.cloud/v1/inverter/{serial}/data-points/{date}"
    return get(api_key, url)

def getCom(api_key):
    """Get communication device data. Requires scope: api:inverter:list."""
    url = "https://api.givenergy.cloud/v1/communication-device"
    return get(api_key, url)

def getSerial(api_key):
    """Get inverter serial from API key. Requires scope: api:inverter:list."""
    return getCom(api_key)[0]['inverter']['serial']

def getEMS(serial, api_key):
    """
    Get EMS (Energy Management System) data.
    Requires scope: api:inverter:read.
    Note: Not tested. Please report success/failure.
    """
    url = f"https://api.givenergy.cloud/v1/ems/{serial}/system-data/latest"
    return get(api_key, url)

def getPrs(serial, api_key):
    """Get inverter presets. Requires scope: api:inverter:control."""
    url = f"https://api.givenergy.cloud/v1/inverter/{serial}/presets"
    return get(api_key, url)

def getSet(serial, api_key):
    """Get inverter settings. Requires scope: api:inverter:control."""
    url = f"https://api.givenergy.cloud/v1/inverter/{serial}/settings"
    return get(api_key, url)

# EV charger functions (untested)

def getChgrs(api_key):
    """Get list of EV chargers by UUID. Requires scope: api:ev-charger:list."""
    url = "https://api.givenergy.cloud/v1/ev-charger"
    return get(api_key, url)

def getChgr(UUID, api_key):
    """Get data from EV charger by UUID. Requires scope: api:ev-charger:read."""
    url = f"https://api.givenergy.cloud/v1/ev-charger/{UUID}"
    return get(api_key, url)

def getChgd(UUID, api_key, start_time, end_time, measurandsNum=0, measurands=1, meteridsNum=0, meter_ids=1):
    """
    Get meter data from EV charger.
    Requires scope: api:ev-charger:data.
    """
    params = {
        "start_time": start_time,
        "end_time": end_time,
        f"measurands[{measurandsNum}]": measurands,
        f"meter_ids[{meteridsNum}]": meter_ids
    }
    url = f"https://api.givenergy.cloud/v1/ev-charger/{UUID}/meter-data"
    return get(api_key, url, params)

def getChgs(UUID, api_key):
    """Get all charging session data for a charger. Requires scope: api:ev-charger:data."""
    url = f"https://api.givenergy.cloud/v1/ev-charger/{UUID}/charging-sessions"
    return get(api_key, url)

def getChgCmds(UUID, api_key):
    """Get charger-supported commands. Requires scope: api:ev-charger:control."""
    url = f"https://api.givenergy.cloud/v1/ev-charger/{UUID}/commands"
    return get(api_key, url)

def getChCmd(UUID, api_key, command_id):
    """Get data for a specific command. Requires scope: api:ev-charger:control."""
    url = f"https://api.givenergy.cloud/v1/ev-charger/{UUID}/commands/{command_id}"
    return get(api_key, url)

# POST functions

def conChgr(UUID, api_key, command_id):
    """Send a control command to an EV charger. Requires scope: api:ev-charger:control."""
    url = f"https://api.givenergy.cloud/v1/ev-charger/{UUID}/commands/{command_id}"
    return post(api_key, url)

def modPrs(serial, api_key, preset):
    """Modify inverter presets. Requires scope: api:inverter:control."""
    url = f"https://api.givenergy.cloud/v1/inverter/{serial}/presets/{preset}"
    return post(api_key, url)

def readSet(serial, api_key, setting_id):
    """Read a setting from the inverter. Requires scope: api:inverter:control."""
    url = f"https://api.givenergy.cloud/v1/inverter/{serial}/settings/{setting_id}/read"
    return post(api_key, url)

def setSet(serial, api_key, setting_id, value):
    """Set a setting on the inverter. Requires scope: api:inverter:control."""
    url = f"https://api.givenergy.cloud/v1/inverter/{serial}/settings/{setting_id}/write"
    return post(api_key, url, value)

# Extra APIs: Elexon and Carbon Intensity

def getElexon():
    """Get actual generation per type from Elexon."""
    url = "https://data.elexon.co.uk/bmrs/api/v1/generation/actual/per-type/day-total?format=json"
    headers = {"accept": "application/json"}
    response = requests.get(url=url, headers=headers)
    return response.json()

def getGen():
    """Get UK generation mix from Carbon Intensity API."""
    headers = {'Accept': 'application/json'}
    r = requests.get('https://api.carbonintensity.org.uk/generation', params={}, headers=headers)
    return r.json()['data']

def getCO2():
    """Get current UK carbon intensity from Carbon Intensity API."""
    headers = {'Accept': 'application/json'}
    r = requests.get('https://api.carbonintensity.org.uk/intensity', params={}, headers=headers)
    return r.json()['data']

# Example usage
if __name__ == "__main__":
    api_key = "YOUR_KEY_HERE"
    try:
        serial = getSerial(api_key)
        print(getData(serial, api_key))
        if input("test post? (y/n): ") == "y":
            print(readSet(serial, api_key, 96))  # 96 is 'Pause Battery'
    except KeyError:
        print("Probably not authed correctly. Just testing Elexon and CO2")
    print(getElexon())
    print(getGen())
    print(getCO2())
