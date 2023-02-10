from seleniumbase import BaseCase

from qBandB_test.conftest import base_url
from unittest.mock import patch
from qBandB.models import VerifiedUser, register

"""
This file defines all integration tests for the frontend homepage.
"""

# create a new user for testing purposes
register("register", "register@test.com", "Password0!")


class FrontEndHomePageTest(BaseCase):
    def test_registration_success(self, *_):
        """
        This is a sample front end unit test to register user
        and verfiy that they are redirected to login page.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open register page
        self.open(base_url + '/register')
        # fill in registration info
        self.type("#email", "test0@test.com")
        self.type("#name", "test")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # test if page redirects to login
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    def test_empty_credentials(self, *_):
        """
        This is front end unit test to check for empty email's
        and passwords.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open register page
        self.open(base_url + '/register')
        # fill in all except for email and password
        self.type("#name", "test")
        # click enter button
        self.click('input[type="submit"]')

        # test if still on register page
        self.assert_equal(self.get_current_url(), base_url + "/register")
        # test to see if email text is present
        self.is_attribute_present("#email", "data-focus-visible-added")

    def test_invalid_email(self, *_):
        """
        The email has to follow addr-spec defined in RFC 5322
        (see https://en.wikipedia.org/wiki/Email_address for a human-friendly
        explanation). You can use external libraries/imports.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "emailtest.testing.com")
        self.type("#name", "email")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # check if still on registration page
        self.assert_equal(self.get_current_url(), base_url + "/register")

    def test_invalid_password(self, *_):
        """
        Password has to be minimum 6 characters, at least one uppercase,
        at least one lower case, and at least one special character.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "password@test.com")
        self.type("#name", "password")
        self.type("#password", "123456")
        self.type("#password2", "123456")
        # click enter button
        self.click('input[type="submit"]')

        # check if still on registration page
        self.assert_equal(self.get_current_url(), base_url + "/register")

    def test_invalid_username_characters(self, *_):
        """
        User name has to be non-empty, alphanumeric-only, and
        space allowed only if it is not as the prefix or suffix.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "username@test.com")
        self.type("#name", "user14!")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # check if still on registration page
        self.assert_equal(self.get_current_url(), base_url + "/register")

    def test_invalid_username_length(self, *_):
        """
        User name has to be longer than 2 characters and less than
        20 characters.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "username@test.com")
        self.type("#name", "invalidtestusernum19")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # check if still on registration page
        self.assert_equal(self.get_current_url(), base_url + "/register")

    def test_duplicate_email(self, *_):
        """
        If the email has been used, the operation failed.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "register@test.com")
        self.type("#name", "duplicate")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # check if still on registration page
        self.assert_equal(self.get_current_url(), base_url + "/register")

    def test_shipping_address(self, *_):
        """
        Shipping address is empty at the time of registration.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "shipping@test.com")
        self.type("#name", "shipping")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # check if shipping address is empty
        self.assert_element_absent("#billing_address", "")

    def test_postal_code(self, *_):
        """
        Postal code is empty at the time of registration.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "postal@test.com")
        self.type("#name", "postal")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # check if shipping address is empty
        self.assert_element_absent("#postal_code", "")

    def test_balance_ammount(self, *_):
        """
        Balance should be initialized as 100 at the time of
        registration.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open registration page
        self.open(base_url + '/register')
        # fill in invalid email
        self.type("#email", "balance@test.com")
        self.type("#name", "balance")
        self.type("#password", "Password0!")
        self.type("#password2", "Password0!")
        # click enter button
        self.click('input[type="submit"]')

        # check if balance is set to 100
        # identify user
        user = VerifiedUser.query.filter_by(username='balance').first()
        # check balance of user created in above lines
        self.assert_equal(user.balance, 100)

    def test_login_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        1. Functionality coverage
        2. Input robustness testing
        3. Input partitioning
        """
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "register@test.com")
        self.type("#password", "Password0!")
        # click enter button
        # still on login page during test for some reason
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        # test if the page redirects to /
        # if true, then login was successful
        self.assert_equal(self.get_current_url(), base_url + "/")
