import requests
from enum import Enum


class API():
    '''
    A Python interface of HackMD API
    '''
    def __init__(self, token):
        self.base_api = 'https://api.hackmd.io/v1/'
        self.token = token
        self.header = {'authorization': f'Bearer {self.token}'}

    class __Method(Enum):
        GET = 1
        POST = 2
        PATCH = 3
        DELETE = 4

    def __request(self, method, url, data=None):
        try:
            if method == self.__Method.GET:
                res = requests.get(url, headers=self.header)
            elif method == self.__Method.POST:
                res = requests.post(url, json=data, headers=self.header)
            elif method == self.__Method.PATCH:
                res = requests.patch(url, json=data, headers=self.header)
            elif method == self.__Method.DELETE:
                res = requests.delete(url, headers=self.header)
            res.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(error)
            return None
        return res

    def __get_result(self, res: requests.Response(), json_format=True):
        if res is None:
            return None
        elif json_format:
            return res.json()
        else:
            return res.text

    def __check_type(self, name, value, require_type):
        assert type(value) is require_type, f'{name} should be {require_type}, {type(value)} is given'

    # ========== misc start ==========
    def get_me(self):
        '''Get user information

        :return: dict object
        :rtype: dict
        '''
        full_api = self.base_api + 'me'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_read_history(self):
        '''Get a history of read notes

        :return: dict object
        :rtype: dict
        '''
        full_api = self.base_api + 'history'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)
    # ========== misc end ==========

    # ========== personal note start ==========
    def get_notes(self):
        '''Get the list of persoanl notes

        :return: dict object
        :rtype: dict
        '''
        full_api = self.base_api + 'notes'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_note(self, note_id):
        '''Get a personal note

        :param str note_id: note ID, can be found using `get_notes()`
        :return: dict object
        :rtype: dict
        '''
        self.__check_type('note_id', note_id, str)
        full_api = self.base_api + 'notes/' + note_id
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def create_note(self, data=None):
        '''Create a personal note

        :param data: json data to create a personal note
            data = {
                'title': 'New note',
                'content': '',
                'readPermission': 'owner'|'signed_in'|'guest',
                'writePermission': 'owner'|'signed_in'|'guest',
                'commentPermission': 'disable'|'forbidden'|'owner'|'signed_in_users'|'everyone',
                'permalink': ''
            }
        :type data: dict or None
        :return: dict object
        :rtype: dict
        '''
        full_api = self.base_api + 'notes'
        res = self.__request(self.__Method.POST, full_api, data)
        return self.__get_result(res)

    def update_note(self, note_id, data=None):
        '''Update a personal note

        :param str note_id: note ID, can be found using `get_notes()`
        :param data: json data to update the personal note
            data = {
                'content': '# Updated personal note',
                'readPermission': 'owner'|'signed_in'|'guest',
                'writePermission': 'owner'|'signed_in'|'guest',
                'permalink': ''
            }
        :type data: dict or None
        :return: 'Accept' on success, otherwise None
        :rtype: str or None
        '''
        self.__check_type('note_id', note_id, str)
        full_api = self.base_api + 'notes/' + note_id
        res = self.__request(self.__Method.PATCH, full_api, data)
        return self.__get_result(res, json_format=False)

    def delete_note(self, note_id):
        '''Delete a personal note

        :param str note_id: note ID, can be found using `get_notes()`
        :return: empty string on success, otherwise None
        :rtype: str or None
        '''
        self.__check_type('note_id', note_id, str)
        full_api = self.base_api + 'notes/' + note_id
        res = self.__request(self.__Method.DELETE, full_api)
        return self.__get_result(res, json_format=False)
    # ========== personal note start ==========

    # ========== team note start ==========
    def get_teams(self):
        '''Get the list of teams to which the user has permission

        :param str note_id: note ID, can be found using `get_notes()`
        :return: dict object
        :rtype: dict
        '''
        full_api = self.base_api + 'teams'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_team_notes(self, team_path):
        '''Get the list of team notes

        :param str team_path: team path, can be found using `get_teams()`
        :return: dict object
        :rtype: dict
        '''
        self.__check_type('team_path', team_path, str)
        full_api = self.base_api + 'teams/' + team_path + '/notes'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_team_note(self, note_id):
        '''Get a team note

        :param str note_id: note ID, can be found using `get_team_notes()`
        :return: dict object
        :rtype: dict
        '''
        return self.get_note(note_id)

    def create_team_note(self, team_path, data=None):
        '''Create a team note

        :param str team_path: team path, can be found using `get_teams()`
        :param data: json data to create a team note
            data = {
                'title': 'New note',
                'content': '',
                'readPermission': 'owner'|'signed_in'|'guest',
                'writePermission': 'owner'|'signed_in'|'guest',
                'commentPermission': 'disable'|'forbidden'|'owner'|'signed_in_users'|'everyone',
                'permalink': ''
            }
        :type data: dict or None
        :return: dict object
        :rtype: dict
        '''
        self.__check_type('team_path', team_path, str)
        full_api = self.base_api + 'teams/' + team_path + '/notes'
        res = self.__request(self.__Method.POST, full_api)
        return self.__get_result(res)

    def update_team_note(self, team_path, note_id, data=None):
        '''Update a team note

        :param str team_path: team path, can be found using `get_teams()`
        :param str note_id: note ID, can be found using `get_team_notes()`
        :param data: json data to update the team note
            data = {
                'content': '# Updated personal note',
                'readPermission': 'owner'|'signed_in'|'guest',
                'writePermission': 'owner'|'signed_in'|'guest',
                'permalink': ''
            }
        :type data: dict or None
        :return: 'Accept' on success, otherwise None
        :rtype: str or None
        '''
        self.__check_type('team_path', team_path, str)
        self.__check_type('note_id', note_id, str)
        full_api = self.base_api + 'teams/' + team_path + '/notes/' + note_id
        res = self.__request(self.__Method.PATCH, full_api)
        return self.__get_result(res)

    def delete_team_note(self, team_path, note_id):
        '''Delete a team note

        :param str team_path: team path, can be found using `get_teams()`
        :param str note_id: note ID, can be found using `get_team_notes()`
        :return: empty string on success, otherwise None
        :rtype: str or None
        '''
        self.__check_type('team_path', team_path, str)
        self.__check_type('note_id', note_id, str)
        full_api = self.base_api + 'teams/' + team_path + '/notes/' + note_id
        res = self.__request(self.__Method.DELETE, full_api)
        return self.__get_result(res, json_format=False)
    # ========== team note end ==========
