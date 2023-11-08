"""
The file name should be test_xxx or xxx_test.
Function (method) name should be testXxx.
Pytest files must be execute not as a regular python, but as pyTest:
Run --> Edit configuration --> "+" --> PyTest --> your pytest file to execute.
If you put the whole folder, then all the test-files will be executed.
"""


def testLogin():
    print("Login successful")
    assert 2 + 2 == 4


def testCalculation():
    print("Login successful")
    assert 2 + 2 == 4


def testTextT():
    print('Test')
