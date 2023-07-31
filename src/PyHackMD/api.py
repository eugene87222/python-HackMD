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

    def __get_result(self, res: requests.Response, json_format=True):
        if res is None:
            return None
        elif json_format:
            return res.json()
        else:
            return res.text

    def __remove_none(self, dict_obj):
        res = {k: v for k, v in dict_obj.items() if v is not None}
        return res

    # ========== misc start ==========
    def get_me(self):
        '''Get user information

        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'me'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_read_history(self):
        '''Get a history of read notes

        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'history'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)
    # ========== misc end ==========

    # ========== personal note start ==========
    def get_notes(self):
        '''Get the list of persoanl notes

        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'notes'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_note(self, note_id: str):
        '''Get a personal note

        :param str note_id: note ID, can be found using `get_notes()`
        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'notes/' + note_id
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def create_note(
            self, title: str,
            content: str = '',
            read_perm: str = 'signed_in',
            write_perm: str = 'owner',
            comment_perm: str = 'signed_in_users'):
        '''Create a personal note

        :param str title: title of the personal note
        :param str content: content of the personal note
        :param str read_perm: read permission of the personal note ('owner'|'signed_in'|'guest')
        :param str write_perm: write permission of the personal note ('owner'|'signed_in'|'guest')
        :param str comment_perm: comment permission of the personal note ('disable'|'forbidden'|'owner'|'signed_in_users'|'everyone')
        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'notes'
        data = {
            'title': title,
            'content': content,
            'readPermission': read_perm,
            'writePermission': write_perm,
            'commentPermission': comment_perm,
            'permalink': ''
        }
        res = self.__request(self.__Method.POST, full_api, data)
        return self.__get_result(res)

    def update_note(
            self, note_id: str,
            content: str | None = None,
            read_perm: str | None = None,
            write_perm: str | None = None,
            comment_perm: str | None = None):
        '''Update a personal note

        :param str note_id: note ID, can be found using `get_notes()`
        :param content: content of the personal note
        :param read_perm: read permission of the personal note ('owner'|'signed_in'|'guest')
        :param write_perm: write permission of the personal note ('owner'|'signed_in'|'guest')
        :param comment_perm: comment permission of the personal note ('disable'|'forbidden'|'owner'|'signed_in_users'|'everyone')
        :type content: str | None, optional
        :type read_perm: str | None, optional
        :type write_perm: str | None, optional
        :type comment_perm: str | None, optional
        :return: 'Accept' on success, otherwise None
        :rtype: str | None
        '''
        full_api = self.base_api + 'notes/' + note_id
        data = {
            'content': content,
            'readPermission': read_perm,
            'writePermission': write_perm,
            'commentPermission': comment_perm,
            'permalink': ''
        }
        data = self.__remove_none(data)
        res = self.__request(self.__Method.PATCH, full_api, data)
        return self.__get_result(res, json_format=False)

    def delete_note(self, note_id: str):
        '''Delete a personal note

        :param str note_id: note ID, can be found using `get_notes()`
        :return: empty string on success, otherwise None
        :rtype: str | None
        '''
        full_api = self.base_api + 'notes/' + note_id
        res = self.__request(self.__Method.DELETE, full_api)
        return self.__get_result(res, json_format=False)
    # ========== personal note start ==========

    # ========== team note start ==========
    def get_teams(self):
        '''Get the list of teams to which the user has permission

        :param str note_id: note ID, can be found using `get_notes()`
        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'teams'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_team_notes(self, team_path: str):
        '''Get the list of team notes

        :param str team_path: team path, can be found using `get_teams()`
        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'teams/' + team_path + '/notes'
        res = self.__request(self.__Method.GET, full_api)
        return self.__get_result(res)

    def get_team_note(self, note_id: str):
        '''Get a team note

        :param str note_id: note ID, can be found using `get_team_notes()`
        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        return self.get_note(note_id)

    def create_team_note(
            self, team_path: str, title: str,
            content: str = '',
            read_perm: str = 'signed_in',
            write_perm: str = 'owner',
            comment_perm: str = 'signed_in_users'):
        '''Create a team note

        :param str team_path: team path, can be found using `get_teams()`
        :param str title: title of the team note
        :param str content: content of the team note
        :param str read_perm: read permission of the team note ('owner'|'signed_in'|'guest')
        :param str write_perm: write permission of the team note ('owner'|'signed_in'|'guest')
        :param str comment_perm: comment permission of the team note ('disable'|'forbidden'|'owner'|'signed_in_users'|'everyone')
        :return: dict on success, otherwise None
        :rtype: dict | None
        '''
        full_api = self.base_api + 'teams/' + team_path + '/notes'
        data = {
            'title': title,
            'content': content,
            'readPermission': read_perm,
            'writePermission': write_perm,
            'commentPermission': comment_perm,
            'permalink': ''
        }
        res = self.__request(self.__Method.POST, full_api, data)
        return self.__get_result(res)

    def update_team_note(
            self, team_path: str, note_id: str,
            content: str | None = None,
            read_perm: str | None = None,
            write_perm: str | None = None,
            comment_perm: str | None = None):
        '''Update a team note

        :param str team_path: team path, can be found using `get_teams()`
        :param str note_id: note ID, can be found using `get_team_notes()`
        :param content: content of the team note
        :param read_perm: read permission of the team note ('owner'|'signed_in'|'guest')
        :param write_perm: write permission of the team note ('owner'|'signed_in'|'guest')
        :param comment_perm: comment permission of the team note ('disable'|'forbidden'|'owner'|'signed_in_users'|'everyone')
        :type content: str | None, optional
        :type read_perm: str | None, optional
        :type write_perm: str | None, optional
        :type comment_perm: str | None, optional
        :return: 'Accept' on success, otherwise None
        :rtype: str | None
        '''
        full_api = self.base_api + 'teams/' + team_path + '/notes/' + note_id
        data = {
            'content': content,
            'readPermission': read_perm,
            'writePermission': write_perm,
            'commentPermission': comment_perm,
            'permalink': ''
        }
        data = self.__remove_none(data)
        res = self.__request(self.__Method.PATCH, full_api)
        return self.__get_result(res, json_format=False)

    def delete_team_note(self, team_path: str, note_id: str):
        '''Delete a team note

        :param str team_path: team path, can be found using `get_teams()`
        :param str note_id: note ID, can be found using `get_team_notes()`
        :return: empty string on success, otherwise None
        :rtype: str | None
        '''
        full_api = self.base_api + 'teams/' + team_path + '/notes/' + note_id
        res = self.__request(self.__Method.DELETE, full_api)
        return self.__get_result(res, json_format=False)
    # ========== team note end ==========
