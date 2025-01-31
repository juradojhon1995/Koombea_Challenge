Feature: Convert Volume Units

  Scenario: Convert Milliliters to Liters
    Given the user opens the conversion app
    And navigates to "Volume" section
    When the user selects "Milliliter" as the input unit
    And the user selects "Liter" as the output unit
    And the user enters "1000"
    Then the converted value should be "1"
