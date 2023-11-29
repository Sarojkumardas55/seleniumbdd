Feature: Sample Feature

  Scenario: Open Google and search
    Given I am on the Google search page
    When I enter "Behave with Selenium" into the search bar
    And I click the search button
    Then I should see search results
