from __future__ import absolute_import, print_function
import operator
import connexion
import six
import json
import requests
from flask import request, g
import ldap
import base64
from simconf import conf_json,get_ip
from hyper import HTTP20Connection
import simconf

########LDAP Configuration###############
ldap_server = 'ldap://localhost:16611'
auth_dn = 'cn=Manager,dc=maxcrc,dc=com'
search_dn = 'o=session,ds=uePolicyData,subdata=services,uid=2620020000092,ds=SUBSCRIBER,o=DEFAULT,dc=C-NTDB'
base_dn = 'o=session,ds=uePolicyData,subdata=services,uid=2620020000092,ds=SUBSCRIBER,o=DEFAULT,dc=C-NTDB'
filter = '(objectClass=uidObject)'
user = 'cn=pgwAdminUser'
pw = 'azMVsxp9=fLQ2NyqE#A!'
########LDAP Configuration###############

from swagger_server.models.error_report import ErrorReport  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.sm_policy_context_data import SmPolicyContextData  # noqa: E501
from swagger_server.models.sm_policy_control import SmPolicyControl  # noqa: E501
from swagger_server.models.sm_policy_decision import SmPolicyDecision  # noqa: E501
from swagger_server.models.sm_policy_delete_data import SmPolicyDeleteData  # noqa: E501
from swagger_server.models.sm_policy_notification import SmPolicyNotification  # noqa: E501
from swagger_server.models.sm_policy_update_context_data import SmPolicyUpdateContextData  # noqa: E501
from swagger_server.models.termination_notification import TerminationNotification  # noqa: E501
from swagger_server.models.ue_camping_rep import UeCampingRep  # noqa: E501
from swagger_server import util

headers = { "Content-Type" : "application/json"}

