# -*- coding: utf-8 -*-
# created by Sreenath P
from analytics import app
from analytics.lib.user import manageuser

m = manageuser.ManageUser()
m.AddUser({'_id': '9902616694', 'username': 'arun', 'password': 'password123', 'role': 'user',
           'name': 'Arun S', 'phone': '9902616694', 'email': 'arun@gmail.com',
           "city": "chennai", "profession": "software engineer"})