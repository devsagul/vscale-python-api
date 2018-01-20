import requests


"""
Function account performs a GET-request at https://api.vscale.io/v1/account,
returns full information on user: name, activation date, email.
The only parameter is token that has to be provided as a str object.
"""


def account(token):
    return requests.get("https://api.vscale.io/v1/account",
                        headers={"X-Token": token}
                        )


"""
Function get_scalets performs a GET-request at
https://api.vscale.io/v1/scalets, returns information on servers.
The only parameter is token that has to be provided as a str object.
"""


def get_scalets(token):
    return requests.get("https://api.vscale.io/v1/scalets",
                        headers={"X-Token": token}
                        )
