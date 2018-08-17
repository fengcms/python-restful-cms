#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys

DB_CONN = 'sqlite:///' + sys.path[0] + '/db/news.db'

PREFIX = {
    'be': '/api/v1/be/',
    'fe': '/api/v1/fe/',
}

ANONYMOUS_API = ['login']

PUBLIC_KEY_PATH = './key/public.pem'
PRIVATE_KEY_PATH = './key/private.pem'
