import pytest

"""
Fixture is a function we execute everytime before/after our function.
Steps to run before EVERY test - SETUP.
Steps to run after EVERY test -TEAR DOWN.
To implement a fixture we use a wrapper @pytest.fixture.
Test the below by running in termina pytest file_name -vs.
"""


@pytest.fixture
def setUp():
    print(f"\n===\nPrior action 1")
    print(f"Prior action 3\n===\n")
    yield
    print(f"\n===\nAfter action 1")
    print(f"After action 2\n===\n")


def testAddItem(setUp):  # the steps from setUp will be executed
    print("Added")


def testRemoveItem():
    print("Removed")
