import pytest
from base_utils.invoke_browser import InvokeBrowser

@pytest.fixture()
def setUp():
    print("will run once before all test")
    yield
    print("will run once after all test")


@pytest.fixture(scope="class")
def oneTimeSetUp(request,browser):
    print("this will run once before the class")
    driver=InvokeBrowser().openBrowser(browser)
    if request.cls is not None:
        request.cls.driver=driver
    yield driver
    print("this will run after the class")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")