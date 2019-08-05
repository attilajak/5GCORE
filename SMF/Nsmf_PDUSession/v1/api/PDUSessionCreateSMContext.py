# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import Flask,request, g
import requests
import json
from flask_restful import Resource,reqparse
from simconf import get_ip

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

parser = reqparse.RequestParser()
parser.add_argument('supi')
parser.add_argument('pduSessionId')
parser.add_argument('ueIpv4Addr')
parser.add_argument('portNumber')



headers = { "Content-Type" : "application/json"}

CurrentPath = "~/5GCORE/SMF/Nsmf_PDUSession/v1/api/PDUSessionCreateSMContext.py"

##create thread
from threading import Thread


def SMFDoingSomething(args):
	print(CurrentPath+":30   [SMF][INFO]   "+"UPF selection ...")
	print(CurrentPath+":31   [SMF][INFO]   "+"SMF SENDS N4 SESSION ESTABILISHMENT REQUEST TO UPF")
	print(CurrentPath+":32   [SMF][INFO]   "+"post http://127.0.0.1:5012/nupf/v1/UpfSmfInterface")
	N4SessionEstabilishmentReq = "http://127.0.0.1:5012/nupf/v1/UpfSmfInterface"
	N4SessionMsg = {"imsi":"208930000000001","CNTunnelID":"23124","InactivityTimer":"20s","MsgType":"N4SessionEstabilishmentReq","CreateDataConnection":"CreateDataConnection"}
	r = requests.post(N4SessionEstabilishmentReq,data=N4SessionMsg)
	if r.status_code == 200:
		print(CurrentPath+":37   [SMF][INFO]   "+"SMF RECEIVES N4 SESSION ESTABILISHMENT RESPONSE FROM UPF")
		data = json.loads(eval((r.content).decode()))
		print(CurrentPath+":39   [SMF][INFO]   "+"transfer n1n2messages to AMF")
		print(CurrentPath+":40   [SMF][INFO]   "+"call AMF N1N2MessagesTransfer operation")
		print(CurrentPath+":36   [SMF][INFO]   "+"post http://127.0.0.1:5001/namf-comm/v1/"+data['imsi']+"/n1-n2-messages")
		N1N2MsgTransfer = "http://127.0.0.1:5001/namf-comm/v1/"+data['imsi']+"/n1-n2-messages"
		MsgSMF2UE = {"AllocatedUEIp":"172.16.0.2","CNTunnelID":data['CNTunnelID'],"UPFURI":data['UPFURI']}
		r1 = requests.post(N1N2MsgTransfer,data=MsgSMF2UE)
		if r1.status_code == 200:
			print(CurrentPath+":41   [SMF][INFO]   SMF SEND BEARER INFO TO AMF")
		else:
			print(CurrentPath+":43   [SMF][ERROR]  "+"SMF SEND BEARER INFO TO AMF FAILURE")
	else:
		print(CurrentPath+":45   [SMF][ERROR]  "+"SMF SENDS N4 SESSION ESTABILISHMENT REQUEST FAILURE")

