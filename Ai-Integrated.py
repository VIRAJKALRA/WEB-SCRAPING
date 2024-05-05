import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
from requests.exceptions import SSLError, ConnectionError
import openai
import os

# Obtain the OpenAI API key from an environment variable.
# Ensure you have set the OPENAI_API_KEY environment variable in your system.

openai.api_key = os.getenv('OPENAI_API_KEY')


# Check if the API key is available
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('viraj.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the sheet by URL
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1UMlK7mO_6gDx84pfddhj3vLG_0Gq9bO_Ivw46NAcz8M/edit').sheet1

# Get URLs and existing cleaned data
urls = sheet.col_values(2)  # URLs are in the second column
cleaned_data = sheet.col_values(3)  # Cleaned data is in the third column

# Function to process text with OpenAI
def process_with_openai(text, prompt_template):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a smart assistant skilled in all aspets related to programming, summarisation, sales and HR work."},
                {"role": "user", "content": prompt_template.format(text)}
            ]
        )
        return response.choices[0].message
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "API Error"


# Iterate over cleaned data to process it through OpenAI
for i, text in enumerate(cleaned_data[1:], start=2):  # Skip header row
    if text not in ["SSL Error", "Connection Error", "General Error", "API Error"]:
        # Process text through a sequence of prompts
        prompt_1_template = "Here's the raw homepage information of my target company. I need you to convert this into a 200 word summary that is organized in the following manner: - Company overview - Product and service offering recap - Potential target industries for this company - What is their core USP - How many times have they used the word 'AI' in their homepage. Here's the homepage information: \n\n{}"
        result_prompt_1 = process_with_openai(text, prompt_1_template)

        prompt_2_template = "I will give you the company overview of a target company I'm trying to pitch to. Can you read through their offering and create a potential sales opportunity for me? My company offers custom HR training and modules. Your potential sales opportunity analysis should be 150 words. It should have multiple bullet points and tell me how I can posit my solution. Ensure it is highly custom built and includes the target companies industry terminology. Here's the summary: \n\n{}"
        result_prompt_2 = process_with_openai(result_prompt_1, prompt_2_template)

        prompt_3_template = "I will give you a potential sales opportunity analysis for a company I'm targeting. You have to create a custom 100 word sales email. The email has to look at elements about what the company offers from ###Company overview### and should include potential sales hooks from ###sales opportunity analysis###. Keep the text extremely human and to the point. ###Company overview### \n{0} ###sales opportunity analysis### \n{1}"
        result_prompt_3 = process_with_openai(result_prompt_1 + " " + result_prompt_2, prompt_3_template.format(result_prompt_1, result_prompt_2))

        # Write results back to the sheet
        sheet.update_cell(i, 4, result_prompt_1)  # Column D
        sheet.update_cell(i, 5, result_prompt_2)  # Column E
        sheet.update_cell(i, 6, result_prompt_3)  # Column F
