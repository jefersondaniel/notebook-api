Feature: List notes

    Scenario: List notes from a notebook
        When I set header "Content-Type" with value "application/json"
        And I send a GET request to "/notebooks/custom-slug/notes"
        Then print response
        Then the response code should be 200
        And the response should contain json:
            """
            {
                "data": [
                    {
                        "type": "notes",
                        "id": "469ba781e138232929c00afa",
                        "attributes": {
                            "name": "Index",
                            "contents": "Hello World"
                        }
                    }
                ]
            }
            """