class SMContextCreate(Resource):

    def __init__(self):
    	pass

    def get(self):
        data = "this is not supported method"
        print(data)
        return data,400

    def post(self):
		args = parser.parse_args()
		reqjson = request.get_json(force=True)
		print(CurrentPath+":59   [SMF][INFO]   "+"Receved SmCreateContextData From AMF:")
		print(CurrentPath+":60   [SMF][INFO]   "+"Handling PDUSessionCreateReq From AMF ...")
		print(CurrentPath+":27   [SMF][INFO]   "+"PCF selection ...")
		print(CurrentPath+":31   [SMF][INFO]   "+"SMF SEND PCF POLICY ASSOCIATION ESTABILISHMENT TO PCF")
		print(CurrentPath+":32   [SMF][INFO]   "+"post http://127.0.0.1:8081/npcf-smpolicycontrol/v1/sm-policies")
		PolicyAssociationReqUri = "http://127.0.0.1:8081/npcf-smpolicycontrol/v1/sm-policies"
		#SMPolicyContextData = {"accNetChId":{"accNetChaIdValue":0,"refPccRuleIds":["string"],"sessionChScope":True},"chargEntityAddr":{"anChargIpv4Addr":"198.51.100.1","anChargIpv6Addr":"2001:db8:85a3::8a2e:370:7334"},"gpsi":"string","supi":reqjson['supi'],"interGrpIds":["a7483748-123-244-35"],"pduSessionId": reqjson['pduSessionId'],"pduSessionType":"IPV4","chargingcharacteristics":"string","dnn":"string","notificationUri":"string","accessType":"3GPP_ACCESS","servingNetwork":{"mnc":"234","mcc":"244"},"userLocationInfo":reqjson['ueLocation'],"ueTimeZone":"string","pei":"string","ipv4Address":"198.51.100.1","ipv6AddressPrefix":"2001:db8:abcd:12::0/64","ipDomain":"string","subsSessAmbr":{"uplink":"06877259326617319404306103 Mbps","downlink":"06877259326617319404306103 Mbps"},"subsDefQos":{"5qi":0,"arp":{"preemptCap":"NOT_PREEMPT","preemptVuln":"NOT_PREEMPTABLE","priorityLevel":1},"priorityLevel":1},"numOfPackFilter":0,"online":True,"offline":True,"3gppPsDataOffStatus":True,"refQosIndication":True,"traceReq":{"traceRef":"773182-56B6DF","traceDepth":"MEDIUM","neTypeList":"dbeDB987cfE5B1ad8f","eventList":"F90","collectionEntityIpv4Addr":"198.51.100.1","collectionEntityIpv6Addr":"2001:db8:85a3::8a2e:370:7334","interfaceList":"F90"},"sliceInfo":{"sst":0,"sd":"38fB1b"},"servNfId":{"servNfInstId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","guami":{"plmnId":{"mcc":"234","mnc":"244"},"amfId":"EF7d5D"},"anGwAddr":{"anGwIpv4Addr":"198.51.100.1","anGwIpv6Addr":"2001:db8:85a3::8a2e:370:7334"}},"suppFeat":"bECfA4","smfId":"3fa85f64-5717-4562-b3fc-2c963f66afa7","recoveryTime":"2019-07-23T17:03:30.926Z"}
		SMPolicyContextData = {"accNetChId":{"accNetChaIdValue":0,"refPccRuleIds":["string"],"sessionChScope":True},"chargEntityAddr":{"anChargIpv4Addr":"198.51.100.1","anChargIpv6Addr":"2001:db8:85a3::8a2e:370:7334"},"gpsi":"string","supi":reqjson['supi'],"interGrpIds":["a7483748-123-244-35"],"pduSessionId": reqjson['pduSessionId'],"pduSessionType":"IPV4","chargingcharacteristics":"string","dnn":"string","notificationUri":"string","accessType":"3GPP_ACCESS","servingNetwork":{"mnc":"234","mcc":"244"},"userLocationInfo":{"eutraLocation":{"tai":{"plmnId":{"mcc":"234","mnc":"244"},"tac":"A198"},"ecgi":{"plmnId":{"mcc":"234","mnc":"244"},"eutraCellId":"8198677"},"ageOfLocationInformation":0,"ueLocationTimestamp":"2019-07-23T17:03:30.925Z","geographicalInformation":"458A884888488456","geodeticInformation":"458A8848884884566789","globalNgenbId":{"plmnId":{"mcc":"234","mnc":"244"},"ngeNbId":"MacroNGeNB-Ab123"}},"nrLocation":{"tai":{"plmnId":{"mcc":"234","mnc":"244"},"tac":"A198"},"ncgi":{"plmnId":{"mcc":"234","mnc":"244"},"nrCellId":"458A88488"},"ageOfLocationInformation":0,"ueLocationTimestamp":"2019-07-23T17:03:30.925Z","geographicalInformation":"458A884888488456","geodeticInformation":"458A8848884884566789","globalGnbId":{"plmnId":{"mcc":"234","mnc":"244"},"ngeNbId":"MacroNGeNB-Ab123"}},"n3gaLocation":{"n3gppTai":{"plmnId":{"mcc":"234","mnc":"244"},"tac":"A198"},"n3IwfId":"888F85","ueIpv4Addr":"127.0.0.1","ueIpv6Addr":"2001:db8:85a3::8a2e:370:7334","portNumber": 5555}},"ueTimeZone":"string","pei":"string","ipv4Address":"198.51.100.1","ipv6AddressPrefix":"2001:db8:abcd:12::0/64","ipDomain":"string","subsSessAmbr":{"uplink":"06877259326617319404306103 Mbps","downlink":"06877259326617319404306103 Mbps"},"subsDefQos":{"5qi":0,"arp":{"preemptCap":"NOT_PREEMPT","preemptVuln":"NOT_PREEMPTABLE","priorityLevel":1},"priorityLevel":1},"numOfPackFilter":0,"online":True,"offline":True,"3gppPsDataOffStatus":True,"refQosIndication":True,"traceReq":{"traceRef":"773182-56B6DF","traceDepth":"MEDIUM","neTypeList":"dbeDB987cfE5B1ad8f","eventList":"F90","collectionEntityIpv4Addr":"198.51.100.1","collectionEntityIpv6Addr":"2001:db8:85a3::8a2e:370:7334","interfaceList":"F90"},"sliceInfo":{"sst":0,"sd":"38fB1b"},"servNfId":{"servNfInstId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","guami":{"plmnId":{"mcc":"234","mnc":"244"},"amfId":"EF7d5D"},"anGwAddr":{"anGwIpv4Addr":"198.51.100.1","anGwIpv6Addr":"2001:db8:85a3::8a2e:370:7334"}},"suppFeat":"bECfA4","smfId":"3fa85f64-5717-4562-b3fc-2c963f66afa7","recoveryTime":"2019-07-23T17:03:30.926Z"}
		SMPolicyContextDatajson = json.dumps(SMPolicyContextData)
		r = requests.post(PolicyAssociationReqUri,data=SMPolicyContextDatajson,headers=headers)
		if r.status_code == 201:
			print(CurrentPath+":41   [SMF][INFO]   SMF COMPLETES POLICY ASSOCIATION ESTABLISHMENT WITH PCF")
			t = Thread(target = SMFDoingSomething,args=(args,))
			t.start()
		else:
			print(CurrentPath+":41   [SMF][INFO]   SMF FAILS POLICY ASSOCIATION ESTABLISHMENT WITH PCF")
		SmContextCreatedData = {"recoveryTime":{},"hSmfUri":"hSmfUri","n2SmInfo":{"contentId":"contentId"},"allocatedEbiList":[{"epsBearerId":2,"arp":{"priorityLevel":9,"preemptCap":"","preemptVuln":""}},{"epsBearerId":2,"arp":{"priorityLevel":9,"preemptCap":"","preemptVuln":""}}],"hoState":"","supportedFeatures":"supportedFeatures","upCnxState":"","smfServiceInstanceId":"smfServiceInstanceId","pduSessionId":20,"sNssai":{"sd":"sd","sst":153},"n2SmInfoType":"","gpsi":"gpsi"}
		return SmContextCreatedData,201,{'Location': 'http://'+get_ip()+':5005/nsmf-pdusession/{apiVersion}/sm-contexts/'+reqjson['supi']}
