import os
from getgauge.python import Messages
import requests


class ServiceClient(object):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.access_token = None

    def _getBaseUrl(self):
        return self.base_url

    def _apiRequest(self, method, endpoint, data: dict = None, json: dict = None, headers: dict = None):
        baseurl = self._getBaseUrl()
        url = baseurl + endpoint

        req = requests.Request(method=method, url=url, params=None, data=data, json=json, headers=headers)
        prepared = req.prepare()
        self._log_request(prepared)

        s = requests.Session()
        response = s.send(prepared)

        self._log_response(response)

        return response

    def _log_request(self, req):
        Messages.write_message('\n<b>{} {}</b>'.format(req.method, req.url))
        Messages.write_message('\n<i>Request Headers:</i>')
        Messages.write_message('\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()))
        Messages.write_message('\n<i>Request Body:</i>')
        Messages.write_message('{}'.format(req.body))

    def _log_response(self, res):
        Messages.write_message('\n---Response---')
        Messages.write_message('<i>Status code:</i> <b>{}</b>'.format(res.status_code))
        Messages.write_message('\n<i>Response Headers:</i>')
        Messages.write_message('\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()))
        if res.status_code != requests.codes.no_content:
            Messages.write_message('\n<i>Response Body:</i>')
            Messages.write_message('{}'.format(res.json()))
