import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
          {'address': address}) + #GOOGLE-GEAOAPI-ACCESS-KEY

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

#sortJson and print country_code
    country_code = js["results"][0]["address_components"]
    country_list = list()
    for item in country_code:
        country_find = item["types"]
        country_list.append(country_find)
    count=-1
#    print(country_list)
    for i in country_list:
        count += 1
        if ['country', 'political'] == i:
            country_code = js["results"][0]["address_components"][int(count)]["short_name"]
            print('Country code',country_code)
        else:pass
