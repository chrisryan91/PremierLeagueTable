# Import libraries
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from simple_colors import *
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

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
This function will ask the user to input one of four options.
Each option is either part of the table or to return to the menu.
It validates for the correct input with an if, elif, else statement.
It runs a while loop until the data entered is valid.
"""


def table(standings):
    while True:
        print(blue("'View top four, bottom three or the entire table.\n"))
        option = input(red("Enter 'a', 'b', 'c' for each or 'back'\n"))
        if option.strip().lower() == "a":
            # Get the data for the top four teams
            top_4 = [standings.row_values(i) for i in range(1, 6)]
            tbl_a = tabulate(top_4, headers='firstrow', tablefmt='fancy_grid')
            print(red(tbl_a))
        elif option.strip().lower() == "b":
            # Get the data from the bottom teams
            bottom = [standings.row_values(i) for i in range(18, 21)]
            tbl_b = tabulate(bottom, headers='firstrow', tablefmt='fancy_grid')
            print(blue(tbl_b))
        elif option.strip().lower() == "c":
            # Get the entire table
            table = standings.get_all_values()
            tbl_c = tabulate(table, headers='firstrow', tablefmt='fancy_grid')
            print(yellow(tbl_c))
        elif option.strip().lower() == "back":
            return
        else:
            print("Invalid choice - please enter 'a', 'b', 'c', or 'back'.")


# When called, this function will validate whether the input is an integer.
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
For these two functions, I used code that I had found via tutorials.
This function takes the row index in use by all_matches function.
It then writes the row index into the progress.txt file.
If the user chooses not to continue when asked the row number will be saved.
"""


def save_progress(index):
    with open("progress.txt", "w") as f:
        f.write(str(index))


"""
This function is called upon to read the saved data in the progress.txt file.
It tries to find the row number to serve as the point to start off again.
It returns the content either as an integer or a string 0 if no value is found.
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
This function will be called if the user chooses to view the table whenever.
It checks if the input is valid with a While loop and If statement.
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
This function will load progress from the progress.txt file.
It will call the new_matchday function after the start of each new matchday.
It prints the current natch and asks for an input for each teams goals.
It calls the update_fixtures fuction with the data - or to quit and go back.
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
        print(Fore.RED + f"{match[3]} vs. {match[4]} - {match[3]} at home!\n")
        print(Fore.YELLOW + "Please enter one positive interger or zero! \n")
        f_rst = Fore.RESET
        chc_a = Fore.BLUE + f"Enter goals for {match[3]} (or 'quit')\n" + f_rst
        home_result = validate_integer_input(chc_a, True)
        if home_result is False:
            save_progress(row_number)
            break
        chc_b = Fore.MAGENTA + f"Enter goals for {match[4]}\n" + f_rst
        away_result = validate_integer_input(chc_b)
        # Update the rest in the fixture worksheet
        update_fixtures(match, home_result, away_result)
        # Update the standings in the corresponding worksheet
        update_standings(match, home_result, away_result)
    end_of_season(standings)


"""
The user can clear the results from the spreadsheets and saved data.
Thhe function will try to write empty data in the cells or the files.
It then updates specific cells in both the spreadsheets.
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
The menu function is what greets the user when they run the program.
It prints off an introduction and asks the user for a choice.
It finds the users choice and calls the correct function.
It confirms if the user wants to clear all data and start again.
The user also has a choice to exit the program.
"""


def menu():
    while True:
        print("-----------------------------------------------")
        print(Fore.RED + "Welcome to the English Premier League Table!")
        print("-----------------------------------------------\n")
        f_B = Fore.BLUE
        f_Y = Fore.YELLOW
        f_G = Fore.GREEN
        f_RT = Fore.RESET
        print("Type"+f_B+" 'league table' "+f_RT+"see the table: \n")
        print("Type"+f_Y+" 'enter results' "+f_RT+"to enter results: \n")
        print("Type"+f_G+" 'clear results' "+f_RT+"to begin again: \n")
        choice = input(Fore.MAGENTA + "Enter choice: "+Fore.RESET+"\n")
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
It prints back what was inputted and finds the row value for each matches.
It first updates the two cells with points the goals scored by each team.
It then updates further two cells with the goal difference of each match.
"""


def update_fixtures(match, home_result, away_result):
    print("\n" + str(home_result) + " : " + str(away_result) + "\n")
    row = int(match[0])
    fixtures.update_cell(int(row), 6, int(home_result))
    fixtures.update_cell(int(row), 7, int(away_result))
    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)
    fixtures.update_cell(int(row), 8, int(home_gd))
    fixtures.update_cell(int(row), 9, int(away_gd))


"""
This function will update the standings spread when called.
It will find the team name from the standings sheet to get its row number.
It then calculates the goal difference for the home and away team.
It then uses an if, elif, else statement to determine what cells to update.
"""


def update_standings(match, home_result, away_result):

    cell_home = standings.find(str(match[3]))
    cell_away = standings.find(str(match[4]))
    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)
    home_before = standings.cell((cell_home.row), 3).value
    away_before = standings.cell((cell_away.row), 3).value
    home_gd_before = standings.cell((cell_home.row), 2).value
    away_gd_before = standings.cell((cell_home.row), 2).value
    if home_result > away_result:
        standings.update_cell((cell_home.row), 3, (int(home_before)+3))
        standings.update_cell((cell_home.row), 2, int(home_gd_before)+home_gd)
        standings.update_cell((cell_away.row), 2, int(away_gd_before)+away_gd)
    elif home_result == away_result:
        standings.update_cell((cell_home.row), 3, (int(home_before)+1))
        standings.update_cell((cell_away.row), 3, (int(away_before)+1))
    else:
        standings.update_cell((cell_away.row), 3, (int(away_before)+3))
        standings.update_cell((cell_home.row), 2, int(home_gd_before)+home_gd)
        standings.update_cell((cell_away.row), 2, int(away_gd_before)+away_gd)
    sort()


"""
This function is called when the sheets have been updated.
It will then sort the cells in the correct order.
It uses the sort function to display the rows by points in descending order.
It then uses an if statement to check if there are two or more top teams.
It will then resort the top teams by goal difference
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


"""
This code runs when the season is over and all matches values entered.
It prints the teams in the top three positions.
The asks if the user would like to view the entire table one last time.
"""


def end_of_season(standings):
    print(blue("We have reached the end of the season! \n"))
    first = standings.acell("A2").value
    second = standings.acell("A3").value
    third = standings.acell("A4").value
    print(yellow("The champions are " + first + "!\n"))
    print(green("Runner up is " + second + "!\n"))
    print(magenta("Third place is " + third + "!\n"))
    while True:
        view_table = input(red("Would you like to view the table?")).lower()
        if view_table in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or'no'.")
        if view_table == 'yes':
            table(standings)


# Calling this function will start the program!
menu()
