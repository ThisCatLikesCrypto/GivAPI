import requests

#!TODO: ADD ANYTHING WITH 'POST' DATA, ANYTHING UNDER 'CONTROL' or 'COMMANDS' CATEGORIES AND ADD SUPPORT FOR PARAMS FOR ALL
#If you can contribute to this please do so at https://github.com/ThisCatLikesCrypto/GivAPI

#Main get function
def get(api_key, url, params="None"):
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    if params == "None":
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers, params=params) #Cannot be trigged atm but leave in
    if response.status_code == 200 or 201:
        # Success
        try:
            data = response.json()['data']
        except: 
            data = {"error":"No data attribute. response.json() is "+response.json()}
    else:
        # Error
        data = {"error": response.status_code}
    return data

#Gets current data, needs api:inverter:read to function
def getData(serial, api_key):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/system-data/latest"
    return get(api_key, url)

#Get all data for a specific date, in 5 minute intervals, needs api:inverter to function
def getDate(serial, api_key, date):
    url = "https://api.givenergy.cloud/v1/inverter/" + serial + "/data-points/" + date
    return get(api_key, url)

#Get account data, needs needs api:account to function
def getAcc(api_key):
    url = 'https://api.givenergy.cloud/v1/account'
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

#Example use
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    serial = getSerial(api_key)
    print(getData(serial, api_key))