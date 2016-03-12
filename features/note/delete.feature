Feature: Delete note

    Scenario: Delete note
        Given I set header "Content-Type" with value "application/json"
        When I send a DELETE request to "/notes/469ba781e138232929c00afa"
        Then the response code should be 204
