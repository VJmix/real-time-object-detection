import requests

# api-endpoint
api_url = 'https://api.thingspeak.com/update?api_key=HIWMKT24HX10PI40'

# location given here
field1 = '0'

# defining a params dict for the parameters to be sent to the API
PARAMS = {'field1': field1}

# sending get request and saving the response as response object
r = requests.get(url = api_url, params = PARAMS) 
