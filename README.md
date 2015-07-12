# Technicolor backend test

Developed in python and mongodb

Install python version 2.7 and mongodb 2.4.9

Python extensions

flask
simplejson
pymongo
flask-login
bson


# REST Api's information attached in test_backend.json file


# Login

http://localhost:1110/loginuser

input

{"username": "9902616691", "password": "sree123"}

# Get users

http://localhost:1110/get_users

input

{"city": "bangalore", "profession": "doctor"}

# Get Mongo DB Status

http://localhost:1110/get_status

# Get Files

http://localhost:1110/get_files

input

{"path": "/home/sreenath/Documents/projects/analytics/analytics/lib"}




