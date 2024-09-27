#!/bin/bash

echo "### SecuLock Automated Setup ###"

# Set the project repository and image paths
REPO_URL="https://github.com/yourusername/seculock.git"
PROJECT_DIR="seculock"
LOGO_PATH="assets/seculock_logo.png"

# Introduction
echo "SecuLock is a cybersecurity project designed to deploy honeypot credentials across multiple platforms and monitor them for breach attempts."

# Step 1: Clone the Repository
echo "Cloning SecuLock repository from $REPO_URL..."
git clone $REPO_URL
cd $PROJECT_DIR

# Step 2: Set up Python virtual environment
echo "Setting up virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Step 3: Install required dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Create the .env file and add API keys and credentials
echo "Creating the .env file..."
touch .env

# Prompt the user to enter their API keys and credentials
echo "Please enter your API keys and credentials for the SecuLock project."
read -p "Enter your SendGrid API Key: " SENDGRID_API_KEY
read -p "Enter your Dropbox Access Token: " DROPBOX_ACCESS_TOKEN
read -p "Enter your Pushbullet Access Token: " PUSHBULLET_ACCESS_TOKEN
read -p "Enter your Google Client ID: " GOOGLE_CLIENT_ID
read -p "Enter your Google Client Secret: " GOOGLE_CLIENT_SECRET
read -p "Enter the Verified From Email (SendGrid): " FROM_EMAIL
read -p "Enter the Recipient Email for breach notifications: " TO_EMAIL

# Add the credentials to the .env file
echo "Writing credentials to .env file..."
cat <<EOT >> .env
# .env file

SENDGRID_API_KEY=$SENDGRID_API_KEY
DROPBOX_ACCESS_TOKEN=$DROPBOX_ACCESS_TOKEN
PUSHBULLET_ACCESS_TOKEN=$PUSHBULLET_ACCESS_TOKEN
GOOGLE_CLIENT_ID=$GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET
FROM_EMAIL=$FROM_EMAIL
TO_EMAIL=$TO_EMAIL
EOT

echo ".env file created successfully!"

# Instructions for Google API setup
echo "### Google APIs Setup ###"
echo "To use Google APIs (Drive, Gmail), ensure you have created OAuth 2.0 credentials in your Google Cloud Console and placed the client_secrets.json file in the root directory of the project."

# Optionally build Docker container
read -p "Do you want to build and run SecuLock in Docker? (y/n): " BUILD_DOCKER
if [ "$BUILD_DOCKER" = "y" ]; then
    echo "Building and running Docker container..."
    docker-compose up --build
fi

# Display instructions for running the project
echo "### SecuLock Setup Complete ###"
echo "To run SecuLock, activate the virtual environment and execute the main Python script:"
echo "source .venv/bin/activate"
echo "python main.py"

# End of script
echo "Thank you for using SecuLock! Logs can be found in logs/breach_logs.log."
