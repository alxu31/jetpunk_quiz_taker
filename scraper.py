# Required modules, need to pipinstall
import requests
from bs4 import BeautifulSoup

# Scrapes for answers
def scrape(url) -> list:
    answers = []
    # Send a request
    response = requests.get(url)
    # Check if successful (200)
    if response.status_code == 200:
        # Parse content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Get all ans divs
        ansDivs = soup.find_all('div', class_='thumb-right')
        print(ansDivs)
        for ans in ansDivs:
            # Appends the answer to the list of answers
            answers.append(ans) # .get_text(strip=True)
    # If response failure
    else:
        print(f"Failed to retrieve. Code: {response.status_code}")

#* Input link
url = input("URL: ")
# Call scrape function
answers = scrape(url)

#? Testing
if __name__ == '__main__':
    # Print scraped info
    if answers:
        for answer in answers:
            print(answer)
    else:
        print("Failed.")