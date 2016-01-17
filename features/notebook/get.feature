Feature: Get notebook

    Scenario: Get notebook
        When I set header "Content-Type" with value "application/json"
        And I send a GET request to "/notebooks/569ba781e138232929c00a86"
        Then print response
        Then the response code should be 200
        And the response should contain json:
            """
            {
                "data": {
                    "type": "notebooks",
                    "id": "%.+%",
                    "attributes": {
                        "slug": "%.+%"
                    },
                    "relationships": {
                        "notes": {
                            "links": {
                                "self": "%.+%"
                            }
                        }
                    }
                }
            }
            """
