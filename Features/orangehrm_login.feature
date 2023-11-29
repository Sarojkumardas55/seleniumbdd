Feature: Login feature

  Scenario: Open orange hrm and login
    Given I am on the orange hrm login page
    When I enter "Admin" into the username
    When I enter "admin123" into the password
    When I click the login button