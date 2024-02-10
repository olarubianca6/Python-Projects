Feature: Search Page

  Scenario: I search for an existing item
    When I enter "htc" in the search input
    And I click the search button
    Then I get at least one result

  Scenario: I search for a non-existing item
    When I enter "iphone" in the search input
    And I click the search button
    Then Error message is displayed
    And The error message is "No products were found that matched your criteria"