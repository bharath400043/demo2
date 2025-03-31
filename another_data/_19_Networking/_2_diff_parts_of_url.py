'''
Created on 30-Mar-2020

@author: VNSquare Tech
'''
'''
https://www.javatpoint.com/                  - Home pagae
https://www.javatpoint.com/python-tutorial   - 
3 points:
---------
1. Request URL 
2. Request method
3. Payload
'''
import urllib.parse
url = "https://www.javatpoint.com/python-tutorial"
# Get tuple with parts of url
tup = urllib.parse.urlparse(url)

# Display contents of tuple
print(tup)
print("Scheme : ", tup.scheme)
print("Netloc : ", tup.netloc)
print("Path   : ", tup.path)
print("Params : ", tup.params)
print("Port   : ", tup.port)
print("URL    : ", tup.geturl())

'''
HTTP Request methods :
--------------------------
GET -- for data retrieval
POST -- to save data(create)
PUT --- to update the record
DELETE --- to delete the record

Request URL     : https://digitalcatalog.paytm.com/dcat/v1/category/17/getcategory?channel=web&version=2&child_site_id=1&site_id=1&locale=en-in
                  https://
                  digitalcatalog.paytm.com
                  /dcat/v1/category/17/getcategory ? 
                      channel=web&
                      version=2&
                      child_site_id=1&
                      site_id=1&
                      locale=en-in
Request Method  : GET
Payload         : 

Request URL : http://amazon.com/signinuser
Request Method : POST
Payload        : {'name':'MadhuNettem',
                  'email':"nettemmadhu@gmail.com',
                  'password':'123456'}


'''