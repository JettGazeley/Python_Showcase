from seleniumbase import BaseCase

from qBandB_test.conftest import base_url
from unittest.mock import patch
from qBandB.models import register, create_listing

# Create new users for testing purposes
register("usertest", "tester@gmail.com", "Password!")
register("usertest1", "tester1@gmail.com", "Password!")

# Create new listings for testing purposes
create_listing("Created Listing", "This is a test description.",
               15, "tester@gmail.com")
create_listing("Created Other Listing", "This is a test description.",
               10, "tester1@gmail.com")


class FrontEndUpdateListingPageTest(BaseCase):

    def login_before_update_listing(self):
        """
        This function will login and go directly to
        the update listing page.

        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # Go to login page
        self.open(base_url + '/login')
        # Enter login info
        self.type("#email", "tester@gmail.com")
        self.type("#password", "#Password!")
        # Click enter button
        self.click('input[type="submit"]')
        # Go to update listing page
        self.click_link("Update Listings")
        # Test to see if redirected to update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')

    def valid_update_listing(self):
        """
        This function will successfully update a product
        and redirect to home page.

        1. Exhaustive output testing (for 'title' field)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Enter valid updated listing info
        self.type("#title", "Created Listing")  # Exhaustive output testing
        self.type("#new_title", "Updated Listing")
        self.type("#description", "This is an updated test description.")
        self.type("#price", 16)
        # Click update button
        self.click('input[type="submit"]')
        # Test to see if on successful update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        self.assert_text("Listing 'Updated Listing' successfully updated.")
        # Go to homepage
        self.click_link("Return to Home Page")
        # Test to see if updated product is displayed
        self.assert_text("Name: Updated Listing")
        self.assert_text("Price: $11.00")
        self.assert_text("Description: This is an updated test description.")

    def invalid_title_field(self):
        """
        This function tests when the old title or 'title' field is invaild.
        This is the only field that cannot be empty upon updating.
        This must be a title of a listing that the current user creates.

        1. Exhaustive output testing
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """

        # Attempt to update with empty 'title' field
        # Go to update listing page
        self.click_link("Update Listings")
        # Do not enter a title and submit -> nothing should happen
        self.click('input[type="submit"]')
        # Test to see if on standard update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        self.assert_text("Update A Listing")

        # Attempt to update with listing title created by a different user.
        self.type("#title", "Created Other Listing")
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        self.assert_text(
            "Listing 'Created Other Listing' could not be updated.")

    def invalid_new_title(self):
        """
        This function tests when an invalid new_title is submitted.

        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # R4-1: contains non-alphanumeric characters
        self.type("#title", "Updated Listing")
        self.type("#new_title", "Updated Listing!")
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R4-1: contains space are prefix
        self.type("#title", "Updated Listing")
        self.type("#new_title", " Updated Listing")
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R4-1: contains space are suffix
        self.type("#title", "Updated Listing")
        self.type("#new_title", "Updated Listing ")
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R4-2: contains more than 80 characters
        self.type("#title", "Updated Listing")
        self.type("#new_title", " Updated Listing" * 10)
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R4-8: user cannot create products that have the same title
        self.type("#title", "Updated Listing")
        # Attempt to update with title of already existing listing
        self.type("#new_title", "Created Other Listing")
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

    def invalid_description(self):
        """
        This function tests when an invalid description is created.

        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # R4-3: description must be at least 20 characters long
        self.type("#title", "Updated Listing")
        self.type("#description", "Updated Listing!!")
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R4-3: description cannot exceed 2000 characters
        self.type("#title", "Updated Listing")
        self.type("#description", "D" * 2001)
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R4-4: description must be longer that its title
        self.type("#title", "Updated Listing")
        self.type("#description", "Description")
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

    def invalid_price(self):
        """
        This function tests when an invalid description is created.

        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # R4-5: price must be greater than 10
        self.type("#title", "Updated Listing")
        self.type("#price", 9)
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R4-5: price must be less than than 10000
        self.type("#title", "Updated Listing")
        self.type("#price", 10001)
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

        # R5-2: price can not be decreased - initial price: $15
        self.type("#title", "Updated Listing")
        self.type("#price", 14)
        # Attempt to update with invalid input
        self.click('input[type="submit"]')
        # Test to see if error message appears on update listing page
        self.assert_equal(self.get_current_url(), base_url + '/updatelisting')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Listing 'Updated Listing' could not be updated.")

    def goto_homepage_from_update_listing(self):
        """
        This function tests what happens when the homepage
        button is clicked from the update listing page.

        1. Input partitioning
        2. Input robustness testing (check to make sure no crashes)
        """
        # Click return to home page link
        self.click_link("Return to Home Page")
        # Test to see if redirected to home page
        self.assert_equal(self.get_current_url(), base_url + '/')
        # Check for visual elements displayed (no crashes)
        self.assert_text("Browse all available products:")
