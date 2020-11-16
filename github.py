import requests
import json


class ListaRepo():
	""" Representa uma lista de repositórios do GitHub
	"""

	def __init__(self, usuario):

		self._usuario = usuario


	def requerer_api(self):
		"""
			Requer e valida ou não, API de acordo com o nome do usuário.
		"""

		response = requests.get(f'https://api.github.com/users/{self._usuario}/repos')

		# verifica se houve sucesso na requisição
		if response.status_code == 200: # OK

			return response.json()

		else:

			return response.status_code
			# 400 - not found
			# 500 - internal server error
			# estes são os mais comuns


	def print_repo(self):
		"""
			Imprime em tela a lista de repositorios
		"""

		# recebe os dados da api
		dados_api = self.requerer_api()


		if type(dados_api) is not int:

			print(f'\nQuantidade de Repositórios: {len(dados_api)}\n')
			
			print('Lista de Repositórios no GitHub:\n')
			
			for i in range(len(dados_api)):

				print(dados_api[i]['name'])

		else:

			print(dados_api)


if __name__ == '__main__':

	user = ListaRepo('uadson')

	user.requerer_api()

	user.print_repo()