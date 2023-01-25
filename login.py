#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret 
import os 
from http.cookies import SimpleCookie

# run cgi_server.py
# make script executable chmod +x login.py
# test on browser with localhost:8080/login.py

# Question 4

# set the cgi form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password

# Question 5
# set a cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None 

# extract username and password from browser cookie if exists
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value 

cookie_ok = cookie_username == secret.username and \
            cookie_password == secret.password

# if cookie is correct set username and password using the cookie
if cookie_ok:
    username = cookie_username
    password = cookie_password

# prints to html
print("Content-Type: text/html")

# if cookie is not there set it
if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

# load html pages
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    # print(login_page())
    # # report the values of the POSTed data in the html
    # print("username:", username)
    # print("password:", password) 
    print(after_login_incorrect())

# Question 7, 8
# can set cookies from the web browser console:
# javascript:document.cookie="username=Felipe"
# javascript:document.cookie="password=password"