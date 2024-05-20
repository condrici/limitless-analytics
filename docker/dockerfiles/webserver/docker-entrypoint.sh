#!/bin/sh

# Installation file requires executable permissions (triggered in docker-compose)
printf "Initializing container from entrypoint file...\n"

####################
# Set working directory
####################

# shellcheck disable=SC2164
cd /app

####################
# Create path used for the application logs
####################

mkdir -p ./logs
touch ./logs/application.log

####################
# Install dependencies
# No virtual environment is used since everything is isolated in a Docker Container
####################

python3 -m pip install -r ./requirements.txt

####################
# Start API
# The Python process will keep the Docker process running
# Otherwise we might have needed to use "tail -f /dev/null"
####################

printf "Initialization complete!\n"
printf "Starting Python application...\n"

python3 ./api.py # Start api