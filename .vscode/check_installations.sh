#!/bin/bash

# Function to check installation
check_installation() {
    $1 --version &> /dev/null
    if [ $? -eq 0 ]; then
        $1 --version
    else
        echo "$2 is not installed"
    fi
}

# Checking software installations
check_installation "python" "Python"
check_installation "pip" "pip"
check_installation "node" "Node.js"
check_installation "npm" "npm"
check_installation "psql" "PostgreSQL"
check_installation "mongosh" "MongoDB"
check_installation "heroku" "Heroku CLI"