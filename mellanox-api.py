import requests
import urllib3
import json


def authenticate(ip, user, password):
    urllib3.disable_warnings()
    url = 'https://{0}/admin/launch?script=rh&template=json-request&action=json-login'.format(ip)
    body = {
        "username": user,
        "password": password
        }
    session = requests.Session()

    try:
        response = session.post(url, json=body, verify=False, timeout=3)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if response:
        response_status = json.loads(response.text)
        if response_status['status'] == 'OK':
            return session
        else:
            return None


def execute_command(session, cmd):
    urllib3.disable_warnings()

    cookie_iter = iter(session.cookies)
    try:
        cookie_att = next(cookie_iter)
    except StopIteration:
        return {}
    ip = cookie_att.__dict__['domain']

    url = 'https://{0}/admin/launch?script=rh&template=json-request&action=json-login'.format(ip)

    body = {
        "cmd": cmd
    }

    if isinstance(cmd, list):
        body = {
            "commands": cmd
        }

    response = session.post(url, json=body, verify=False, timeout=3)

    if response:
        return json.loads(response.text)
    else:
        return {}


def logout(session):
    urllib3.disable_warnings()

    cookie_iter = iter(session.cookies)
    try:
        cookie_att = next(cookie_iter)
    except StopIteration:
        return {}

    ip = cookie_att.__dict__['domain']

    url = 'https://{0}/admin/launch?script=rh&template=json-request&action=json-logout'.format(ip)

    response = session.post(url, verify=False, timeout=3)


    if response:
        return True
    else:
        return False


def execute_single_command(ip, user, password, cmd):
    urllib3.disable_warnings()
    url = 'https://{0}/admin/launch?script=rh&template=json-request&action=json-login'.format(ip)
    body = {
        "username": user,
        "password": password,
        "cmd": cmd
        }

    if isinstance(cmd, list):
        body = {
            "username": user,
            "password": password,
            "commands": cmd
        }

    try:
        response = requests.post(url, json=body, verify=False, timeout=3)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if response:
        return json.loads(response.text)
    else:
        return {}


def main():
    #management port IP address
    ip='192.168.1.20'
    user='admin'
    password='admin'

    #multiple commands in a list of strings
    cmds = ['show interfaces ethernet 1/13','show interface ethernet 1/1']
    #sinlge command in a string
    cmd = 'show fan'

    #authentication and command execution in a single call
    out1 = execute_single_command(ip,user,password,cmd)

    #authentication and session usage
    s = authenticate(ip,user,password)
    out2 = execute_command(s,cmds)
    out3 = execute_command(s, cmd)
    #session end
    logout(s)

if __name__ == '__main__':
    main()