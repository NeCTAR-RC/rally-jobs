#!/usr/bin/env python

import os
import sys
import json
import time

result = '/run/cloud-init/result.json'
retry = 0
max_retries = 30

while retry < max_retries:
    if os.path.exists(result):
        # Unreadable by non-root user
        r = os.system("sudo chmod +r %s" % result)
        ret = json.load(open(result, 'r'))

        errors = len(ret['v1']['errors'])
        print(json.dumps({'cloud-init errors': errors}))

        if errors:
            sys.exit(1)
        else:
            sys.exit(0)
    else:
        time.sleep(1)
        retry = retry + 1

# Timed out
print(json.dumps({'cloud-init errors': -1}))
sys.exit(1)
