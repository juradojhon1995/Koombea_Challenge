Feature: Convert Acceleration Units

  Scenario: Convert Kilometer per Hour per Second to Mile per Minute per Second
    Given the user opens the conversion app
    And navigates to "Acceleration" section
    When the user selects "Kilometer per Hour per Second" as the input unit
    And the user selects "Mile per Minute per Second" as the output unit
    And the user enters "50"
    Then the converted value should be "0.5178"
    When the user clicks the invert units button
    Then the converted value should be "4 828.032"



