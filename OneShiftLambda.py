#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# import boto3
import json
import base64

print('Loading function')


def get_job(event, context):
    if 'Authorization' not in event:
        raise Exception('400')

    auth_info = event['Authorization']
    if not auth_info:
        raise Exception('400')

    try:
        username, password = base64.b64decode(auth_info.replace('Basic ', '')).split(b':', 1)
    except Exception as e:
        return "Access denied"

    return username, password
