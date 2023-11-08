import pytest

"""
We can execute only specific functions (method) from a file by marking them.
To mark we need to user a wrapper @pytest.mark.marker_name.
Execute only marked function in terminal -v marker_name.
System markers: 
'skip/skipif' - skipping test case (reported as skip) 
'xfail' - expected fail (reported as xfail)
"""


def testOne():
    print("Login successful")
    assert 2 + 2 == 4


@pytest.mark.sanity
def testTwo():
    print("Login successful")
    assert 2 + 2 == 4
