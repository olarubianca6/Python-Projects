Feature: Registration Page

  Background: Open register page
    Given I am on the register page

  @regression @sanity
  Scenario: Check that URL is correct
    Then The register page URL is "https://demo.nopcommerce.com/register"

  @regression @smoke
  Scenario: Register new account with valid data
    When I enter "TestFirstName" in the first name input
    And I enter "TestLastName" in the last name input
    And I enter a unique email address in the email input
    And I select "10" as my birth day
    And I select "May" as my birth month
    And I select "1995" as my birth year
    And I enter "alabalaportocala" in the new password input
    And I enter "alabalaportocala" in the password confirm input
    And I click the register button
    Then Success  message is displayed
    And The succes message is "Your registration completed"

  @regression @negative
  Scenario:  Check that trying to register without completing mandatory fields displays errors
    When I enter " " in the register email input
    And I click the register button
    Then First name error is displayed
    And Last name error is displayed
    And Email error is displayed
    And Password error is displayed
    And Password confirm error is displayed