import sys

import requests
from bs4 import BeautifulSoup
import pyttsx3


# Function to fetch webpage content
def get_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None


# Unified interface
print("Web Scraping and Text to Speech")
print("-------------------------------")


while True:
    # Get user input for the webpage URL
    print("\n[Enter 'exit' to exit program]")
    webpage_url = input("Enter the URL of the webpage to scrape: ")
    if webpage_url == 'exit':
        break
    webpage_content = get_webpage_content(webpage_url)

    while True:
        if webpage_content:
            soup = BeautifulSoup(webpage_content, 'html.parser')

            # Accept the HTML Tag to be scraped
            print("\n[Enter 'back' to go back or 'exit' to exit program]")
            html_tag = input(
                "Enter the HTML Tag to be scraped: ")

            if html_tag == 'back':
                break
            elif html_tag == 'exit':
                exit()
            else:
                content = soup.find_all(html_tag)

            if content:
                # Extract and print content
                print("\nWeb Content:")
                for idx, line in enumerate(content, start=1):
                    print(f"{idx}. {line.text}")

                while True:
                    # Get user input for the line index to convert to speech
                    print("\n[Enter 'back' to go back or 'exit' to exit program]")
                    line_index = input(
                        "Enter the index of the headline to convert to speech: ")

                    if line_index == 'back':
                        break
                    elif line_index == 'exit':
                        exit()
                    else:
                        try:
                            line_index = int(line_index)
                            if 1 <= line_index <= len(content):
                                selected_line = content[line_index - 1].text

                                # Convert line to speech
                                reader = pyttsx3.init()
                                reader.say(selected_line)
                                reader.runAndWait()

                                print("\nSelected line converted to speech.")
                            else:
                                print("\nInvalid line index.")
                        except ValueError:
                            print("\nInvalid input. Please enter a valid number.")
            else:
                print("\nHTML Tag doesn't exist or failed to retrieve its content!")
        else:
            print("\nURL doesn't exist or failed to retrieve webpage content!")
