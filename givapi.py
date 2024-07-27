import requests

#!TODO: Add smart device data/requests and multiple-setting requests. Also add engineer+ and company+ stuff but I likely will not do that
#Copyright Wilbur Williams <contact@wilburwilliams.uk> 2024. Licensed under GPL3.
#If you can contribute to this please do so at https://github.com/ThisCatLikesCrypto/GivAPI
#For documentation on the API please see https://beta.givenergy.cloud/docs/api/v1
#This has been built for GivEnergy API version 1.22.0, and is for end-user accounts. Nothing that requires higher account types is included.

#Main get function
def get(api_key, url, params=None):
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    if params == None:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers, params=params) #Cannot be triggered atm but leave in
    if response.status_code == 200 or 201:
        # Success
        data = response.json()['data']
    else:
        # Error
        data = {"error": response.status_code}
    return data

#Main post function
def post(api_key, url, value=None):
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    indata = {"value": value}

    if value == None:
        response = requests.post(url, headers=headers)
    else:
        response = requests.post(url, headers=headers, json=indata)

    if str(response.status_code).startswith("2"):
        try:
            data = response.json()['data']
            return data
        except:
            data = {"error": "Something went wrong. response.json() is "+response.json()}

##!Get functions

#!Account
#Get account data, needs needs api:account to function
def getAcc(api_key):
    url = 'https://api.givenergy.cloud/v1/account'
    return get(api_key, url)

#!Inverter stuff

#Gets current data, needs api:inverter:read to function
def getData(serial, api_key):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/system-data/latest"
    return get(api_key, url)

#Get all data for a specific date, in 5 minute intervals, needs api:inverter to function
def getDate(serial, api_key, date):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/data-points/" + date
    return get(api_key, url)

#Get communication device data, needs api:inverter:list
def getCom(api_key):
    url = "https://api.givenergy.cloud/v1/communication-device"
    return get(api_key, url)

#Get serial from api key, needs api:inverter:list, only works with one inverter
def getSerial(api_key):
    return getCom(api_key)[0]['inverter']['serial']

#Get EMS data, needs api:inverter:read
def getEMS(serial, api_key): #if anyone with an EMS uses this please tell me whether it worked or not because I cannot verify it, since I don't have one
    url = "https://api.givenergy.cloud/v1/ems/" + serial + "/system-data/latest"
    return get(api_key, url)

#Get inverter presets, needs api:inverter:control
def getPrs(serial, api_key):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/presets"
    return get(api_key, url)


#Get inverter settings, needs api:inverter:control, yes the function name sounds cool
def getSet(serial, api_key):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/settings"
    return get(api_key, url)


#!EV charger stuff
##!For ALL EV charger stuff I cannot verify whether it works or not, since I don't have a GivEnergy one. Please report back if you have one whether it works or not

#Get list of chargers by UUID, needs api:ev-charger:list
def getChgrs(api_key):
    url = "https://api.givenergy.cloud/v1/ev-charger"
    return get(api_key, url)

#Get data from charger by UUID, needs api:ev-charger:read
def getChgr(UUID, api_key):
    url = "https://api.givenergy.cloud/v1/ev-charger/" + UUID
    return get(api_key, url)

#Get meter data from charger by UUID, needs api:ev-charger:data
def getChgd(UUID, api_key, start_time, end_time, measurandsNum=0, measurands=1, meteridsNum=0, meter_ids=1):
    params = {"start_time": start_time, "end_time": end_time, f"measurands[{measurandsNum}]": measurands, f"meter_ids[{meteridsNum}]": meter_ids}
    url = "https://api.givenergy.cloud/v1/ev-charger/" + UUID + "/meter-data"
    return get(api_key, url, params)

#Get all charging sessions data (by UUID), needs api:ev-charger:data
def getChgs(UUID, api_key):
    url = "https://api.givenergy.cloud/v1/ev-charger/" + UUID + "/charging-sessions"
    return get(api_key, url)

#Get charger supported commands, needs api:ev-charger:control
def getChgCmds(UUID, api_key):
    url = "https://api.givenergy.cloud/v1/ev-charger/" + UUID + "/commands"
    return get(api_key, url)

#Get command data, needs api:ev-charger:control
def getChCmd(UUID, api_key, command_id):
    url = "https://api.givenergy.cloud/v1/ev-charger/" + UUID + "/commands/" + command_id
    return get(api_key, url)

##!Post functions

#!EV Charger

#Control an EV charger, needs api:ev-charger:control
def conChgr(UUID, api_key, command_id):
    url = "https://api.givenergy.cloud/v1/ev-charger/" + UUID + "/commands/" + str(command_id)
    return post(api_key, url)

#!Inverter

#Modify inverter presets, needs api:inverter:control
def modPrs(serial, api_key, preset):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/presets/" + preset
    return post(api_key, url)

#Read setting, needs api:inverter:control
def readSet(serial, api_key, setting_id):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/settings/" + str(setting_id) + "/read"
    return post(api_key, url)

#Set setting, needs api:inverter:control
def setSet(serial, api_key, setting_id, value):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/settings/" + str(setting_id) + "/write"
    return post(api_key, url, value)


##!Extra: Elexon and Carbon Intensity APIs
def getElexon():
    url = "https://data.elexon.co.uk/bmrs/api/v1/generation/actual/per-type/day-total?format=json"
    headers = {"accept": "application/json"}
    response = requests.get(url=url, headers=headers)
    return response.json()

def getGen():
    headers = {'Accept': 'application/json'}
    r = requests.get('https://api.carbonintensity.org.uk/generation', params={}, headers = headers)
    data = r.json()['data']
    return data

def getCO2():
    headers = {'Accept': 'application/json'}
    r = requests.get('https://api.carbonintensity.org.uk/intensity', params={}, headers = headers)
    data = r.json()['data']
    return data

#Example use
if __name__ == "__main__":
    api_key = "YOUR_KEY_HERE"
    try:
        serial = getSerial(api_key)
        print(getData(serial, api_key))
        if input("test post? (y/n): ") == "y":
            print(readSet(serial, api_key, 96)) #96 is 'Pause Battery', I just needed something to test POST
    except KeyError:
        print("Probably not authed correctly. Just testing elexon and CO2")
    print(getElexon())
    print(getGen())
    print(getCO2())
