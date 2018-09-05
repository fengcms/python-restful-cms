#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys

DB_CONN = 'sqlite:///' + sys.path[0] + '/db/news.db'
# DB_CONN = 'mysql+pymysql://root:123456@localhost:3306/news'
# DB_CONN = 'postgresql+pypostgresql://postgres:123456@localhost:5432/news'
# DB_CONN = 'postgresql+psycopg2://postgres:123456@localhost:5432/news'

REDIS_CONFIG = {
    'host': 'localhost',
    'port': 6379,
}

REDIS_SPEED_API_PREFIX_LIST = ['/api/v1/fe/']

REDIS_SPEED_TIME = 5

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

# 后台接口黑名单
BLACK_AUTH = {
    'login': ['LS', 'GET', 'PUT', 'DELETE'],
    'site': ['GET', 'PUT', 'DELETE'],
}

# 前台接口白名单
WHITE_AUTH = {
    'article': ['LS', 'GET'],
    'channel': ['LS', 'GET'],
    'site': ['LS', 'GET'],
    'author': ['LS', 'GET'],
    'tags': ['LS', 'GET'],
    'origin': ['LS', 'GET'],
    'editor': [],
    'manages': [],
    'tree_channel': ['LS'],
}
