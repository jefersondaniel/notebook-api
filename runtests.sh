#!/bin/bash

docker-compose start && docker-compose run --rm -e BASE_URL=web:8000 web behave $@
