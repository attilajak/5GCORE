# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
import json
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse

from .. import users
#from users import Users



MCC_VALID = "208"
MNC_VALID = "93"
TAC_VALID = "1"

info = "                                                                                         "+"|--------------------------------------------------------------|\n"\
      +"                                                                                         "+"|                       eNB infos table                        |\n"\
      +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n"\
      +"                                                                                         "+"        ID            MCC             MNC             TAC\n"\
      +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n"

def display(eNBInfo):
    print(eNBInfo)
    #print("|--------------|---------------|---------------|---------------|")
    #print("     ID            MCC             MNC             TAC")
    #print("|--------------|---------------|---------------|---------------|")
    #print("    "+ID+"    ","    "+MCC+"    ","       "+MNC+"      ","       "+TAC+"      ")
class AMF3GPPREGISTER(Resource):
    global info
    def __init__(self):
        self.info = info
        #print("hello")


    def put(self,ueId):
        #Write amf UE context data into UDR
        SendtoUDRMsg = "http://127.0.0.1:8080/subscription-data/123/context-data/amf-3gpp-access"
        access3gppInfo = { "amfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "supportedFeatures": "string", "purgeFlag": True, "pei": "string", "deregCallbackUri": "string", "pcscfRestorationCallbackUri": "string", "initialRegistrationInd": True, "guami": { "plmnId": { "mcc": "string", "mnc": "string" }, "amfId": "string" }, "backupAmfInfo": [ { "backupAmf": "string", "guamiList": [ { "plmnId": { "mcc": "string", "mnc": "string" }, "amfId": "string" } ] } ], "drFlag": True, "urrpIndicator": True, "amfEeSubscriptionId": "string", "epsInterworkingInfo": { "epsIwkPgws": { "additionalProp1": { "pgwFqdn": "string", "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }, "additionalProp2": { "pgwFqdn": "string", "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }, "additionalProp3": { "pgwFqdn": "string", "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" } } } }
        headers = { "Content-Type" : "application/json"}
        access3gppInfojson = json.dumps(access3gppInfo)
        r = requests.put(SendtoUDRMsg,data=access3gppInfojson,headers=headers)
        if r.status_code == 200 :
            return access3gppInfo,201
