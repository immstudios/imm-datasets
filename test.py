#!/usr/bin/env python3

from immdatasets import *

data_key = "43074114-b8a0-11e7-a139-005056a0a347"
data = get_data(data_key)

if data.is_success:
    for val in data.data:
        print(data.title, val)
else:
    print ("Something's wrong")
