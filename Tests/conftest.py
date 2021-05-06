from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from config.config import TestData

@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request) :
    if request.param == "chrome" :

        #These 2 lines of code is for the Read Discriptor Error that coming while running the TCs :
        #The Error is
        #Failed to read descriptor from node connection: A device attached to the system is not functioning
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #These 2 lines of code ends here
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    if request.param =="FF" :
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get(TestData.Base_URL)
    request.cls.driver = driver


    yield
    driver.close()
