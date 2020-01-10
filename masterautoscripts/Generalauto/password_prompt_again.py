# -*- coding:utf-8 -*-
import getpass

# username = getpass.getuser()
# print('User Name:{}'.format(username))

while True:
    username = input('Input your linux username:')
    passwd = getpass.getpass('Input your Linux user password:')

    if username == 'root' and passwd == 'xxx':
        print("Disable {} remote login.".format(username))
    elif username == '' and passwd == '':
        print("Please re-enter your login username and password")
    elif username and passwd:
        print('Welcome login Linux system.')
        break
    else:
        print('Your linux password input incorrect')

