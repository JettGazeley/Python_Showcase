from seleniumbase import BaseCase

from qBandB_test.conftest import base_url
from unittest.mock import patch
from qBandB.models import register

# Create a new user for testing purposes
register("testregisteruser", "update0@test.com", "Password0!")


class FrontEndUpdateUserTest(BaseCase):

    def login_setup(self, *_):
        """
        This function is used for login and navigation
        to the update user profile page
        """
        # open login page
        self.open((base_url + '/login'))
        # login
        self.type("#email", "update0@test.com")
        self.type("#password", "Password0!")
        # submit the info
        self.click("input[type=\"submit\"]")
        # go to update profile
        self.click_link_text("Update Profile")

    def update_check_test(self, *_):
        """
        R3-1: A user is only able to update his/her user name, user email,
        billing address, and postal code.
        1. Input robustness testing
        2. Functionality coverage
        3. Code coverage
        """
        # since we are already setup, check if fields visible
        self.assert_text("#user_username", "testregisteruser")
        self.assert_text("#new_username", "rightuser")
        self.assert_text("#email", "Email")
        self.assert_text("#billing_address", "Billing Address")
        self.assert_text("#postal_code", "Postal Code")

    def billing_update_test(self, *_):
        """
        R3-2: Billing Address should be non-empty, alphanumeric only,
        with no special characters.
        1. Exhaustive output testing
        2. Input robustness testing
        3. Input partitioning
        """
        # pass in arguments
        self.type("#user_username", "testregisteruser")
        # give invalid billing address
        self.type("#billing_address", "123 Test St!")
        # submit info and check if update failed
        self.click("input[type=\"submit\"]")
        self.assert_text("Profile Update Failed", "#error_message")

    def postal_code_update_test(self, *_):
        """
        R3-3: Postal code should be non-empty, alphanumeric-only,
        and no special characters such as !.
        Postal code has to be a valid Canadian postal code.
        1. Exhaustive output testing
        2. Input robustness testing
        3. Input partitioning
        """
        # pass in arguments
        self.type("#user_username", "testregisteruser")
        # give invalid postal code
        self.type("#postal_code", "123 KHM")
        # submit info and check if update failed
        self.click("input[type=\"submit\"]")
        self.assert_text("Profile Update Failed", "#error_message")

    def username_update_test(self, *_):
        """
        R3-4: User name follows the requirements above. 
        This test is based on Input coverage testing.
        1. Exhaustive output testing
        2. Input robustness testing
        3. Input partitioning
        """
        # pass in current username
        self.type("#user_username", "testregisteruser")
        # starting space
        self.type("#new_username", " startingSpace")
        self.click("input[type=\"submit\"]")
        self.assert_text("Profile Update Failed", "#error_message")

        # pass in current username
        self.type("#user_username", "testregisteruser")
        # ending space
        self.type("#new_username", "endingSpace ")
        self.click("input[type=\"submit\"]")
        self.assert_text("Profile Update Failed", "#error_message")

        # pass in current username
        self.type("#user_username", "testregisteruser")
        # too few characters
        self.type("#new_username", "abc")
        self.click("input[type=\"submit\"]")
        self.assert_text("Profile Update Failed", "#error_message")

        # pass in current username
        self.type("#user_username", "testregisteruser")
        # too many characters
        self.type("#new_username", "veryVeryLongTestUsername")
        self.click("input[type=\"submit\"]")
        self.assert_text("Profile Update Failed", "#error_message")

    def test_successful_update(self, *_):
        """
        This function will test to make sure that all profile parameters
        can be successfully updated. This test is based on Functionality
        coverage testing.
        1. Exhaustive output testing
        2. Input robustness testing
        3. Functionality coverage
        """
        # open update page
        self.open((base_url + '/updateprofile'))

        # pass in current username
        self.type("#user_username", "testregisteruser")
        # update username
        self.type("#new_username", "rightTest")
        # update email address
        self.type("#email", "right0@test.com")
        # update address
        self.type("#billing_address", "456 NewAddress St.")
        # update postal code
        self.type("#postal_code", "K7K 1C7")

        # submit the info
        self.click("input[type=\"submit\"]")
        # check for successful message
        self.assert_text("Successfully updated user profile", "#message")
