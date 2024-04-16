# GivAPI
GivEnergy API Interface.
Install with pip install GivAPI (import with 'import givapi').  

# Functions
get() is an internal function to handle GET requests.  
post() is an internal function to handle POST requests.
getData(serial, api_key) returns current data.  
getDate(serial, api_key, date) returns data for said date. Requires an ISO8601 date.
getPrs(serial, api_key) returns inverter presets.
getSet(serial, api_key) returns inverter settings.
getAcc(api_key) returns your account data.  
getCom(api_key) returns com device data.  
getSerial(api_key) returns the serial of the first inverter in the list.  
getEMS(serial, api_key) returns EMS data.  
getChgrs(api_key) returns a list of charger UUIDs.  
getChgr(UUID, api_key) returns data by charger UUID.  
getChgd(UUID, api_key, start_time, end_time, measurandsNum=0, measurands=1, meteridsNum=0, meter_ids=1) returns meter data from charger by UUID and other parameters.  
getChgs(UUID, api_key) returns all charging sessions data from charger[UUID].
getChgCmds(UUID, api_key) returns all commands supported by your charger.
getChCmd(UUID, api_key, command_id) returns the data for a specific charger command.

conChgr(UUID, api_key, command_id) allows you to control a charger by command id.
modPrs(serial, api_key, preset) allows you to modify inverter presets.
readSet(serial, api_key, setting_id) allows you to read inverter settings.
setSet(serial, api_key, setting_id, value) allows you to set inverter settings.

# Contributing
Make a pull request and I'll look at it when I have time.
