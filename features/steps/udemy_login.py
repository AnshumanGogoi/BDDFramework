#You can implement step definitions for undefined steps with these snippets:
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""

Pass arguments from feature file

"""


@when('Open udemy Loginpage')
def step_impl(context):
    context.driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.ID, 'email--1').send_keys(user)
    context.driver.find_element(By.ID, 'id_password').send_keys(pwd)

@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element(By.ID, 'submit-id-submit').click()

@then(u'User must successfully login')
def step_impl(context):
    title = context.driver.title
    print(title)
    context.driver.close()