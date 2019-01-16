#!/usr/bin/env python
# -*- coding: utf-8 -*-
import qiniu
from qiniu import CdnManager
import os
# 账户ak，sk
access_key = 'LacO1P2gosqmXiijB_LSeGcPtx02AIf6sCSmEuGG'
secret_key = 'y5_yrSgYC0N-ILh2Tp0pU0ibKtyZxTkM9dVEySNM'
auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)
# 需要刷新的目录链接

dirs = ['http://blog.jswh.me']
for entry in os.scandir('./output'):
    if entry.is_file():
        dirs.append('http://blog.jswh.me/' + entry.name)
# 刷新链接
refresh_result = cdn_manager.refresh_urls(dirs)
print(refresh_result)
# 获取所有文件
prefretch_result = cdn_manager.prefetch_urls(dirs)
print(prefretch_result)

