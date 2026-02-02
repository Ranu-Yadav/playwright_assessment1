
Feature: test cases related to add or upload photograph

Background:
    Given user is already logged in and My Info page

@smoke
Scenario: user can upload photograph
    When user upload image
    Then image should be successfully updated