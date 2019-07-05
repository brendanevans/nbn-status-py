import json
import requests

def getLocId(address):
    session = requests.Session()
    baseurl = 'https://places.nbnco.net.au/places/v1/autocomplete?query='

    jsonHeaderData = {
    'Referer': 'https://www.nbnco.com.au/when-do-i-get-it/rollout-map.html'
    }

    request = session.get(
        baseurl + address,
        headers = jsonHeaderData
    )

    response = request.json()
    return response

def searchLocId(locId):
    session = requests.Session()
    baseurl = 'https://places.nbnco.net.au/places/v2/details/'

    jsonHeaderData = {
    'Referer': 'https://www.nbnco.com.au/when-do-i-get-it/rollout-map.html'
    }

    request = session.get(
        baseurl + locId,
        headers = jsonHeaderData
    )

    response = request.json()
    return(response)

def searchAddress(address):
    locId = getLocId(address)
    if not len(locId['suggestions']) == 0:
        response = searchLocId(locId['suggestions'][0]['id'])
        return(response)
    else:
        return('Address not found.')

Test = searchAddress('Bbc/mcdonalds, Shop 4 214 Brisbane Rd, Booval, QLD')
print(Test)
