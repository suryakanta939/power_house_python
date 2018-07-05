import unittest
import pytest
import names

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestBrowser(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        print("hello this is the onetime set up class to run")

    # @pytest.fixture(autouse=True)
    # def methodSetUp(self, setUp):
    #     print("hello this is the onetime set up method to run")


    def test_methodA(self):
        print("this one is methosd A")

