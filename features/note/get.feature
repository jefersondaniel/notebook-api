Feature: Update note

    Scenario: Update note
        Given I set header "Content-Type" with value "application/json"
        When I send a GET request to "/notes/469ba781e138232929c00afa"
        Then the response code should be 200
        And the response should contain json:
            """
            {
                "data": {
                    "type": "notes",
                    "id": "469ba781e138232929c00afa",
                    "attributes": {
                        "resume": "Hello World",
                        "contents": "Hello World"
                    }
                }
            }
            """
