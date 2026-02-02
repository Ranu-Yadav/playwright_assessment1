
Feature: test cases related to Personal details

#Background:

@smoke
Scenario: user can view his profile
    Given user is already logged in
    When user navigate to my profile
    Then user should be able to view his profile

@smoke
Scenario Outline: user can edit personal details
    Given user is already logged in
    When user update personal details
    Then successfully updated pop up should come

    Examples:
    |First Name| Middle Name| Last Name |
    |new       |test        | user      |

