Feature: Delete note

    Scenario: Delete note
        When I set header "Content-Type" with value "application/json"
        And I send a DELETE request to "/notes/469ba781e138232929c00afa"
        Then the response code should be 204
