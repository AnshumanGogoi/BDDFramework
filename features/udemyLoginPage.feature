Feature: Udemy login page
    Background: common steps
      Given I launch browser
      When I open application
      And Enter valid usermane and password
      And click on login

    Scenario: Login to udemy
      Then User must login to the Homepage

    Scenario: Search course
      When navigate to search page
      Then search page should display

    Scenario: Search user
      When navigate to user
      Then username should display
