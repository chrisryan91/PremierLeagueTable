import gspread 
from google.oauth2.service_account import Credentials

import numpy as np
from tabulate import tabulate
import pandas as pd

import time

t = 3

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


def menu():

        print("Welcome to Premier League Soccer Table \n")
        print("Type 'league table' to see the table: - \n")
        print("Type 'enter results' to enter matchday results: - \n")
        print("Type 'clear table to clear the table and enter results from Matchday 1: - \n")
        choice = input(f"Enter choice: - \n")

        if choice == str("league table"):
            table()

        elif choice == str("enter results"):
            all_matches()

        elif choice == str("clear results"):
            clear_results()

        else: 
            print("Invalid results - try again! \n")
            menu()

def all_matches():

    for match in fixtures.get_all_values():

            if int(match[0]) % 10 == 1:
                
                print("Would you like to view the table after matchday one? \n")

                print("Enter 'yes' to view the tables or 'no' to continue to matchday two!")

                while True:
                    
                    option = input("Please enter yes or no: - ")

                    try:
                        option != "Yes" or option == "no":
                    
                    except: 
                        pass

                    if option == "yes" or "no":
                        
                        print("Thanks \n")

                        break
                    
                    print("Invalid Answer! Try again :)")

            print(f"{match[1]} \n")

            print(f"{match[3]} vs. {match[4]} - {match[3]} play at home! \n")

            print("Please enter one positive interger or zero for both teams in the match! \n")

            home_result = input(f"Enter goals scored by {match[3]} \n")

            away_result = input(f"Enter goals score by {match[4]} \n")

            update_fixtures(match, home_result, away_result)

            update_standings(match, home_result, away_result)
    

def update_fixtures(match, home_result, away_result):
        
        print(str(home_result) + " : " + str(away_result) + "\n")

        row = int(match[0])

        fixtures.update_cell(int(row), 6, int(home_result))

        fixtures.update_cell(int(row), 7, int(away_result))

        home_gd = int(home_result) - int(away_result)

        away_gd = int(away_result) - int(home_result)

        fixtures.update_cell(int(row), 8, int(home_gd))

        fixtures.update_cell(int(row), 9, int(away_gd))

                
def clear_results():

    pass

def update_standings(match, home_result, away_result):

    cell_home = standings.find(str(match[3]))
    cell_away = standings.find(str(match[4]))
    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)


    standings.update_cell((cell_home.row), 3, +3)

    if home_result > away_result:
        standings.update_cell((cell_home.row), 3, +3)
        standings.update_cell((cell_home.row), 2, home_gd)
        standings.update_cell((cell_away.row), 2, away_gd)

    if home_result == away_result:
        standings.update_cell((cell_home.row), 3, +1)
        standings.update_cell((cell_away.row), 3, +1)

    else: 
        standings.update_cell((cell_away.row), 3, +3)
        standings.update_cell((cell_home.row), 2, home_gd)
        standings.update_cell((cell_away.row), 2, away_gd)

    sort()

def table():
    
    print("Do you want to view the entire table, top four or bottom three? \n")
    print("Enter a, b or c for top four, bottom three or the entire table respectively! \n")
    option = input("Enter single digit a, b, c or the word 'back' \n")

    if option == "a":   

        first = standings.row_values(1)
        second = standings.row_values(2)
        third = standings.row_values(3)
        fourth = standings.row_values(3)

        top_four = [first, second, third, fourth]

        print(tabulate(top_four, headers='firstrow', tablefmt='fancy_grid'))
 

    elif option == "b":

        eighteen = standings.row_values(18)
        nineteen = standings.row_values(19)
        twenty = standings.row_values(20)

        bottom_three = [eighteen, nineteen, twenty]

        print(tabulate(bottom_three, headers='firstrow', tablefmt='fancy_grid'))

    elif option == "c":

        table = standings.get_all_values()

        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    elif option == "back":
        menu()

def sort():
    
    standings.sort((3, 'des'), range='B2:C21')

    gd_sort = [item for item in standings.col_values(3) if item]

    top_cell = standings.acell('C2').value

    top = gd_sort.count(top_cell)

    if top > 1:
         
        new_top = (top + 1)

        range_string = 'A2:C' + str(new_top)

        print(range_string)

        standings.sort((2, 'des'), range=range_string)
         
menu()


