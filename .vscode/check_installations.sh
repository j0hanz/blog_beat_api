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
python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
echo -n "🔍 Checking software installations"
for i in $(seq 1 3); do
    sleep 0.5
    echo -n "."
done
echo
check_installation "python" "Python"
check_installation "pip" "pip"
check_installation "node" "Node.js"
check_installation "npm" "npm"
check_installation "psql" "PostgreSQL"
check_installation "mongosh" "MongoDB"
check_installation "heroku" "Heroku CLI"