"""
This script demonstrates how to read text files, using Python
We import two modules: csv and pandas.
The text file name is data_text.csv:

First name,Middle Name,Last Name,Age,Gender
John,A.,Smith,28,M
Alice,Elizabeth,Johnson,32,F
Robert,,Williams,45,M
Patricia,Ann,Brown,38,F
Michael,Herbert,Jones,27,M
"""

import csv
import pandas as pd


# read the file as a simple text file
def read_as_text(file_path: str, msg: str) -> None:
    print(f"=== {msg} ===")
    with open(file_path, "r") as file:
        content = file.read()

    print(content)
    print("== done with text ===\n")


# read the file, using the csv module
# opens the file and uses csv.reader to iterate over the rows
def read_with_csv_module(file_path: str, msg: str) -> None:
    print(f"=== {msg} ===")

    with open(file_path, "r", newline="") as file:
        csv_reader = csv.reader(file)
        # each row is printed as a list of values
        for row in csv_reader:
            print(row)

    print("=== done with csv ===\n")


# reads the CSV file into a DataFrame with pd.read_csv() and then prints the whole DataFrame
def read_with_pandas(file_path: str, msg: str) -> None:
    print(f"=== {msg} ===")

    df = pd.read_csv(file_path)

    # print the DataFrame to verify its content
    print(df)

    print("=== done with pandas===\n")


# use pandas DataFrame to read the JSON file
def read_json(file_path: str, msg: str) -> None:
    print(f"=== {msg} ===")

    # read the JSON file into a DataFrame
    df = pd.read_json(file_path)

    # print the DataFrame to verify its content
    print(df)

    print("=== done with JSON ===\n")


if __name__ == "__main__":
    path_to_file = "data\\data_text.csv"

    # call each function to demonstrate the different methods
    read_as_text(path_to_file, "Data as Text")
    read_with_csv_module(path_to_file, "Data as CSV")
    read_with_pandas(path_to_file, "Reading Data as CSV, Using Pandas")

    json_path = "data\\data_text.json"
    read_json(json_path, "Reading Data as JSON, Using Pandas")

    print("\n\nthat's all   :)")
