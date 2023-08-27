import gspread 
from google.oauth2.service_account import Credentials

"""
Tabulate is imported and installed as it helps display our league table nicely on the terminal.
"""

from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('league_table')

"""
We have two spreadsheet to get from the worksheet.
Data will be pulled from one sheet and data will then update the sheets.
From the standings spreadsheet we will update the terminal. 
"""

fixtures = SHEET.worksheet('fixtures')
standings = SHEET.worksheet('standings')

"""

"""

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

"""
The all_matches function loops through each row in the spreadsheet which is then used to determine the fixture.
Each row on the fixture spread sheet has columns for: Match Number, Matchday, Matchdate, Home team, Away team, Home goals and Away goals.
Within the loop firstly asks the user if they would like to view the league as it stands - this will recur when the matchday value changes.
Secondly, the function will ask the user to input the goals for each team - one team being the home team, the other the away team.
With the values given, we update each row in turn.
"""

def all_matches():

    for match in fixtures.get_all_values():
        """
        At the tenth game, the matchday will change. 
        The modulo operator checks if the remainder if the matchday is divided by ten. 
        If the remainder is zero, a new matchday prompts to view the updated table.
        """
        if int(match[0]) % 10 == 0:
            
            print(f"Would you like to view the table after {match[1]} ? \n")

            print("Enter 'yes' to view the tables or 'no' to continue!")
            
            """
            After decaring a new list, we run a while loop which contains an if, elif, else statement to determine if the users choice.
            """

            after_matchday = ''

            while True:

                after_matchday = input('Do you want to continue? yes/no: ')

                if after_matchday.lower() == 'yes':

                    print('User typed yes')

                    table()

                elif after_matchday.lower() == 'no':

                    print('User typed no')

                    break

                else:
                    print('Type yes/no')

        """
        Within a while loop, we ask for the users input and validate the data. 
        We ask for two inputs - the home team score and the away team score.
        The data is validated with try, except, else which checks if the input is an interger.
        """

        while True:

            print(f"{match[1]} \n")

            print(f"{match[3]} vs. {match[4]} - {match[3]} play at home! \n")

            print("Please enter one positive interger or zero for both teams in the match! \n")

            home_result = input(f"Enter goals scored by {match[3]} \n")

            away_result = input(f"Enter goals score by {match[4]} \n")

            try:
                int(home_result)   

                int(away_result)    

            except ValueError:

                print("Not an integer!")

                continue

            else:

                print("Yes an integer!")

                break 
        
        """
        Two functions are called with valid input data which will update our spreadsheets.
        The two functions to update two seperate spreadsheets - one with match data, one with our table. 
        
        """

        update_fixtures(match, home_result, away_result)
        update_standings(match, home_result, away_result)

"""
From the menu, we can choose to clear the results. This will remove all values added from the tables so the process can be reset
The clear_results function will remove four columns rom the fixtures sheet and two from the standings sheet. 
It then updates standings sheet with values removed that need to be in-place when the update_standings function is updated.
"""

def clear_results():

    try:

        fixtures.delete_columns(6, 7)
        fixtures.delete_columns(7, 8)
        standings.delete_columns(2, 3)

        update_list = standings.range('B1:C1')
        cell_values = ["Goal Difference", "Points"]

        for i, val in enumerate(cell_values):  #gives us a tuple of an index and value

            update_list[i].value = val    #use the index on cell_list and the val from cell_values

        standings.update_cells(update_list)

    except Exception as e:
        print("An error occured:", str(e))
    
    menu()  

"""
Define menu function which will run first and users can return to. 
It presents three options which the user can choose from with properly submitted inputs.
If the string is non equal to either of the three options it returns the menu function.
"""
def menu():
        while True:
            print("Welcome to the English Premier League Table! \n")
            print("Type 'league table' to see the table: - \n")
            print("Type 'enter results' to enter matchday results: - \n")
            print("Type 'clear table to clear the results from the table and begin again: - \n")
            choice = input(f"Enter choice: - \n")

            """
            An if, elif, else statement is used to determine the users choice.
            If the users choice is equal to a value it returns a specific function - table, all_matches and clear_results.
            """

            if choice.strip().lower() == str("league table"):
                table()

            elif choice.strip().lower() == str("enter results"):
                all_matches()

            elif choice.strip().lower() == str("clear results"):
                confirmation = input("Are you sure you want to clear the table? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    clear_results()
            
            elif choice.strip().lower() == "exit":
                print("Exiting the program. Goodbye!")
                break
            else: 
                print("Invalid results - try again! \n")

"""
The update_fixtures function updates each row successively with four values.
"""

def update_fixtures(match, home_result, away_result):
    
    print(str(home_result) + " : " + str(away_result) + "\n")

    """
    By converting the row value to an interger, we can use the update_cell function to update each cell in-turn with home goals and away goals.
    By substituting one value from another, the goal difference can be determined. 
    """

    row = int(match[0])
    fixtures.update_cell(int(row), 6, int(home_result))
    fixtures.update_cell(int(row), 7, int(away_result))

    """
    The goal difference will contribute to determining league position
    """

    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)
    fixtures.update_cell(int(row), 8, int(home_gd))
    fixtures.update_cell(int(row), 9, int(away_gd))

"""
The update_standings function will update the standings spreadsheet. 
Each row has a team in column A with two empty cells in B and C to contain Goal Difference and Points. 
The sort function is called when the sheet has updated.
"""

def update_standings(match, home_result, away_result):

    """
    The standings sheet is searched to return the position of the two teams.
    The match list we looped through in the all_matches function was pulled from the fixture spreadsheet.
    """

    cell_home = standings.find(str(match[3]))
    cell_away = standings.find(str(match[4]))
    home_gd = int(home_result) - int(away_result)
    away_gd = int(away_result) - int(home_result)

    """
    Using if, elif and else the winner is determine by checking the goals scored for each team for each fixture.
    Once updated, the sort function is returned.
    """

    if home_result > away_result:
        standings.update_cell((cell_home.row), 3, +3)
        standings.update_cell((cell_home.row), 2, home_gd)
        standings.update_cell((cell_away.row), 2, away_gd)

    elif home_result == away_result:
        standings.update_cell((cell_home.row), 3, +1)
        standings.update_cell((cell_away.row), 3, +1)

    else: 
        standings.update_cell((cell_away.row), 3, +3)
        standings.update_cell((cell_home.row), 2, home_gd)
        standings.update_cell((cell_away.row), 2, away_gd)

    sort()

"""

"""

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


