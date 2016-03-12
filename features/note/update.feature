Feature: Update note

    Scenario: Update note
        Given I set header "Content-Type" with value "application/json"
        When I send a PUT request to "/notes/469ba781e138232929c00afa" with body:
            """
            {
                "data": {
                    "type": "notes",
                    "attributes": {
                        "resume": "Hello World",
                        "contents": "Some contents"
                    }
                }
            }
            """
        Then the response code should be 200
        And the response should contain json:
            """
            {
                "data": {
                    "type": "notes",
                    "id": "469ba781e138232929c00afa",
                    "attributes": {
                        "resume": "Hello World",
                        "contents": "Some contents"
                    }
                }
            }
            """
