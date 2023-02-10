from qBandB.models import *
from datetime import datetime
import time
import pytest


# Tests for registering a user


def test_r1_1_register():
    '''
    R1-1: Email cannot be empty. password cannot be empty.
    '''
    assert register('user1', 'sara@sara.com', 'aA123456!') is True

    # Testing password requirement
    assert register('user2', 'invalid@test.com', '') is False

    # Testing email requirement
    assert register('user3', '', 'aA123456!') is False


def test_r1_2_register():
    '''
    R1-2: A user is uniquely identified by his/her user id
    - automatically generated.
    '''
    # Use the login to get the user object and compare ids
    user1 = login('sara@sara.com', 'aA123456!')
    register('user4', 'rabab@rabab.com', 'aA123456!')
    user4 = login('rabab@rabab.com', 'aA123456!')

    assert user1.id is not None
    assert user4.id is not None
    assert user1.id != user4.id


def test_r1_3_register():
    '''
    R1-3: The email has to follow addr-spec defined in RFC 5322
    (see https://en.wikipedia.org/wiki/Email_address for a human-friendly
    explanation). You can use external libraries/imports.
    '''
    # Testing a valid email
    assert register('user5', 'jett@jeff.com', 'aA123456!') is True

    # Testing an invalid email
    assert register('user6', 'liv.elliot.ca', 'aA123456!') is False


def test_r1_4_register():
    '''
    R1-4: Password has to meet the required complexity:
    minimum length 6, at least one upper case, at least one
    lower case, and at least one special character.
    '''
    # Testing a valid password
    assert register('user7', 'liv@elliot.com', 'bB123_') is True

    # Testing invalid passwords
    assert register('user8', 'invalid@test.com', 'aA12!') is False
    assert register('user9', 'invalid@test.com', 'a123456!') is False
    assert register('user10', 'invalid@test.com', 'A123456!') is False
    assert register('user11', 'invalid@test.com', 'aA123456') is False


def test_r1_5_register():
    '''
    R1-5: User name has to be non-empty, alphanumeric-only, and
    space allowed only if it is not as the prefix or suffix.
    '''
    # Testing a valid username
    assert register('user 12', 'user12@test.com', 'aA123456!') is True

    # Testing for invalid usernames
    assert register('', 'invalid@test.com', 'aA123456!') is False
    assert register('user14!', 'invalid@test.com', 'aA123456!') is False
    assert register(' user15', 'invalid@test.com', 'aA123456!') is False
    assert register('user16 ', 'invalid@test.com', 'aA123456!') is False


def test_r1_6_register():
    '''
    R1-6: User name has to be longer than 2 characters and less than
    20 characters.
    '''
    # Testing a valid username
    assert register('user17', 'user17@test.com', 'aA123456!') is True

    # Testing for invalid usernames
    assert register('u0', 'invalid@test.com', 'aA123456!') is False
    assert register(
        'invalidtestusernum19',
        'invalid@test.com',
        'aA123456!') is False


def test_r1_7_register():
    '''
    R1-7: If the email has been used, the operation failed.
    '''

    # Testing if user1 can be added again
    assert register('user1', 'sara@sara.com', 'aA123456!') is False


def test_r1_8_register():
    '''
    R1-8: Shipping address is empty at the time of registration.
    '''

    # Check if an added user has an empty shipping address
    user1 = login('sara@sara.com', 'aA123456!')
    assert user1.billing_address is ''


def test_r1_9_register():
    '''
    R1-9: Postal code is empty at the time of registration.
    '''

    # Check if an added user has an empty postal code
    user1 = login('sara@sara.com', 'aA123456!')
    assert user1.postal_code is ''


def test_r1_10_register():
    '''
    R1-10: Balance should be initialized as 100 at the time of
    registration. (free $100 dollar signup bonus).
    '''

    # Check if an added user has an empty shipping address
    user1 = login('sara@sara.com', 'aA123456!')
    assert user1.balance == 100

# Tests for when a user tries to log in


def test_r2_1_register():
    '''
    R2-1: A user can log in using her/his email address and the password.
    '''

    # Check if an existing user can log in
    user1 = login('sara@sara.com', 'aA123456!')
    assert user1 is not None
    assert user1.username == 'user1'

    # Check if a non-existing user can log in
    user2 = login('invalid@test.com', 'aA123456!')
    assert user2 is None


