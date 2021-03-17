# Mellanox-Onyx-API
Usage examples of the JSON API

The latest API example on the Mellanox Community page was not up-to-date so I've decided to create examples which work with Onyx version 3.9.0300 and possibly newer versions as well. 

## Previous JSON API
* URL: http://<switch-ip-address>/admin/launch?script=rh&template=login&action=login
* Using POST operation
* Headers: Content-Type: application/x-www-form-urlencoded
* Body: f_user_id=admin&f_password=admin (or another user)
 
After getting session cookie, the user can send commands in JSON format.
This version of the API is not supported in this repository.

## Current JSON API
Now it is possible to execute commands and login to the system in a single API call.It is possible to get a session cookie as well and re-use it for every command call.
* URL: https://<switch-ip-address>/admin/launch?script=rh&template=json-request&action=json-login
* Using POST operation
* Headers: Content-Type: application/json
* Body: {"username":"admin", "password":"admin"} (or another user) - JSON notation

## Example
Demonstration of both simultaneous login and command execution API calls, as well as API sessions.
Single API call with multiple commands example is also present. 

## Environment
* Python 3.7.0
* Tested switch: Mellanox SN2010 Onyx v. 3.9.0300