def sm_policies_notify_terminate_post(body):  # noqa: E501
    """sm_policies_notify_terminate_post

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TerminationNotification.from_dict(connexion.request.get_json())  # noqa: E501
        print("In sm_policies_notify_terminate_post")
    return 'do some magic!'


def sm_policies_notify_update_post(body):  # noqa: E501
    """sm_policies_notify_update_post

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: UeCampingRep
    """
    if connexion.request.is_json:
        body = SmPolicyNotification.from_dict(connexion.request.get_json())  # noqa: E501
	#print(connexion.request.get_json())
    print("In sm_policies_notify_update_post")
    NotificationUri = "http://127.0.0.1:5005/nsmf-pdusession/v1/777777/notify/update"
    smContext = {"resourceUri":"http://127.0.0.1:8081/npcf-smpolicycontrol/v1/sm-policies/5656565","smPolicyDecision":{"sessRules":{"additionalProp1":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp2":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp3":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"}},"pccRules":{"additionalProp1":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp2":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp3":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"}},"pcscfRestIndication":True,"qosDecs":{"additionalProp1":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp2":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp3":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True}},"chgDecs":{"additionalProp1":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp2":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp3":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0}},"chargingInfo":{"primaryChfAddress":"string","secondaryChfAddress":"string"},"traffContDecs":{"additionalProp1":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp2":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp3":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}}},"umDecs":{"additionalProp1":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp2":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp3":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]}},"qosChars":{"additionalProp1":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp2":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp3":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0}},"reflectiveQoSTimer":0,"conds":{"additionalProp1":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"},"additionalProp2":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"},"additionalProp3":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"}},"revalidationTime":"2019-07-24T07:37:22.159Z","offline":True,"online":True,"policyCtrlReqTriggers":["PLMN_CH","string"],"lastReqRuleData":[{"refPccRuleIds":["string"],"reqData":["CH_ID","string"]}],"lastReqUsageData":{"refUmIds":["string"],"allUmIds":True},"praInfos":{"additionalProp1":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp2":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp3":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]}},"ipv4Index":0,"ipv6Index":0,"suppFeat":"string"}}
    smContextjson = json.dumps(smContext)
    r = requests.post(NotificationUri,data=smContextjson,headers=headers)
    if (r.status_code != 200) and (r.status_code != 204):
        return "[PCF][ERROR] smContextUpdate Notification Failed"
    AnUri = "http://127.0.0.1:5555/notification"
    notificationStatus = {'success'}
    print("simconf before=",simconf.notificationStatus)
    simconf.notificationStatus=1
    print("simconf after=",simconf.notificationStatus)
    ret = requests.post(AnUri,data="true",headers=headers)
    return '[PCF][INFO] do some magic!'

def sm_policies_post(body):  # noqa: E501
    """sm_policies_post

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: SmPolicyDecision
    """
    if connexion.request.is_json:
        body = SmPolicyContextData.from_dict(connexion.request.get_json())  # noqa: E501
    #get supi and sessionid from request body
    # check if sessionid already present in LDAP,write only if not present. otherwise continue without write
    response = {"sessRules":{"additionalProp1":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp2":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp3":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"}},"pccRules":{"additionalProp1":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp2":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp3":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"}},"pcscfRestIndication":True,"qosDecs":{"additionalProp1":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp2":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp3":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True}},"chgDecs":{"additionalProp1":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp2":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp3":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0}},"chargingInfo":{"primaryChfAddress":"string","secondaryChfAddress":"string"},"traffContDecs":{"additionalProp1":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp2":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp3":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}}},"umDecs":{"additionalProp1":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp2":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp3":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]}},"qosChars":{"additionalProp1":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp2":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp3":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0}},"reflectiveQoSTimer":0,"conds":{"additionalProp1":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"},"additionalProp2":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"},"additionalProp3":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"}},"revalidationTime":"2019-07-24T07:37:22.159Z","offline":True,"online":True,"policyCtrlReqTriggers":["PLMN_CH","string"],"lastReqRuleData":[{"refPccRuleIds":["string"],"reqData":["CH_ID","string"]}],"lastReqUsageData":{"refUmIds":["string"],"allUmIds":True},"praInfos":{"additionalProp1":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp2":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp3":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]}},"ipv4Index":0,"ipv6Index":0,"suppFeat":"string"}

    supi = body.supi
    sessionid = body.pdu_session_id

    print("****"+supi+"******")
    print("****"+str(sessionid)+"******")

    add_dn = 'sessionId='+supi+str(sessionid)
    final_dn = add_dn+','+base_dn
    print("**final_dn**"+final_dn+"******")

    sessionIdValue = str(supi+str(sessionid))
    print(sessionIdValue)
    add_record = [ ('objectClass', ['pcf5GSessionId']), ('sessionId', sessionIdValue), ('blobData', str(response)) ]

    print(add_record)

    ldapc = ldap.initialize(ldap_server)

    result = ldapc.simple_bind_s(user,pw)
    print("bind success")
    print(result)
    attrs = ['st']

    try:
        recordexists = ldapc.search_s(final_dn,ldap.SCOPE_SUBTREE)
        print(recordexists)
    except ldap.LDAPError, e:
        print(e)
    try:
        result = ldapc.add_s(final_dn,add_record)
    except ldap.LDAPError, e:
        print(e)
    ldapc.unbind()
    print(result)

    #import pdb; pdb.set_trace()
    #RequestUri = "http://"+conf_json['udr_policy_ip_address']+":"+conf_json['udr_policy_port_number']+"/policy-data/ues/"+body.supi+"/sm-data"
    RequestUri = "http://"+conf_json['udr_policy_ip_address']+":"+conf_json['udr_policy_port_number']+"/nudr-dr/v1/policy-data/ues/imsi-"+body.supi+"/sm-data"
    #r = requests.get(RequestUri)
    udrcon = HTTP20Connection(conf_json['udr_policy_ip_address']+":"+"7003")
    streamid = udrcon.request('GET', "/nudr-dr/v1/policy-data/ues/imsi-"+body.supi+"/sm-data")
    #print("streamid: "+str(streamid))
    resp = udrcon.get_response()
    #if r.status_code == 200:
    if resp.status == 200:
        #querydata = r.json() # do I need this data for subscribing?
        print(resp.read())
        SubscribeData = {"notificationUri":"http://"+get_ip()+":8081/npcf-smpolicycontrol/v1/sm-policies/notify","monitoredResourceUris":["http://"+conf_json['udr_policy_ip_address']+":"+conf_json['udr_policy_port_number']+"/policy-data/ues/"+body.supi+"/sm-data"]}
        UdrSubscribeUri = "http://"+conf_json['udr_policy_ip_address']+":"+conf_json['udr_policy_port_number']+"/policy-data/subs-to-notify"
        SubscribeDatajson = json.dumps(SubscribeData)
        r1 = requests.post(UdrSubscribeUri,data=SubscribeDatajson,headers=headers)
        if r1.status_code == 201:
            print("Subscription to Policy Control Subscription Successful")
    else:
        print("[PCF][ERROR]: GET "+"/nudr-dr/v1/policy-data/ues/uid-"+body.supi+"/sm-data"+"Failed")
    return response,201,{'Location': 'http://'+get_ip()+':8081/npcf-smpolicycontrol/v1/sm-policies/'+sessionIdValue}


def sm_policies_sm_policy_id_delete_post(body, sm_policy_id):  # noqa: E501
    """sm_policies_sm_policy_id_delete_post

     # noqa: E501

    :param body:
    :type body: dict | bytes
    :param sm_policy_id: Identifier of a policy association
    :type sm_policy_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = SmPolicyDeleteData.from_dict(connexion.request.get_json())  # noqa: E501
    #trigger smContext Update towards SMFDoingSomething
    NotificationUri = "http://127.0.0.1:5005/nsmf-pdusession/v1/777777/notify/update"
    smContext = {"resourceUri":"http://127.0.0.1:8081/npcf-smpolicycontrol/v1/sm-policies/5656565","smPolicyDecision":{"sessRules":{"additionalProp1":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp2":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp3":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"}},"pccRules":{"additionalProp1":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp2":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp3":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"}},"pcscfRestIndication":True,"qosDecs":{"additionalProp1":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp2":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp3":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True}},"chgDecs":{"additionalProp1":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp2":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp3":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0}},"chargingInfo":{"primaryChfAddress":"string","secondaryChfAddress":"string"},"traffContDecs":{"additionalProp1":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp2":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp3":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}}},"umDecs":{"additionalProp1":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp2":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp3":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-24T07:37:22.158Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]}},"qosChars":{"additionalProp1":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp2":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp3":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0}},"reflectiveQoSTimer":0,"conds":{"additionalProp1":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"},"additionalProp2":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"},"additionalProp3":{"condId":"string","activationTime":"2019-07-24T07:37:22.159Z","deactivationTime":"2019-07-24T07:37:22.159Z"}},"revalidationTime":"2019-07-24T07:37:22.159Z","offline":True,"online":True,"policyCtrlReqTriggers":["PLMN_CH","string"],"lastReqRuleData":[{"refPccRuleIds":["string"],"reqData":["CH_ID","string"]}],"lastReqUsageData":{"refUmIds":["string"],"allUmIds":True},"praInfos":{"additionalProp1":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp2":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp3":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]}},"ipv4Index":0,"ipv6Index":0,"suppFeat":"string"}}
    smContextjson = json.dumps(smContext)
    r = requests.post(NotificationUri,data=smContextjson,headers=headers)
    if (r.status_code != 200) and (r.status_code != 204):
        return "[PCF][ERROR] smContextUpdate Notification Failed"
    return '[PCF][INFO] do some magic!'

