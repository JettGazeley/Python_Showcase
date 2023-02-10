from qBandB.models import create_listing
import os


def test_param1():
    '''
    Test first parameter - title
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert create_listing(line,
                                      '200 Rabab Street property by the water',
                                      200, 'Rabab@email.com') is False
            except Exception as e:
                assert False, f"'test_param1' raised an exception {e}"
    file.close()


def test_param2():
    '''
    Test second parameter - description
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert create_listing('Beautiful apartment',
                                      line,
                                      200, 'Rabab@email.com') is False
            except Exception as e:
                assert False, f"'test_param2' raised an exception {e}"
    file.close()


def test_param3():
    '''
    Test third parameter - price
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert create_listing('Beautiful apartment',
                                      '200 Rabab Street property by the water',
                                      line, 'Rabab@email.com') is False
            except Exception as e:
                assert False, f"'test_param3' raised an exception {e}"
    file.close()


def test_param4():
    '''
    Test third parameter - email
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert create_listing('Beautiful apartment',
                                      '200 Rabab Street property by the water',
                                      200, line) is False
            except Exception as e:
                assert False, f"'test_param4' raised an exception {e}"
    file.close()


def test_param5():
    '''
    Test third parameter - date created
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert create_listing('Beautiful apartment',
                                      '200 Rabab Street property by the water',
                                      200, 'Rabab@email.com', line) is False
            except Exception as e:
                assert False, f"'test_param5' raised an exception {e}"
    file.close()
