import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import re
import time

# Define the URL of the Trustpilot review page for Google
url = "https://www.trustpilot.com/review/www.google.com"

# Set up the Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Specify the name of the Google Sheet and the worksheet
sheet_name = "trustpilot"
worksheet_name = "data"

while True:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. Extract the average rating
        average_rating = soup.find('span', class_='typography_heading-m__T_L_X typography_appearance-default__AAY17').text
        # Convert average rating to a float
        average_rating = float(average_rating)

        # 2. Extract the total reviews
        total_reviews_elem = soup.find('p', {'class': 'typography_body-l__KUYFJ typography_appearance-default__AAY17', 'data-reviews-count-typography': 'true'})
        total_reviews = re.sub(r"[^\d]", "", total_reviews_elem.text)
        # Convert total reviews to an int
        total_reviews = int(total_reviews)


        # 3. Extract the breakdown of reviews for each star rating
        star_ratings = soup.find_all('label', class_='styles_row__wvn4i')

        star_data = {}
        for count in star_ratings:
            star_label = count.find('p', class_='typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_labelCell__vLP9S').text
            title = count['title']
            # print("Title:", title)  # Print the title to see its format
            # Updated regular expression pattern to match numbers with commas
            matches = re.search(r'(\d+(?:,\d+)?) of (\d+(?:,\d+)?) reviews', title)
            if matches:
                # Replace commas with empty strings before converting to int
                reviews_count = int(matches.group(1).replace(',', ''))
                # print("Matched Reviews Count:", reviews_count)  # Print the extracted number of reviews
            else:
                reviews_count = 0
            star_data[star_label] = reviews_count

        # Current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Convert timestamp to a datetime object
        timestamp_datetime = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        # Format it back to the desired string format
        formatted_timestamp = timestamp_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Print the extracted data
        print("Timestamp:", timestamp)
        print("Average Rating:", average_rating)
        print("Total Reviews:", total_reviews)
        print("Star Ratings:")
        for star, percentage in star_data.items():
            print(star, percentage)

        # Add data to Google Sheet
        sheet = client.open(sheet_name).worksheet(worksheet_name)
        data = [timestamp, average_rating, total_reviews]
        data.extend([star_data.get(label, "N/A") for label in ["5-star", "4-star", "3-star", "2-star", "1-star"]])

        # Insert the data as a new row at the beginning of the worksheet
        sheet.insert_row(data, 2)  # 2 means it's inserted as the second row (after headers)

        # Wait for the amount of seconds for the next parsing
        time.sleep(3600)

    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
