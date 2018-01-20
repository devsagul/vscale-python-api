import requests


"""
Function account performs GET-request at https://api.vscale.io/v1/account,
returns full information on user: name, activation date, email.
The only parameter is token that has to be provided as a str object
"""


def account(token):
    return requests.get("https://api.vscale.io/v1/account",
                        headers={"X-Token": token}
                        )


"""

"""


def