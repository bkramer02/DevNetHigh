#Author: Bkramer02
#DevNetHigh Wk2 Challenge
#Create program to get a random Chuck Norris joke and parse the JSON for output to the screen

import requests

r = requests.get('https://api.chucknorris.io/jokes/random')
jsonResponse = r.json()
print(f'The random Chuck Norris joke is: {jsonResponse["value"]}')


