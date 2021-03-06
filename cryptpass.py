#!/usr/bin/env python

# cryptpass -- Create encrypted Unix password in Python.
# Copyright (C) 2017  Isabell Cowan and Bodhi Digital LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import string
from random import SystemRandom
from crypt import crypt
from getpass import getpass

def get_salt(saltlen):
    copts = string.ascii_letters + string.digits
    sysrand = SystemRandom()
    salt = ""
    for i in range(saltlen):
        salt += sysrand.choice(copts)

    return salt

def input_passwd():
    pw, conf = getpass("Password: "), getpass("Confirm: ")
    if pw != conf:
        print("Does not match!")
        exit(1)

    return pw

def crypt_passwd(pw, salt):
    return crypt(pw, "$6${0}$".format(salt))

def main():
    salt = get_salt(8)
    pw = input_passwd()
    cpw = crypt_passwd(pw, salt)
    print(cpw)

main()

# vim: set ts=4 sw=4 et syn=python