def test_r2_2_register():
    '''
    R2-2: The login function should check if the supplied inputs meet the
    same email/password requirements as above, before checking the database.
    '''
    # R1-1
    assert login('', 'aA123456!') is None

    assert login('invalid@test.com', '') is None

    # R1-3
    user1 = login('jett@jeff.com', 'aA123456!')
    assert user1 is not None

    assert login('live.elliot.ca', 'aA123456!') is None

    # R1-4
    user1 = login('liv@elliot.com', 'bB123_')
    assert user1 is not None

    assert login('invalid@test.com', 'aA12!') is None

    assert login('invalid@test.com', 'a123456!') is None

    assert login('invalid@test.com', 'A123456!') is None

    assert login('invalid@test.com', 'aA123456') is None


def test_create_listing():
    '''
    Testing create_listing function with arguments that meet every
      requirement
    '''
    assert create_listing('Beautiful 4 bedroom apartment',
                          '200 Rabab Street property by the water', 200,
                          'Rabab@email.com') is True


def test_r4_1():
    '''
    Testing R4-1: Alphanumeric with no space before or after
    '''
    assert create_listing(' Beautiful 4 bedroom apartment',
                          '200 Rabab Street property by the water', 200,
                          'Rabab@email.com') is False
    assert create_listing('Beautiful 4 bedroom apartment ',
                          '200 Rabab Street property by the water', 200,
                          'Rabab@email.com') is False
    assert create_listing('#$%!!!',
                          '200 Rabab Street property by the water', 200,
                          'Rabab@email.com') is False


def test_r4_2():
    '''
    Testing R4-2: Title no longer than 80 characters
    '''
    assert create_listing('Beautiful' * 20,
                          '200 Rabab Street property by the water', 200,
                          'Rabab@email.com') is False


def test_r4_3():
    '''
    Testing R4-3: Description between 20 and 2000 characters
    '''
    assert create_listing('apartment', '$200/night!',
                          200, 'Rabab@email.com') is False
    assert create_listing('apartment', 'apartment!' * 300,
                          200, 'Rabab@email.com') is False


def test_r4_4():
    '''
    Testing R4-4: Description longer than title
    '''
    assert create_listing('Beautiful 4 bedroom apartment kingston',
                          'Rabab Street location', 200,
                          'Rabab@email.com') is False


def test_r4_5():
    '''
    Testing R4-5: Price between 10 and 10000
    '''
    assert create_listing(
        'Beautiful apartment', '200 Rabab Street property by the water', 2,
        'Rabab@email.com') is False
    assert create_listing(
        'Amazing apartment', '200 Rabab Street property by the water',
        1002000, 'Rabab@email.com') is False


def test_r4_6():
    '''
    Testing R4-6: Date between 2021-01-02 and 2025-01-02
    '''
    assert create_listing('4 bedroom apartment',
                          '200 Rabab Street property by the water',
                          200, 'Rabab@email.com',
                          datetime(2026, 1, 2)) is False
    assert create_listing('4 bedrooms available',
                          '200 Rabab Street property by the water',
                          200, 'Rabab@email.com',
                          datetime(2020, 1, 2)) is False


def test_r4_7():
    '''
    Testing R4-7: Owner must exist in database
    '''
    assert create_listing('4 bedrooms',
                          '200 Rabab Street property by the water',
                          200, 'notrabab@rabab.com') is False


def test_r4_8():
    '''
    Testing R4-8: User's products must have different titles
    '''
    assert create_listing('Beautiful 4 bedroom apartment',
                          '200 Rabab Street property by the water', 200,
                          'Rabab@email.com') is False


def test_update_listing():
    '''
    Creating a listing for testing purposes since
    update listing functionality requires listing id.
    '''

    assert update_listing('Rabab@email.com', 'Test', 'Tests',
                          'This is a test description.', 100) is True


def test_r4_1_update_list():
    '''
    R4-1: No spaces as prefix or suffix in Listing title.
    '''

    # Testing R4-1: space as title prefix
    assert update_listing('Rabab@email.com', 'Test', ' Tests',
                          'This is a test description.', 100) is False

    # Testing R4-1: space as title suffix
    assert update_listing('Rabab@email.com', 'Test', 'Tests ',
                          'This is a test description.', 100) is False


