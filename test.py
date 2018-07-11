#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

# for testing chatbot server in localhost
content = input('content : ')
payload = {'user_key': 'used-in-test', 'type': 'text', 'content': content}
r = requests.get('http://127.0.0.1:5000/message', json=payload)
print(r.text)
