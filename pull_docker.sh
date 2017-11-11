#!/usr/bin/env bash

# exit script if any command fails (non-zero value)
set -e
# Pull all the images we need to run the containers
docker pull subigya/codium_learn:latest