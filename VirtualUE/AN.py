##UE infos
##sim card : imsi 208930000000001    ,     msisdn  32435235366    ,     key : 0x8baf473f2f8fd09487cccbd7097c6862     , opc :  0xe734f8734007d6c5ce7a0508809e7e9c
##status : be ready to registration request
##connecting eNB ID : 28192

##eNB info
##eNB:   MCC 208 ,  MNC 93  , ID 28192, TAC  01
from __future__ import absolute_import
from flask import Flask, render_template
import v1
import requests
from threading import Thread
import sys
import signal
from flask_restful import Resource,reqparse
from v1 import variables
import subprocess
import socket,struct
import json

headers = { "Content-Type" : "application/json"}
#def get_ip_address(ifname):
#	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#	return socket.inet_ntoa(fcntl.ioctl(
#		s.fileno(),
#		0x8915,
#		struct.pack('256s',bytes(ifname[:15]))
#	)[20:24])

def quit(signum,frame):
	print(CurrentPath+":29   [UE][INFO]   "+"ue begin deregisteration req")
	UEInitialDeregistrationReq = "http://"+sys.argv[5]+":5555/uederegister"
	r = requests.post(UEInitialDeregistrationReq)
	if r.status_code == 200:
		sys.exit()
	#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
	#p.wait()
	UEInitialDeregistrationReq = "http://"+sys.argv[5]+":5001/namf-comm/v1/amfeNBInterface"
	#UEInitialDeregistrationReq = "http://172.20.10.9:5001/namf-comm/v1/amfeNBInterface"
	MsgLoad = {"suci":variables.suci,"CNTunnelID":variables.CNTunnelID,"MsgType":"UEInitialDeregistrationReq","DeregistrationType":"SwitchOff","AccessType":"3GPP"}
	r = requests.post(UEInitialDeregistrationReq,data=MsgLoad)
	ret = b'"DeregistrationAccept"\n'
	if ret == r.content :
		print(CurrentPath+":34   [UE][INFO]   "+"DeregistrationAccept")
		print(CurrentPath+":35   [VM][INFO]   "+"delete enp0s8 configuration")
		#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
		print(CurrentPath+":36   [eNB][INFO]  "+"Release AN Request")
		ReleaseANReq = "http://"+sys.argv[5]+":5001/namf-comm/v1/amfeNBInterface"
		#ReleaseANReq = "http://172.20.10.9:5001/namf-comm/v1/amfeNBInterface"
		eNBMsg = {"eNBID":"28192","MsgType":"ReleaseANReq"}
		r1 = requests.post(ReleaseANReq,data=eNBMsg)
		if r1.status_code == 200:
			print(CurrentPath+":52   [eNB][INFO]  "+"Release eNB success")
			#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
		else:
			print(CurrentPath+":54   [eNB][ERROR]  "+"Release eNB failure")
	#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
	#p.wait()


def create_app():
	app = Flask(__name__, static_folder='static')
	app.register_blueprint(
		v1.bp,
		url_prefix='/nue/v1')
	return app

CurrentPath = "~/5GCORE/UE/AN.py"

registration_status = 0
deregistration_status = 0
pdu_session_status = 0
#def ReqFromAMF():
#	create_app().run(port=5555)


#def running():
#	global enp0s3Ip
#	create_app().run(host=enp0s3Ip,port=int(sys.argv[3]))

#print(CurrentPath+":106   [VM][INFO]   "+"config enp0s3 ip")
#print(CurrentPath+":107   [VM][INFO]   "+"sudo ifconfig enp0s3 192.168.1.110")
#p = subprocess.Popen('sudo ifconfig enp0s3 192.168.1.110/24',shell=True)
#print(CurrentPath+":109   [enp0s3][ip] "+get_ip_address('enp0s3'))
enp0s3Ip = "127.0.0.1"
#enp0s3Ip = get_ip_address('enp0s3')
#t = Thread(target = running)
#t.start()

#t = Thread(target = RegisterReq,args=())
#t.start()
#print("parameter number: "+str(len(sys.argv)))
#print("parameters :"+str(sys.argv))
#print(sys.argv[1])
signal.signal(signal.SIGINT,quit)
#InitialReq()
#t = Thread(target = running)
#t.start
app = Flask(__name__)
@app.route('/')
def index():
	global pdu_session_status
	global registration_status
	return render_template('basic.html',regsuccess=registration_status,pdusuccess=pdu_session_status,deregsuccess=deregistration_status)

