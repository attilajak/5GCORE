# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
import requests
from flask import request, g

from flask_restful import Resource,reqparse
from .. import logs
import json

parser = reqparse.RequestParser()
##parse eNB Infos
parser.add_argument('MCC')
parser.add_argument('MNC')
parser.add_argument('TAC')
parser.add_argument('ID')
##parse UE eNB ID
parser.add_argument('eNBID')
##parse UE sim card infos
parser.add_argument('imsi')
parser.add_argument('msisdn')
parser.add_argument('key')
parser.add_argument('opc')
parser.add_argument('PEI')
##parse NASMsg
parser.add_argument('PDUSessionID')
parser.add_argument('RequestType')
parser.add_argument('PDUType')
##parse MsgType
parser.add_argument('MsgType')
##parse ToAmfANInterface
parser.add_argument('AllocatedUEIp')
parser.add_argument('CNTunnelID')
parser.add_argument('UPFURI')
#parse ueListenPort
parser.add_argument('ueListenPort')
##global eNB parameters
MCC_VALID = "208"
MNC_VALID = "93"
TAC_VALID = "01"
##parse parameters of SMContext
parser.add_argument('DeregistrationType')
parser.add_argument('AccessType')
parser.add_argument('CreateDataConnection')
#eNB Collections
#eNB Collections
eNBCollection = []
#map of imsi and ueListenPort
Maps = []
#LoopLog
timer_interval = 10

headers = { "Content-Type" : "application/json"}
## current path
CurrentPath = "~/5GCORE/AMF/Namf_Communication/v1/api/eNBAndAMFInterface.py"
#Log infos
info = CurrentPath+":47   [AMF][INFO]    "+"|--------------------------------------------------------------|\n"\
      +CurrentPath+":48   [AMF][INFO]    "+"|                       eNB infos table                        |\n"\
      +CurrentPath+":49   [AMF][INFO]    "+"|--------------|---------------|---------------|---------------|\n"\
      +CurrentPath+":50   [AMF][INFO]    "+"|       ID     |      MCC      |      MNC      |      TAC      |\n"\
      +CurrentPath+":51   [AMF][INFO]    "+"|--------------|---------------|---------------|---------------|\n"

timer = None
import threading
from threading import Thread
def N2PDUSessionReq(args):
	print(CurrentPath+":56   [AMF][INFO]   "+"AMF PREPARE PDU SESSION ESTABILISHMENT REQ MSG ...")
	logs.s1uBearer += 1
	stcs = logs.info\
               +CurrentPath+":60   [AMF][INFO]  "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +CurrentPath+":61   [AMF][INFO]  "+"|----------------|-----------------|-----------------|-----------------|\n"
	print(stcs)
	print(CurrentPath+":68   [AMF][INFO]   "+"s1uBearer has been created successfully")
	if len(Maps) == 0:
		print(CurrentPath+":68   [AMF][ERROR]   "+"no imsi exists")
	for i in range(len(Maps)):
		if operator.eq(Maps[i]['imsi'],args['imsi']) :
			Port = Maps[i]['ueListenPort']
			UEURI = "http://"+Port+"/nue/v1/fromamfside"
			Msg2UE = {"AllocatedUEIp":args['AllocatedUEIp'],"UPFURI":args['UPFURI'],"CNTunnelID":args['CNTunnelID'],"imsi":args['imsi'],"status":"PDUSessionEstabilishmentReqAccept"}
			#ReqNumber = 1
			#while(ReqNumber<5):
			r = requests.post(UEURI,data=Msg2UE)
				#ReqNumber += 1
			if r.status_code == 200:
				print(CurrentPath+":78   [AMF][INFO]   "+"return Req Accept infos to UE")
				#break
			else:
				print(CurrentPath+":78   [AMF][INFO]   "+"Not return Req Accept infos to UE")
			break


def statistics():
	stcs = logs.info+CurrentPath+":74   [AMF][INFO]  "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +CurrentPath+":75   [AMF][INFO]  "+"|----------------|-----------------|-----------------|-----------------|\n"
	print(stcs)
	global timer
	if timer != None:
		timer.finished.wait(timer_interval)
		timer.function()
	else:
		timer = threading.Timer(timer_interval, statistics)
		timer.start()
