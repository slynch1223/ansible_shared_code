#!/usr/bin/python

# Data Types
dictionary = dict(str="string", int=1, bool=True)

list = ["string", 123, True]

#######################################################################
# Use Environment Variables
import os

username = os.getenv("username")
password = os.getenv("password")


#######################################################################
# Use Time for sleep
import time

time.sleep(3)

#######################################################################
# Get Current Timestamps
import datetime

now = datetime.datetime.now()
timestamp = now.strftime("%m/%d/%Y %I:%M:%S %p")

#######################################################################
# Create Random Passphrase
import random

passphrase_length = 12
passphrase = "".join([random.choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%") for i in range(passphrase_length)])

#######################################################################
# Read a CSV file
import csv

with open("Path to CVS file", newline="") as csvfile:
    for i, row in enumerate(csv.DictReader):
        print(row["Column_Name"])

#######################################################################
# Ignore URL Certificate Validation Warnings
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#######################################################################
# Make Different HTTP Requests with different Auth Types
import requests


def http_basic_auth_get(url):
    try:
        req = requests.get(url=url, auth=(username, password), verify=False)

        if not req.ok:
            print(str(req.json()))
            print(req.reason)
        return req.json()
    except Exception as err:
        print(str(err))
        print(req.reason)


def http_token_auth_get(url):
    try:
        req = requests.get(url=url, headers={"Authorization": "token " + "my_token"}, verify=False)

        if not req.ok:
            print(str(req.json()))
            print(req.reason)
        return req.json()
    except Exception as err:
        print(str(err))
        print(req.reason)


def http_basic_auth_post(url, body):
    try:
        req = requests.post(url=url, auth=(username, password), verify=False, json=body)

        if not req.ok:
            print(str(req.json()))
            print(req.reason)
        return req.json()
    except Exception as err:
        print(str(err))
        print(req.reason)


def http_token_auth_post(url, body):
    try:
        req = requests.post(url=url, headers={"Authorization": "token " + "my_token"}, verify=False, json=body)

        if not req.ok:
            print(str(req.json()))
            print(req.reason)
        return req.json()
    except Exception as err:
        print(str(err))
        print(req.reason)


#######################################################################
# Use pyodbc to Query a SQL database
import pyodbc

connection_string = "DRIVER={ODBC Drvier 17 ofr SQL Server};SERVER=mySqlServer.com; DATABASE=myDatabase; UID=username; PWD=password"


def sql_select(query, conn_string):
    try:
        connection = pyodbc.connect(conn_string)
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        connection.close()
        return results
    except Exception as err:
        print(str(err))


def sql_update(query, conn_string):
    try:
        connection = pyodbc.connect(conn_string)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        count = cursor.rowcount
        connection.close()
        return count
    except Exception as err:
        print(str(err))


#######################################################################
# Function to sort list by object property

my_list = [dict(name="Bob"), dict(name="Susan")]

sorted_list = sorted(my_list, key=lambda x: x["name"])
