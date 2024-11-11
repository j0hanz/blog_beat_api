#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is installed"
    python3 --version
else
    echo "Python is not installed"
fi

# Check if pip is installed
if command -v pip &>/dev/null; then
    echo "pip is installed"
    pip --version
else
    echo "pip is not installed"
fi

# List installed Python packages
pip list

# Check if Node.js is installed
if command -v node &>/dev/null; then
    echo "Node.js is installed"
    node --version
else
    echo "Node.js is not installed"
fi

# Check if npm is installed
if command -v npm &>/dev/null; then
    echo "npm is installed"
    npm --version
else
    echo "npm is not installed"
fi

# Check if PostgreSQL is installed
if command -v psql &>/dev/null; then
    echo "PostgreSQL is installed"
    psql --version
else
    echo "PostgreSQL is not installed"
fi

# Check if MongoDB is installed
if command -v mongosh &>/dev/null; then
    echo "MongoDB is installed"
    mongosh --version
else
    echo "MongoDB is not installed"
fi

# Check if Heroku CLI is installed
if command -v heroku &>/dev/null; then
    echo "Heroku CLI is installed"
    heroku --version
else
    echo "Heroku CLI is not installed"
fi