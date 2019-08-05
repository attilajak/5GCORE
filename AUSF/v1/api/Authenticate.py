# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse
import json
from simconf import get_ip
import base64


#from sqlalchemy import Column, String, create_engine,LargeBinary
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()
headers = { "Content-Type" : "application/json"}
from .. import status
parser = reqparse.RequestParser()
parser.add_argument('supiOrSuci')
parser.add_argument('servingNetworkName')
parser.add_argument('resynchronizationInfo')
parser.add_argument('pei')
parser.add_argument('traceData')


CurrentPath = "~/5GCORE/AUSF/v1/api/Authenticate.py"

class AUTH(Resource):
    global info
    def __init__(self):
    	pass
    def post(self):
    	args = parser.parse_args()
        print(CurrentPath+":28   [AUSF][INFO]   "+"receive UE Authentication request")
    	print(CurrentPath+":29   [AUSF][INFO]   "+"BEGIN AUTHENTICATION...")
    	print(CurrentPath+":31   [AUSF][INFO]   "+"call UDM UEAuthentication operation with ue suci("+args['supiOrSuci']+") and http method(post)")
    	print(CurrentPath+":32   [AUSF][INFO]   "+"http://127.0.0.1:5007/nudm-ueau/v1/"+args['supiOrSuci']+"/security-information/generate-auth-data")
        GenerateAuthFromUDM =  "http://127.0.0.1:5007/nudm-ueau/v1/"+args['supiOrSuci']+"/security-information/generate-auth-data"
    	AuthenticationInfoRequest = {"servingNetworkName": args['servingNetworkName'],"resynchronizationInfo": {"rand": "12345678123456781234567812345678","auts": "1234567812345678123456781234"},"ausfInstanceId": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        AuthenticationInfoRequestjson = json.dumps(AuthenticationInfoRequest)
    	r = requests.post(GenerateAuthFromUDM,data=AuthenticationInfoRequestjson,headers=headers)
    	if r.status_code == 200 :
            print(CurrentPath+":50   [AUSF][INFO]   "+"authentication finished with successful result")
            data = r.json()
            print(data)
            authCtxId = data['supi']
            return {"authType": "5G_AKA","5gAuthData": {"rand":"da23aec51529D7cbBE0d8d5bfaeF313c","hxresStar":"8A9c5f27A2BdBd5EA62f295e08422B03","autn":"C1bd49D80c3894ECe6222A23dD090317"},"_links": {"additionalProperties": "linkuri"} },201,{'Location': 'http://'+get_ip()+':5020/nausf-auth/v1/ue-authentications/'+authCtxId}


    def delete(self):
        status.upStatus = b'"up de Config"'
        print("release up config")
