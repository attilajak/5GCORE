# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse


parser = reqparse.RequestParser()
parser.add_argument('suci')
parser.add_argument('eNBID')
parser.add_argument('msisdn')
parser.add_argument('key')
parser.add_argument('opc')
parser.add_argument('ueIP')
parser.add_argument('ueListenPort')

MCC_VALID = "262"
MNC_VALID = "00"
TAC_VALID = "A198"

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
class UEREGISTERREQ(Resource):
	global info
	def __init__(self):
		self.info = info
		#print("hello")
	def get(self):
		data={'name':"hello",'passwd':"world"}
		return data,200

	def post(self):
		args = parser.parse_args()
		InitialLoopLog = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
		Msg = {"MsgType":"InitialLoopLog"}
		r = requests.post(InitialLoopLog, data=Msg)
		print(CurrentPath+":26   "+"[eNB][INFO]   "+"Be Ready to Initiate connection to AMF for N2 Signaling(eNB<->AMF)  ...")
		print(CurrentPath+":27   "+"[eNB][INFO]   "+"call AMF amfeNBInterface operation with MsgType(eNBConnect2AMF) and http method(post)")
		print(CurrentPath+":28   "+"[eNB][INFO]   "+"post http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
		ConnecteNB2AMF = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
		eNBInfo = {"ID":args['eNBID'],"MCC":MCC_VALID,"MNC":MNC_VALID,"TAC":TAC_VALID,"MsgType":"eNBConnect2AMF"}
		r1 = requests.post(ConnecteNB2AMF, data=eNBInfo)
		ret = b'"eNBConnect2AMFSuccess"\n'
		if ret == r1.content :
			print(CurrentPath+":34   "+"[eNB][INFO]   "+(r1.content).decode())
			print(CurrentPath+":35   "+"[UE][INFO]   "+"Be Ready to initial connection to AMF via eNB for N1 Signaling(UE<->AMF) ...")
			print(CurrentPath+":36   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(UEConnect2AMF) and http method(post)")
			print(CurrentPath+":37   "+"[UE][INFO]   "+"http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
			UEConnect2AMFViaeNB = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
			UEConnectionInfo = {"eNBID":args['eNBID'],"MsgType":"UEConnect2AMF"}
			r2 = requests.post(UEConnect2AMFViaeNB,data=UEConnectionInfo)
			ret = b'"UEConnected2AMFSuccess"\n'
			if ret == r2.content :
				print(CurrentPath+":43   "+"[UE][INFO]   "+(r2.content).decode())
				print(CurrentPath+":44   "+"[UE][INFO]   "+"Be Ready to registe to AMF ...")
				print(CurrentPath+":45   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(UERegisterRequest) and http method(post)")
				print(CurrentPath+":46   "+"[UE][INFO]   "+"http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
				UERegisterRequestUri = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
				UEInfo = {"suci":args['suci'],"msisdn":"32435235366","key":"8baf473f2f8fd09487cccbd7097c6862","opc":"e734f8734007d6c5ce7a0508809e7e9c","MsgType":"UERegisterRequest","ueListenPort":args['ueIP']+":"+args['ueListenPort']}
				r3 = requests.post(UERegisterRequestUri,data=UEInfo)
				ret = b'"UERegister2AMFSuccess"\n'
				if ret == r3.content :
					return "UERegister2AMFSuccess"
					print(CurrentPath+":52   [UE][INFO]   "+(r3.content).decode())
					print(CurrentPath+":53   [UE][INFO]   "+"response AMF Identity Request")
					print(CurrentPath+":54   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(IdentityRsp) and http method(post)")
					print(CurrentPath+":55   "+"[UE][INFO]   "+"http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
					IdentityRsp = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
					RspMsg = {"PEI":"imei-089322137616763","MsgType":"IdentityRsp"}
					r4 = requests.post(IdentityRsp,data=RspMsg)
					if r4.status_code == 200:
						print(CurrentPath+":60   [UE][INFO]   "+"IdentityRspSuccess")
						print(CurrentPath+":61   [UE][INFO]   "+"Be Ready to initial PDU SESSION ESTABILISHMENT REQUEST")
						print(CurrentPath+":62   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(PDUSessionEstabilishReq) and http method(post)")
						print(CurrentPath+":63   "+"[UE][INFO]   "+"http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
						PDUSessionEstabilishReq = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
						NASMsg = {"suci":args['suci'],"PDUSessionID":"10","RequestType":"InitialRequest","PDUType":"IPv4v6","MsgType":"PDUSessionEstabilishReq","CreateDataConnection":"TRUE"}
						r5 = requests.post(PDUSessionEstabilishReq,data=NASMsg)
						ret = b'"PDUSessionEstablishmentAccept"\n'
						if ret == r5.content :
							print("[UE][INFO]   PDUSessionEstablishmentAccept")
						else:
							print((r5.content).decode())
							print("[UE][ERROR]  PDUSessionEstablishmentNotAccept")
					else :
						print(CurrentPath+":74   [UE][ERROR]  "+"IdentityRspFailure")
				else :
					print(CurrentPath+":76   [UE][ERROR]  "+(r3.content).decode())
			else :
				print(CurrentPath+":78   [UE][ERROR]  "+(r2.content).decode())
		else :
			print(CurrentPath+":68   "+"[eNB][ERROR]   "+(r1.content).decode())

	def delete(self):
		#if logs.eNBConnected>=1:
			#logs.eNBConnected-=1
			#stcs = logs.info+"                                                                                         "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
				#        +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n"
			#print(stcs)
		#else:
			#print("no eNB has been connected")
		return "delete_eNB_rsp"
