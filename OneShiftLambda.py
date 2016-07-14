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
    except (TypeError, ValueError):
        return '400'

    if "test@oneshift.com.au" == username and "myPass1" != password:
        raise Exception('401')

    return 'Ok'

