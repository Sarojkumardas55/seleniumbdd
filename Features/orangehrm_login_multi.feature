Feature: Login feature

  Scenario Outline: Open orange hrm and login
    Given I am on the orange hrm login page
    When I enter "<username>" into the username
    When I enter "<password>" into the password
    When I click the login button
    Examples:
      | username | password |
      | Admin    | admin123 |
      | Admin    | Admin123 |
      | admin    | admin123 |