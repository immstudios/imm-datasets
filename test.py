#!/usr/bin/env python3

import random

from immdatasets import *

data_key = "43074114-b8a0-11e7-a139-005056a0a347"
data = get_data(data_key)

if data.is_error:
    print ("Something's wrong")
    sys.exit(0)

print(data.title, random.choice(data.data))