def test_r4_2_update_list():
    '''
    R4-2: Title cannot exceed 80 characters.
    '''

    # Testing R4-2: title longer than 80 char
    assert update_listing('Rabab@email.com', 'Test', 'T' * 81,
                          'This is a test description.', 100) is False


def test_r4_3_update_list():
    '''
    R4-3: Description has minimum length of 20
    characters and a maximum of 2000 characters.
    '''

    # Testing R4-3: description less than 20 char
    assert update_listing('Rabab@email.com', 'Test', 'Test',
                          'Too short!.', 100) is False

    # Testing R4-3: description greater than 2000 char
    assert update_listing('Rabab@email.com', 'Test',
                          'Test', 'T' * 2001, 100) is False


def test_r4_4_update_list():
    '''
    R4-4: Description has to be longer than the product's title.
    '''

    # Testing R4-4: description shorter than title
    assert update_listing('Rabab@email.com', 'Test',
                          'Test', 'Tes', 100) is False


def test_r4_5_update_list():
    '''
    R4-5: Price has to be of range [10, 10000]
    '''

    # Testing R4-5: price less than 10
    assert update_listing('Rabab@email.com', 'Test',
                          'Test', 'This is a test description.', 9) is False

    # Testing R4-5: price greater than 10000
    assert update_listing('Rabab@email.com', 'Test',
                          'Test', 'This is a test description.',
                          10001) is False


def test_r4_6_update_list():
    '''
    R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
    '''

    # Testing R4-6: last modifed date before 2021-01-02
    assert update_listing('Rabab@email.com', 'Test', 'Test',
                          'This is a test description.', 1000,
                          datetime(2020, 1, 2)) is False

    # Testing R4-6: last modifed date after 2025-01-02
    assert update_listing('Rabab@email.com', 'Test', 'Test',
                          'This is a test description.', 1000,
                          datetime(2026, 1, 2)) is False


# def test_r4_7_update_list():
#     '''
#     R4-7: The owner of the corresponding product must exist in the database.
#     '''

#     # Testing R4-7: email does not exist in database
#     assert update_listing(listing_id=1,
#                           user_email='Rabab@mail.com',
#                           title='Listing',
#                           description='Updated description!',
#                           price=300) is False


def test_r4_8_update_list():
    '''
    R4-8: A user cannot create products that have the same title.
    '''

    # Testing R4-8: cannot update listing title to existing listing of theirs

    # Create two listings with different titles
    # Update title of one listing to have the same as the other
    # Will return False

    create_listing('Test Title',
                   'This is a test description.',
                   100, 'Rabab@email.com')

    update_listing('Rabab@email.com', 'Test', 'Test Title',
                   'This is a test description.', 100) is False


def test_r5_2_update_list():
    '''
    R5-2: Price cannot be decreased.
    '''

    # Testing R5-2: decreasing listing price
    assert update_listing('Rabab@email.com', 'Test', 'Test',
                          'This is a test description.', 10) is False


def test_r5_3_update_list():
    '''
    R5-3: last_modified_date should be updated when
    the update operation is successful.
    '''

    # Testing R5-3: ensure last modifed date is modifed after update

    # Query to find the correct listing based on the title
    create_listing('Test2', 'This is a test description.',
                   11, 'Rabab@email.com')

    listing_to_update = Listing.query.filter_by(title='Test2').first()

    # Store previously modifed date
    prev_modified = listing_to_update.last_modified_date

    # For current and modifed date to be different, sleep for one second
    time.sleep(1)

    # Update listing
    update_listing('Rabab@email.com', 'Test2', 'Test2',
                   'This is a test description.', 100)

    # Compare dates
    assert prev_modified < listing_to_update.last_modified_date


def test_r3_1():
    '''
    A user is only able to update his/her user name, user email,
    billing address, and postal code.
    '''
    test_user = VerifiedUser.query.filter_by(username='Jett').first()
    assert update_user('Jett', new_username="NewJett") is True
    assert update_user('NewJett', email="jett@gmail.com") is True
    assert update_user('NewJett', billing_address="123 Updated St.") is True
    assert update_user('NewJett', postal_code="K7M 4B1") is True

    assert test_user.username == "NewJett"
    assert test_user.email == "jett@gmail.com"
    assert test_user.billing_address == "123 Updated St."
    assert test_user.postal_code == "K7M 4B1"

    # Changing back to Jett for future test cases
    assert update_user("NewJett", new_username='Jett')


