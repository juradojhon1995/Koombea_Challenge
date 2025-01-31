Feature: API Test for Rick and Morty

  Scenario: Verify response for a character
    Given url 'https://rickandmortyapi.com/api/character/1'
    When method GET
    Then status 200
    * print '✅ Response for Rick:', karate.pretty(response)
    And match response.name == 'Rick Sanchez'

  Scenario: Verify response for another character
    Given url 'https://rickandmortyapi.com/api/character/2'
    When method GET
    Then status 200
    * print '✅ Response for Morty:', karate.pretty(response)
    And match response.name == 'Morty Smith'
    And match response.status == 'Alive'
    And match response.species == 'Human'

  Scenario: Verify response for a non-existing character
    Given url 'https://rickandmortyapi.com/api/character/9999'
    When method GET
    Then status 404
    * print '❌ Response for non-existing character:', karate.pretty(response)

  Scenario: Verify total number of characters in the API
  Given url 'https://rickandmortyapi.com/api/character'
  When method GET
  Then status 200
  * def totalCharacters = response.info.count
  * print '✅ Total characters in API:', totalCharacters
  And assert totalCharacters > 800

  Scenario: Verify response headers for a character
    Given url 'https://rickandmortyapi.com/api/character/4'
    When method GET
    Then status 200
    * print '✅ Checking response headers...'
    And match responseHeaders['Content-Type'][0] == 'application/json; charset=utf-8'
    And match responseHeaders['Server'][0] == 'Netlify'
    And match responseHeaders['Access-Control-Allow-Origin'][0] == '*'

  Scenario: Count human characters in the first page
  Given url 'https://rickandmortyapi.com/api/character?page=1'
  When method GET
  Then status 200
  * def characters = response.results
  * def humans = characters.filter(x => x.species == 'Human')
  * def humanCount = karate.sizeOf(humans)
  * print '✅ Humans:', humanCount





