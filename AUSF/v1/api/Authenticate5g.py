# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse
import json
import base64
#from sqlalchemy import Column, String, create_engine,LargeBinary
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

from .. import status
parser = reqparse.RequestParser()



CurrentPath = "~/5GCORE/AUSF/v1/api/Authenticate5g.py"

class AUTH5G(Resource):
    global info
    def __init__(self):
        pass
    def post(self,ueContextId):
        supi = ueContextId
        print(CurrentPath+":28   [AUSF][INFO]   "+"receive UE Authentication request with 5g AKA")
        print(CurrentPath+":29   [AUSF][INFO]   "+"BEGIN AUTHENTICATION...")
        return {"authResult": "AUTHENTICATION_SUCCESS","supi": supi,"kseaf": "string"}


    def delete(self):
        status.upStatus = b'"up de Config"'
        print("release up config")
