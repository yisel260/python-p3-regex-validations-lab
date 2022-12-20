import re

from regex import name_regex, phone_regex, email_regex

class TestNameRegEx:
    '''name_regex in regex.py'''

    def test_matches_john_cena(self):
        '''matches the string "John Cena".'''
        assert name_regex.fullmatch("John Cena")

    def test_matches_anya_taylor_joy(self):
        '''matches the string "Anya Taylor-Joy".'''
        assert name_regex.fullmatch("Anya Taylor-Joy")

    def test_matches_dangelo(self):
        '''matches the string "D'Angelo".'''
        assert name_regex.fullmatch("D'Angelo")

    def test_does_not_match_empty(self):
        '''does not match an empty string.'''
        assert not name_regex.fullmatch("")

    def test_does_not_match_lowercase_john_cena(self):
        '''does not match a lowercase string.'''
        assert not name_regex.fullmatch("john cena")

    def test_does_not_match_string_with_numbers(self):
        '''does not match a string containing numbers.'''
        assert not name_regex.fullmatch("J0hn C3na")

    def test_does_not_match_string_with_whitespace_other_than_one_space(self):
        '''does not match a string containing non-single-space whitespace sequences.'''
        assert not name_regex.fullmatch("John   Cena")

class TestPhoneRegEx:
    '''phone_regex in regex.py'''

    def test_matches_format_nnnnnnnnnn(self):
        '''matches the string "5555555555"'''
        assert phone_regex.fullmatch("5555555555")
        
    def test_matches_format_nnn_nnn_nnnn(self):
        '''matches the string "555-555-5555"'''
        assert phone_regex.fullmatch("555-555-5555")

    def test_matches_format_parentheses_space(self):
        '''matches the string "(555) 555-5555'''
        assert phone_regex.fullmatch("(555) 555-5555")

    def test_does_not_match_9_digits(self):
        '''does not match the string "555555555"'''
        assert not phone_regex.fullmatch("555555555")
    
    def test_does_not_match_non_digit_characters(self):
        '''does not match the string "aaaaaaaaaa"'''
        assert not phone_regex.fullmatch("aaaaaaaaaa")

    def test_does_not_match_multiple_dashes(self):
        '''does not match the string "555--555--5555".'''
        assert not phone_regex.fullmatch("555--555--5555")

class TestEmailRegEx:
    '''email_regex in regex.py'''

    def test_matches_name_email(self):
        '''matches an email address with all alpha characters, @, and a domain.'''
        assert email_regex.fullmatch("johncena@wwe.com")

    def test_matches_dot_name_email(self):
        '''matches an email address with alpha characters, single dots, @, and a domain.'''
        assert email_regex.fullmatch("john.cena@wwe.com")

    def test_matches_dot_name_number_email(self):
        '''matches an email address with alphanumeric characters, single dots, @, and a domain.'''
        assert email_regex.fullmatch("john.cena123@wwe.com")

    def test_does_not_match_first_character_non_alpha_email(self):
        '''does not match an email address that begins with a number.'''
        assert not email_regex.fullmatch("123john.cena@wwe.com")

    def test_does_not_match_no_at_email(self):
        '''does not match an email address without an @.'''
        assert not email_regex.fullmatch("johncena.com")

    def test_does_not_match_invalid_character_email(self):
        '''does not match an email address with a $.'''
        assert not email_regex.fullmatch("john$cena@wwe.com")
    
    def test_does_not_match_no_domain_email(self):
        '''does not match an email address without a domain.'''
        assert not email_regex.fullmatch("johncena@")
        