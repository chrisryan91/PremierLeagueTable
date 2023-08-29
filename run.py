# Import libraries
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from simple_colors import *


# Define scope of access for Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


# From Service account JSON file load credentials
# Authorize use of the credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)


# Open the Google Sheet titled 'league_table'
SHEET = GSPREAD_CLIENT.open('league_table')


# Get the two worksheets titled 'fixtures' and 'standings'
fixtures = SHEET.worksheet('fixtures')
standings = SHEET.worksheet('standings')


"""
When called, this function will ask the user to input one of four options depending on what part of the table they want to see.
It provides the option to go back to the main menu. 
It uses tabulate the display the data from the standings spreadsheet nicely on the terminal.
It validates for the correct input with an if, elif, else statement and runs a while loop until the data entered is valid.
"""
def table(standings):
    while True:
        print("'View top four, bottom three or the entire table.\n")
        option = input("Enter 'a', 'b', 'c' for each or 'back' to go back! \n")
        if option.strip().lower() == "a":
            # Get the data for the top four teams
            top_4 = [standings.row_values(i) for i in range(1, 6)]
            table_3 = tabulate(top_4, headers='firstrow', tablefmt='fancy_grid')
            print(red(table_3))
        elif option.strip().lower() == "b":
            # Get the data from the bottom teams
            bottom = [standings.row_values(i) for i in range(18, 21)]
            table_2 = tabulate(bottom, headers='firstrow', tablefmt='fancy_grid')
            print(blue(table_3))
        elif option.strip().lower() == "c":
            # Get the entire table
            table = standings.get_all_values()
            table_3 = tabulate(table, headers='firstrow', tablefmt='fancy_grid')
            print(yellow(table_3))
        elif option.strip().lower() == "back":
            return
        else:
            print("Invalid choice - please enter 'a', 'b', 'c', or 'back'.")


"""
When called, this function will validate whether the input is an interget or not. 
It runs a while loop with a try, except statement inside it which raises a value error is the valid is not an integer.
"""
def validate_integer_input(prompt, allow_quit=False):
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            value >= 0
            return value
        except ValueError:
            if allow_quit is True:
                if user_input == "quit":
                    return False
            print("Invalid input. Please enter a valid integer.")


"""
For these two functions, I used code that I had found on Stack Overflow.
The full credits are in the readme.md.
The save_progress function takes the row index in use by the all_matches function and writes it to the file.
After the data entry for each match, if the user chooses not to continue the row number will be saved.
"""
def save_progress(index):
    with open("progress.txt", "w") as f:
        f.write(str(index))


"""
This function is called upon to read the saved data in the progress.txt file.
It contains a try, except statement that attempts to find the row number to serve as the point to start off again.
It returns the content either as an integer or zero if no value is found. 
"""
def load_progress():
    try:
        with open("progress.txt", "r") as f:
            content = f.read()
            if content.strip():
                return int(content)
            else:
                return 0
    except FileNotFoundError:
        return 0


"""
This function will be called if the user chooses to view the table after each matchday has finished.
It contains a while loop and an if, else statement to check if the input is valid.
It calls the table function to display the table.
"""
def new_matchday(matchday_number):
    print(f"Starting {matchday_number}? \n")
    while True:
        view_table = input("Would you like to view the table?").lower()
        if view_table in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or'no'.")
    if view_table == 'yes':
        table(standings)


"""
When called, this function will load progress from the progress.txt file. It will determine which match to seek data for.
The function will call the new_matchday function after the start of each new matchday.
It prints the current matchday, the two teams currently playing, and asks for an input for each.
It calls the update_fixtures fuction with the data.
It then runs a while loop with another query regarding if they want to continue entering data or go back to the menu.
Data will be saved if they choose not to continue.
"""
def all_matches():
    # Load progress from the progress.txt file
    start_index = load_progress()
    for row_number, match in enumerate(fixtures.get_all_values(), start=1):
        if row_number <= start_index:
            continue
        matchday_number = int(match[1])
        if row_number % 11 == 0:
            new_matchday(matchday_number)
        print(Fore.GREEN + f"Matchday {match[1]} \n")
        print(Fore.BLUE + f"{match[3]} vs. {match[4]} - {match[3]} play at home! \n")
        print(Fore.YELLOW + "Please enter one positive interger or zero! \n")
        home_result = validate_integer_input("Enter goals for " + Fore.RED + f"{match[3]}" + Fore.RESET + " (or) " + Fore.BLUE + "'quit'" + Fore.RESET + " to quit)\n" + Fore.RESET, True)
        if home_result is False:
            save_progress(row_number)
            break
        away_result = validate_integer_input("Enter goals for " + Fore.MAGENTA + f"{match[4]}\n" + Fore.RESET)
        # Update the rest in the fixture worksheet
        update_fixtures(match, home_result, away_result)
        # Update the standings in the corresponding worksheet
        update_standings(match, home_result, away_result)


