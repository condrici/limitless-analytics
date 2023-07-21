#!/bin/sh

# Installation file requires executable permissions (triggered in docker-compose)
sh /app/bin/install

# Fix docker container exiting with code 0
tail -f /dev/null