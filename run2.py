import gspread 
from google.oauth2.service_account import Credentials

import numpy as np

import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('league_table')

fixtures = SHEET.worksheet('fixtures')
standings = SHEET.worksheet('standings')

def get_all_values():

    for match in fixtures.get_all_values():
        
        if int(match[1]) > 1:

            table()

        print(f"Matchday {match[1]} \n")

        print(f"{match[3]} vs. {match[4]} - {match[3]} play at home! \n")

        home_result = input(f"Enter goals scored by {match[3]} \n")

        away_result = input(f"Enter goals score by {match[4]} \n")

        print(str(home_result) + " : " + str(away_result) + "\n")

        update_results(match, home_result, away_result)

def update_results(match, home_result, away_result):

        row = int(match[0])

        fixtures.update_cell(int(row), 6, int(home_result))

        fixtures.update_cell(int(row), 7, int(away_result))

        home_gd = int(home_result) - int(away_result)

        away_gd = int(away_result) - int(home_result)

        fixtures.update_cell(int(row), 8, int(home_gd))

        fixtures.update_cell(int(row), 9, int(away_gd))

def table():
    
    as_it_stands = standings.get_all_records()

get_all_values()


