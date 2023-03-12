import pytest
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver


#this is update fr new demo file