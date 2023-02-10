from qBandB import app
# from atexit import register
# from email.policy import default
# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import re

from sqlalchemy.orm import relationship

'''
Setting up SQLAlchemy and data models so
data models can be mapped into database tables
'''
db = SQLAlchemy(app)

"""A test to see if the flask app is working"""


class VerifiedUser(db.Model):
    """This class represents a verified user"""
    __tablename__ = 'verifieduser'

    # User info
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    # Contact info
    email = db.Column(db.String(120), unique=True, nullable=False)
    # decided to make phone numbers strings to allow for "-"
    phone_number = db.Column(db.String(16), nullable=True)
    billing_address = db.Column(db.String(200), nullable=True)
    postal_code = db.Column(db.String(100), nullable=True)
    balance = db.Column(db.Numeric(precision=8, scale=2),
                        default=100, nullable=False)

    # verification info
    registered_on = db.Column(db.String(15), unique=False,
                              nullable=False, default=datetime.utcnow)
    verified = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<User %r>, <Registered On: %r>' \
            % self.username % self.registered_on


class Listing(db.Model):
    """This class represents a listing made in QB&B"""
    __tablename__ = "listing"

    id = db.Column(db.Integer, primary_key=True)
    # Title of house or apartment listing
    title = db.Column(db.String(200), unique=True,
                      nullable=False)
    # Desciption of house or apartment
    description = db.Column(db.Text)
    # price of house or apartment
    price = db.Column(db.Numeric(precision=8, scale=2),
                      nullable=False)
    # last modified date of listing
    last_modified_date = db.Column(db.DateTime, nullable=False,
                                   default=datetime.utcnow)

    # id of verified user that posted this listing
    user_id = db.Column(db.Integer, db.ForeignKey("verifieduser.id"),
                        nullable=False)
    user = db.relationship("VerifiedUser", backref="listings")

    # creating a one to many relationship with bookings
    bookings = relationship("Booking", back_populates="listing")

    def __repr__(self):
        # String representation of a Listing instance
        return '<Listing %r>' % self.id


class Booking(db.Model):
    """This class represents a booking made in QB&B"""
    id = db.Column(db.Integer, primary_key=True)
    # start date and time of the specific booking
    start_date = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    # end date and time of the specific booking
    end_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    # id of verified user that made the booking
    user_id = db.Column(db.Integer, db.ForeignKey("verifieduser.id"),
                        nullable=False)
    user = db.relationship(
        "VerifiedUser",
        backref="bookings",
        foreign_keys=[user_id])

    # id of listing that was booked
    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id"),
                           nullable=False)
    listing = db.relationship(
        "Listing",
        back_populates="bookings")

    def __repr__(self):
        # String representation of a Booking instance
        return '<Booking %r>' % self.id


class Review(db.Model):
    """
    Represents reviews made by users
    stored in database.
    """

    # Id of the user submitting the review
    id = db.Column(db.Integer, primary_key=True)
    # Score inputed by the user
    score = db.Column(db.Numeric(precision=2, scale=1),
                      nullable=False)
    # Review inputed by the user
    review = db.Column(db.Text)

    # id of verified user that posted the review
    user_id = db.Column(db.Integer, db.ForeignKey("verifieduser.id"),
                        nullable=False)
    user = db.relationship(
        "VerifiedUser",
        backref="reviews",
        foreign_keys=[user_id])

    # id of listing that the review is about
    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id"),
                           nullable=False)
    listing = db.relationship(
        "Listing",
        backref="listing_reviews",
        foreign_keys=[listing_id])

    def __repr__(self):
        # string representation of a review instance
        return '<Review %r>' % self.id

# Helper functions for validating inputs


def valid_email(email):
    """
    Checks if a email meets addr-sepc in RFC 5322
        Parameters:
            email (string)
        Returns:
            True if the email is valid, and False if it is not.
    """
    # Using a try catch statement with the email-validator library functions

    valid_email = ""

    try:
        valid_email = validate_email(email)
    except ValueError as e:
        print('Email address is not valid')
        return False

    if valid_email:
        return True


def valid_username(username):
    """
    Checks if a username is valid.
        Parameters:
            username (string)
        Returns:
            True if the username is valid, and False if it is not
    """
    if not (2 < len(username) < 20):
        print("Username must be longer than 2 and smaller than 20 characters.")
        return False
    valid_char = bool(re.match('[a-zA-z0-9\\s]+$', username))
    if valid_char is False:
        print("Username can only contain alpha-numeric letters and spaces.")
        return False
    else:
        if username[0] == " " or username[-1] == " ":
            print("Username cannot start or end with a space.")
            return False
        else:
            return True