"""
In the menu, the user has the option to clear all the results from the spreadsheets and data from the progress file.
If called, the function will use a try, except statement to write empty data in the cells or the files for the results.
It first opens the progress.txt and writes empty data.
It then updates specific cells in both the spreadsheets by looping through a list of ranges.
If there is no error, it calls the menu function.
"""
def clear_results(fixtures, standings):
    try:
        with open("progress.txt", "w") as f:
            f.write("")
        # Clear values in columns 6, 7, and 8 of the fixtures worksheet
        range_to_clear = fixtures.range('F1:I' + str(fixtures.row_count))
        for cell in range_to_clear:
            cell.value = ''
        fixtures.update_cells(range_to_clear)
        # Clear values in columns 2 and 3 of the standings worksheet
        range_to_clear = standings.range('B2:C' + str(standings.row_count))
        for cell in range_to_clear:
            cell.value = 0
        standings.update_cells(range_to_clear)
        update_list = standings.range('A1:C1')
        cell_values = ["Team", "Goal Difference", "Points"]
        # Gives us a tuple of an index and value
        for i, val in enumerate(cell_values):
            # Use the index on cell_list and the val from cell_values
            update_list[i].value = val
        standings.update_cells(update_list)
    except Exception as e:
        print("An error occured:", str(e))
    menu()


"""
The menu function is what greets the user when they run the program. It prints off an introduction and asks the user for a choice.
It runs a while loop and determines the users choice with an if, elif and else statement to check the input.
Depending on the choice, it calls the associated function. 
It runs another while loop with an if, elif, else statement to confirm if the user wants to clear all data and start again.
The user also has a choice to exit the program. If selected, the choice to exit will break the while loop.
"""
def menu():
    while True:
        print("-----------------------------------------------")
        print(Fore.RED + "Welcome to the English Premier League Table!")
        print("-----------------------------------------------\n")
        print("Type" + Fore.BLUE + " 'league table' " + Fore.RESET + "see the table: - \n")
        print("Type" + Fore.YELLOW + " 'enter results' " + Fore.RESET + "to enter matchday results: - \n")
        print("Type" + Fore.GREEN + " 'clear results' " + Fore.RESET + "to begin again: - \n")
        choice = input(Fore.MAGENTA + "Enter choice: " + Fore.RESET + "\n")
        if choice.strip().lower() == str("league table"):
            table(standings)
        elif choice.strip().lower() == str("enter results"):
            all_matches()
        elif choice.strip().lower() == str("clear results"):
            while True:
                confirmation = input("Are you sure? Type 'yes' or 'no': ")
                if confirmation.strip().lower() == "yes":
                    clear_results(fixtures, standings)
                    break
                elif confirmation.strip().lower() == "no":
                    print("Cancelled!")
                    break
                else:
                    print("Invalid data! Try again.")
        elif choice.strip().lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid results - try again! \n")


"""
This function will update the fixtures spreadsheet when called.
It first prints and result that was inputted and finds the row value for each of the matches.
It first updates the two cells with points the goals scored by each team.
It then updates further two cells with a calculated goal difference of each match.
"""
def update_fixtures(match, home_result, away_result):
    print(str(home_result) + " : " + str(away_result) + "\n")
    row = int(match[0])
    fixtures.update_cell(int(row), 6, int(home_result))
    fixtures.update_cell(int(row), 7, int(away_result))
    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)
    fixtures.update_cell(int(row), 8, int(home_gd))
    fixtures.update_cell(int(row), 9, int(away_gd))


"""
This function will update the standings spread when called.
It will first find the team name from the first spreadsheet to get its row number.
It then calculates the goal difference for the Home and Away team - and the values already present in the cells from prior entries. 
It then uses an if, elif, else statement to determine what cells to update - if there is a home team win, draw, or away team win.
"""
def update_standings(match, home_result, away_result):

    cell_home = standings.find(str(match[3]))
    cell_away = standings.find(str(match[4]))
    print(match[3])
    print(match[4])
    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)
    home_before = standings.cell((cell_home.row), 3).value
    away_before = standings.cell((cell_away.row), 3).value
    home_gd_before = standings.cell((cell_home.row), 2).value
    away_gd_before = standings.cell((cell_home.row), 2).value
    if home_result > away_result:
        standings.update_cell((cell_home.row), 3, (int(home_before) +3))
        standings.update_cell((cell_home.row), 2, int(home_gd_before) + home_gd)
        standings.update_cell((cell_away.row), 2, int(away_gd_before) + away_gd)
    elif home_result == away_result:
        standings.update_cell((cell_home.row), 3, (int(home_before) + 1))
        standings.update_cell((cell_away.row), 3, (int(away_before) + 1))
    else:
        standings.update_cell((cell_away.row), 3, (int(away_before) + 3))
        standings.update_cell((cell_home.row), 2, int(home_gd_before) +  home_gd)
        standings.update_cell((cell_away.row), 2, int(away_gd_before) + away_gd)
    sort()


"""
This function is called when the sheets have been updated - it will subsequently sort the cells in the correct order.
It uses the sort function from gspread to display the rows - i.e teams - by points in descending order. 
It then uses an if statement to check if there are two or more top teams, and will then resort the top teams by goal difference
"""
def sort():
    # The standings are sorted by points
    standings.sort((3, 'des'), range='A2:C21')
    gd_sort = [item for item in standings.col_values(3) if item]
    top_cell = standings.acell('C2').value
    top = gd_sort.count(top_cell)
    # This will determine who is top based on goal difference
    if top > 1:
        new_top = (top + 1)
        range_string = 'A2:C' + str(new_top)
        print(range_string)
        # This will sort by goal difference if points are equal
        standings.sort((2, 'des'), range=range_string)


# Calling this function will start the program!
menu()
