Feature: Create notebook

    Scenario: Send a empty body and receive a new notebook
        Given I set header "Content-Type" with value "application/json"
        When I send a POST request to "/notebooks" with body:
            """
            {
                "data": {
                    "type": "notebooks",
                    "attributes": {}
                }
            }
            """
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

    Scenario: Send a unique slug and receive a new notebook
        Given I set header "Content-Type" with value "application/json"
        When I send a POST request to "/notebooks" with body:
            """
            {
                "data": {
                    "type": "notebooks",
                    "attributes": {
                        "slug": "new-slug"
                    }
                }
            }
            """
        Then the response code should be 200
        And the response should contain json:
            """
            {
                "data": {
                    "type": "notebooks",
                    "id": "%.+%",
                    "attributes": {
                        "slug": "new-slug"
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


    Scenario: Send a existing slug and receive a error
        Given I set header "Content-Type" with value "application/json"
        When I send a POST request to "/notebooks" with body:
            """
            {
                "data": {
                    "type": "notebooks",
                    "attributes": {
                        "slug": "custom-slug"
                    }
                }
            }
            """
        Then the response code should be 400
        And the response should contain json:
            """
            {
                "errors": [
                    {
                        "status": 400,
                        "detail": "%.+%"
                    }
                ]
            }
            """