def sm_policies_sm_policy_id_get(sm_policy_id):  # noqa: E501
    """sm_policies_sm_policy_id_get

     # noqa: E501

    :param sm_policy_id: Identifier of a policy association
    :type sm_policy_id: str

    :rtype: SmPolicyControl
    """
    print("In sm_policies_sm_policy_id_get")
    data = connexion.request.data  # noqa: E501
    print("sm_policy_id=",data)
    #ldapc = ldap.initialize(ldap_server)
    final_dn = 'uid='+sm_policy_id+','+base_dn

    udrcon = HTTP20Connection(conf_json['udr_policy_ip_address']+":"+"7003")
    streamid = udrcon.request('GET', "/nudr-dr/v1/policy-data/ues/imsi-2620020000092/sessionblob/262002000009210")
    #print("streamid: "+str(streamid))
    resp = udrcon.get_response()
    print(resp.read())
    #if r.status_code == 200:
    if resp.status == 200:
       return "sessionBlobDataReceived"
    else:
        print("[PCF][ERROR]: GET "+"/nudr-dr/v1/policy-data/ues/uid-imsi-2620020000092/sm-data"+" Failed")
    return resp.read(),201,{'Location': 'http://'+get_ip()+':8081/npcf-smpolicycontrol/v1/sm-policies/'}
    



    #return {"context":{"accNetChId":{"accNetChaIdValue":0,"refPccRuleIds":["string"],"sessionChScope":True},"chargEntityAddr":{"anChargIpv4Addr":"198.51.100.1","anChargIpv6Addr":"2001:db8:85a3::8a2e:370:7334"},"gpsi":"string","supi":"string","interGrpIds":["string"],"pduSessionId":0,"chargingcharacteristics":"string","dnn":"string","notificationUri":"string","accessType":"3GPP_ACCESS","servingNetwork":{"mnc":"string","mcc":"string"},"userLocationInfo":{"eutraLocation":{"tai":{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"},"ecgi":{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"},"ageOfLocationInformation":0,"ueLocationTimestamp":"2019-07-23T17:08:08.481Z","geographicalInformation":"string","geodeticInformation":"string","globalNgenbId":{"plmnId":{"mcc":"string","mnc":"string"},"n3IwfId":"string","gNbId":{"bitLength":0,"gNBValue":"string"},"ngeNbId":"string"}},"nrLocation":{"tai":{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"},"ncgi":{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"},"ageOfLocationInformation":0,"ueLocationTimestamp":"2019-07-23T17:08:08.481Z","geographicalInformation":"string","geodeticInformation":"string","globalGnbId":{"plmnId":{"mcc":"string","mnc":"string"},"n3IwfId":"string","gNbId":{"bitLength":0,"gNBValue":"string"},"ngeNbId":"string"}},"n3gaLocation":{"n3gppTai":{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"},"n3IwfId":"string","ueIpv4Addr":"198.51.100.1","ueIpv6Addr":"2001:db8:85a3::8a2e:370:7334","portNumber":0}},"ueTimeZone":"string","pei":"string","ipv4Address":"198.51.100.1","ipv6AddressPrefix":"2001:db8:abcd:12::0\/64","ipDomain":"string","subsSessAmbr":{"uplink":"string","downlink":"string"},"subsDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0},"numOfPackFilter":0,"online":True,"offline":True,"3gppPsDataOffStatus":True,"refQosIndication":True,"traceReq":{"traceRef":"string","neTypeList":"string","eventList":"string","collectionEntityIpv4Addr":"198.51.100.1","collectionEntityIpv6Addr":"2001:db8:85a3::8a2e:370:7334","interfaceList":"string"},"sliceInfo":{"sst":0,"sd":"string"},"servNfId":{"servNfInstId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","guami":{"plmnId":{"mcc":"string","mnc":"string"},"amfId":"string"},"anGwAddr":{"anGwIpv4Addr":"198.51.100.1","anGwIpv6Addr":"2001:db8:85a3::8a2e:370:7334"}},"suppFeat":"string","smfId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","recoveryTime":"2019-07-23T17:08:08.481Z"},"policy":{"sessRules":{"additionalProp1":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp2":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp3":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"}},"pccRules":{"additionalProp1":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp2":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp3":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"}},"pcscfRestIndication":True,"qosDecs":{"additionalProp1":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp2":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp3":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True}},"chgDecs":{"additionalProp1":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp2":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp3":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0}},"chargingInfo":{"primaryChfAddress":"string","secondaryChfAddress":"string"},"traffContDecs":{"additionalProp1":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp2":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp3":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}}},"umDecs":{"additionalProp1":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-23T17:08:08.482Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp2":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-23T17:08:08.482Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp3":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-23T17:08:08.482Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]}},"qosChars":{"additionalProp1":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp2":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp3":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0}},"reflectiveQoSTimer":0,"conds":{"additionalProp1":{"condId":"string","activationTime":"2019-07-23T17:08:08.482Z","deactivationTime":"2019-07-23T17:08:08.482Z"},"additionalProp2":{"condId":"string","activationTime":"2019-07-23T17:08:08.482Z","deactivationTime":"2019-07-23T17:08:08.482Z"},"additionalProp3":{"condId":"string","activationTime":"2019-07-23T17:08:08.482Z","deactivationTime":"2019-07-23T17:08:08.482Z"}},"revalidationTime":"2019-07-23T17:08:08.482Z","offline":True,"online":True,"policyCtrlReqTriggers":["PLMN_CH","string"],"lastReqRuleData":[{"refPccRuleIds":["string"],"reqData":["CH_ID","string"]}],"lastReqUsageData":{"refUmIds":["string"],"allUmIds":True},"praInfos":{"additionalProp1":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp2":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp3":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]}},"ipv4Index":0,"ipv6Index":0,"suppFeat":"string"}}



def sm_policies_sm_policy_id_update_post(body, sm_policy_id):  # noqa: E501
    """sm_policies_sm_policy_id_update_post

     # noqa: E501

    :param body:
    :type body: dict | bytes
    :param sm_policy_id: Identifier of a policy association
    :type sm_policy_id: str

    :rtype: SmPolicyDecision
    """
    if connexion.request.is_json:
        body = SmPolicyUpdateContextData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
