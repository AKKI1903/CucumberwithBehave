# Created by ankushsharma at 07.03.23
Feature: Basic form Controls
  Check all type of form interaction on one window

  Scenario: Basic Control Interactions
    Given I am on the Basic Form page
    When I interact with all the basic forms
    And Non English label and locator
    Then I click Submit on Form with Validation Form
