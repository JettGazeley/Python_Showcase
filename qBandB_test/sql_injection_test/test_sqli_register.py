from qBandB.models import register
import os


def test_param1():
    '''
    Test first parameter - username
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert register(line, 'firstp@test.com', 'aA123456!') is False
            except Exception as e:
                assert False, f"'test_param1' raised an exception {e}"
    file.close()


def test_param2():
    '''
    Test second parameter - email
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert register('user2', line, 'aA123456!') is False
            except Exception as e:
                assert False, f"'test_param2' raised an exception {e}"
    file.close()


def test_param3():
    '''
    Test third parameter - password
    '''
    this_dir, this_filename = os.path.split(__file__)
    myfile = os.path.join(this_dir, 'test_generic_sqli.txt')
    with open(myfile) as file:
        data = file.read()
        for line in data:
            try:
                assert register('user3', 'thirdp@test.com', line) is False
            except Exception as e:
                assert False, f"'test_param3' raised an exception {e}"
    file.close()
