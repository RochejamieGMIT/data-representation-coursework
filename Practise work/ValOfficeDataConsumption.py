import requests
import json
import urllib.parse
url = "https://api.valoff.ie/api/Property/GetProperties"

parametersDict = {
    "Download" : "false",
    "Format" : "json",
    "CategorySelected":"RETAIL (SHOPS)",
    "LocalAuthority":"WATERFORD CITY AND COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate"


}


def getall():
    parameters = urllib.parse.urlencode(parametersDict)
    #print(parameters)
    fullurl = url +"?" + parameters
    response = requests.get(fullurl)
    
    return response.json()


if __name__ == "__main__":
    with open("valoff.json","wt") as fp:
        print(json.dumps(getall()),file=fp)