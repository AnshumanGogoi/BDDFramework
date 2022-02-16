Feature: Udemy login
  Scenario: Login to udemy using valid parameters
    Given Launch chrome browser
    When Open udemy Loginpage
    And Enter username "gogoi.anshuman21@gmail.com" and password "sunny08642"
    And Click on login button
    Then User must successfully login

  Scenario Outline: Login to Udemy with multiple parameters
    Given Launch chrome browser
    When Open udemy Loginpage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login

    Examples:
      | username  | password  |
      | username1 | password1 |
      | username2 | password2 |
      | username3 | password3 |
