import requests


def search_avatar(user):
    """Busca o avatar de um usuário no GitHub

    Args:
        user (str): string com o nome de usuário no GitHub
        return: (str) string com o link do avatar
    """

    url = f"https://api.github.com/users/{user}"
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(search_avatar('uadson'))