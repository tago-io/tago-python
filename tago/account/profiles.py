import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Profiles:
    def __init__(self, acc_token):
        self.token = acc_token
        self.default_headers = { 'content-type': 'application/json', 'Account-Token': acc_token }
        return

    # TODO test it
    def list(self):
        return requests.get('{api_endpoint}/profile'.format(api_endpoint = API_TAGO), headers = self.default_headers).json()

    # TODO test it
    def info(self, profile_id):
        if profile_id is None or profile_id == '':
            raise ValueError('Profile ID parameter is obrigatory.')
        return requests.get('{api_endpoint}/profile/{profile_id}'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers).json()

    # TODO test it
    def edit(self, profile_id, data):
        data = data if data else {}
        return requests.put('{api_endpoint}/profile/{profile_id}'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, data = json.dumps(data)).json()

    # TODO test it
    def delete(self, profile_id):
        return requests.delete('{api_endpoint}/profile/{profile_id}'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers).json()

    # TODO test it
    def create(self, data):
        data = data if data else {}
        return requests.post('{api_endpoint}/profile'.format(api_endpoint = API_TAGO), headers = self.default_headers, data = json.dumps(data)).json()

    # TODO review it
    def usageStatisticList(self, profile_id, date, timezone):
        params = {
            'date': date,
            'timezone': timezone
        }
        return requests.get('{api_endpoint}/profile/{profile_id}/statistics'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, params = json.dumps(params)).json()

    # TODO review it
    def tokenList(self, profile_id, page = 1, amount = 20, filter = {}, fields = ['name', 'token', 'created_at'], orderBy = 'created_at,desc'):
        params = {
            'page': page,
            'filter': filter,
            'amount': amount,
            'orderBy': orderBy,
            'fields': fields
        }
        return requests.get('{api_endpoint}/profile/{profile_id}/token'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, params = json.dumps(params)).json()

    # TODO test it
    def shareList(self, profile_id):
        return requests.get('{api_endpoint}/profile/{profile_id}/share'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers).json()

    # TODO test it
    def shareCreate(self, profile_id, email):
        data = {'email' : email}
        return requests.get('{api_endpoint}/profile/{profile_id}/share'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, data = json.dumps(data)).json()

    # TODO test it
    def shareDelete(self, profile_id, share_id):
        return requests.delete('{api_endpoint}/profile/{profile_id}/share/{share_id}'.format(api_endpoint = API_TAGO, profile_id = profile_id, share_id = share_id), headers = self.default_headers).json()

    # TODO review it
    def tokenCreate(self, profile_id, data):
        data = data if data else {}
        data['profile_id'] = profile_id
        return requests.post('{api_endpoint}/profile/{profile_id}/token'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, data = json.dumps(data)).json()

    # TODO test it
    def tokenDelete(self, profile_id, token):
        return requests.delete('{api_endpoint}/profile/{profile_id}/token/{token}'.format(api_endpoint = API_TAGO, profile_id = profile_id, token = token), headers = self.default_headers).json()

    # TODO test it
    def addonList(self, profile_id):
        return requests.get('{api_endpoint}/profile/{profile_id}/addons'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers).json()

    # TODO test it
    def addonEdit(self, profile_id, data):
        return requests.post('{api_endpoint}/profile/{profile_id}/addons'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, data = json.dumps(data)).json()

    # TODO test it
    def serviceEdit(self, profile_id, data):
        return requests.post('{api_endpoint}/profile/{profile_id}/services'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, data = json.dumps(data)).json()

    # TODO test it
    def transferTokenToAnotherProfile(self, target_profile_id):
        return requests.put('{api_endpoint}/profile/switch/{target_profile_id}'.format(api_endpoint = API_TAGO, target_profile_id = target_profile_id), headers = self.default_headers).json()

    # TODO test it
    def summary(self, profile_id, params):
        return requests.get('{api_endpoint}/profile/{profile_id}/summary'.format(api_endpoint = API_TAGO, profile_id = profile_id), headers = self.default_headers, params = json.dumps(params)).json()
