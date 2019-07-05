# NBN Status
A basic set of functions to check NBN status at a given address.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.  Do whatever you want with it after that.

### Prerequisites
NBN Status requires JSON and [requests](http://docs.python-requests.org/en/master/).  JSON is an included module.  Install requests using
```
python3 -m pip install requests
```

### Installing
Installation is not required as such, just import the functions where you need them.. or copy them in if you want.

### Usage
Finding the current Status for an Address requires searching by a Location ID (locId).  You can find a locId by running getLocId('Address')
```
getLocId('Address')
```
*Example*
```
getLocId('41 Adelaide St, Brisbane City, QLD')
```
*Example Output*
```
{
    "timestamp": 1549436268061,
    "source": "lapi",
    "suggestions": [
        {
            "id": "LOC000125851254",
            "formattedAddress": "41 Adelaide St, Brisbane City, QLD",
            "latitude": -27.4698502,
            "longitude": 153.02373292
        },
        {
            "id": "LOC000098649356",
            "formattedAddress": "Unit 41 208 Adelaide St, Brisbane City, QLD",
            "latitude": -27.466901,
            "longitude": 153.026392
        },
        ... Another 3 entries ...
    ]
}
```
You can then use the id from one of the suggestions to find exact details using searchLocId('locId')

*Example*
```
searchLocId('LOC000125851254')
```
*Example output*
```
{
    "timestamp": 1549436527235,
    "location": {
        "id": "LOC000125851254",
        "formattedAddress": "LOT 1 41 ADELAIDE ST BRISBANE CITY QLD 4000 Australia",
        "latitude": -27.4698502,
        "longitude": 153.02373292
    },
    "servingArea": {
        "csaId": "CSA400000010134",
        "techType": "FTTC",
        "serviceType": "Fixed line",
        "serviceStatus": "proposed",
        "serviceCategory": "brownfields",
        "rfsMessage": "Jan-Jun 2020",
        "description": "Charlotte"
    },
    "addressDetail": {
        "id": "LOC000125851254",
        "latitude": -27.4698502,
        "longitude": 153.02373292,
        "reasonCode": "FTTC_NA",
        "serviceType": "Fixed line",
        "serviceStatus": "proposed",
        "techType": "FTTC",
        "rfsMessage": "Jan-Jun 2020",
        "formattedAddress": "LOT 1 41 ADELAIDE ST BRISBANE CITY QLD 4000 Australia",
        "frustrated": false
    }
}
```
Or you can perform both steps in one command using searchAddress

**Be aware that if multiple addresses are found it will search for the first suggestion returned**

In the example above, it will automatically search for locId LOC000125851254.

## Tests
The following 8 scenarios have been tested.  If you believe there are more, or find someway for it to return other data, please let me know.
### getLocId
* Finds a single address
* Finds multiple addresses
* Unable to find the address
### searchLocId
* Finds the locId
* Does not find the locId
### searchAddress
* Finds a single address (and searches for it)
* Finds multiple addresses (and searches for the first match)
* Unable to find the address

## Authors
* **Brendan Evans** - [BrendanEvans](https://github.com/brendanevans)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [ChrisHardinge](https://github.com/chrishardinge) - This is a python rewrite of his PHP based [nbn-lookup](https://github.com/chrishardinge/nbn-lookup)