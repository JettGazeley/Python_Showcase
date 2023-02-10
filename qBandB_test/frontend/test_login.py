from seleniumbase import BaseCase

from qBandB_test.conftest import base_url
from unittest.mock import patch
from qBandB.models import VerifiedUser, register

"""
This file defines integration tests for logging in through
the frontend homepage.
All of these test cases use requirement partitioning for the A2
requirements.
"""

# create new users for testing purposes
register("newTest", "newtest0@test.com", "Aa123456!")
register("LivTest", "liv@elliot.ca", "cC123#")
register("test3", "test3@test.com", "Aa123!")


class FrontEndHomePageTest(BaseCase):
    def test_login_valid(self, *_):
        """
        R2-1: A user can log in using her/his email address and the password.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (valid email and password)
        3. Input robustness testing
        """
        # open login page
        self.open(base_url + '/login')
        # fill a valid email and password (inout partitioning)
        self.type("#email", "newtest0@test.com")
        self.type("#password", "Aa123456!")
        # submit the login info
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        # output should be a welcome message for the user
        # at the index page
        self.assert_element("#welcome-header")
        self.assert_text("Welcome newTest!", "#welcome-header")

        # test if the page redirects to /
        # if true, then login was successful and nothing crashed (robustness)
        self.assert_equal(self.get_current_url(), base_url + "/")

    def test_login_invalid_email(self, *_):
        """
        R2-1: A user can log in using her/his email address and the password.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (email not registered)
        3. Input robustness testing
        """
        # open login page
        self.open(base_url + '/login')
        # fill a non-existing email and password (input partitioning)
        self.type("#email", "notregistered@email.com")
        self.type("#password", "Aa123456!")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the correct error message (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # if invalid, redirect to login again and check if page did not
        # crash (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_invalid_password(self, *_):
        """
        R2-1: A user can log in using her/his email address and the password.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (wrong password and email combination)
        3. Input robustness testing
        """
        # open login page
        self.open(base_url + '/login')
        # fill a valid email but invalid password
        self.type("#email", "newtest@test.com")
        self.type("#password", "a123456!")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the correct error message (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # if invalid, redirect to login again and check if page did not crash
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_empty_email(self, *_):
        """
        R2-2 (R1-1): Email cannot be empty. password cannot be empty.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (empty email)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill an empty email and any password
        self.type("#email", "")
        self.type("#password", "Aa123456!")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the correct message, since page shouldn't submit when email
        # field is empty (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # if invalid, redirect to login again and check if page did not crash
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_empty_pwd(self, *_):
        """
        R2-2 (R1-1): Email cannot be empty. password cannot be empty.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (empty password)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill any email and empty password
        self.type("#email", "newtest@test.com")
        self.type("#password", "")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the correct message, since page
        # shouldn't submit when password field is empty
        # (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # if invalid, redirect to login again and check if page did not crash
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_valid_addr_spec(self, *_):
        """
        R2-2 (R1-3): The email has to follow addr-spec defined in RFC 5322.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (valid addr-spec email)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill in a valid email and password
        self.type("#email", "test3@test.com")
        self.type("#password", "Aa123!")
        # submit the login info
        self.click('input[type="submit"]')

        # output should be a welcome message for the user at the index page
        # (exhaustive output testing)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome test3!", "#welcome-header")

        # if valid, should redirect to the index page
        # # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/")

    def test_login_invalid_addr_spec(self, *_):
        """
        R2-2 (R1-3): The email has to follow addr-spec defined in RFC 5322.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (invalid email)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill an invalid email and any password
        self.type("#email", "liv.elliot.ca")
        self.type("#password", "cC123#")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the correct message, since page shouldn't submit when email
        # does not follow addr-spec
        # (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # if invalid, redirect to login again and check if page did not crash
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_valid_pwd(self, *_):
        """
        R2-2 (R1-4):  Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower
        case, and at least one special character.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (valid password)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill in a valid email and 6-letter password
        self.type("#email", "liv@elliot.ca")
        self.type("#password", "cC123#")
        # submit the login info
        self.click('input[type="submit"]')

        # output should be a welcome message for the user at the index page
        # (exhaustive output testing)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome LivTest!", "#welcome-header")

        # if valid, should redirect to the index page
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/")

    def test_login_invalid_short_password(self, *_):
        """
        R2-2 (R1-4):  Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower
        case, and at least one special character.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (short password)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill in a valid email and invalid password
        self.type("#email", "liv@elliot.ca")
        self.type("#password", "C123#")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the correct message, since database shouldn't
        # be checked when password is too short
        # (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # if invalid, redirect to login again and check if page did not crash
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_invalid_no_upper(self, *_):
        """
        R2-2 (R1-4):  Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower
        case, and at least one special character.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (password without upper case letter)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill in a valid email and invalid password
        self.type("#email", "liv@elliot.ca")
        self.type("#password", "c1234#")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the error message, since database shouldn't
        # be checked since password only has lowercase letters
        # (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # if invalid, redirect to login again and check if page did not crash
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_invalid_no_lower(self, *_):
        """
        R2-2 (R1-4):  Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower
        case, and at least one special character.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (password without upper case letter)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill in a valid email and invalid password
        self.type("#email", "liv@elliot.ca")
        self.type("#password", "C1234#")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the error message, since database shouldn't
        # be checked since password only has uppercase letters
        # (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # if invalid, redirect to login again and check if page did not crash
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")

    def test_login_invalid_no_special(self, *_):
        """
        R2-2 (R1-4):  Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least one lower
        case, and at least one special character.
        Black box methods:
        1. Exhaustive output testing (1/3 of the outputs are tested)
        2. Input partitioning (password without special character)
        3. Input robustness testing (check state of page)
        """

        # open login page
        self.open(base_url + '/login')
        # fill in a valid email and invalid password
        self.type("#email", "liv@elliot.ca")
        self.type("#password", "cC1234")
        # submit the login info
        self.click('input[type="submit"]')

        # check for the error message, since database shouldn't
        # be checked since password does not contain a special character
        # (exhaustive output testing)
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # if invalid, redirect to login again and check if page did not crash
        # (input robustness testing)
        self.assert_equal(self.get_current_url(), base_url + "/login")
