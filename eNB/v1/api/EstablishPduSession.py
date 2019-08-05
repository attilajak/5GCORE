# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import Flask,request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse
import json

headers = { "Content-Type" : "application/json"}
parser = reqparse.RequestParser()
parser.add_argument('DNN')
parser.add_argument('PduSessionId')
parser.add_argument('snssai')
parser.add_argument('sst')
parser.add_argument('sd')
parser.add_argument('ueIP')
parser.add_argument('ueListenPort')

MCC_VALID = "262"
MNC_VALID = "00"
TAC_VALID = "1"

CurrentPath = "~/5GCORE/eNB/v1/api/UERegisterRequest.py"

info = "                                                                                         "+"|--------------------------------------------------------------|\n"\
	  +"                                                                                         "+"|                       eNB infos table                        |\n"\
	  +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n"\
	  +"                                                                                         "+"        ID            MCC             MNC             TAC\n"\

def display(eNBInfo):
	print(eNBInfo)
	#print("|--------------|---------------|---------------|---------------|")
	#print("     ID            MCC             MNC             TAC")
	#print("|--------------|---------------|---------------|---------------|")
	#print("    "+ID+"    ","    "+MCC+"    ","       "+MNC+"      ","       "+TAC+"      ")
class ESTABLISHPDU(Resource):
	global info
	def __init__(self):
		self.info = info
		#print("hello")
	def get(self):
		data={'name':"hello",'passwd':"world"}
		return data,200

	def post(self):
		args = parser.parse_args()
		print(CurrentPath+":53   [UE][INFO]   "+"response AMF Identity Request")
		print(CurrentPath+":54   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(IdentityRsp) and http method(post)")
		print(CurrentPath+":55   "+"[UE][INFO]   "+"http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
		IdentityRsp = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
		RspMsg = {"PEI":"2769169126891","MsgType":"IdentityRsp"}
		RspMsgjson = json.dumps(RspMsg)
		r4 = requests.post(IdentityRsp,data=RspMsgjson,headers=headers)
		if r4.status_code == 200:
			print(CurrentPath+":60   [UE][INFO]   "+"IdentityRspSuccess")
			print(CurrentPath+":61   [UE][INFO]   "+"Be Ready to initial PDU SESSION ESTABILISHMENT REQUEST")
			print(CurrentPath+":62   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(PDUSessionEstabilishReq) and http method(post)")
			print(CurrentPath+":63   "+"[UE][INFO]   "+"http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
			reqjson = request.get_json(force=True)
			print(reqjson)
			PDUSessionEstabilishReq = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
			NASMsg = {"DNN":reqjson['DNN'],"PduSessionId":reqjson['PduSessionId'],"snssai": reqjson['snssai'],"RequestType":"InitialRequest","PDUType":"IPv4v6","MsgType":"PDUSessionEstabilishReq","CreateDataConnection":"TRUE"}
			NASMsgjson = json.dumps(NASMsg)
			r5 = requests.post(PDUSessionEstabilishReq,data=NASMsgjson,headers=headers)
			ret = b'"PDUSessionEstablishmentAccept"\n'
			if ret == r5.content :
				print((r5.content).decode())
				print("[UE][INFO]   PDUSessionEstablishmentAccept")
				return "PDUSessionEstablishmentAccept"
			else:
				print((r5.content).decode())
				print("[UE][ERROR]  PDUSessionEstablishmentNotAccept")
				return "PDUSessionEstablishmentNotAccept"
		else :
			print(CurrentPath+":74   [UE][ERROR]  "+"IdentityRspFailure")

	def delete(self):
		#if logs.eNBConnected>=1:
			#logs.eNBConnected-=1
			#stcs = logs.info+"                                                                                         "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
				#        +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n"
			#print(stcs)
		#else:
			#print("no eNB has been connected")
		return "delete_eNB_rsp"
