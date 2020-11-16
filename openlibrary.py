import requests
import json


def request_api():

	response = requests.get('https://openlibrary.org/works/OL45883W.json')

	if response.status_code == 200:

		return response.json()

	else:

		return response.status_code


def print_books():

	dados_api = request_api()

	if type(dados_api) is not int:

		for i in range(len(dados_api)):

			print(dados_api)

	else:
	
		print(dados_api)		


request_api()

print_books()


