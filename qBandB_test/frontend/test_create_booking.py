from seleniumbase import BaseCase

from qBandB_test.conftest import base_url
from unittest.mock import patch
from qBandB.models import register, create_listing

# Create a new user for testing purposes
register("bookinguser", "bookinguser0@gmail.com", "Password0!")
# Create a new listing for testing purposes
create_listing(
    "BookingTest",
    "Used for Frontend Testing",
    75,
    "imadealisting@gmail.com")


class FrontEndCreateBookingPageTest(BaseCase):

    def login_before_create_booking(self):
        """
        This function will login and go to the create listing page
        to set up for future tests.
        """
        # Open login page
        self.open(base_url + '/login')
        # Enter valid credentials
        self.type("#email", "bookinguser0@gmail.com")
        self.type("#password", "Password0!")
        # Submit
        self.click('input[type="submit"]')
        # Go to create booking page
        self.click("Create Booking")  # may need to update for Sara's changes
        # Check if link worked as expected
        self.assert_equal(self.get_current_url(), base_url + "/createbooking")

    def submit_valid_booking_info(self):
        """
        This function will test what happens when a booking is created
        using valid info.
        Black box methods:
        1. Exhaustive output testing (tests for 1/2 outputs of this page)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Open booking page
        self.click_link('Create New Booking')
        # Enter valid listing info
        self.type('#start', '03/09/2022')
        self.type('#end', '03/12/2022')
        self.type('#user_email', 'bookinguser0@gmail.com')
        self.type('#listing_title', 'BookingTest')
        # Submit
        self.click('input[type="submit"]')
        # Make sure app went back to the homepage
        self.assert_equal(self.get_current_url(), base_url + "/")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Browse all available products:")

    def booking_listed_same_user(self):
        """
        This function will test that a user cannot book
        a listing that they created.
        Black box methods:
        1. Exhaustive output testing (tests for 1/2 outputs of this page)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Open booking page
        self.click_link('Create New Booking')
        # Enter Listing Info
        self.type('#start', '03/13/2022')
        self.type('#end', '03/14/2022')
        # User email matches that of created listing
        self.type('#user_email', 'imadealisting@gmail.com')
        # Submit
        self.type('#listing_title', 'BookingTest')
        # Make sure app is still on booking page
        self.assert_equal(self.get_current_url(), base_url + "/createbooking")
        # Check for visual elements
        self.assert_text("Unable to create booking.")

    def booking_balance_check(self):
        """
        This function will test that a user cannot book a lisiting
        that costs more than their balance.
        Black box methods:
        1. Exhaustive output testing (tests for 1/2 outputs of this page)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Open booking page
        self.click_link('Create New Booking')
        # Enter Listing Info
        self.type('#start', '03/15/2022')
        self.type('#end', '03/16/2022')
        # User email should have 25 avaliable for 75 listing
        self.type('#user_email', 'bookinguser0@gmail.com')
        self.type('#listing_title', 'BookingTest')
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on booking page
        self.assert_equal(self.get_current_url(), base_url + "/createbooking")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create booking.")

    def booking_overlap_check(self):
        """
        This function will test that a user cannot book a lisiting
        that has already been booked for one of the days
        Black box methods:
        1. Exhaustive output testing (tests for 1/2 outputs of this page)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Open booking page
        self.click_link('Create New Booking')
        # Enter Listing Info
        # This should conflict with the first booking
        self.type('#start', '03/10/2022')
        self.type('#end', '03/13/2022')
        self.type('#user_email', 'bookinguser0@gmail.com')
        self.type('#listing_title', 'BookingTest')
        # Submit
        self.click('input[type="submit"]')
        # Make sure app is still on booking page
        self.assert_equal(self.get_current_url(), base_url + "/createbooking")
        # Make sure visual elements are displayed (no crashes)
        self.assert_text("Unable to create booking.")

    def booking_appear_homepage_check(self):
        """
        This function will test that a user can see their bookings on their
        homepage.
        Black box methods:
        1. Exhaustive output testing (tests for 1/2 outputs of this page)
        2. Input partitioning
        3. Input robustness testing (check to make sure no crashes)
        """
        # Open index page
        self.click_link('Return to Home Page')
        # Check that link worked 
        self.assert_equal(self.get_current_url(), base_url + "/")
        # Check for Booking Test booking
        self.assert_text("Upcoming bookings")
        self.assert_text("Listing: BookingTest")
        self.assert_text("Start date: 03/09/2022")
