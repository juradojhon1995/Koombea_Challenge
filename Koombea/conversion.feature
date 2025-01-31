Feature: Convert Units

  Scenario: Convert Length
    Given the user opens the conversion app
    When the user selects Length conversion
    And enters "100"
    Then the converted value should be displayed
