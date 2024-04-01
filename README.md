# GivAPI
GivEnergy API Interface. Doesn't include much at the moment.  
Install with pip install GivAPI (import with 'import givapi').  

# Functions
get() is an internal function to handle GET requests.  
getData(serial, api_key) returns current data.  
getDate(serial, api_key, date) returns data for said date. Requires an ISO8601 date.  
getAcc(api_key) returns your account data.  
getCom(api_key) returns com device data.  
getSerial(api_key) returns the serial of the first inverter in the list.  
getEMS(serial, api_key) returns EMS data.  
getChgrs(api_key) returns a list of charger UUIDs.  
getChgr(UUID, api_key) returns data by charger UUID.  
getChgd(UUID, api_key, start_time, end_time, measurandsNum=0, measurands=1, meteridsNum=0, meter_ids=1) returns meter data from charger by UUID and other parameters.  
getChgs(UUID, api_key) returns all charging sessions data from charger[UUID].  

# Contributing
Make a pull request and I'll look at it when I have time.
