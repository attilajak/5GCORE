# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse


parser = reqparse.RequestParser()
parser.add_argument('imsi')
parser.add_argument('eNBID')
parser.add_argument('msisdn')
parser.add_argument('key')
parser.add_argument('opc')
parser.add_argument('ueIP')
parser.add_argument('ueListenPort')
parser.add_argument('CNTunnelID')

MCC_VALID = "208"
MNC_VALID = "93"
TAC_VALID = "1"

CurrentPath = "~/5GCORE/eNB/v1/api/UEDeRegisterRequest.py"

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
class UEDEREGISTERREQ(Resource):
	global info
	def __init__(self):
		self.info = info
		#print("hello")
	def get(self):
		data={'name':"hello",'passwd':"world"}
		return data,200

	def post(self):
		args = parser.parse_args()
		UEInitialDeregistrationReq = "http://"+args['ueIP']+":5001/namf-comm/v1/amfeNBInterface"
		MsgLoad = {"imsi":args['imsi'],"CNTunnelID":args['CNTunnelID'],"MsgType":"UEInitialDeregistrationReq","DeregistrationType":"SwitchOff","AccessType":"3GPP"}
		r = requests.post(UEInitialDeregistrationReq,data=MsgLoad)
		ret = b'"DeregistrationAccept"\n'
		if ret == r.content :
			print(CurrentPath+":34   [UE][INFO]   "+"DeregistrationAccept")
			#print(CurrentPath+":35   [VM][INFO]   "+"delete enp0s8 configuration")
			#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
			print(CurrentPath+":36   [eNB][INFO]  "+"Release AN Request")
			ReleaseANReq = "http://"+args['ueIP']+":5001/namf-comm/v1/amfeNBInterface"
			#ReleaseANReq = "http://172.20.10.9:5001/namf-comm/v1/amfeNBInterface"
			eNBMsg = {"eNBID":args['eNBID'],"MsgType":"ReleaseANReq"}
			r1 = requests.post(ReleaseANReq,data=eNBMsg)
			if r1.status_code == 200:
				print(CurrentPath+":52   [eNB][INFO]  "+"Release eNB success")
				return "DeregistrationAccept"
				#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
			else:
				print(CurrentPath+":54   [eNB][ERROR]  "+"Release eNB failure")
				return "DeregistrationFailed"
		else:
			print(CurrentPath+":55   [eNB][ERROR]  "+"UE Deregistration Failure")
			return "DeregistrationFailed"

	def delete(self):
		#if logs.eNBConnected>=1:
			#logs.eNBConnected-=1
			#stcs = logs.info+"                                                                                         "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
				#        +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n"
			#print(stcs)
		#else:
			#print("no eNB has been connected")
		return "delete_eNB_rsp"
