from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
import sys



@pytest.fixture(scope="module")
def setpath():
    global driver
    path = "D:\\SeleniumPracticewithPython\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("http://yppodappdt:8080/preonboarding/#/login")
    yield
    driver.close()


def test_regi(setpath):
    driver.maximize_window()


def test_login(setpath):
    driver.find_element_by_xpath("//input[@name='uname']").send_keys("nafisa.ujloomwale")
    driver.find_element_by_xpath("//input[@name='passwd']").send_keys("Momin$12345")
    driver.find_element_by_xpath("//button[text()='Login']").click()
    url_title = driver.title
    assert url_title == "PreOnBoarding"

# def test_click_requisition(setpath):
# driver.find_element_by_xpath("//*[@id='main']/div/div/section/div/div/div[4]/div/h4/a/i").click()
