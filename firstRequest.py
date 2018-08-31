# importing the requests library
import requests
import datetime
 
# api-endpoint
URL = "http://www.mscloms.com:14/Home/CheckRecordAgainstCell"
MOB_NO="03353778342"
data={'CellNo':MOB_NO}

 
# sending get request and saving the response as response object
try:
    r = requests.post(url = URL, data = data)
    yourData=r.json()
    print("Url: ",URL,"\nTime:",datetime.datetime.now(),"\nResponse:",r.json())
except TimeoutError as e:
    print("Request ",URL," was timeout at: ",datetime.datetime.now())
    print(e)

URL="http://www.mscloms.com:14/Home/ChecktankerCount"
data={'AreaID':'', 'TownID': 'M'}
try:
    r = requests.post(url = URL, data = data)
    print("Url: ",URL,"\nTime:",datetime.datetime.now(),"\nResponse:",r.json())
except TimeoutError as e:
    print("Request ",URL," was timeout at: ",datetime.datetime.now())
    print(e)

URL="http://www.mscloms.com:14/Home/GetGallons"
data={'AreaID':'1016', 'TownID': 'M', 'Add1':yourData["result"]["HouseNo"],'Add2':yourData["result"]["Block"],'Add3':yourData["result"]["Town"],'Add4':yourData["result"]["Area"] }
print("Posting data...: ",data);
try:
    r = requests.post(url = URL, data = data)
    print("Url: ",URL,"\nTime:",datetime.datetime.now(),"\nResponse:",r.json())
except TimeoutError as e:
    print("Request ",URL," was timeout at: ",datetime.datetime.now())
    print(e)

URL="http://www.mscloms.com:14/Home/CheckConsumption"
data={'MOB_NO':MOB_NO,'ADDRESS1':yourData["result"]["HouseNo"],'ADDRESS2':yourData["result"]["Block"],'ADDRESS3':yourData["result"]["Town"],'ADDRESS4':yourData["result"]["Area"],'KWSB_NO':'','TS_ID':'1' }
print("Posting data...: ",data);
try:
    r = requests.post(url = URL, data = data)
    print("Url: ",URL,"\nTime:",datetime.datetime.now(),"\nResponse:",r.json())
except TimeoutError as e:
    print("Request ",URL," was timeout at: ",datetime.datetime.now())
    print(e)    
    
