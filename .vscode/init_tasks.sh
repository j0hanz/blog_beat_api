#!/bin/sh

# Logging and fancy text output
python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
echo -n "🔄 Preparing workspace environment"
for i in $(seq 1 10); do
    sleep 0.75
    echo -n "."
done
echo

# Function to check installation with limited output
check_installation() {
    if command -v "$1" >/dev/null 2>&1; then
        version=$("$1" --version | head -n 1)
        echo "✅ $2 is installed ($version)"
    else
        echo "❌ $2 is not installed"
    fi
}

# Function to install VS Code extensions with limited output
install_vscode_extensions() {
    python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
    echo -n "🔄 Installing extensions"
    for i in $(seq 1 5); do
        sleep 0.5
        echo -n "."
    done
    echo
    EXT_DIR="${GITPOD_REPO_ROOT}/.vscode/extensions"
    if [ -d "$EXT_DIR" ]; then
        for file in "$EXT_DIR"/*.vsix; do
            if [ -f "$file" ]; then
                extension_name=$(basename "$file")
                echo "Installing extension: $extension_name"
                if code --install-extension "$file"; then
                    echo "✅ Successfully installed: $extension_name"
                else
                    echo "❌ Failed to install: $extension_name"
                fi
            fi
        done
    else
        echo "⚠️ No .vsix files found in $EXT_DIR. Skipping installation."
    fi
}

# Function to install Python dependencies with limited output
install_requirements() {
    python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
    echo -n "🔄 Installing dependencies"
    for i in $(seq 1 5); do
        sleep 0.5
        echo -n "."
    done
    echo
    if [ -f "requirements.txt" ]; then
        if pip install -r requirements.txt; then
            echo "✅ Dependencies installed successfully."
        else
            echo "❌ Failed to install dependencies."
            return 1
        fi
    else
        echo "⚠️ requirements.txt not found. Skipping installation."
    fi
}

# Main setup process
sleep 1

# Install VS Code extensions
install_vscode_extensions

sleep 1

# Install Python dependencies
install_requirements

sleep 1

pip list

sleep 1

python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
pip-review

# Check for installations with minimal output
tools="python pip node npm psql mongosh heroku docker aws git"
names="Python pip Node.js npm PostgreSQL MongoDB Heroku CLI Docker AWS CLI Git"
python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
echo -n "🔍 Checking software installations"
for i in $(seq 1 5); do
    sleep 0.5
    echo -n "."
done
echo
for tool in $tools; do
    check_installation "$tool" "$tool" || echo "⚠️ $tool not installed or not found."
done

# Final message with minimal output
if [ $? -eq 0 ]; then
    python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
    echo "✅ Setup complete! You are ready to start coding."
    echo ""
    # Run display_repo_info.py
    python .vscode/display_repo_info.py
else
    python -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.long_line)"
    echo "❌ Setup failed! Please check the logs and retry."
fi
