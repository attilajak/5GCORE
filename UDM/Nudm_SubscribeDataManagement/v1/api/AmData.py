# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import Flask,request, g
import requests
import json
from simconf import conf_json
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse
from .. import users
#from users import Users

parser = reqparse.RequestParser()

class AMDATA(Resource):
    global info
    def __init__(self):
        self.info = 0;

    def get(self,supi):
        servingPlmnId = request.args.get("plmn-id")
        ueId = "imsi-"+supi
        UdrGetAmDataUri =  "http://"+conf_json['udr_sub_ip_address']+":"+conf_json['udr_sub_port_number']+"/subscription-data/"+ueId+"/"+servingPlmnId+"/provisioned-data/am-data"
        r = requests.get(UdrGetAmDataUri)
        if r.status_code == 200:
            UdrAmData = r.json()
            print(UdrAmData)
            data={"gpsis":UdrAmData['gpsis'],"internalGroupIds":UdrAmData['internalGroupIds'],"nssai":UdrAmData['nssai'],"ratRestrictions":UdrAmData['ratRestrictions'],"forbiddenAreas":UdrAmData['forbiddenAreas'],"coreNetworkTypeRestrictions":UdrAmData['coreNetworkTypeRestrictions'],"ueUsageType":UdrAmData['ueUsageType'],"mpsPriority":UdrAmData['mpsPriority'],"mcsPriority":UdrAmData['mcsPriority'],"dlPacketCount":UdrAmData['dlPacketCount'],"sorInfo":UdrAmData['sorInfo'],"upuInfo":UdrAmData['upuInfo'],"micoAllowed":UdrAmData['micoAllowed'],"sharedAmDataIds":UdrAmData['sharedAmDataIds'],"subscribedDnnList":UdrAmData['subscribedDnnList']}
            headers = { "Content-Type" : "application/json"}
            datajson = json.dumps(data)
            return data,200
