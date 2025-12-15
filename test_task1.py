import pytest

@pytest.fixture
def setup():
    print("Browser setup")
    yield
    print("Browser teardown")

def test_login(setup):
    print("test execution")
