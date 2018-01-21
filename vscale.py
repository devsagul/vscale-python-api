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


"""
Function get_locations performs a GET-request at
https://api.vscale.io/v1/locations, returns list of data-centers, 
as well as images and configurations available at the centers.
Token has to be provided as a str object.
"""


def get_locations(token):
    return requests.get("https://api.vscale.io/v1/locations",
                        headers={"X-Token": token}
                        )


"""
Function get_images performs a GET-request at
https://api.vscale.io/v1/images, returns list of images, 
as well as data-centers and configurations available for the images.
Token has to be provided as a str object.
"""


def get_images(token):
    return requests.get("https://api.vscale.io/v1/images",
                        headers={"X-Token": token}
                        )


"""
Function get_rplans performs a GET-request at
https://api.vscale.io/v1/rplans, returns list of available configurations.
Token has to be provided as a str object.
"""


def get_rplans(token):
    return requests.get("https://api.vscale.io/v1/rplans",
                        headers={"X-Token": token}
                        )


"""
Function get_prices performs a GET-request at 
https://api.vscale.io/v1/billing/prices, returns list of prices for 
available configurations.
Token has to be provided as a str object.
"""


def get_prices(token):
    return requests.get("https://api.vscale.io/v1/billing/prices",
                        headers={"X-Token": token}
                        )


"""
Function list_ssh performs a GET-request at 
https://api.vscale.io/v1/sshkeys, returns list of SSH-keys on your account.
Token has to be provided as a str object.
"""


def list_ssh(token):
    return requests.get("https://api.vscale.io/v1/sshkeys",
                        headers={"X-Token": token}
                        )


"""
Function new_ssh performs a POST-request at
https://api.vscale.io/v1/sshkeys, adds new SSH-key to your account.
Token has to be provided as a str object.
Name has to be provided as a str object.
Public key has to be provided as a str object.
"""


def new_ssh(token, name, key):
    return requests.post("https://api.vscale.io/v1/sshkeys",
                         headers={"Content-Type":
                                  "application/json;charset=UTF-8",
                                  "X-Token": token},
                         data={"name": str(name),
                               "key": str(key)}
                         )


"""
Function new_ssh performs a DELETE-request at
https://api.vscale.io/v1/sshkeys, deletes SSH-key from your account.
Token has to be provided as a str object.
Key id has to be provided as a str object.
"""


def delete_ssh(token, keyid):
    return requests.delete("https://api.vscale.io/v1/sshkeys"+str(keyid),
                           headers={"Content-Type":
                                    "application/json;charset=UTF-8",
                                    "X-Token": token}
                           )


"""
Function notifications performs a GET-request at
https://api.vscale.io/v1/billing/notify, return information on notification 
policy.
Token has to be provided as a str object.
"""


def notifications(token):
    return requests.get("https://api.vscale.io/v1/billing/notify",
                        headers={"X-Token": token}
                        )


"""
Function set_notifications performs a PUT-request at 
https://api.vscale.io/v1/billing/notify, sets new notification policy.
Token has to be provided as a str object.
Balance has to be provided as a str object.
"""


def set_notifications(token, balance):
    return requests.put("https://api.vscale.io/v1/billing/notify",
                        headers={"X-Token": token},
                        data={"notify_balance": str(balance)}
                        )


"""
Function get_balance performs a GET-request at 
https://api.vscale.io/v1/billing/balance, returns information on balance.
Token has to be provided as a str object.
"""


def get_balance(token):
    return requests.get("https://api.vscale.io/v1/billing/balance",
                        headers={"X-Token": token}
                        )


"""
Function get_payments performs a GET-request at 
https://api.vscale.io/v1/billing/payments, returns information on last 
payments.
Token has to be provided as a str object.
"""


def get_payments(token):
    return requests.get("https://api.vscale.io/v1/billing/payments",
                        headers={"X-Token": token}
                        )


"""
Function consumption performs a GET-request at 
https://api.vscale.io/v1/billing/consumption, returns all the spendings 
from start date till end date excluding the latter one.
Token has to be provided as a str object.
Start and end date have to be provided as a str object in form YYYY-MM-DD.
"""