def valid_password(password):
    """
    Checks if a password is valid.
        Parameters:
            password (string)
        Returns:
            True if the password is valid, and False if the password is
            invalid.
    """
    if (len(password) < 6):
        print("Password must contain at least 6 characters.")
        return False
    if not any(c.isalpha() for c in password):
        print("Password must contain letters.")
        return False
    if not any(c.isupper() for c in password):
        print("Password must contain at least one upper case character.")
        return False
    if not any(c.islower() for c in password):
        print("Password must contain at least one lower case character.")
        return False
    if password.isalnum():
        print("Password must contain at least one special character.")
        return False
    return True


# Create tables so objects can be added and changed
db.create_all()


def register(username, email, password):
    """
    Registers a valid user.
        Parameters:
            username (string)
            email (string)
            password (string)
        Returns:
            True if the user has been registered, False otherwise.
    """
    # Check if the user is unique
    users = VerifiedUser.query.filter_by(email=email).all()
    if len(users) > 0:
        print("Can only register a unique email.")
        return False

    # Check if the information is valid
    if not (valid_password(password) and
            valid_email(email) and
            valid_username(username)):
        return False

    # add the user
    user = VerifiedUser(
        email=email,
        username=username,
        password=password,
        postal_code="",
        billing_address="",
        phone_number="")

    # add user to database and commit
    db.session.add(user)
    db.session.commit()

    return True


def login(email, password):
    # Check if the email and password are valid
    if not (valid_email(email) and valid_password(password)):
        return None

    # Check if the email and password combination exists
    users = VerifiedUser.query.filter_by(email=email, password=password).all()
    if len(users) != 1:
        return None

    # return user object if found
    return users[0]


def create_listing(title, description, price, user_email,
                   last_modified_date=datetime.utcnow()):
    '''
    This function creates a listing.
    Parameters:
        title: String title of listing
        description: String description of listing
        price: Numeric price of listing
        user_email: String email of user
        last_modified_date: Datetime defaulted to current time
    Returns:
        Boolean value: True if listing was successfully created
                       False otherwise
    '''
    # Create a specific user for testing if not already created
    is_rabab = VerifiedUser.query.filter_by(email="Rabab@email.com").all()
    if len(is_rabab) == 0:
        user1 = VerifiedUser(username="Rabab", password="password",
                             email="Rabab@email.com",
                             phone_number="613-613-6133",
                             billing_address="200 Rabab St",
                             postal_code="K2K 2K2", balance=0)
        db.session.add(user1)
        db.session.commit()

    # R4-1
    result = re.match("^[^\\ ][a-zA-Z0-9 ]*[^\\ ]$", title)
    if result is None:
        print("The title of the product has to be alphanumeric-only, ")
        print("and space allowed only if it is not as prefix and suffix.")
        return False

    # R4-2
    if len(title) > 80:
        print("The title of the product is longer than 80 characters.")
        return False

    # R4-3
    result = re.match("^.{20,2000}$", description)
    if result is None:
        print("Description minimum length is 20 characters ")
        print("and maximum is 2000 characters.")
        return False

    # R4-4
    if len(title) > len(description):
        print("Description has to be longer than the product's title.")
        return False

    # R4-5
    try:
        if (int(price) < 10) or (int(price) > 10000):
            print("Price has to be of range [10, 10000].")
            return False
    except ValueError as e:
        print('Price is not an integer')
        return False

    # R4-6
    try:
        after_date = datetime(2021, 1, 2)
        before_date = datetime(2025, 1, 2)
        if (last_modified_date < after_date) or \
                (last_modified_date > before_date):
            print("Last modified date must be after 2021-01-02 ")
            print("and before 2025-01-02.")
            return False
    except TypeError as e:
        print('Time entered is invalid')
        return False

    # R4-7
    current_user = VerifiedUser.query.filter_by(email=user_email).all()
    if len(current_user) == 0:
        print("The owner of the corresponding product must exist ")
        print("in the database.")
        return False

    # R4-8
    current_user = VerifiedUser.query.filter_by(email=user_email).first()
    print("User ID: {}", current_user.id)
    products = Listing.query.filter_by(
        user=current_user, title=title).all()
    if len(products) > 0:
        print("A user cannot create products that have the same title.")
        return False

    # Add new listing to database
    new_listing = Listing(
        title=title,
        description=description,
        price=price,
        last_modified_date=last_modified_date,
        user=current_user)
    db.session.add(new_listing)
    db.session.commit()
    return True


