Feature: test cases related to login

@smoke
Scenario Outline: test login with valid username and password

    Given user is on login page
    When user entered valid {username} and {password}
    Then user redirected to dashboard page

    Examples:
    |username | password  |
    |jobin    | Password@1|

Scenario Outline: test login with invalid username and valid password

    Given user is on login page
    When user entered invalid {username} and valid {password}
    Then Invalid credentials error will appear

    Examples:
    |username | password|
    |Admins    | admin123|

Scenario Outline: test login with valid username and invalid password

    Given user is on login page
    When user entered valid {username} and invalid {password}
    Then Invalid credentials error will appear

    Examples:
    |username | password|
    |Admin    | admin1234|

Scenario Outline: test login with invalid username and invalid password

    Given user is on login page
    When user entered invalid {username} and invalid {password}
    Then Invalid credentials error will appear

    Examples:
    |username | password|
    |Admins   | admin1234|