@app.route('/ueregister',methods=['POST'])
def RegisterReq():
	global enp0s3Ip
	global registration_status
	global pdu_session_status
	Msg = {"MsgType":"UERegisterReq","suci":sys.argv[2],"eNBID":sys.argv[1],"msisdn":"32435235366","key":"8baf473f2f8fd09487cccbd7097c6862","opc":"e734f8734007d6c5ce7a0508809e7e9c","ueIP":enp0s3Ip,"ueListenPort":sys.argv[3]}
	UERegisterReqUri = "http://"+sys.argv[5]+":5000/Nenb-transfer/v1/ueregisterrequest"
	Msgjson = json.dumps(Msg)
	r = requests.post(UERegisterReqUri, data=Msgjson,headers=headers)
	ret = b'"UERegister2AMFSuccess"\n'
	if ret == r.content :
		registration_status = 1
		print(CurrentPath+":52   [UE][INFO]   "+(r.content).decode())
		return render_template('basic.html',regsuccess=registration_status,pdusuccess=pdu_session_status,deregsuccess=deregistration_status)
	else :
		registration_status = 2
		print(CurrentPath+":52   [UE][INFO]   "+(r.content).decode())
		return render_template('basic.html',regsuccess=registration_status,pdusuccess=pdu_session_status,deregsuccess=deregistration_status)

@app.route('/uederegister',methods=['POST'])
def DeRegisterReq():
	global enp0s3Ip
	global deregistration_status
	global registration_status
	global pdu_session_status
	Msg = {"MsgType":"UEDeRegisterReq","suci":sys.argv[2],"eNBID":sys.argv[1],"msisdn":"32435235366","key":"8baf473f2f8fd09487cccbd7097c6862","opc":"e734f8734007d6c5ce7a0508809e7e9c","ueIP":enp0s3Ip,"ueListenPort":sys.argv[3],"CNTunnelID":variables.CNTunnelID}
	UEDeRegisterReqUri = "http://"+sys.argv[5]+":5000/Nenb-transfer/v1/uederegisterrequest"
	Msgjson = json.dumps(Msg)
	r = requests.post(UEDeRegisterReqUri, data=Msgjson,headers=headers)
	ret = b'"DeregistrationAccept"\n'
	if ret == r.content :
		deregistration_status = 1
		registration_status = 0
		pdu_session_status = 0
		print(CurrentPath+":52   [UE][INFO]   "+(r.content).decode())
		return render_template('basic.html',regsuccess=registration_status,pdusuccess=pdu_session_status,deregsuccess=deregistration_status)
	else :
		deregistration_status = 2
		print(CurrentPath+":52   [UE][INFO]   "+(r.content).decode())
		return render_template('basic.html',regsuccess=registration_status,pdusuccess=pdu_session_status,deregsuccess=deregistration_status)

@app.route('/establishpdu',methods=['POST'])
def EstPduReq():
	global enp0s3Ip
	global pdu_session_status
	global registration_status
	Msg = {"MsgType":"Initial request","DNN":"www","PduSessionId":10,"snssai": { "sst": 55, "sd": "38fB1b" },"ueIP":enp0s3Ip,"ueListenPort":sys.argv[3]}
	PDUSessionReqUri = "http://"+sys.argv[5]+":5000/Nenb-transfer/v1/establishpdusession"
	Msgjson = json.dumps(Msg)
	r = requests.post(PDUSessionReqUri, data=Msgjson,headers=headers)
	ret = b'"PDUSessionEstablishmentAccept"\n'
	if ret == r.content :
		pdu_session_status = 1
		print(CurrentPath+":52   [UE][INFO]   "+(r.content).decode())
		return render_template('basic.html',regsuccess=registration_status,pdusuccess=pdu_session_status,deregsuccess=deregistration_status)
	else :
		pdu_session_status = 2
		print(CurrentPath+":52   [UE][INFO]   "+(r.content).decode())
		return render_template('basic.html',regsuccess=registration_status,pdusuccess=pdu_session_status,deregsuccess=deregistration_status)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=int(sys.argv[4]))
