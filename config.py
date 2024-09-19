bot_token = "6816017020:AAGbb3BOczYoI8OlT47YepkX1d716PUgkF0"



import requests

url = "https://numbersapi.p.rapidapi.com/1729/math"

querystring = {"fragment":"true","json":"true"}

headers = {
	"X-RapidAPI-Key": "1a9c89d109msh0972e353c763929p12529ejsn9d1f230bdddf",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
