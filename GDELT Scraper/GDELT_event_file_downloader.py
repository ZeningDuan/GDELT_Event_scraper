"""
This scraper is for downloading GDELT event files from http://data.gdeltproject.org/events/index.html. 
Author: Zening DUAN, zeningduan1995@gmail.com
Last Edit: Nov 25, 2024
"""

import requests
import pandas as pd
import time
import re

def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response

        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print(f"File downloaded and saved as {save_path}")
    except Exception as e:
        print(f"Failed to download {save_path}: {str(e)}")


def loadtxt(file_path):
    # Initialize an empty list to store the zip file names
    zip_file_names = []

    try:
        # Open the file with the specified encoding
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                # Use regular expression to find zip file names in each line
                matches = re.findall(r'\b\S+\.zip\b', line)
                if matches:
                    # Add the found zip file names to the list
                    zip_file_names.extend(matches)

        # Create a DataFrame from the list of zip file names
        df = pd.DataFrame(zip_file_names, columns=['ZipFileNames'])

        # Print the DataFrame (optional)
        print("DataFrame:")
        print(df)

        # You can save the DataFrame to a CSV file if needed
        # df.to_csv('zip_file_names.csv', index=False)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return df




if __name__ == "__main__":
    
    file_path = "All_GDELT_Event_Files.txt"  # Replace with the path to your text file
    df = loadtxt(file_path)
    
    '''
    Start downloading
    '''

    n = 0 
    for i in df['ZipFileNames']:
        print(i)
        save_path = "files/" + i        # Replace with the desired save path and filename
        download_file('http://data.gdeltproject.org/events/' + i, save_path)
        print(n)
        n+=1
        time.sleep(5)