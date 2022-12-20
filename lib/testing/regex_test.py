import re

from regex import name_regex, phone_regex, email_regex

class TestNameRegEx:
    '''name_regex in regex.py'''

    def test_matches_its_such_a_lovely_day(self):
        '''matches the string "It's such a lovely day today."'''
        assert(name_regex.fullmatch("It's such a lovely day today."))

class TestPhoneRegEx:
    '''phone_regex in regex.py'''

    def test_matches_its_such_a_lovely_day(self):
        '''matches the string "It's such a lovely day today."'''
        assert(phone_regex.fullmatch("It's such a lovely day today."))

class TestEmailRegEx:
    '''email_regex in regex.py'''

    def test_matches_its_such_a_lovely_day(self):
        '''matches the string "It's such a lovely day today."'''
        assert(email_regex.fullmatch("It's such a lovely day today."))
