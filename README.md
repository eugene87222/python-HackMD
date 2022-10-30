# Table of Contents
- [What's this](#whats-this)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Basic Usage](#bacis-usage)
        - [User API](#user-api)
        - [User Notes API](#user-notes-api)
        - [Teams API](#teams-api)
        - [Team Notes API](#team-notes-api)

# What's this

A Python interface for HackMD API

# Getting Started

## Prerequisites

- Python 3.6+
- HackMD API token ([How to create a token](https://hackmd.io/@hackmd-api/how-to-issue-an-api-token))

## Installation

```shell
pip install python-HackMD
```

## Basic Usage

Let's create an API object before everything starts.

```python
from PyHackMD import API
api = API('<token>')
```

### User API

1. Get user information
```python
data = api.get_me()
print(data)
```

### User Notes API

1. Get a list of notes in the user's workspace
```python
data = api.get_notes()
print(data)
```

2. Get a note
```python
# note_id can be obtained using get_notes()
data = api.get_note('<note_id>')
print(data)
```

3. Create a note
```python
data = api.create_note(
            title='New Note',
            content='blablabla',
            read_perm='signed_in',
            write_perm='owner',
            comment_perm='signed_in_users')
print(data)
```

4. Update a note
```python
# note_id can be obtained using get_notes()
data = api.update_note(
            '<note_id>',
            content='blablabla',
            read_perm='signed_in',
            write_perm='owner',
            comment_perm='signed_in_users')
print(data)
```

5. Delete a note
```python
# note_id can be obtained using get_notes()
data = api.delete_note('<note_id>')
print(data)
```

6. Get a history of read notes
```python
data = api.get_read_history()
print(data)
```

### Teams API

1. Get a list of the teams to which the user has permission
```python
data = api.get_teams()
print(data)
```

### Team Notes API

1. Get a list of notes in a Team's workspace
```python
# team_path can be obtained using get_teams()
data = api.get_team_notes('<team_path>')
print(data)
```

2. Get a note in a Team's workspace
```python
# note_id can be obtained using get_team_notes()
data = api.get_team_note('<note_id>')
print(data)
```

3. Create a note in a Team workspace
```python
# team_path can be obtained using get_teams()
data = api.create_team_note(
            '<team_path>'
            title='New Note',
            content='blablabla',
            read_perm='signed_in',
            write_perm='owner',
            comment_perm='signed_in_users')
print(data)
```

4. Update a note in a Team's workspace
```python
# team_path can be obtained using get_teams()
# note_id can be obtained using get_team_notes()
data = api.update_team_note(
            '<team_path>', '<note_id>',
            content='blablabla',
            read_perm='signed_in',
            write_perm='owner',
            comment_perm='signed_in_users')
print(data)
```

5. Delete a note in a Team's workspace
```python
# team_path can be obtained using get_teams()
# note_id can be obtained using get_team_notes()
data = api.delete_team_note('<team_path>', '<note_id>')
print(data)
```
