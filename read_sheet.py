import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
from requests.exceptions import SSLError, ConnectionError

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('assignmeny-422309-a89548ec7d2f.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the sheet by URL
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1yP8Ma5zyIt_Is_8cHKBcEe82AI3RnugMIwKAw0QvcJA/edit#gid=511860887').sheet1

# Get URLs
urls = sheet.col_values(2)  # Assuming URLs are in the second column

# Function to scrape and clean data
def scrape_and_clean(url):
    try:
        response = requests.get(url, verify=False)  # Bypass SSL verification
        soup = BeautifulSoup(response.text, 'html.parser')

        # Identify and remove unwanted elements like headers, footers, and advertisements
        for element in soup.find_all(['script', 'style', 'header', 'footer', 'nav', 'aside']):
            element.decompose()

        # Remove elements that could be classified as advertisements or non-main content areas
        for element in soup.find_all(class_=lambda x: x and ("ad" in x or "banner" in x or "popup" in x)):
            element.decompose()

        # Get text and strip whitespace
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    except SSLError as e:
        print(f"SSL Error scraping {url}: {e}")
        return "SSL Error"
    except ConnectionError as e:
        print(f"Connection Error scraping {url}: {e}")
        return "Connection Error"
    except Exception as e:
        print(f"General Error scraping {url}: {e}")
        return "General Error"

# Scrape and store data
for i, url in enumerate(urls[1:], start=2):  # Skip header row
    data = scrape_and_clean(url)
    if data:
        # Write scraped data back to the sheet
        sheet.update_cell(i, 3, data)  # Store the data in the third column
