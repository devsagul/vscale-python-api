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


"""
Function scalet_restart performs a PATCH-request at
https://api.vscale.io/v1/scalets/scalet_id, restarts a server
that has given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
"""


def scalet_restart(token, scalet_id):
    return requests.patch("https://api.vscale.io/v1/scalets/"+str(scalet_id)+
                          "/restart",
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.dumps({"id": str(scalet_id)})
                          )


"""
Function scalet_rebuild performs a PATCH-request at
https://api.vscale.io/v1/scalets/scalet_id, reinstalls an OS on the server
with a given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Old root password will be deleted, new root password has to be provided as 
a str object.
Information on scalet's id can be found in output of function get_scalets.
"""


def scalet_rebuild(token, scalet_id, password):
    return requests.patch("https://api.vscale.io/v1/scalets/"+str(scalet_id)+
                          "/rebuild",
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.dumps({"password": str(password)})
                          )

"""
Function scalet_stop performs a PATCH-request at
https://api.vscale.io/v1/scalets/scalet_id, stops the server
with a given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
"""


def scalet_stop(token, scalet_id):
    return requests.patch("https://api.vscale.io/v1/scalets/"+str(scalet_id)+
                          "/stop",
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.dumps({"id": str(scalet_id)})
                          )

"""
Function scalet_start performs a PATCH-request at
https://api.vscale.io/v1/scalets/scalet_id, starts the server
with a given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
"""


def scalet_start(token, scalet_id):
    return requests.patch("https://api.vscale.io/v1/scalets/"+str(scalet_id)+
                          "/start",
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.dumps({"id": str(scalet_id)})
                          )


"""
Function scalet_upgrade performs a POST-request at
https://api.vscale.io/v1/scalets/scalet_id, upgrades the server
with a given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
Third parameter is an id of a desired configuration, has to be provided as 
str object.
"""


def scalet_upgrade(token, scalet_id, rplan):
    return requests.post("https://api.vscale.io/v1/scalets/"+str(scalet_id)+
                          "/upgrade",
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.dumps({"rplan": str(rplan)})
                          )


"""
Function scalet_delete performs a DELETE-request at
https://api.vscale.io/v1/scalets/scalet_id, deletes the server
with a given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
"""


def scalet_delete(token, scalet_id):
    return requests.delete("https://api.vscale.io/v1/scalets/"+str(scalet_id),
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token}
                          )


"""
Function tasks_info performs a GET-request at
https://api.vscale.io/v1/tasks, returns information on current tasks.
Token has to be provided as a str object.
"""


def tasks_info(token):
    return requests.get("https://api.vscale.io/v1/tasks",
                          headers={"X-Token": token}
                          )


"""
Function scalet_add_ssh performs a PATCH-request at 
https://api.vscale.io/v1/scalets/scalet_id, adds given SSH-key to the server
with a given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
The third parameter is a list of ssh-keys. List of available ssh-keys 
may be obtained via sshkeys_list function (see beelow). 
"""


def scalet_add_ssh(token, scalet_id, keys):
    return requests.patch("https://api.vscale.io/v1/scalets/" + str(scalet_id),
                           headers={"Content-Type":
                                    "application/json;charset=UTF-8",
                                    "X-Token": token},
                            data=json.dumps({"keys": keys})
                           )


"""
Function scalet_backup performs a POST-request at
https://api.vscale.io/v1/scalets/scalet_id, creates backup of the server 
with a given scalet_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
The third parameter is the name of backup to be created. Must be provided 
as a str object.
"""


def scalet_backup(token, scalet_id, name):
    return requests.post("https://api.vscale.io/v1/scalets/"+str(scalet_id)+
                          "/backup",
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.dumps({"name": str(name)})
                          )


"""
Function scalet_restore performs a PATCH-request at 
https://api.vscale.io/v1/scalets/scalet_id, restores server 
with a given scalet_id from a buckup with a given backup_id.
Token has to be provided as a str object.
The second parameter is scalet_id that can be provided as an str object.
Information on scalet's id can be found in output of function get_scalets.
The third parameter is the id of backup to be created. Must be provided 
as a str object.
"""


