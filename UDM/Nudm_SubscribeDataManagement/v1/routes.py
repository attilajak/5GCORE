# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
###
### The code is auto generated, your change will be overwritten by
### code generating.
###
from __future__ import absolute_import

from .api.AmData import AMDATA
from .api.SdmSubscribe import SDMSUBSCRIBE


routes = [
    dict(resource=AMDATA, urls=['/<string:supi>/am-data'], endpoint='AmData'),
    dict(resource=SDMSUBSCRIBE, urls=['/<string:supi>/sdm-subscriptions'], endpoint='SdmSubscribe'),

]