def test_r3_2():
    '''
    Billing Address should be non-empty, alphanumeric only,
    with no special characters.
    '''

    assert update_user("Jett", billing_address="") is False
    assert update_user("Jett", billing_address="123 Test St!") is False
    assert update_user("Jett", billing_address="12 $#@ Bad Address") is False
    assert update_user(
        "Jett",
        billing_address=r"200 Queen St\ Kingston ON") is False


def test_r3_3():
    '''
    Postal code should be non-empty, alphanumeric-only,
    and no special characters such as !.
    Postal code has to be a valid Canadian postal code.
    '''

    assert update_user('Jett', postal_code='K7M9') is False
    assert update_user('Jett', postal_code='Z2T 1B8') is False


def test_r3_4():
    '''
    User name follows the requirements above.
    '''

    assert update_user('Jett', new_username=' startingSpace') is False
    assert update_user('Jett', new_username='endingSpace ') is False
    assert update_user('Jett', new_username='abc') is False
    assert update_user(
        'Jett',
        new_username='veryVeryLongTestUsername') is False


def test_booking_1():
    '''
    User can book a listing.
    '''
    # Create user to book the listing
    register('Olivia', 'liv@hotmail.com', 'Password123!')
    test_user = VerifiedUser.query.filter_by(username='Olivia').first()
    test_user.balance = 1000

    # Create listing to be booked
    create_listing('Three Bedroom Unit',
                   'This is a three bedroom unit that can be booked.', 200,
                   'Rabab@email.com')

    # Book the listing
    assert create_booking("03/03/2022", "03/05/2022",
                          "liv@hotmail.com", "Three Bedroom Unit") is True


def test_booking_2():
    '''
    User cannot book their own listing.
    '''

    # Create a listing by the user
    create_listing('One Bedroom Unit',
                   'This is a one bedroom unit that can be booked.',
                   200, 'liv@hotmail.com')

    # Try to book the user's own listing
    assert create_booking("03/03/2022", "03/05/2022",
                          "liv@hotmail.com", "One Bedroom Unit") is False


def test_booking_3():
    '''
    User cannot book a listing that costs 
    more than his/her balance.
    '''

    # Create listing that costs more than the user's balance
    create_listing('Six Bedroom Unit',
                   'This is a six bedroom unit that can be booked.',
                   2000, 'Rabab@email.com')

    # Attempt to book the listing over user's balance
    assert create_booking("03/03/2022", "03/05/2022",
                          "liv@hotmail.com", "Six Bedroom Unit") is False


def test_booking_4():
    '''
    A user cannot book a listing that is already 
    booked with the overlapped dates.
    '''

    create_listing('Seven Bedroom Unit',
                   'This is a seven bedroom unit that can be booked.',
                   250, 'Rabab@email.com')

    register('Liver', 'liver@hotmail.com', 'Password123!')
    liv = VerifiedUser.query.filter_by(username='Liver').first()
    liv.balance = 1000

    # User 'Olivia' currently booked from Jan. 4th, to Jan. 7th, 2022
    create_booking("01/04/2022", "01/07/2022",
                   "liv@hotmail.com",
                   "Seven Bedroom Unit")

    # User 'Liver' attempts to book listing from Jan. 2nd, to Jan. 5th, 2022
    assert create_booking("01/02/2022", "01/05/2022",
                          "liver@hotmail.com",
                          "Seven Bedroom Unit") is False

    # User 'Liver' attempt to book listing from Jan. 5th, to Jan. 8th, 2022
    assert create_booking("01/05/2022", "01/06/2022",
                          "liver@hotmail.com",
                          "Seven Bedroom Unit") is False

    # User 'Liver' attempt to book listing from Jan. 2th, to Jan. 8th, 2022
    assert create_booking("01/02/2022", "01/08/2022",
                          "liver@hotmail.com",
                          "Seven Bedroom Unit") is False

    # User 'Liver' attempt to book listing from Jan. 4th, to Jan. 5th, 2022
    assert create_booking("01/04/2022", "01/05/2022",
                          "liver@hotmail.com",
                          "Seven Bedroom Unit") is False
