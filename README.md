# WEB-SCRAPING
Introduction
This README file accompanies the Python script designed to scrape data from company homepages, process it through AI-powered prompts with OpenAI, and store both raw and processed data in Google Sheets. This document provides all necessary setup and usage instructions.

Prerequisites
Before you begin, ensure you have the following:

Python 3.8 or higher installed on your system.
Pip for installing Python packages.
Installation Steps
1. Install Python Libraries
Open a terminal or command prompt and run the following command to install the required libraries:

bash
Copy code
pip install gspread oauth2client requests beautifulsoup4 openai
2. Google Sheets API Configuration
Create a Google Cloud Project:
Visit the Google Cloud Console.
Create a new project or select an existing one.
Enable Google Sheets API:
Navigate to the "APIs & Services > Library" section.
Search for "Google Sheets API" and enable it for your project.
Create Service Account and Download Credentials:
Go to "IAM & Admin > Service Accounts" and create a new service account.
Assign the project role of "Editor" or a custom role with permissions to access Google Sheets.
Create a key for this account (choose JSON format) and download it.
Note: Keep this JSON file secure and do not share it publicly.
3. OpenAI API Configuration
Register for OpenAI:
Sign up at OpenAI and follow the instructions to obtain an API key.
Set the API Key:
It's recommended to set the API key as an environment variable for security reasons:
bash
Copy code
export OPENAI_API_KEY='your_openai_api_key_here'
4. Google Sheet Setup
Prepare the Sheet:
Make a copy of the provided target company Google Sheet template.
Share the sheet with the email address of your service account (found in your service account JSON key file).
Document the URL:
Ensure that the script is updated with the URL of your new copied Google Sheet.
Running the Script
Navigate to the directory containing your script.
Run the script using Python:
bash
Copy code
python your_script_name.py
Documentation and Troubleshooting
Documentation: Ensure all code segments are well-commented, explaining their purpose and functionality.
Troubleshooting: If errors occur, check API key configurations, ensure all dependencies are installed correctly, and the Google Sheet URL is correctly configured in your script.
