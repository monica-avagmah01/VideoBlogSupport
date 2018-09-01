import requests 
import re
from httplib import HTTPResponse
url = 'https://run.leadsquared.com/Home/SignIn/'
values = {'EmailID': 'aakar@acadgild.com',
          'Password': 'Welcome124!'}

r = requests.post(url, data=values)
r.encoding = 'utf-8'
print (r.status_code)

host = "https://api.leadsquared.com/v2/"
accessKey = "u$rc8ba297f16840f59eea298cf48169387"
secretKey = "666bbb18d76f7fe9185ced7288f642066b20361d"
id = "2a556b43-69c3-40e3-a23f-34003b82c3ee"

api_url = host+"LeadManagement.svc/Leads.RecentlyModified?accessKey="+accessKey+"&secretKey="+secretKey+"&id="+id
#ata = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

data = {
    "Parameter": {
        "FromDate": "2018-05-01 00:00:00",
        "ToDate": "2018-08-01 00:00:00"
    },
    "Paging": {
        "PageIndex": 1,
        "PageSize": 100
    }
}

try:
	r = requests.post(api_url, json=data, headers=headers)
except requests.exceptions.RequestException as err:
	print("Not able to connect", err)

r.encoding = 'utf-8'

#print(r.json())
if (r.status_code != 200):
	print(r.text)
	exit(0)
elif(r.status_code == 200):
	dump_file = open("all_leads.txt","w+")
	dump_file.write(r.text.encode('utf-8'))
	dump_file.close()
	m = re.search('\"RecordCount\":([0-9]+)', r.text).groups()	
	print("Number of records updated: ", int(str(m[0])))
