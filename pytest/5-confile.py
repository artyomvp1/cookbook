import pytest

"""
In order to not create a fixture in every test file we can create a confile.
The "confile.py" should contain the fixture functions. 
The confile is to be contained in a directory with the test files. 
Hence you just use a fixture function name as an argument for your test cases.
autouse argument in the fixture, will apply the fixture to every test case, so we don't need to put fixture as an argument to every test case.
scope argument is to define the scope level of the fixture (session, module, function (by default))
"""


@pytest.fixture
def theFixture():  # autouse=True scope="session"
    print(f"\n===\nPrior action 1")
    print(f"Prior action 3\n===\n")
    yield
    print(f"\n===\nAfter action 1")
    print(f"After action 2\n===\n")
