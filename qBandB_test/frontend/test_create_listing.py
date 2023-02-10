from seleniumbase import BaseCase

from qBandB_test.conftest import base_url
from unittest.mock import patch
from qBandB.models import register

# Create a new user for testing purposes
register("testuser", "test0@gmail.com", "Password0!")


class FrontEndCreateListingPageTest(BaseCase):

    def login_before_create_listing(self):
        """
        This function will login and go to the create listing page
        to set up for future tests.
        """
        # Open login page
        self.open(base_url + '/login')
        # Enter valid credentials
        self.type("#email", "test0@gmail.com")
        self.type("#password", "Password0!")
        # Submit
        self.click('input[type="submit"]')
        # Go to create new listing page
        self.click_link("Create New Listing")
        # Make sure it is on the right page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")

    def submit_valid_listing_info(self):
        """
        This function will test what happens when a listing is created
        using valid info.
        Black box methods:
        1. Exhaustive output testing (tests for 1/2 outputs of this page)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Enter valid listing info
        self.type("#title", "Beautiful Apartment")
        self.type("#description", "Stunning 4 bedroom apartment")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app went back to the homepage
        self.assert_equal(self.get_current_url(), base_url + "/")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Browse all available products:")

    def submit_empty_fields(self):
        """
        This function will test what happens when a listing is created
        with empty fields.
        Black box methods:
        1. Exhaustive output testing (tests for 1/2 outputs of this page)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Return to create listing page
        self.click_link("Create New Listing")
        # Submit with empty fields
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Create New Listing")

    def submit_missing_title(self):
        """
        This function will test what happens when a listing is created
        with a title missing.
        Black box methods:
        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        self.type("#description", "Stunning 4 bedroom apartment")
        self.type("#price", "200")
        # Submit with no title
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Create New Listing")

    def submit_missing_description(self):
        """
        This function will test what happens when a listing is created
        with a description missing.
        Black box methods:
        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        self.type("#title", "Great Apartment")
        self.type("#price", "200")
        # Submit with no description
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Create New Listing")

    def submit_missing_price(self):
        """
        This function will test what happens when a listing is created
        with a price missing.
        Black box methods:
        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        self.type("#title", "Incredible Apartment")
        self.type("#description", "Stunning 4 bedroom apartment")
        # Submit with no price
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Create New Listing")

    def submit_missing_two_fields(self):
        """
        This function will test what happens when a listing is created
        with 2 empty fields.
        Black box methods:
        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        self.type("#description", "Stunning 4 bedroom apartment")
        # Submit with empty fields
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Create New Listing")

    def submit_invalid_title(self):
        """
        This function will test what happens when a listing is created
        using an invalid title.
        Black box methods:
        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # Enter title starting with space (4.1)
        self.type("#title", " Beautiful 4 bedroom apartment")
        self.type("#description", "200 Rabab Street property by the water")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

        # Enter title ending with space (4.1)
        self.type("#title", "Beautiful 4 bedroom apartment ")
        self.type("#description", "200 Rabab Street property by the water")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

        # Enter non-alphanumeric title (4.1)
        self.type("#title", "#$%!!!")
        self.type("#description", "200 Rabab Street property by the water")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

        # Enter title longer than 80 characters (4.2)
        self.type("#title", "Beautiful" * 20)
        self.type("#description", "200 Rabab Street property by the water")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

        # Enter already existing title (4.8)
        self.type("#title", "Beautiful apartment")
        self.type("#description", "200 Rabab Street property by the water")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

    def submit_invalid_description(self):
        """
        This function will test what happens when a listing is created
        using an invalid description.
        Black box methods:
        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # Enter description less than 20 characters (4.3)
        self.type("#title", "apartment")
        self.type("#description", "$200/night!")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

        # Enter description more than 2000 characters (4.3)
        self.type("#title", "apartment")
        self.type("#description", "apartment!" * 300)
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

        # Enter description shorter than title (4.4)
        self.type("#title", "Beautiful 4 bedroom apartment kingston")
        self.type("#description", "Rabab Street location")
        self.type("#price", "200")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

    def submit_invalid_price(self):
        """
        This function will test what happens when a listing is created
        using an invalid price.
        Black box methods:
        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # Enter price less than 10 (4.5)
        self.type("#title", "Great apartment")
        self.type("#description", "200 Rabab Street property by the water")
        self.type("#price", "2")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

        # Enter price more than 10000 (4.5)
        self.type("#title", "Great apartment")
        self.type("#description", "200 Rabab Street property by the water")
        self.type("#price", "1002000")
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on create listing page
        self.assert_equal(self.get_current_url(), base_url + "/createlisting")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create listing.")

    def goto_homepage_from_create_listing(self):
        """
        This function will test what happens when the homepage
        button is clicked from the create listing page.
        Black box methods:
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Click return to homepage
        self.click_link("Return to Home Page")
        # Make sure app went back to the homepage
        self.assert_equal(self.get_current_url(), base_url + "/")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Browse all available products:")
