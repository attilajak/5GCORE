# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse
import json
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
    	print(CurrentPath+":30   [AUSF][INFO]   "+"GET UE INFOS FROM UDM...")
    	print(CurrentPath+":31   [AUSF][INFO]   "+"call UDM UEAuthentication operation with ue imsi("+"208930000000001"+") and http method(post)")
    	#print(CurrentPath+":32   [AUSF][INFO]   "+"post http://127.0.0.1:5007/nudm-ueAuth/v1/Get")
        print(CurrentPath+":32   [AUSF][INFO]   "+"http://127.0.0.1:5007/nudm-ueau/v1/"+args['supiOrSuci']+"/security-information/generate-auth-data")
        GenerateAuthFromUDM =  "http://127.0.0.1:5007/nudm-ueau/v1/"+args['supiOrSuci']+"/security-information/generate-auth-data"
    	UEImsi = {"imsi":"208930000000001"}
        AuthenticationInfoRequest = {"servingNetworkName": "5G:mnc123.mcc456.3gppnetwork.org","resynchronizationInfo": {"rand": "12345678123456781234567812345678","auts": "1234567812345678123456781234"},"ausfInstanceId": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        #r = requests.post(GetUEInfoFromUDM,data=UEImsi)
        AuthenticationInfoRequestjson = json.dumps(AuthenticationInfoRequest)
    	r = requests.post(GenerateAuthFromUDM,data=AuthenticationInfoRequestjson,headers=headers)
    	#print(((r.content).decode()))
    	#data = json.loads(eval((r.content).decode()))
    	#print(data,type(data))
    	#print(data['key'],args['key'])
    	#if not operator.eq(args['imsi'],data['imsi']):
    		#print(CurrentPath+":41   [AUSF][INFO]   "+"authentication finished with failed result: AUSFGotWrongMsgStoreInUDMMysql")
    		#return "AUSFGotWrongMsgStoreInUDMMysql"
    	#elif not operator.eq(args['key'],data['key']):
    		#print(CurrentPath+":44   [AUSF][INFO]   "+"authentication finished with failed result: UEAuthFailure")
    		#return "UEAuthFailure"
    	#elif not operator.eq(args['opc'],data['opc']):
    		#print(CurrentPath+":47   [AUSF][INFO]   "+"authentication finished with failed result: UEAuthFailure")
    		#return "UEAuthFailure"
    	#else :
        if r.status_code == 200 :
            print(CurrentPath+":50   [AUSF][INFO]   "+"authentication finished with successful result")
            data = r.json()
            return {"_links": "8888888" }


    def delete(self):
        status.upStatus = b'"up de Config"'
        print("release up config")
