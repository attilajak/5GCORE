# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
###
### The code is auto generated, your change will be overwritten by
### code generating.
###
from __future__ import absolute_import

from .api.Authenticate import AUTH
from .api.Authenticate5g import AUTH5G



routes = [
    dict(resource=AUTH, urls=['/ue-authentications'], endpoint='Authenticate'),
    dict(resource=AUTH5G, urls=['/ue-authentications/<string:ueContextId>/5g-aka-confirmation'], endpoint='Authenticate5g'),


]
