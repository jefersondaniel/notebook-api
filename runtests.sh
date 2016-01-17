#!/bin/bash

docker-compose start && docker-compose run --rm -e HOST=web -e PORT=8000 web behave $@
