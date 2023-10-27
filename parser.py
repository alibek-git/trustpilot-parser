import requests
from bs4 import BeautifulSoup

# Define the URL of the Trustpilot review page for Google
url = "https://www.trustpilot.com/review/www.google.com"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. Extract the average rating
    average_rating = soup.find('span', class_='typography_heading-m__T_L_X typography_appearance-default__AAY17').text

    # 2. Extract the total reviews
    total_reviews_elem = soup.find('p', {'class': 'typography_body-l__KUYFJ typography_appearance-default__AAY17', 'data-reviews-count-typography': 'true'})
    total_reviews = total_reviews_elem.text.split()[0]  # Extract the numeric part

    # 3. Extract the breakdown of reviews for each star rating
    star_ratings = soup.find_all('label', class_='styles_row__wvn4i')

    star_data = {}
    for rating in star_ratings:
        star_label = rating.find('p', class_='typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_labelCell__vLP9S').text
        star_percentage = rating.find('p', class_='typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_cell__qnPHy styles_percentageCell__cHAnb').text
        star_data[star_label] = star_percentage

    # Print the extracted data
    print("Average Rating:", average_rating)
    print("Total Reviews:", total_reviews)
    print("Star Ratings:")
    for star, percentage in star_data.items():
        print(star, percentage)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
