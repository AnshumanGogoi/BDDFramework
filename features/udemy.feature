Feature: Udemy Logo
  Scenario: Logo present
    Given launch chrome browser
    When open udemy homepage
    Then verify the logo is present
    And close the browser
