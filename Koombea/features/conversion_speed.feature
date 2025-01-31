Feature: Convert Speed Units

  Scenario: Convert Kilometers per Hour to Miles per Hour
    Given the user opens the conversion app
    And navigates to "Speed" section
    When the user selects "Kilometer per hour" as the input unit
    And the user selects "Mile per hour" as the output unit
    And the user enters "500"
    Then the converted value should be "310.6856"
