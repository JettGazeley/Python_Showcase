# Python Showcase

[![Pytest-All](https://github.com/beepbeep63/CISC-CMPE-327/actions/workflows/style_check.yml/badge.svg?branch=main)](https://github.com/beepbeep63/CISC-CMPE-327/actions/workflows/style_check.yml)

[![Python PEP8](https://github.com/beepbeep63/CISC-CMPE-327/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/beepbeep63/CISC-CMPE-327/actions/workflows/pytest.yml)

# This project was created during my software quality assurance course at Queen's University
# Our goal for this project was to create an Airbnb clone
The README below contains information relating to our sprint reviews and retrospectives

# A4 Review and Retrospect

The testing file for the frontend is qBandB_test\frontend\test_frontend.py.

## Login Testing

test_login_valid() - tests R2-1. A valid email and password are used as one input partition. One out of three outputs are tested, which is the change in the welcome header element to "Welcome {{user.username}}". Robustness is tested by making sure the program has not crashed, and has successfully redirected to the index page.

test_login_invalid_email() - tests R2-1. A non-registered email and password combination are used as one input partition. One out of three outputs are tested, which is the change in the message element to "login failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_invalid_password() - tests R2-1. A registered email and invalid password combination are used as one input partition. One out of three outputs are tested, which is the change in the message element to "login failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_empty_email() - tests R2-2 and R1-1. An empty email and any password combination are used as one input partition. One out of three outputs are tested, which is the change in the message element to "Please login". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_empty_pwd() - tests R2-2 and R1-1. Any email and an empty password combination are used as one input partition. One out of three outputs are tested, which is the change in the message element to "Please login". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_valid_addr_spec() - tests R2-2 and R1-3. An addr-spec following registered email and a valid password combination are used as one input partition. One out of three outputs are tested, which is the change in the welcome header element to "Welcome {{user.username}}". Robustness is tested by making sure the program has redirected to the index page.

test_login_invalid_addr_spec() - tests R2-2 and R1-3. A no addr-spec following email and a valid password combination are used as one input partition. One out of three outputs are tested, which is the change in the message element to "login failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_valid_pwd() - tests R2-2 and R1-4. A valid, registered email and a valid 6-letter password combination are used as one input partition. One out of three outputs are tested, which is the change in the welcome header element to "Welcome {{user.username}}". Robustness is tested by making sure the program has redirected to the index page.

test_login_invalid_short_password() - tests R2-2 and R1-4. A registered email and an invalid, 5-letter password combination are used as one input partition. One out of three outputs are tested, which is the change in the message element to "login failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_invalid_no_upper() - tests R2-2 and R1-4. A registered email and an invalid password with only lower case letter(s) are used as one input partition. One out of three outputs are tested, which is the change in the message element to "login failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_invalid_no_lower() - tests R2-2 and R1-4. A registered email and an invalid password with only upper case letter(s) are used as one input partition. One out of three outputs are tested, which is the change in the message element to "login failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

test_login_invalid_no_special() - tests R2-2 and R1-4. A registered email and an invalid password with no special character(s) are used as one input partition. One out of three outputs are tested, which is the change in the message element to "login failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the login page.

## Create Listing Page Testing

login_before_create_listing() - This function will login and go to the create listing page to set up for future tests.

submit_valid_listing_info() - This function will test what happens when a listing is created using valid info. Input that meets all of the criteria is used as one input partition. One out of two outputs is tested, which is a redirect to the homepage. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the homepage.

submit_empty_fields() - This function will test what happens when a listing is created with empty fields. No input is used as one input partition. One out of two outputs is tested, which is staying on the create listing page. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

submit_missing_title() - This function will test what happens when a listing is created with a title missing. Having only the description and price entered as input is used as one input partition. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

submit_missing_description() - This function will test what happens when a listing is created with a description missing. Having only the title and price entered as input is used as one input partition. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

submit_missing_price() - This function will test what happens when a listing is created with a price missing. Having only the title and description entered as input is used as one input partition. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

submit_missing_two_fields() - This function will test what happens when a listing is created with two fields missing. Having only the description entered as input is used as one input partition. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

submit_invalid_title() - This function will test what happens when a listing is created using an invalid title. Tests R4-1, R4-2, and R4-8. A title starting with a space, and title ending with a space, a non-alphanumeric title, a title longer than 80 characters, and an already existing title are used as input partitions. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

submit_invalid_description() - This function will test what happens when a listing is created using an invalid description. Tests R4-3 and R4-4. A description less than 20 characters, a description more than 2000 characters, and a description shorter than the listing's title are used as input partitions. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

submit_invalid_price() - This function will test what happens when a listing is created using an invalid price. Tests R4-5. A price less than 10 and a price more than 10000 are used as input partitions. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the create listing page.

goto_homepage_from_create_listing() - This function will test what happens when the homepage button is clicked from the create listing page. Clicking the homepage button is used as one input partition. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the homepage.

## Update User Testing

update_check_test() - tests R3-1. Robustness is tested by making sure the program has not crashed, and has successfully stayed on the update page. The text for each field is used to check for all functionality via functionality coverage. Code coverage is achieved through checking the text fields as well, as these would only be avaliable if the backend supported it.

billing_update_test() - tests R3-2. A registered username and an invalid billing address with an exclamation point is used as one input partition. The output of this input is tested through the change in the message element to "Profile Update Failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the update page with the correct message.

postal_code_update_test() - tests R3-3. A registered username and an invalid postal code with an invalid format is used as one input partition. The output of this input is tested through the change in the message element to "Profile Update Failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the update page with the correct message.

username_update_test() - tests R3-4. A registered username and an invalid new username with a starting space in the new username is used as one input partition. The output of this input is tested through the change in the message element to "Profile Update Failed". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the update page with the correct message.

test_successful_update() - tests that all profile parameters can be successfully updated. A registered username and all possible valid parameters are passed in partitions. The output of this input is tested through the change in the message element to "Successfully updated user profile". Robustness is tested by making sure the program has not crashed, and has successfully redirected back to the update page with the correct message.
goto_homepage_from_update_listing(self) - this function tests to see if the “Return to Home Page” link correctly redirects the user to the home page when clicked. Robustness testing is used to ensure that the program has not crashed, and that the page has been redirected correctly.

## User Registration Testing

test_registration_success() - tests functionality of valid registration parameters. This function will test what happens when a user is registered with valid information. Input partition takes place at the username, email and password fields. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the login page.

test_empty_credentials() - tests R1-5 and R1-1. This function will test what happens when a user is registered with no information. Input partition takes place at the username, email and password fields. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the login page.

test_invalid_id() - tests R1-2. This function will test what happens when a user is registered with valid information and makes sure the id is unique. Input partition takes place at the username, email and password fields. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page indicating a non-unique id.

test_invalid_email() - tests R1-3. This function will test what happens when a user is registered with an invalid email address. Input partition takes place at the email field. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page to ask for a valid email.

test_invalid_password() - tests R1-4. This function will test what happens when a user is registered with an invalid password. Input partition takes place at the password field. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page to ask for a valid password.

test_invalid_username_characters() - tests R1-5. This function will test what happens when a user is registered with invalid characters for their username. Input partition takes place at the username field. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page to ask for a valid username.

test_invalid_username_length() - tests R1-6. This function will test what happens when a user is registered with too many or too few characters for their username. Input partition takes place at the username field. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page to ask for a valid username.

test_duplicate_email() - tests R1-7. This function will test what happens when a user is registered with a duplicate email address. Input partition takes place at the email field. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page to ask for a valid email.

test_shipping_address() - tests R1-8. This function will test what happens when a user is registered with an invalid billing address. Input partition takes place at the billing_address field. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page to ask for a valid billing address.

test_postal_code() - tests R1-9. This function will test what happens when a user is registered with an invalid postal code. Input partition takes place at the postal_code field. Robustness is tested by making sure that the program has not crashed, and has successfully redirected back to the register page to ask for a valid postal code.

test_balance_ammount() - tests R1-10. This function will test what happens when a user is registered with a valid information, and checks that the balance ammount is correct. Input partition takes place at the balance field. Robustness is tested by making sure that the program has not crashed, and has successfully asserted the balance ammount to be 100 for the registered user.

test_login_success() - tests that registration was a success by accessing login with correct credentials. Input partition takes place at all fields required for login. Robustness is tested by making sure that the program has not crashed, and has successfully redirected to the home page after login.

## Update Listing Testing

login_before_update_listing() - tests R2-1. A valid email and password is used as one input partition to login. Once submitted, the program tests if the the page has been successfully redirected to the home page. Robustness testing is used to ensure that the program has not crashed.

valid_update_listing() - tests R5-4. Valid listing title (part of exhaustive output testing), new listing tile, description, and price are used as input for one partition. One of two outputs are tested, which is the change in the Update Listing Header to “Listing ‘{{title.title}}’ successfully updated.” Robustness testing is used to ensure that the program has not crashed.

invalid_title_field() - Empty listing title field is used as input to test one of three outputs, which is staying on the same update listing page with the heading “Update A Listing”. A listing title created by a different user than the current user is used as input in the #title field. Testing one of three outputs which is “Listing ‘‘{{title.title}}' could not be updated.” (exhaustive output testing). Robustness testing is used to ensure that the program has not crashed.

invalid_new_title() - tests R4-1, R4-2, and R4-8. A title containing non-alphanumeric characters, a space as the prefix, a space a the suffix, and an already existing title are used as input for one partition in the #new_title field. Testing one of two outputs which is “Listing ‘‘{{title.title}}' could not be updated.”. Robustness testing is used to ensure that the program has not crashed.

invalid_description() - tests R4-3, R4-4. A description containing less than 20 characters, more than 2000 characters, and a description length less than the title/new_title are used as input for one partition in the #description field. Testing one of two outputs, which is “Listing ‘‘{{title.title}}' could not be updated.”. Robustness testing is used to ensure that the program has not crashed.

invalid_price() - tests R4-5 and R5-2. A price less than 1, greater than 10000, and less than original price are used as input for one partition in the #price field. Testing one of two outputs, which is “Listing ‘‘{{title.title}}' could not be updated.”. Robustness testing is used to ensure that the program has not crashed.

goto_homepage_from_update_listing(self) - this function tests to see if the “Return to Home Page” link correctly redirects the user to the home page when clicked. Robustness testing is used to ensure that the program has not crashed, and that the page has been redirected correctly.

## Create Booking Frontend-Testing

submit_valid_booking_info(self) - test R6-1 - this function tests to see that a booking can be created with valid booking information on the frontend. Robustness testing is used to ensure that the program has not crashed, and that the page has been redirected correctly. 

booking_listed_same_user(self) - tests R6-2 - this function tests that a user cannot book a listing that they have created. In this test, we use exhaustive output testing, input partitioning, and robustness testing to test the functionality. 

booking_balance_check(self) - tests R6-3 - this function will test that a user cannot book a listing that costs more than their balance. The reason that this test works is because of the price of the valid_booking_info listing. Again, we use exhaustive output testing, input partitioning and input robustness testing to test the frontend

booking_overlap_check(self) - tests R6-4 - this function will test that a user cannot book a listing that has already been booked for one of the days they are requesting. The reason this test works is that the days overlap with the days booked in the valid booking test above. Here we use exhaustive output testing, input partitioning and input robustness testing for the frontend.

booking_appear_homepage_check(self) - tests R6-5 - this function will ensure that a user can see their bookings on their homepage. For testing, we return to the homepage and look to see if the valid booking test above is shown. To verify this, we use exhaustive output testing, input partitioning and input robustness testing. 
