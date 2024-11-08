#!/bin/bash

# URL for SonarQube health check
SONAR_URL="http://sonarqube:9000/api/system/ping"

# Timeout for waiting (in seconds)
TIMEOUT=300
WAIT_TIME=5

# Check if SonarQube is up
echo "Waiting for SonarQube to be ready..."

for (( i=0; i<$TIMEOUT; i+=$WAIT_TIME )); do
  if curl -s $SONAR_URL | grep -q "pong"; then
    echo "SonarQube is up and running!"
    exit 0
  fi
  echo "SonarQube not ready yet. Waiting $WAIT_TIME seconds..."
  sleep $WAIT_TIME
done

echo "SonarQube did not become ready in $TIMEOUT seconds."
exit 1
