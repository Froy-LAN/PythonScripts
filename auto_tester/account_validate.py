#!/usr/bin/env python3

import re

class Account:
    def __init__(self, f_name, l_name, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone

    def print(self):
        print(self.f_name + ", " + self.l_name + ", "  + self.phone)


def validate_user(user):
    #email_check = r"^[a-zA-Z][\w]*?[.-_+]{0,1}[\w]*@[\w]*.(com|net|edu)"
    phone_check = r"\(\d{3}\) \d{3}\-\d{4}"

    fn = user.f_name
    ln = user.l_name
    ph = user.phone

    if not fn.isalpha():
        return 1

    if not ln.isalpha():
        return 1

    if not re.search(phone_check, ph):
        return 1

    print("User contains valid information")
    return 0