class INTERFACEeNBSide(Resource):

    global info

    def __init__(self):
        self.info = info

    def post(self):
        global info,MCC_VALID,MNC_VALID,TAC_VALID,eNBCollection
        args = parser.parse_args()
        MsgType = args['MsgType']
        if operator.eq(MsgType,"eNBConnect2AMF"):
        	print(CurrentPath+":84   [AMF][INFO]   "+"AMF receives eNB connection request")
        	print(CurrentPath+":85   [AMF][INFO]   "+"AMF handling eNB connection request ...")
        	ID = args['ID']
        	ID = args['ID']
        	MCC = args['MCC']
        	MNC = args['MNC']
        	TAC = args['TAC']
        	if not operator.eq(MCC_VALID,MCC):
            		return "BAD MCC"
        	elif not operator.eq(MNC_VALID,MNC):
            		return "BAD MNC"
        	elif not operator.eq(TAC_VALID,TAC):
            		return "BAD TAC"
        	#return "eNBConnect2AMFSuccess"
        	self.info += CurrentPath+":110   [AMF][INFO]   "+("|     "+ID+"    "+"|      "+MCC+"      "+"|     "+"    "+MNC+"    "+"|       "+"   "+TAC+"   "+"|     "+"\n")\
                     +CurrentPath+":111   [AMF][INFO]   "+"|--------------|---------------|---------------|---------------|\n"
        	if len(eNBCollection)==0:
        		eNB = {'ID':ID,'MCC':MCC,'MNC':MNC,'TAC':TAC}
        		eNBCollection.append(eNB)
        		logs.eNBConnected+=1
        		print(CurrentPath+":104   [AMF][INFO]   "+"eNB Infos recoded in AMF")
        		print(self.info)
        		info = self.info
        		print("\n\n")
        	else :
        		for i in range(len(eNBCollection)):
        			eNB = {'ID':ID,'MCC':MCC,'MNC':MNC,'TAC':TAC}
        			if eNBCollection[i]['ID']==eNB['ID']:
        				break
       				elif i==len(eNBCollection)-1:
        				eNBCollection.append(eNB)
        				logs.eNBConnected+=1
        				print(CurrentPath+":116   [AMF][INFO]   "+"eNB Infos recoded in AMF")
        				print(self.info)
        				info = self.info
        				print("\n\n")
        	print(CurrentPath+":120   [AMF][INFO]   "+"statistics Infos recoded in AMF")
        	stcs = logs.info+CurrentPath+":133  [AMF][INFO]  "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +CurrentPath+":134  [AMF][INFO]  "+"|----------------|-----------------|-----------------|-----------------|\n"
        	print(stcs)
        	return "eNBConnect2AMFSuccess"
        elif operator.eq(MsgType,"UEConnect2AMF"):
        	print(CurrentPath+":126   [AMF][INFO]   "+"AMF receives UE connection request")
        	print(CurrentPath+":127   [AMF][INFO]   "+"AMF handling UE connection request ...")
        	eNBID = args['eNBID']
        	if len(eNBCollection) == 0:
        		print(CurrentPath+":130   [AMF][ERROR]   "+"no eNB active in AMF")
        		return "NoeNBActiveInAMF"
        	for i in range(len(eNBCollection)):
        		if eNBCollection[i]['ID'] == eNBID:
        			logs.UEConnected += 1
        			print(CurrentPath+":135   [AMF][INFO]   "+"statistics Infos recoded in AMF")
        			stcs = logs.info+CurrentPath+":148  [AMF][INFO]  "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +CurrentPath+":149  [AMF][INFO]  "+"|----------------|-----------------|-----------------|-----------------|\n"
        			print(stcs)
        			return "UEConnected2AMFSuccess"
        		elif i == len(eNBCollection)-1:
        			print(CurrentPath+":141   [AMF][ERROR]   "+"no eNB corresponding to UE eNBID")
        			return "NoeNBCorrespond2UEeNBID"
        elif operator.eq(MsgType,"UERegisterRequest"):
            print(CurrentPath+":144   [AMF][INFO]   "+"AMF receives UE registration request")
            print(CurrentPath+":145   [AMF][INFO]   "+"AMF handling UE registration request ...")
            print(CurrentPath+":146   [AMF][INFO]   "+"call AMF UEContextTransfer operation with ue imsi("+args['imsi']+") and http method(post)")
            print(CurrentPath+":147   [AMF][INFO]   "+"POST http://127.0.0.1/namf-comm/v1/ue-contexts/"+args['imsi']+"/transfer")
            print(CurrentPath+":148   [AMF][INFO]   "+"AMF COMMUNICATION UECONTEXT TRANSFER SUCCESS")
            print(CurrentPath+":149   [AMF][INFO]   "+"BEGIN AUTHENTICATION PROCEDURE...")
            print(CurrentPath+":150   [AMF][INFO]   "+"SEND UE SIM CARD INFOS TO AUSF...")
            print(CurrentPath+":151   [AMF][INFO]   "+"call AUSF authentication operation with http method(post)")
            print(CurrentPath+":152   [AMF][INFO]   "+"post http://127.0.0.1:5020/nausf-auth/v1/ue-authentications")
            ImsiAndListenPort = {"imsi":args['imsi'],"ueListenPort":args['ueListenPort']}
            SendUEMsgToAUSF = "http://127.0.0.1:5020/nausf-auth/v1/ue-authentications"
            UEAuthInfo = {"supiOrSuci":"208930000000001","servingNetworkName":"string","resynchronizationInfo":{"rand":"string","auts":"string"},"pei":"string","traceData":{"traceRef":"string","neTypeList":"string","eventList":"string","collectionEntityIpv4Addr":"198.51.100.1","collectionEntityIpv6Addr":"2001:db8:85a3::8a2e:370:7334","interfaceList": "string"}}
            UEAuthInfojson = json.dumps(UEAuthInfo)
            r = requests.post(SendUEMsgToAUSF,data=UEAuthInfojson,headers=headers)
            if r.status_code == 200:
                Auth5GInfo = {"resStar":"12345678123456781234567812345678"}
                Auth5GInfojson = json.dumps(Auth5GInfo)
                print(((r.content).decode()))
                data = json.loads((r.content).decode())
                SendUEMsgToAUSF = "http://127.0.0.1:5020/nausf-auth/v1/ue-authentications/"+data['_links']+"/5g-aka-confirmation"
                r = requests.post(SendUEMsgToAUSF,data=Auth5GInfojson,headers=headers)
                if r.status_code == 200 :
                    print(CurrentPath+":157   [AMF][INFO]   "+"UEAuthSuccess")
                    Send3gppAccessToUDM = "http://127.0.0.1:5009/nudm-uecm/v1/77743333/registrations/amf-3gpp-access"
                    access3gppInfo = { "amfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "supportedFeatures": "string", "purgeFlag": True, "pei": "string", "deregCallbackUri": "string", "pcscfRestorationCallbackUri": "string", "initialRegistrationInd": True, "guami": { "plmnId": { "mcc": "string", "mnc": "string" }, "amfId": "string" }, "backupAmfInfo": [ { "backupAmf": "string", "guamiList": [ { "plmnId": { "mcc": "string", "mnc": "string" }, "amfId": "string" } ] } ], "drFlag": True, "urrpIndicator": True, "amfEeSubscriptionId": "string", "epsInterworkingInfo": { "epsIwkPgws": { "additionalProp1": { "pgwFqdn": "string", "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }, "additionalProp2": { "pgwFqdn": "string", "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }, "additionalProp3": { "pgwFqdn": "string", "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" } } } }
                    access3gppInfojson = json.dumps(access3gppInfo)
                    r = requests.put(Send3gppAccessToUDM,data=access3gppInfojson,headers=headers)
                    if r.status_code == 201 :
                        print(CurrentPath+":157   [AMF][INFO]   "+"Nudm_UECM_Registration Success ")
                        GetSDMAmData = "http://127.0.0.1:5025/nudm-sdm/v1/"+args['imsi']+"/am-data"
                        r = requests.get(GetSDMAmData)
                        if r.status_code == 200:
                            AmSubscription = {"nfInstanceId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","implicitUnsubscribe":True,"expires":"2019-07-17T10:26:39.748Z","callbackReference":"http://127.0.0.1:5001/namf-comm/v1/"+args['imsi']+"/am-data/notify","monitoredResourceUris":["http://127.0.0.1:5025/nudm-sdm/v1/"+args['imsi']+"/am-data"],"singleNssai":{"sst":0,"sd":"string"},"dnn":"string","subscriptionId":"string","plmnId":{"mcc":"string","mnc":"string"}}
                            SubscribePost = "http://127.0.0.1:5025/nudm-sdm/v1/"+args['imsi']+"/sdm-subscriptions"
                            AmSubscriptionjson = json.dumps(AmSubscription)
                            r = requests.post(SubscribePost,data=AmSubscriptionjson,headers=headers)
                            if r.status_code == 200:
                                logs.UEAttached += 1
                                stcs = logs.info+CurrentPath+":172  [AMF][INFO]  "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+CurrentPath+":173  [AMF][INFO]  "+"|----------------|-----------------|-----------------|-----------------|\n"
                                print(CurrentPath+":161   [AMF][INFO]   "+"statistics recoded in AMF")
                                print(stcs)
                                print(CurrentPath+":163   [AMF][INFO]   "+(r.content).decode())
                                print(CurrentPath+":164   [AMF][INFO]   "+"PATCH http://127.0.0.1/namf-comm/v1/ue-contexts/"+args['imsi'])
                                print(CurrentPath+":165   [AMF][INFO]   "+"IdentityRequest...")
                                return "UERegister2AMFSuccess"
                            else :
                                print(CurrentPath+":168   [AMF][ERROR]  "+(r.content).decode())
                                return "UERegister2AMFFailure"
                    else :
                        print(CurrentPath+":168   [AMF][ERROR]  "+(r.content).decode())
                        return "UERegister2AMFFailure"
            else :
                print(CurrentPath+":168   [AMF][ERROR]  "+(r.content).decode())
                return "UERegister2AMFFailure"
        elif operator.eq(MsgType,"IdentityRsp"):
        	print(CurrentPath+":171   [AMF][INFO]   "+"IdentityResponseFromUE")
        	print(CurrentPath+":172   [AMF][INFO]   "+"UE PEI : "+args['PEI'])
        	return None,200
        elif operator.eq(MsgType,"PDUSessionEstabilishReq"):
            print(CurrentPath+":175   [AMF][INFO]   "+"RecvPDUSessionEstabilishReqFromUE")
            print(CurrentPath+":176   [AMF][INFO]   "+"Choosing SMF ...")
            print(CurrentPath+":177   [AMF][INFO]   "+"sending SmContextCreateData to SMF to Create PDUSessionContext ...")
            print(CurrentPath+":178   [AMF][INFO]   "+"call SMF Create SMContext operation with http method(post)")
            print(CurrentPath+":179   [AMF][INFO]   "+"post http://127.0.0.1:5005/nsmf-pdusession/v1/sm-contexts")
            PDUSessionCreateSMContextReq = "http://127.0.0.1:5005/nsmf-pdusession/v1/sm-contexts"
            #SmContextCreateData = {"imsi":args['imsi'],"PDUSessionID":args['PDUSessionID'],"RequestType":args['RequestType'],"PDUType":args['PDUType'],"CreateDataConnection":args['CreateDataConnection']}
            SmContextCreateData = { "supi": args['imsi'], "unauthenticatedSupi": False, "pei": "string", "gpsi": "string", "pduSessionId": args['PDUSessionID'], "dnn": "string", "sNssai": { "sd": "sd", "sst": 153 }, "hplmnSnssai": { "sd": "sd", "sst": 153 }, "servingNfId": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "guami": { "plmnId": { "mcc": "234", "mnc": "244" }, "amfId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }, "servingNetwork": { "mcc": "234", "mnc": "244" }, "n1SmMsg": { "contentId": "contentId" }, "anType": "3GPP_ACCESS", "ueLocation": { "eutraLocation": { "tai": { "plmnId": { "mcc": "234", "mnc": "244" }, "tac": "A198" }, "ecgi": { "plmnId": { "mcc": "234", "mnc": "244" }, "eutraCellId": "458A88488" }, "ageOfLocationInformation": 0, "ueLocationTimestamp": "2019-07-24T16:58:05.172Z", "geographicalInformation": "458A884888488456", "geodeticInformation": "458A8848884884566789", "globalNgenbId": { "plmnId": { "mcc": "234", "mnc": "244" }, "ngeNbId": "MacroNGeNB-Ab123" } }, "nrLocation": { "tai": { "plmnId": { "mcc": "234", "mnc": "244" }, "tac": "A198" }, "ncgi": { "plmnId": { "mcc": "234", "mnc": "244" }, "nrCellId": "458A88488" }, "ageOfLocationInformation": 0, "ueLocationTimestamp": "2019-07-24T16:58:05.172Z", "geographicalInformation": "458A884888488456", "geodeticInformation": "458A8848884884566789", "globalGnbId": { "plmnId": { "mcc": "234", "mnc": "244" }, "ngeNbId": "MacroNGeNB-Ab123" } }, "n3gaLocation": { "n3gppTai": { "plmnId": { "mcc": "234", "mnc": "244" }, "tac": "A198" }, "n3IwfId": "888F85", "ueIpv4Addr": "127.0.0.1", "ueIpv6Addr": "2001:db8:85a3::8a2e:370:7334", "portNumber": 5555 } }, "ueTimeZone": "string", "addUeLocation": { "eutraLocation": { "tai": { "plmnId": { "mcc": "234", "mnc": "244" }, "tac": "A198" }, "ecgi": { "plmnId": { "mcc": "234", "mnc": "244" }, "eutraCellId": "458A88488" }, "ageOfLocationInformation": 0, "ueLocationTimestamp": "2019-07-24T16:58:05.172Z", "geographicalInformation": "458A884888488456", "geodeticInformation": "458A8848884884566789", "globalNgenbId": { "plmnId": { "mcc": "234", "mnc": "244" }, "ngeNbId": "MacroNGeNB-Ab123" } }, "nrLocation": { "tai": { "plmnId": { "mcc": "234", "mnc": "244" }, "tac": "A198" }, "ncgi": { "plmnId": { "mcc": "234", "mnc": "244" }, "nrCellId": "458A88488" }, "ageOfLocationInformation": 0, "ueLocationTimestamp": "2019-07-24T16:58:05.173Z", "geographicalInformation": "458A884888488456", "geodeticInformation": "458A884888488456", "globalGnbId": { "plmnId": { "mcc": "234", "mnc": "244" }, "ngeNbId": "MacroNGeNB-Ab123" } }, "n3gaLocation": { "n3gppTai": { "plmnId": { "mcc": "234", "mnc": "244" }, "tac": "A198" }, "n3IwfId": "888F85", "ueIpv4Addr": "127.0.0.1", "ueIpv6Addr": "2001:db8:85a3::8a2e:370:7334", "portNumber": 5555 } }, "smContextStatusUri": "string", "hSmfUri": "string", "additionalHsmfUri": [ "string" ], "oldPduSessionId": 0, "pduSessionsActivateList": [ 0 ], "ueEpsPdnConnection": "string", "pcfId": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "nrfUri": "string", "supportedFeatures": "bECfA4", "backupAmfInfo": [ { "backupAmf": "string", "guamiList": [ { "plmnId": { "mcc": "234", "mnc": "244" }, "amfId": "3fa85f64-5717-4562-b3fc-2c963f66afa6" } ] } ], "traceData": { "traceRef": "string", "neTypeList": "string", "eventList": "string", "collectionEntityIpv4Addr": "198.51.100.1", "collectionEntityIpv6Addr": "2001:db8:85a3::8a2e:370:7334", "interfaceList": "string" }, "udmGroupId": "string", "routingIndicator": "string", "indirectForwardingFlag": True, "targetId": { "ranNodeId": { "plmnId": { "mcc": "234", "mnc": "244" }, "ngeNbId": "MacroNGeNB-Ab123" }, "tai": { "plmnId": { "mcc": "234", "mnc": "244" }, "tac": "A198" } }, "epsBearerCtxStatus": "f0BC" }
            SmContextCreateDatajson = json.dumps(SmContextCreateData)
            r = requests.post(PDUSessionCreateSMContextReq,data=SmContextCreateDatajson,headers=headers)
            if r.status_code == 201:
                print(CurrentPath+":184   [AMF][INFO]   "+"SmContextCreatedData")
                print(CurrentPath+":185   [AMF][INFO]   "+"SmContextCreatedData:  "+(r.content).decode())
                return "PDUSessionEstablishmentAccept"
            else :
                print(CurrentPath+":187   [AMF][INFO]   "+"SmContextCreateError\n\n")
                return "PDUSessionEstablishmentNotAccept"
        elif operator.eq(MsgType,"ToAmfANInterface"):
        	t = Thread(target = N2PDUSessionReq,args=(args,))
        	t.start()
        	t.join()
        	return None,200
        	#print("[AMF][INFO]   "+"AMF PREPARE PDU SESSION ESTABILISHMENT REQ MSG ...")
        	#UEURI = "http://127.0.0.1:5555/nue/v1/fromamfside"
        	#Msg2UE = {"AllocatedUEIp":args['AllocatedUEIp'],"UPFURI":args['UPFURI'],"CNTunnelID":args['CNTunnelID'],"imsi":args['imsi'],"status":"PDUSessionEstabilishmentReqAccept"}
        	#r = requests.post(UEURI,data=Msg2UE)
        	#logs.s1uBearer += 1
        	#stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                #        +"|----------------|-----------------|-----------------|-----------------|\n"
       		#print(stcs)

        elif operator.eq(MsgType,"UEInitialDeregistrationReq"):
        	print(CurrentPath+":203   [AMF][INFO]   "+"Receive UE Initial Deregistration Request")
        	#print(CurrentPath+":204   [AMF][INFO]   "+"post http://127.0.0.1:5005/nsmf-pdusession/v1/sm-contexts/"+args['imsi']+"/release")
        	ReleaseSMContextReq2SMF = "http://127.0.0.1:5005/nsmf-pdusession/v1/sm-contexts/"+"208930000000001"+"/release"
        	r = requests.post(ReleaseSMContextReq2SMF,data=args)
       		if r.status_code == 204:
        		#print(CurrentPath+":208   [AMF][INFO]   "+"Release SMContext about "+args['imsi']+" success")
        		print(CurrentPath+":209   [AMF][INFO]   "+"SMF Response 204 No Content")
        		logs.s1uBearer -= 1
        		logs.UEAttached -= 1
        		logs.UEConnected -= 1
        		stcs = logs.info+CurrentPath+":226  [AMF][INFO]  "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +CurrentPath+":227  [AMF][INFO]  "+"|----------------|-----------------|-----------------|-----------------|\n"
        		print(CurrentPath+":215   [AMF][INFO]   "+"statistics recoded in AMF")
       			print(stcs)
        		return "DeregistrationAccept"
       		else:
        		print(CurrentPath+":219   [AMF][ERROR]  "+"Release SMContext about "+args['imsi']+" failure")
        		return "DeregistrationNotAccept"

        elif operator.eq(MsgType,"ReleaseANReq"):
        	print(CurrentPath+":223   [AMF][INFO]   "+"Receive Release AN Request")
        	logs.eNBConnected -= 1
        	stcs = logs.info+CurrentPath+":238  [AMF][INFO]  "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +CurrentPath+":239  [AMF][INFO]  "+"|----------------|-----------------|-----------------|-----------------|\n"
        	print(CurrentPath+":227   [AMF][INFO]  "+"statistics recoded in AMF")
        	print(stcs)
        	for i in range(len(eNBCollection)):
        		if operator.eq(args['eNBID'],eNBCollection[i]['ID']):
        			#self.info -= ("|     "+eNBCollection[i]['ID']+"    "+"|      "+eNBCollection[i]['MCC']+"      "+"|     "+"    "+eNBCollection[i]['MNC']+"    "+"|       "+"    "+eNBCollection[i]['TAC']+"   "+"|     "+"\n")\
                     #+"|--------------|---------------|---------------|---------------|\n"
        			#info = self.info
        			eNBCollection.remove(eNBCollection[i])
        			break
        	#print(self.info)
        	return None,200

        elif operator.eq(MsgType,"InitialLoopLog"):
        	timer = threading.Timer(timer_interval,statistics)
        	timer.start()
        else:
            print(CurrentPath+":283   [AMF][INFO]  "+"AMF doesn't recv any MsgType")
