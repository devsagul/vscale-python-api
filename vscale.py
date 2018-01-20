import requests
import json


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


"""
Function create_scalet performs a POST-request at
https://api.vscale.io/v1/scalets, returns information on created server.
Parameters:
token - API token, must be provided as a str object
name - name of a server to be created
password - password for the server. Can be set to None, if authentication 
will be established via SSH keys (see below)
make_from - image to create server from
rplan - id of payment plan
do_start - boolean value that detects if server has to be started after 
creation
location - id of data-center where to create a server
"""


def create_scalet(token,
                  name,
                  password,
                  keys=None,
                  make_from="ubuntu_14.04_64_002_master",
                  rplan="medium",
                  do_start=False,
                  location="spb0"):
    data = {"make_from": str(make_from),
            "rplan": str(rplan),
            "do_start": bool(do_start),
            "name": str(name),
            "location": str(location)
            }

    if password != "" and password is not None:
        data["password"] = str(password)
    if keys is not None:
        data["keys"] = list(keys)

    return requests.post("https://api.vscale.io/v1/scalets",
                         headers={"Content-Type":
                                  "application/json;charset=UTF-8",
                                  "X-Token": token},
                         data=json.dumps(data)
                         )


"""
Function scalet_info performs a GET-request at
https://api.vscale.io/v1/scalets/scalet_id, returns information on server
that has given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
"""


def scalet_info(token, scalet_id):
    return requests.get("https://api.vscale.io/v1/scalets/"+str(scalet_id),
                        headers={"X-Token": token}
                        )