def consumption(token, start, end):
    return requests.get("https://api.vscale.io/v1/billing/consumption"+
                        "?start="+str(start)+"&end="+str(end),
                        headers={"X-Token": token}
                        )


"""
Function get_domains performs a GET-request at 
https://api.vscale.io/v1/domains/, returns list of domains.
Token has to be provided as a str object.
"""


def get_domains(token):
    return requests.get("https://api.vscale.io/v1/domains/",
                        headers={"X-Token": token}
                        )


"""
Function new_domain performs a POST-request at 
https://api.vscale.io/v1/domains/, creates new domain. 
Token has to be provided as a str object.
Name has to be provided as a str object.
BIND file has to be provided as a str object.
"""


def new_domain(token, name, bind_file=None):
    data = {"name": str(name)}
    if bind_file is not None and bind_file != "":
        data["bind_zone"] = bind_file
    return requests.post("https://api.vscale.io/v1/domains/",
                         headers={"Content-Type":
                                  "application/json;charset=UTF-8",
                                  "X-Token": token},
                         data=json.loads(data)
                         )


"""
Function domain_info performs a GET-request at 
https://api.vscale.io/v1/domains/, gets information of the domain with 
a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
"""


def domain_info(token, domainid):
    return requests.get("https://api.vscale.io/v1/domains/"+str(domainid),
                        headers={"X-Token": token}
                        )


"""
Function update_domain performs a PATCH-request at 
https://api.vscale.io/v1/domains/, updates information of the domain 
with a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
Tags have to be provided as a list.
"""


def update_domain(token, domainid, tags):
    return requests.patch("https://api.vscale.io/v1/domains/"+str(domainid),
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token},
                          data=json.loads({"tags": str(tags)})
                          )


"""
Function delete_domain performs a DELETE-request at 
https://api.vscale.io/v1/domains/, deletes the domain with a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
"""


def delete_domain(token, domainid):
    return requests.delete("https://api.vscale.io/v1/domains/"+str(domainid),
                          headers={"Content-Type":
                                   "application/json;charset=UTF-8",
                                   "X-Token": token}
                           )


"""
Function domain_records performs a GET-request at 
https://api.vscale.io/v1/domains/, returns list of records of the domain 
with a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
"""


def domain_records(token, domainid):
    return requests.get("https://api.vscale.io/v1/domains/"+str(domainid)+
                        "/records/",
                        headers={"X-Token": token}
                        )


"""
Function set_domain_record performs a POST-request at 
https://api.vscale.io/v1/domains/, creates new resource record for 
the domain with a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
Data has to be provided as a dict object.
"""


def set_domain_record(token, domainid, data):
    return requests.post("https://api.vscale.io/v1/domains/"+str(domainid)+
                         "/records/",
                         headers={"Content-Type":
                                  "application/json;charset=UTF-8",
                                  "X-Token": token},
                         data=json.loads(data)
                         )


"""
Function update_domain_record performs a PUT-request at 
https://api.vscale.io/v1/domains/, updates resource record with a given 
record id for the domain with a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
Record id has to be provided as a str object.
Data has to be provided as a dict object.
"""


def update_domain_record(token, domainid, recordid, data):
    return requests.put("https://api.vscale.io/v1/domains/"+str(domainid)+
                        "/records/"+str(recordid),
                        headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token},
                        data=json.loads(data)
                        )


"""
Function delete_domain_record performs a DELETE-request at 
https://api.vscale.io/v1/domains/, deletes resource record with a given 
record id for the domain with a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
Record id has to be provided as a str object.
"""


def delete_domain_record(token, domainid, recordid):
    return requests.delete("https://api.vscale.io/v1/domains/"+
                           str(domainid)+"/records/"+str(recordid),
                           headers={"Content-Type":
                                 "application/json;charset=UTF-8",
                                 "X-Token": token}
                           )


"""
Function get_domain_record performs a GET-request at 
https://api.vscale.io/v1/domains/, gets resource record with a given 
record id for the domain with a given domain id.
Token has to be provided as a str object.
Domain id has to be provided as a str object.
Record id has to be provided as a str object.
"""


def get_domain_record(token, domainid, recordid):
    return requests.get("https://api.vscale.io/v1/domains/"+
                        str(domainid)+"/records/"+str(recordid),
                        headers={"X-Token": token}
                        )
