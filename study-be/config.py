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

PAGESIZE = 10

# 配置上传路径
UPLOAD_PATH = './upload/'
# 常见图片格式16进制文件头标志
SUPPORT_TYPE = {
    'ffd8ffe':'jpg',
    '89504e470d0a1a0a0000':'png',
    '474946383961':'gif',
}
