# Libraries you may need:
import csv, collections, dictionary, pandas as pd, openpyxl
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = []

    @staticmethod
    def process_file(filename):

        data = []

        if filename.endswith(".csv"):
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(dict(row))
                print(data)
            return data

        elif filename.endswith(".txt"):
            with open(filename, 'r') as file:
                text = file.read()
                print(text)
        elif filename.endswith(".xlsx"):
            data = pd.read_excel(filename)
            print(data)
            return data

        else:
            print("Error: File not found.")
            return None

    def transfer_data(source_data, destination_file):

        if source_data is None:
            print("Error: Unable to fetch web data.")
            return

        if destination_file.endswith(".csv"):
            with open(destination_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=source_data[0].keys())
                writer.writeheader()
                for row in source_data:
                    writer.writerow(row)
        elif destination_file.endswith(".txt"):
            with open(destination_file, 'w') as file:
                for row in source_data:
                    file.write(str(row))
        elif destination_file.endswith(".xlsx"):
            df = pd.DataFrame(source_data)
            df.to_excel(destination_file, index=False)
        else:
            print("Error: File not found.")
            return None

    def fetch_web_data(url):
        try:
            with urlopen(url) as response:
                source_data = response.read().decode('utf-8')
            return source_data
        except HTTPError as e:
            print(f"HTTP Error: {e}")
        except URLError as e:
            print(f"URL Error: {e}")
        except Exception as e:
            print(f"Error fetching web data: {e}")

    #
    # def analyze_content():
    #
    # def generate_summary():

# Analyze content & display result area
