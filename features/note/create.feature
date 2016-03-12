Feature: Create note

    Scenario: Create note
        Given I set header "Content-Type" with value "application/json"
        When I send a POST request to "/notebooks/custom-slug/notes" with body:
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
                    "id": "%.+%",
                    "attributes": {
                        "resume": "Hello World",
                        "contents": "Some contents"
                    }
                }
            }
            """
