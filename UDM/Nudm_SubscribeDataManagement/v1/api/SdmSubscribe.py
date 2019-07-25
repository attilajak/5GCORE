# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse
import json


from .. import users
#from users import Users


class SDMSUBSCRIBE(Resource):
    global info
    def __init__(self):
        self.info = 0;

    def post(self,supi):
        SubscribeData = {"nfInstanceId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","implicitUnsubscribe":True,"expires":"2019-07-17T10:26:39.748Z","callbackReference":"string","monitoredResourceUris":["string"],"singleNssai":{"sst":0,"sd":"string"},"dnn":"string","subscriptionId":"string","plmnId":{"mcc":"string","mnc":"string"}}
        UdrSubscribeUri = "http://127.0.0.1:8080/subscription-data/63465656/context-data/sdm-subscriptions"
        headers = { "Content-Type" : "application/json"}
        SubscribeDatajson = json.dumps(SubscribeData)
        r = requests.post(UdrSubscribeUri,data=SubscribeDatajson,headers=headers)
        if r.status_code == 201:
            return SubscribeData,200
