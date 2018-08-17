#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core import rest

async def doProcess(app, name, request, query, method, oid=None):
    if oid == None:
        response = getattr(rest, method)(query, name)
    else:
        response = getattr(rest, method)(query, name, oid)
    return response