def scalet_restore(token, scalet_id, backup_id):
    return requests.post("https://api.vscale.io/v1/scalets/"+str(scalet_id)+
                          "/rebuild",
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.dumps({"make_from": str(backup_id)})
                          )


"""
Function add_tag performs a POST-request at
https://api.vscale.io/v1/scalets/tags, adds new server tag.
Token has to be provided as a str object.
The second parameter is the name of tag to be added.
The third parameter is a list of scalet ids to which tag should be added. 
This parameter is optional.
"""


def add_tag(token, tag_name, scalets=None):
    data={"name": str(tag_name)}
    if scalets is not None:
        data["scalets"] = scalets
    return requests.post("https://api.vscale.io/v1/scalets/tags",
                        headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token},
                        data=json.dumps(data)
                        )


"""
Function get_tags performs a GET-request at 
https://api.vscale.io/v1/scalets/tags, returns list of server tags.
Token has to be provided as a str object.
"""


def get_tags(token):
    return requests.get("https://api.vscale.io/v1/scalets/tags",
                          headers={"X-Token": token}
                          )


"""
Function tag_info performs a GET-request at
https://api.vscale.io/v1/scalets/tags, returns info on a tag with a given
tag id.
Token has to be provided as a str object.
Tag id has to be provided as a str object.
"""


def tag_info(token, tagid):
    return requests.get("https://api.vscale.io/v1/scalets/tags/"+str(tagid),
                          headers={"X-Token": token}
                          )


"""
Function update_tag performs a PUT-request at
https://api.vscale.io/v1/scalets/tags, updates name and scalets of the tag 
with a given tag id.
Token has to be provided as a str object.
Tag id has to be provided as a str object.
Name is the new tag name. Has to be provided as a str object.
The third parameter is a list of scalet ids to which tag should be added. 
This parameter is optional.
"""


def update_tag(token, tagid, tag_name, scalets=None):
    data={"name": str(tag_name)}
    if scalets is not None:
        data["scalets"] = scalets
    return requests.put("https://api.vscale.io/v1/scalets/tags/"+str(tagid),
                        headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token},
                        data=json.dumps(data)
                        )


"""
Function delete_tag performs a DELETE-request at
https://api.vscale.io/v1/scalets/tags, deletes tag with a given tag id.
Token has to be provided as a str object.
Tag id has to be provided as a str object.
"""


def delete_tag(token, tagid):
    return requests.delete("https://api.vscale.io/v1/scalets/tags/"+
                           str(tagid),
                           headers={"X-Token": token}
                           )

"""
Function get_backups performs a GET-request at
https://api.vscale.io/v1/backups, returns list of backups.
Token has to be provided as a str object.
"""


def get_backups(token):
    return requests.get("https://api.vscale.io/v1/backups",
                        headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token}
                        )


"""
Function backup_info performs a GET-request at
https://api.vscale.io/v1/backups, returns info on a backup with a given id.
Token has to be provided as a str object.
Backup id has to be provided as a str object.
"""


def backup_info(token, backupid):
    return requests.get("https://api.vscale.io/v1/backups/"+str(backupid),
                        headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token}
                        )


"""
Function delete_backup performs a DELETE-request at
https://api.vscale.io/v1/backups, deletes backup with a given id.
Token has to be provided as a str object.
Backup id has to be provided as a str object.
"""


def delete_backup(token, backupid):
    return requests.delete("https://api.vscale.io/v1/backups/"+str(backupid),
                        headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token}
                        )


"""
Function relocate_backup performs a POST-request at 
https://api.vscale.io/v1/backups, relocates backup into new zone.
Token has to be provided as a str object.
Backup id has to be provided as a str object.
Destination has to be provided as a str object.
"""


def relocate_backup(token, backupid, destination):
    return requests.post("https://api.vscale.io/v1/backups/"+
                         str(backupid)+"/relocate",
                        headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token},
                        data={"destination": str(destination)}
                        )
