from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given(u'I launch browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I launch browser')


@when(u'I open application')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open application')


@when(u'Enter valid usermane and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter valid usermane and password')


@when(u'click on login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click on login')


@then(u'User must login to the Homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User must login to the Homepage')


@when(u'navigate to search page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When navigate to search page')


@then(u'search page should display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then search page should display')


@when(u'navigate to user')
def step_impl(context):
    raise NotImplementedError(u'STEP: When navigate to user')


@then(u'username should display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then username should display')
