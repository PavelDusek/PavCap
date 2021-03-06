import json
import requests

import warnings
warnings.filterwarnings('once')

class Project(object):

    def __init__(self, token, url, secure = True ):
        self.token = token
        self.url = url
        self.secure = secure

    def info( self ):
        data = {
                'token': self.token,
                'content': 'project',
                'format': 'json',
                'returnFormat': 'json'
        }
        r = requests.post(url = self.url, data = data, verify= self.secure)
        j = json.loads(r.text)
        return j

    def listFields( self ):
        data = {
            'token': self.token,
            'content': 'exportFieldNames',
            'format': 'json',
            'returnFormat': 'json',
        }
        r = requests.post(url = self.url, data = data, verify= self.secure)
        json_fields = json.loads(r.text)
        fields = [ field['original_field_name'] for field in json_fields ]
        return fields

    def listIds( self ):
        fields = self.listFields()
        record_id_name = fields[0]
        data = {
            'token': self.token,
            'content': 'record',
            'format': 'json',
            'fields': record_id_name,
            'returnFormat': 'json',
        }
        r = requests.post( url = self.url, data = data, verify = self.secure )
        j = json.loads(r.text)
        ids = [ record_id[record_id_name] for record_id in j]
        #remove duplicates:
        ids = list(set(ids))
        return sorted(ids)

    def getData(self, ids ):
        data = {
            'token': self.token,
            'content': 'record',
            'format': 'json',
            'returnFormat': 'json',
        }

        #decide whether ids is just one id (str) or list of ids (list)
        if isinstance(ids, str):
            data['records'] = ids
        elif isinstance(ids, list):
            for n,i in enumerate(ids):
                data[f"records[{n}]"] = i
        else:
            raise TypeError("ids must be str or list")
        r = requests.post( url = self.url, data = data, verify = self.secure )
        j = json.loads(r.text)
        return j

    def upload( self, upload_data, behavior = 'normal' ):
        if not isinstance( upload_data, list):
            upload_data = [ upload_data ]
        data = {
            'token': self.token,
            'content': 'record',
            'format': 'json',
            'type': 'flat',
            'overwriteBehavior': behavior,
            'forceAutoNumber': 'false',
            'data': json.dumps( upload_data ),
            'returnContent': 'count',
            'returnFormat': 'json',
        }
        r = requests.post( url = self.url, data = data, verify = self.secure )
        return r.text

__doc__ = """
Pavel Dusek's simple library for REDCap (https://www.project-redcap.org/) API communication in Python.
"""
