#!/bin/bash

docker-compose start db && sleep 3
docker-compose start web && sleep 3
docker-compose run --rm -e BASE_URL=web:8000 web behave $@
