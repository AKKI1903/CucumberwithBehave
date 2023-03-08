# Created by ankushsharma at 07.03.23
Feature: Registration form
  verify the Content and valid fields have data present or not

  Scenario: Open the page and validate
    Given I am on the Registration page
    When I enter all the valid details
    Then I click on Submit


