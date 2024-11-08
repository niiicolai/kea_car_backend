#!/bin/bash

curl -u admin:admin -X POST "http://localhost:9000/api/user_tokens/generate" -d "name=test-token"
