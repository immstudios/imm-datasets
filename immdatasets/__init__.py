import json
import time

import requests

__all__ = ["get_data"]

class DataResponse():
    def __init__(self, **kwargs):
        self._data = kwargs

    @property
    def data(self):
        return self._data["data"]

    @property
    def title(self):
        return self._data["title"]

    @property
    def response(self):
        return self._data["response"]

    @property
    def is_success(self):
        return self.response < 400

    @property
    def is_error(self):
        return self.response >= 400


def get_data(key):
    rresponse = requests.get("https://data.immstudios.org/{}.json".format(key))
    if rresponse.status_code != 200:
        return DataResponse(
                response=rresponse.status_code,
                time=time.time(),
                data={}
            )
    try:
        result_data = json.loads(rresponse.text)
    except Exception:
        return DataResponse(
                response=500,
                time=time.time(),
                data=None
            )
    return DataResponse(**result_data)
