#Author: Bkramer02
#DevNetHigh Wk2 Challenge
#Create program to get a random Chuck Norris joke and parse the JSON for output to the screen

import requests

r = requests.get('https://api.chucknorris.io/jokes/random')
jsonResponse = r.json()
print(f'The random Chuck Norris joke is: {jsonResponse["value"]}')



#print(r.status_code)
#print(r.values)

""" 
jsonResponse = r.json()
print("Entire JSON response")
print(jsonResponse)

print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    print(key, ":", value)

print("Access directly using a JSON key name")
print("Joke is ")
print(jsonResponse["value"])
 """
