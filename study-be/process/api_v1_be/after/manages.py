#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

async def ls (response):
    for i in response['list']:
        i.pop('password')
        i['account'] = i.pop('username')
    return response

async def get (response):
    response.pop('password')
    response['account'] = response.pop('username')
    return response
