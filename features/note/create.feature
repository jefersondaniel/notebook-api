Feature: Create note

    Scenario: Create note
        When I set header "Content-Type" with value "application/json"
        And I send a POST request to "/notebooks/custom-slug/notes" with body:
            """
            {
                "data": {
                    "type": "notes",
                    "attributes": {
                        "name": "Hello World",
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
                    "id": "%.+%",
                    "attributes": {
                        "name": "Hello World",
                        "contents": "Some contents"
                    }
                }
            }
            """
