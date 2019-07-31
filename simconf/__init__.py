# -*- coding: utf-8 -*-
from __future__ import absolute_import
import json
import socket

conf_str = '{"udr_sub_ip_address":"127.0.0.1","udr_sub_port_number":"8080","udr_policy_ip_address":"127.0.0.1","udr_policy_port_number":"8082"}'

conf_json = json.loads(conf_str)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    f = open("5gcore.conf","r")
    conf_str = f.read()
    f.close()
    conf_json = json.loads(conf_str)

#    url="http://127.0.0.1:5001/Namf-Communication/v1/amfeNBInterface"
#    eNBinfo={'ID':'2731802','MCC': "208","MNC":"93","TAC":"1"}
#    r = requests.post(url, data=eNBinfo)
#    if r.status_code != 200 :
#    	print("http communication error!")
#    else :
#    	ConnectOk = b'"connect_ok"\n'
#    	if r.content == ConnectOk :
#        	print("eNB connect 5GCore successfully!")
#        	print("init eNB transfer service successfully!")
#        	create_app().run(port=5000,debug=True)
