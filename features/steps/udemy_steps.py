#You can implement step definitions for undefined steps with these snippets:
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('launch chrome browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open udemy homepage')
def openUdemyHomepage(context):
    context.driver.get("https://www.udemy.com")

@then('verify the logo is present')
def verifyLogoPresent(context):
    print(context.driver.title)


@then('close the browser')
def closeBrowser(context):
    context.driver.close()