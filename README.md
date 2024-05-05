# WEB-SCRAPING
Introduction
This document is intended to help you set up and run the Python script designed for scraping company homepages and processing the data using AI-powered prompts with OpenAI, and organizing the results in Google Sheets.

What You Need
Python 3.8 or higher
Google Sheets and OpenAI accounts
Access to the internet
Installation Steps
1. Install Necessary Libraries
You will need to install several libraries to get the script working. These include gspread, oauth2client, requests, beautifulsoup4, and openai. You can install these using pip, Python’s package installer.

2. Google Sheets API Configuration
To interact with Google Sheets, you will need to:

Create a project in the Google Cloud Console.
Enable the Google Sheets API for your project.
Create a service account and download the JSON key file. Store this file securely and do not share it publicly.
3. OpenAI API Configuration
For processing with OpenAI:

Sign up at OpenAI and obtain an API key.
For security, set the API key as an environment variable on your machine.
4. Prepare Your Google Sheet
Copy the target company Google Sheet template provided in the project guidelines.
Share this sheet with the service account using the email provided in your JSON key file.
Running the Script
Navigate to the script directory in your terminal.
Execute the script by running it with Python.
Documentation and Troubleshooting
Documentation: Ensure you understand each part of the script and what it does. This will help if you need to make any adjustments.
Troubleshooting: If you encounter issues, check that your API keys are correctly set up and that all libraries are installed correctly. Ensure that the Google Sheet URL is correct in your script.

