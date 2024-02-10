Feature: Login Page

  Background: Open login page
    Given I am on the login page

  @regression @sanity
  Scenario: Check that URL is correct
    Then The page URL is "https://demo.nopcommerce.com/login"

  @regression @smoke
  Scenario Outline: Log in with unregistered email
    When I enter "<email>" in the email input
    And I enter "<password>" in the password input
    And I click the login button
    Then I should see "No customer account found" message
    Examples:
      | email             | password            |
      | py_ta@gmail.com   | 121232424234234     |
      | ta_py@yahoo.com   | dsfhjdsgfhjdsgfdshj |
      | sadsadsd@sdfsd.dv | w3er4werfwerwe      |