def check_price(price):
    """
    Verifies if the listing title is valid.
    Parameters:
        price: new listing price
    Returns:
        Boolean Value: True if title is valid and can be updated
                       False otherwise
    """

    if (10 <= price <= 10000):
        return True
    else:
        print("Need listing price be greater than $10 and less than $10000.")
        return False


def check_title(title, new_title):
    """
    Verifies if the listing title is valid.
    Parameters:
        title: new listing title
        description: new listing description
    Returns:
        Boolean Value: True if title is valid and can be updated
                       False otherwise
    """

    # If the title has not been updated
    if (title == new_title):
        return True

    # Return False if listing title exceeds 80 charcters
    if not (0 <= len(new_title) <= 80):
        print("Listing title can have an maximum of 80 characters.")
        return False

    # Return False if listing title is not alphanumeric or a space
    for char in new_title:
        # if the char is not alphanumeric or a space
        if not (char.isalnum() or char.isspace()):
            print("Listing title cannot contain symbols.")
            return False

    # Return False if the listing title contains a space as a prefix or suffix
    if new_title[0].isspace() or new_title[len(new_title) - 1].isspace():
        print("Listing title cannont have a space as a prefix or suffix.")
        return False

    # Return False if the listing title already exists in database
    # List of listings created by the user with the same title
    listings = Listing.query.filter_by(title=new_title).all()

    # If listing with this title already exists
    if len(listings) > 0:
        print("A user cannot create products that have the same title.")
        return False

    return True


def check_description(description, new_title):
    """
    Verifies if the listing description is valid.
    Parameters:
        description: new listing description
        title_new: new listing title
    Return: True if description is valid and can be updated
            False otherwise
    """

    # If description is longer than the new title and less than 2000 chars
    if (len(new_title) <= len(description) <= 2000):
        return True
    else:
        print("Invalid length of listing description.")


def update_listing(owner_email, title, new_title=None,
                   description=None, price=None,
                   last_modified_date=datetime.utcnow()):
    """
    This function updates an existing listing.
    Parameters:
        listing_id: id used to identify the rental listing being updated
        owner_id: id of the user updating the listing
        title: title of listing to change
        title_new: new listing title
        description: new listing description
        price: new listing price
    Returns:
        Boolean Value: True if listing was successfully created
                       False otherwise
    """

    # Create listing to update for testing purposes
    # If not already created
    test_listing = Listing.query.filter_by(title='Test').first()

    if test_listing is None:
        create_listing('Test', 'This is a test description.',
                       11, 'Rabab@email.com')

    # find listing based on title
    # this assumes that there cannot be multiple listings with the same title
    # which is not true
    listing_owner = VerifiedUser.query.filter_by(email=owner_email).first()
    if listing_owner is None:
        print("User does not exist in the database.")
        return False

    # query for listing based on current title and owner email
    listing_to_update = Listing.query.filter_by(
        title=title, user=listing_owner).first()
    if listing_to_update is None:
        print("Listing \'" + title +
              "\' does not exist in the database with this user.")
        return False

    # R5-2: update listing price
    if price is not None:
        if check_price(price):
            # update price if than greater or equal to previous price
            if (price >= listing_to_update.price):
                listing_to_update.price = price
            else:
                print("Listing price cannot be decreased.")
                return False
        else:
            return False

    # R5-4: update listing title
    if new_title is not None:
        if check_title(title, new_title):
            listing_to_update.title = new_title
        else:
            return False
    else:
        new_title = title

    # R5-4: update listing description
    if description is not None:
        if check_description(description, new_title):
            if (len(description) < 20):
                print("Description cannot be less than 20 characters.")
                return False
            listing_to_update.description = description
        else:
            return False

    # R5-3: Last modified date automatically updated
    after_date = datetime(2021, 1, 2)
    before_date = datetime(2025, 1, 2)
    if (last_modified_date < after_date) or (last_modified_date > before_date):
        print("Last modified date must be after 2021-01-02 " +
              "and before 2025-01-02.")
        return False
    else:
        listing_to_update.last_modified_date = datetime.utcnow()

    # Commit and return true if listing successfully updated
    db.session.commit()
    return True


