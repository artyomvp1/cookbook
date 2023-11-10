import pytest
"""
Option 1
"params" argument in a fixture will provide the emphasized parameters to the test case using the fixture.
The test case will be executed as many times as many numbers of parameters we put.

Option 2
mark.parametrize wrapper accepts in a tuple arguments and result. Use assert to validate (uncomment option 2 to see).

Execute the following from terming using pytest file_name -vs
"""


#Option 1
@pytest.fixture(params=['a', 'b'])
def demo_fixture(request):
    print(request.param)


def testLogin(demo_fixture):
    print("Test")


# Option 2
# @pytest.mark.parametrize("a, b, result", [(2, 6, 8), (2, 2, 5), (10, 5, 15)])  # true, fail, true
# def testLogoff(a, b, result):
#     assert a + b == result
