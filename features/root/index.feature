Feature: Show Index

    Scenario: Show available links
        When I send a GET request to "/"
        Then the response code should be 200
        And the response should contain json:
            """
            {
                "links": {
                    "self": "/",
                    "notebooks": "/notebooks",
                    "notes": "/notes"
                }
            }
            """
