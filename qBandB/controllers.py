from flask import render_template, request, session, redirect
from qBandB.models import *


from qBandB import app


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            try:
                user = VerifiedUser.query.filter_by(email=email).one_or_none()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                pass
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = login(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information
        between a user's browser and the end server.
        Typically it is packed and stored in the browser cookies.
        They will be past along between every request the browser made
        to this services. Here we store the user object into the
        session, so we can tell if the client has already login
        in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='login failed')


@app.route('/')
@authenticate
def home(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals

    # get list of products
    products = Listing.query.all()
    # get list of bookings
    user = VerifiedUser.query.filter_by(email=session['logged_in']).first()
    bookings = Booking.query.filter_by(user=user).all()

    return render_template(
        'index.html',
        user=user,
        products=products,
        bookings=bookings)


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = register(name, email, password)
        if not success:
            error_message = "Registration failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/createlisting', methods=['GET'])
def createlisting_get():
    # templates are stored in the templates folder
    return render_template('create_listing.html', message='')


@app.route('/createlisting', methods=['POST'])
def createlisting_post():
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    # use email from the session
    email = session['logged_in']
    error_message = None

    # use backend api to create a listing
    success = create_listing(title, description, price, email)
    if not success:
        error_message = "Unable to create listing."
    # if there is any error messages when creating a new listing
    # at the backend, reset the page and display the error message.
    if error_message:
        return render_template('create_listing.html', message=error_message)
    else:
        return redirect('/')


@app.route('/updateprofile', methods=['GET'])
def update_profile_get():
    return render_template('update_profile.html', message='')


@app.route('/updateprofile', methods=['POST'])
def update_profile_post():
    user_username = request.form.get('user_username')

    email = request.form.get('email')
    if email != '':
        success = update_user(user_username, email=email)

    billing_address = request.form.get('billing_address')
    if billing_address != '':
        success = update_user(user_username, billing_address=billing_address)

    postal_code = request.form.get('postal_code')
    if postal_code != '':
        success = update_user(user_username, postal_code=postal_code)

    new_username = request.form.get('new_username')
    if new_username != '':
        success = update_user(user_username, new_username=new_username)
    error_message = None

    if not success:
        error_message = "Profile Update Failed"
    if error_message:
        return render_template('update_profile.html', message=error_message)
    else:
        # once redirct page has been decided, update info below
        return render_template(
            'update_profile.html',
            message='Successfully updated user profile')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


@app.route("/updatelisting", methods=['GET'])
def updatelisting_get():
    # templates are stored inthe templates folder
    return render_template('update_listing.html', message='')


@ app.route("/updatelisting", methods=['POST'])
def updatelisting_post():
    email = session['logged_in']
    title = request.form.get("title")
    # check if listing exists
    success = update_listing(email, title)

    new_title = request.form.get('new_title')
    if new_title != '':
        # use backend api to update the listing
        success = update_listing(
            owner_email=email,
            title=title,
            new_title=new_title)
        # set the local title variable to the new title if the user inputs a
        # new title
        title = new_title
    else:
        # set the new_title to the previous one if the user doesn't update the
        # title
        new_title = title

    description = request.form.get("description")
    if description != '':
        success = update_listing(
            owner_email=email,
            title=title,
            description=description)

    price = request.form.get("price")
    if price != '':
        price = float(price)
        success = update_listing(owner_email=email, title=title, price=price)

    error_message = None

    if not success:
        error_message = ("Listing \'" + title + "\' could not be updated.")

    # if the listing was not successfully updated
    # at the backend, display the error message on the update listing page
    if error_message:
        return render_template("update_listing.html", message=error_message)
    else:
        return render_template("update_listing.html",
                               message=("Listing \'" + new_title +
                                        "\' successfully updated."))


@app.route('/createbooking', methods=['GET'])
def createbooking_get():
    # templates are stored in the templates folder
    return render_template('create_booking.html', message='')


@app.route('/createbooking', methods=['POST'])
def createbooking_post():
    start = request.form.get('start')
    end = request.form.get('end')
    # use email from the session
    email = session['logged_in']
    listing = request.form.get('listing')
    error_message = None

    # use backend api to create a booking
    success = create_booking(start, end, email, listing)
    if not success:
        error_message = "Unable to create booking."
    # if there is any error messages when creating a new booking
    # at the backend, reset the page and display the error message.
    if error_message:
        return render_template('create_booking.html', message=error_message)
    else:
        return redirect('/')
