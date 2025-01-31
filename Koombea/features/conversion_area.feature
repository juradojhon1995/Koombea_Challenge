Feature: Convert Area Units

  Scenario: Convert Square Meters to Square Feet
    Given the user opens the conversion app
    And navigates to "Area" section
    When the user selects "Square meter" as the input unit
    And the user selects "Square foot" as the output unit
    And the user enters "100"
    Then the converted value should be "1 076.391"
