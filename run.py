# Import libraries
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate


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


# Function that displays different parts of the table based on user input
def table(standings):
    while True:
        print("'View top four, bottom three or the entire table.\n")
        option = input("Enter 'a', 'b', 'c' for each or 'back' to go back! \n")
        if option.strip().lower() == "a":
            # Get the data for the top four teams
            top_4 = [standings.row_values(i) for i in range(1, 6)]
            print(tabulate(top_4, headers='firstrow', tablefmt='fancy_grid'))
        elif option.strip().lower() == "b":
            # Get the data from the bottom teams
            bottom = [standings.row_values(i) for i in range(18, 21)]
            print(tabulate(bottom, headers='firstrow', tablefmt='fancy_grid'))
        elif option.strip().lower() == "c":
            # Get the entire table
            table = standings.get_all_values()
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        elif option.strip().lower() == "back":
            return
        else:
            print("Invalid choice - please enter 'a', 'b', 'c', or 'back'.")


# Function that will validate interger input from the user
def validate_interger_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Function that saves progress to a file
def save_progress(index):
    with open("progress.txt", "w") as f:
        f.write(str(index))


# Function to load the previously saved progress
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


# Function that handles the results from each matchday
def all_matches():
    # Load progress from the progress.txt file
    start_index = load_progress()
    for row_number, match in enumerate(fixtures.get_all_values(), start=1):
        if row_number <= start_index:
            continue
        matchday_number = int(match[1])
        if row_number % 11 == 0:
            print(f"Starting {matchday_number}? \n")
            while True:
                view_table = input("Would you like to view the table?").lower()
                if view_table in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or'no'.")
            if view_table == 'yes':
                table(standings)
        print(f"{match[1]} \n")
        print(f"{match[3]} vs. {match[4]} - {match[3]} play at home! \n")
        print("Please enter one positive interger or zero! \n")
        home_result = validate_interger_input(f"Enter goals for {match[3]} \n")
        away_result = validate_interger_input(f"Enter goals for {match[4]} \n")
        # Update the rest in the fixture worksheet
        update_fixtures(match, home_result, away_result)
        # Update the standings in the corresponding worksheet
        update_standings(match, home_result, away_result)
        # Start a loop to validate data
        while True:
            after_matchday = input("Continue? Input 'yes' or 'no'): ").lower()
            if after_matchday in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if after_matchday == 'no':
            # Save the progress and exit the loop
            save_progress(row_number)
            break


# Function that will clear the matchday results and standings
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


# The function to run the main menu
def menu():
    while True:
        print("-----------------------------------------------")
        print("Welcome to the English Premier League Table!")
        print("-----------------------------------------------\n")
        print("Type 'league table' to see the table: - \n")
        print("Type 'enter results' to enter matchday results: - \n")
        print("Type 'clear results' to begin again: - \n")
        choice = input(f"Enter choice: - \n")
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


# Function to update the worksheet with match results
def update_fixtures(match, home_result, away_result):
    print(str(home_result) + " : " + str(away_result) + "\n")
    row = int(match[0])
    # Updates home and away goals in worksheet
    fixtures.update_cell(int(row), 6, int(home_result))
    fixtures.update_cell(int(row), 7, int(away_result))
    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)
    # Updates the goal difference on the worksheet
    fixtures.update_cell(int(row), 8, int(home_gd))
    fixtures.update_cell(int(row), 9, int(away_gd))


# Function to update standings based on the results of the match
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
    # Updates if the Home Team wins
    if home_result > away_result:
        standings.update_cell((cell_home.row), 3, (int(home_before) +3))
        standings.update_cell((cell_home.row), 2, int(home_gd_before) + home_gd)
        standings.update_cell((cell_away.row), 2, int(away_gd_before) + away_gd)
    # Updates if the result is a draw
    elif home_result == away_result:
        standings.update_cell((cell_home.row), 3, (int(home_before) + 1))
        standings.update_cell((cell_away.row), 3, (int(away_before) + 1))
    # Updates if the Away Team wins
    else:
        standings.update_cell((cell_away.row), 3, (int(away_before) + 3))
        standings.update_cell((cell_home.row), 2, int(home_gd_before) +  home_gd)
        standings.update_cell((cell_away.row), 2, int(away_gd_before) + away_gd)
    sort()


# Function to sort the standings
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
