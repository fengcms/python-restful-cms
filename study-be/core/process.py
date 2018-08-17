#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import ok

async def doProcess(app, name, request, query, method, oid=None):
    rep = {
        'api_name': name,
        'method': method,
        'query': query
    }
    if oid != None:
        rep['id'] = oid
    return ok(rep)