is_jett = VerifiedUser.query.filter_by(username='Jett').all()
if len(is_jett) == 0:
    user1 = VerifiedUser(username="Jett", password="password",
                         email="jett@email.com",
                         phone_number="613-613-6133",
                         billing_address="200 Jett St.",
                         postal_code="K2K 1B3", balance=0)
    db.session.add(user1)


def update_user(
        user_username,
        new_username=None,
        email=None,
        billing_address=None,
        postal_code=None):
    """This function updates the user's information in the database"""

    # Identify user
    user = VerifiedUser.query.filter_by(username=user_username).first()

    if new_username is not None:
        '''
        Alphanumeric followed that is between 4 and 10 characters
        '''
        username_regex = r'^[a-zA-Z0-9]{4,10}$'
        check = re.search(username_regex, new_username)

        if check is not None:
            user.username = new_username
            print("Username is Updated")

        else:
            print("Username is not valid")
            return False

    if email is not None:
        if not (valid_email(email)):
            print("Email address is not valid")
            return False

        else:
            user.email = email
            print("Email address is Updated")

    if billing_address is not None:
        '''
        This allows 1-5 digits for the house number, a space and a
        character followed by a period (for N. or S.), 1-2 words for the
        street name, finished with an abbreviation (like st. or rd.).
        '''
        billing_address_regex = r'\d{1,5}\w.\s(\b\w*\b\s){1,2}\w*\.'
        check = re.search(billing_address_regex, billing_address)

        if check is not None:
            user.billing_address = billing_address
            print("Billing Address is Valid")

        else:
            print("Billing Address is not Valid")
            return False

    if postal_code is not None:
        '''
        Valid Canadian Postal Code
        '''
        postal_regex = (r'[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]'
                        r'\s\d[ABCEGHJ-NPRSTV-Z]\d')
        check = re.search(postal_regex, postal_code)

        if check is not None:
            user.postal_code = postal_code
            print("Postal Code is Updated")

        else:
            print("Postal Code is not valid")
            return False
    db.session.commit()
    return True


is_komal = VerifiedUser.query.filter_by(username='Komal').all()
if len(is_komal) == 0:
    komal = VerifiedUser(username="Komal", password="password",
                         email="komal@gmail.com",
                         phone_number="613-613-6133",
                         billing_address="200 Komal St.",
                         postal_code="K2K 1B3", balance=100)
    db.session.add(komal)

is_basma = VerifiedUser.query.filter_by(username='Basma').all()
if len(is_komal) == 0:
    basma = VerifiedUser(username="Basma", password="password",
                         email="basma@gmail.com",
                         phone_number="613-613-6133",
                         billing_address="200 Basma St.",
                         postal_code="K2K 1B3", balance=100)
    db.session.add(basma)

is_listing = Listing.query.filter_by(title='New House').all()
if len(is_listing) == 0:
    listing1 = Listing(
        title="New House",
        description="Very New House. Pls Buy.",
        last_modified_date=datetime.utcnow(),
        user=user1,
        price=10)
    db.session.add(listing1)


def create_booking(start, end, user_email, listing_title):
    """
    This function creates a new booking.
    Parameters:
        start: start date of the booking
        end: end date of the booking
        user_email: email of the user that wants to book
        listing_title: title of the listing to book
    Returns:
        Boolean Value: True if booking was successfully created
                       False otherwise
    """
    # get the user object
    user = VerifiedUser.query.filter_by(email=user_email).first()

    # get the listing object
    listing = Listing.query.filter_by(title=listing_title).first()

    # check if the user has made the listing
    if (listing.user == user):
        print("Owner cannot booking their own listing.")
        return False

    if (user.balance < listing.price):
        print("Not enough balance to book the listing")
        return False

    # turn the start and end input into datetime objects
    startDate = datetime.strptime(start, "%m/%d/%Y")
    endDate = datetime.strptime(end, "%m/%d/%Y")

    # start time must be before datetime
    if (startDate > endDate):
        print("Start date must be before end date.")
        return False

    for b in listing.bookings:
        if (startDate <= b.end_date) and (b.start_date <= endDate):
            print("Booking dates cannot overlap with existing bookings.")
            return False

    new_booking = Booking(
        start_date=startDate,
        end_date=endDate,
        user=user,
        listing=listing)
    db.session.add(new_booking)
    db.session.commit()
    return True


'''
Testing:
(In python shell)
from qBandB.models import *
create_booking("03/03/2022", "03/05/2022", "komal@gmail.com",
"New House")

to test for overlap error:
create_booking("03/04/2022", "03/05/2022", "basma@gmail.com",
"New House")
'''
