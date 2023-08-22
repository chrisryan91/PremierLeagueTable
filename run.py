import gspread 
from google.oauth2.service_account import Credentials

import numpy as np


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('league_table')

table = SHEET.worksheet('table')
fixtures = SHEET.worksheet('fixtures')


Arsenal = table.acell('A2').value
AstonVilla = table.acell('A3').value
Bournemouth = table.acell('A4').value
Brentford = table.acell('A5').value
Brighton = table.acell('A6').value
Burnley = table.acell('A7').value
Chelsea = table.acell('A8').value
CrystalPalace = table.acell('A9').value
Everton = table.acell('A10').value
Fulham = table.acell('A11').value
Liverpool = table.acell('A12').value
Luton = table.acell('A13').value
ManCity = table.acell('A14').value
ManUnited = table.acell('A15').value
Newcastle = table.acell('A16').value
Nottingham = table.acell('A17').value
Sheffield = table.acell('A18').value
Tottenham = table.acell("A19").value
WestHam = table.acell('A20').value
Wolves = table.acell('A21').value

team_a = (
Burnley,
Newcastle,
Sheffield,
Everton,
Brighton,
Arsenal,
Bournemouth,
Chelsea,
Brentford,
ManUnited,
CrystalPalace,
Liverpool,
Fulham,
Wolves,
Luton,
WestHam,
AstonVilla,
Tottenham,
ManCity,
Nottingham,
Burnley,
Brentford,
Arsenal,
Newcastle,
Chelsea,
Sheffield,
ManUnited,
Bournemouth,
Brighton,
Everton,
Liverpool,
Brentford,
Sheffield,
Arsenal,
Arsenal,
Brighton,
Chelsea,
Burnley,
Luton,
CrystalPalace,
Everton,
Newcastle,
ManUnited,
Nottingham,
Bournemouth,
AstonVilla,
Wolves,
Fulham,
WestHam,
Tottenham,
Chelsea,
Brighton,
Brentford,
CrystalPalace,
Burnley,
Sheffield,
ManCity,
Arsenal,
Liverpool,
Luton,
Bournemouth,
Nottingham,
AstonVilla,
Newcastle,
Fulham,
ManUnited,
Tottenham,
Everton,
Wolves,
WestHam,
Wolves,
Everton,
ManUnited,
Burnley,
Brighton,
Arsenal,
WestHam,
CrystalPalace,
Fulham,
Luton,
Chelsea,
ManCity,
Brentford,
Newcastle,
Liverpool,
Tottenham,
Nottingham,
Sheffield,
AstonVilla,
Bournemouth,
Chelsea,
Bournemouth,
WestHam,
Brighton,
AstonVilla,
ManUnited,
Wolves,
Liverpool,
Arsenal,
CrystalPalace,
Newcastle,
Nottingham,
ManCity,
Everton,
Tottenham,
Burnley,
Luton,
Fulham,
Brentford,
Sheffield,
Liverpool,
Arsenal,
CrystalPalace,
AstonVilla,
ManUnited,
Chelsea,
Bournemouth,
WestHam,
Brighton,
Wolves,
Brentford,
Tottenham,
Sheffield,
Nottingham,
Newcastle,
Luton,
ManCity,
Everton,
Burnley,
Fulham,
Bournemouth,
Chelsea,
WestHam,
Nottingham,
Liverpool,
Brentford,
Newcastle,
Burnley,
ManCity,
Arsenal,
Luton,
CrystalPalace,
Brighton,
Wolves,
Sheffield,
AstonVilla,
Everton,
Fulham,
Tottenham,
ManUnited,
AstonVilla,
ManUnited,
Sheffield,
Brighton,
Everton,
CrystalPalace,
Luton,
Tottenham,
Wolves,
Fulham,
Brentford,
Arsenal,
ManCity,
Burnley,
Newcastle,
Bournemouth,
Liverpool,
Chelsea,
Nottingham,
WestHam,
Liverpool,
Nottingham,
ManCity,
CrystalPalace,
Fulham,
Wolves,
Tottenham,
WestHam,
Luton,
AstonVilla,
ManUnited,
Chelsea,
Bournemouth,
Burnley,
Sheffield,
Everton,
Newcastle,
Brighton,
Arsenal,
Brentford,
Fulham,
Tottenham,
CrystalPalace,
WestHam,
AstonVilla,
Luton,
Wolves,
Nottingham,
Liverpool,
ManCity,
Arsenal,
Chelsea,
Bournemouth,
Burnley,
Brentford,
Brighton,
Everton,
Newcastle,
ManUnited,
Sheffield,
Nottingham,
WestHam,
Tottenham,
Luton,
Fulham,
Wolves,
AstonVilla,
CrystalPalace,
ManCity,
Liverpool,
Sheffield,
Brighton,
Burnley,
Arsenal,
Newcastle,
Brentford,
Bournemouth,
Everton,
ManUnited,
Chelsea,
WestHam,
Fulham,
Wolves,
Tottenham,
Liverpool,
CrystalPalace,
ManCity,
AstonVilla,
Nottingham,
Luton,
Burnley,
Fulham,
Newcastle,
Sheffield,
ManCity,
Everton,
Brentford,
Luton,
Nottingham,
Tottenham,
WestHam,
CrystalPalace,
Brighton,
ManUnited,
Liverpool,
Bournemouth,
Arsenal,
AstonVilla,
Wolves,
Chelsea,
Sheffield,
Luton,
Burnley,
Fulham,
Brentford,
Tottenham,
Nottingham,
ManCity,
Everton,
Newcastle,
Arsenal,
WestHam,
ManUnited,
Wolves,
CrystalPalace,
Liverpool,
Chelsea,
Brighton,
Bournemouth,
AstonVilla,
WestHam,
Wolves,
Burnley,
Arsenal,
Everton,
Brighton,
CrystalPalace,
Luton,
ManUnited,
Fulham,
ManCity,
Liverpool,
Chelsea,
Nottingham,
Bournemouth,
Sheffield,
Tottenham,
Brentford,
Newcastle,
AstonVilla,
Brentford,
Bournemouth,
Nottingham,
Arsenal,
WestHam,
Burnley,
ManCity,
Newcastle,
Chelsea,
Liverpool,
Brighton,
Luton,
AstonVilla,
Everton,
Sheffield,
ManUnited,
CrystalPalace,
Fulham,
Tottenham,
Wolves,
Arsenal,
Burnley,
Liverpool,
Chelsea,
WestHam,
ManCity,
Bournemouth,
Brentford,
Newcastle,
Nottingham,
Wolves,
AstonVilla,
Luton,
Sheffield,
Brighton,
Fulham,
Tottenham,
ManUnited,
Everton,
CrystalPalace,
Tottenham,
Everton,
Bournemouth,
ManUnited,
AstonVilla,
Fulham,
WestHam,
Wolves,
Nottingham,
Newcastle,
Brighton,
Arsenal,
Luton,
Brentford,
CrystalPalace,
Burnley,
Sheffield,
Liverpool,
Chelsea,
ManCity,
ManUnited,
Bournemouth,
Newcastle,
Tottenham,
Nottingham,
Wolves,
AstonVilla,
WestHam,
Fulham,
Everton,
CrystalPalace,
Chelsea,
Arsenal,
Luton,
Brighton,
Brentford,
Burnley,
Sheffield,
ManCity,
Liverpool
)

team_b = (ManCity,
AstonVilla,
CrystalPalace,
Fulham,
Luton,
Nottingham,
WestHam,
Liverpool,
Tottenham,
Wolves,
Arsenal,
Bournemouth,
Brentford,
Brighton,
Burnley,
Chelsea,
Everton,
ManUnited,
Newcastle,
Sheffield,
AstonVilla,
CrystalPalace,
Fulham,
Liverpool,
Luton,
ManCity,
Nottingham,
Tottenham,
WestHam,
Wolves,
AstonVilla,
Bournemouth,
Everton,
Fulham,
ManUnited,
Newcastle,
Nottingham,
Tottenham,
WestHam,
Wolves,
Arsenal,
Brentford,
Brighton,
Burnley,
Chelsea,
CrystalPalace,
Liverpool,
Luton,
ManCity,
Sheffield,
AstonVilla,
Bournemouth,
Everton,
Fulham,
ManUnited,
Newcastle,
Nottingham,
Tottenham,
WestHam,
Wolves,
Arsenal,
Brentford,
Brighton,
Burnley,
Chelsea,
CrystalPalace,
Liverpool,
Luton,
ManCity,
Sheffield,
AstonVilla,
Bournemouth,
Brentford,
Chelsea,
Liverpool,
ManCity,
Newcastle,
Nottingham,
Sheffield,
Tottenham,
Arsenal,
Brighton,
Burnley,
CrystalPalace,
Everton,
Fulham,
Luton,
ManUnited,
WestHam,
Wolves,
Brentford,
Burnley,
Everton,
Fulham,
Luton,
ManCity,
Newcastle,
Nottingham,
Sheffield,
Tottenham,
Arsenal,
AstonVilla,
Bournemouth,
Brighton,
Chelsea,
CrystalPalace,
Liverpool,
ManUnited,
WestHam,
Wolves,
Brentford,
Burnley,
Everton,
Fulham,
Luton,
ManCity,
Newcastle,
Nottingham,
Sheffield,
Tottenham,
Arsenal,
AstonVilla,
Bournemouth,
Brighton,
Chelsea,
CrystalPalace,
Liverpool,
ManUnited,
WestHam,
Wolves,
AstonVilla,
Brighton,
CrystalPalace,
Everton,
Fulham,
Luton,
ManUnited,
Sheffield,
Tottenham,
Wolves,
Arsenal,
Bournemouth,
Brentford,
Burnley,
Liverpool,
ManCity,
Newcastle,
Nottingham,
WestHam,
Chelsea,
Arsenal,
Bournemouth,
Brentford,
Burnley,
Chelsea,
Liverpool,
ManCity,
Newcastle,
Nottingham,
WestHam,
AstonVilla,
Brighton,
CrystalPalace,
Everton,
Fulham,
Luton,
ManUnited,
Sheffield,
Tottenham,
Wolves,
Arsenal,
Bournemouth,
Brentford,
Brighton,
Burnley,
Chelsea,
Everton,
ManUnited,
Newcastle,
Sheffield,
AstonVilla,
CrystalPalace,
Fulham,
Liverpool,
Luton,
ManCity,
Nottingham,
Tottenham,
WestHam,
Wolves,
Arsenal,
Bournemouth,
Brentford,
Brighton,
Burnley,
Chelsea,
Everton,
ManUnited,
Newcastle,
Sheffield,
CrystalPalace,
Fulham,
Liverpool,
Luton,
Nottingham,
Wolves,
AstonVilla,
ManCity,
Tottenham,
WestHam,
Arsenal,
Bournemouth,
Brentford,
Brighton,
Everton,
ManUnited,
Newcastle,
Sheffield,
Burnley,
Chelsea,
AstonVilla,
CrystalPalace,
Fulham,
Liverpool,
Luton,
ManCity,
Nottingham,
Tottenham,
WestHam,
Wolves,
Arsenal,
Bournemouth,
Brentford,
Brighton,
Burnley,
Chelsea,
Everton,
ManUnited,
Newcastle,
Sheffield,
Arsenal,
AstonVilla,
Bournemouth,
Brighton,
Chelsea,
CrystalPalace,
Liverpool,
ManUnited,
WestHam,
Wolves,
Brentford,
Burnley,
Everton,
Fulham,
Luton,
ManCity,
Newcastle,
Nottingham,
Sheffield,
Tottenham,
Arsenal,
AstonVilla,
Bournemouth,
Brighton,
Chelsea,
CrystalPalace,
Liverpool,
ManUnited,
WestHam,
Wolves,
Brentford,
Burnley,
Everton,
Fulham,
Luton,
ManCity,
Newcastle,
Nottingham,
Sheffield,
Tottenham,
AstonVilla,
Bournemouth,
Brentford,
Chelsea,
Liverpool,
ManCity,
Newcastle,
Nottingham,
Sheffield,
Tottenham,
Arsenal,
Brighton,
Burnley,
CrystalPalace,
Everton,
Fulham,
Luton,
ManUnited,
WestHam,
Wolves,
Brighton,
CrystalPalace,
Fulham,
Luton,
Tottenham,
Wolves,
AstonVilla,
Everton,
ManUnited,
Sheffield,
Arsenal,
Bournemouth,
Brentford,
Burnley,
Chelsea,
Liverpool,
ManCity,
Newcastle,
Nottingham,
WestHam,
AstonVilla,
Brighton,
CrystalPalace,
Everton,
Fulham,
Luton,
ManUnited,
Sheffield,
Tottenham,
Wolves,
Arsenal,
Bournemouth,
Brentford,
Burnley,
Chelsea,
Liverpool,
ManCity,
Newcastle,
Nottingham,
WestHam,
Arsenal,
Brentford,
Brighton,
Burnley,
Chelsea,
CrystalPalace,
Liverpool,
Luton,
ManCity,
Sheffield,
AstonVilla,
Bournemouth,
Everton,
Fulham,
ManUnited,
Newcastle,
Nottingham,
Tottenham,
WestHam,
Wolves,
Arsenal,
Brentford,
Brighton,
Burnley,
Chelsea,
CrystalPalace,
Liverpool,
Luton,
ManCity,
Sheffield,
AstonVilla,
Bournemouth,
Everton,
Fulham,
ManUnited,
Newcastle,
Nottingham,
Tottenham,
WestHam,
Wolves)

def get_match_winner():

    #while True:
        for (a, b) in zip(team_a, team_b):
            print("----------------------------------------")
            print(f"Enter the goals scored for {a} and {b} \n")
            print(f"{a} play at home! \n")
            print(f"{b} play away! \n")

            team_one_score = input(f"Enter {a} goals scored here: \n")
            team_two_score = input(f"Enter {b} goals scored here: \n")

            #validate_data(team_one_score, team_two_score)

            if team_one_score > team_two_score:

                home_team_winner(a, b, team_one_score, team_two_score)

            elif team_one_score == team_two_score:
                
                draw(a, b, team_one_score, team_two_score)   
                
            else:
                
                away_team_winner(a, b, team_one_score, team_two_score)

                
        """"
        if validate_data(team_one_score, team_two_score):
            print("Data is valid!")
            break
        """

""" 
def validate_data(c, d):

    try:
        [int(a, b) for (a, b) in zip(a, b)] 
        raise ValueError(
            f"Please enter a single numerical digit \n"
        )

    except ValueError as e:
        print(f"Invalid data: {e} and try again! \n")
        return False

    return True
"""

def home_team_winner(a, b, team_one_score, team_two_score):
        
    cell_list = []

    #get the headers from row #1

    headers = table.row_values(1)

    # find the column "Weight", we will remember this column #

    colToUpdate = headers.index('Points')
    col2ToUpdate = headers.index('Won')
    col4ToUpdate = headers.index('Loss')
    col5ToUpdate = headers.index('Goals Scored')
    col6ToUpdate = headers.index('Goals Against')
    col7ToUpdate = headers.index('Goal Difference')

    cellLookup = table.find(a)

    # get the cell to be updated

    cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
    cell2ToUpdate = table.cell(cellLookup.row, col2ToUpdate+1)
    cell5ToUpdate = table.cell(cellLookup.row, col5ToUpdate+1)
    cell6ToUpdate = table.cell(cellLookup.row, col6ToUpdate+1)
    cell7ToUpdate = table.cell(cellLookup.row, col7ToUpdate+1)

    # update the cell's value

    cellToUpdate.value = int(cellToUpdate.value) + 3
    cell2ToUpdate.value = int(cell2ToUpdate.value) + 1
    cell5ToUpdate.value = team_one_score
    cell6ToUpdate.value = team_two_score
    cell7ToUpdate.value = int(team_one_score) - int(team_two_score)

    # put it in the queue
    cell_list.append(cellToUpdate)
    cell_list.append(cell2ToUpdate)
    cell_list.append(cell5ToUpdate)
    cell_list.append(cell6ToUpdate)
    cell_list.append(cell7ToUpdate)

    # task 2 of 2

    cellLookup = table.find(b)

    # get the cell to be updated

    cell4ToUpdate = table.cell(cellLookup.row, col4ToUpdate+1)
    cell5ToUpdate = table.cell(cellLookup.row, col5ToUpdate+1)
    cell6ToUpdate = table.cell(cellLookup.row, col6ToUpdate+1)
    cell7ToUpdate = table.cell(cellLookup.row, col7ToUpdate+1)

    # update the cell's value

    cell4ToUpdate.value = int(cell4ToUpdate.value) + 1
    cell5ToUpdate.value = team_two_score
    cell6ToUpdate.value = team_one_score
    cell7ToUpdate.value = int(team_two_score) - int(team_one_score)

    # put it in the queue

    cell_list.append(cell4ToUpdate)
    cell_list.append(cell5ToUpdate)
    cell_list.append(cell6ToUpdate)
    cell_list.append(cell7ToUpdate)

    # now, do it

    table.update_cells(cell_list)

    table.sort((2, 'des'), range='A2:H21')

def draw(a, b, team_one_score, team_two_score):

    cell_list = []
    
    #get the headers from row #1

    headers = table.row_values(1)

    # find the column "Weight", we will remember this column #

    colToUpdate = headers.index('Points')
    col3ToUpdate = headers.index('Draw')
    col5ToUpdate = headers.index('Goals Scored')
    col6ToUpdate = headers.index('Goals Against')

    cellLookup = table.find(a)

    # get the cell to be updated

    cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
    cell3ToUpdate = table.cell(cellLookup.row, col3ToUpdate+1)
    cell5ToUpdate = table.cell(cellLookup.row, col5ToUpdate+1)
    cell6ToUpdate = table.cell(cellLookup.row, col6ToUpdate+1)

    # update the cell's value

    cellToUpdate.value = int(cellToUpdate.value) + 1
    cell3ToUpdate.value = int(cell3ToUpdate.value) + 1
    cell5ToUpdate.value = team_one_score
    cell6ToUpdate.value = team_two_score

    # put it in the queue
    cell_list.append(cellToUpdate)
    cell_list.append(cell3ToUpdate)
    cell_list.append(cell5ToUpdate)
    cell_list.append(cell6ToUpdate)

    # task 2 of 2

    cellLookup = table.find(b)

    # get the cell to be updated

    cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
    cell3ToUpdate = table.cell(cellLookup.row, col3ToUpdate+1)
    cell5ToUpdate = table.cell(cellLookup.row, col5ToUpdate+1)
    cell6ToUpdate = table.cell(cellLookup.row, col6ToUpdate+1)

    # update the cell's value

    cellToUpdate.value = int(cellToUpdate.value) + 1
    cell3ToUpdate.value = int(cell3ToUpdate.value) + 1
    cell5ToUpdate.value = team_two_score
    cell6ToUpdate.value = team_one_score


    # put it in the queue

    cell_list.append(cellToUpdate)
    cell_list.append(cell3ToUpdate)
    cell_list.append(cell5ToUpdate)
    cell_list.append(cell6ToUpdate)

    # now, do it

    table.update_cells(cell_list)

    table.sort((2, 'des'), range='A2:H21')

def away_team_winner(a, b, team_one_score, team_two_score):

    cell_list = []

    #get the headers from row #1

    headers = table.row_values(1)

    # find the column "Weight", we will remember this column #

    colToUpdate = headers.index('Points')
    col2ToUpdate = headers.index('Won')
    col4ToUpdate = headers.index('Loss')
    col5ToUpdate = headers.index('Goals Scored')
    col6ToUpdate = headers.index('Goals Against')
    col7ToUpdate = headers.index('Goal Difference')

    cellLookup = table.find(a)

    # get the cell to be updated

    cell4ToUpdate = table.cell(cellLookup.row, col4ToUpdate+1)
    cell5ToUpdate = table.cell(cellLookup.row, col5ToUpdate+1)
    cell6ToUpdate = table.cell(cellLookup.row, col6ToUpdate+1)
    cell7ToUpdate = table.cell(cellLookup.row, col7ToUpdate+1)

    # update the cell's value

    cell4ToUpdate.value = int(cell4ToUpdate.value) + 1
    cell5ToUpdate.value = team_one_score
    cell6ToUpdate.value = team_two_score
    cell7ToUpdate.value = int(team_one_score) - int(team_two_score)

    # put it in the queue

    cell_list.append(cell4ToUpdate)
    cell_list.append(cell5ToUpdate)
    cell_list.append(cell6ToUpdate)
    cell_list.append(cell7ToUpdate)

    # task 2 of 2

    cellLookup = table.find(b)

    # get the cell to be updated

    cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
    cell2ToUpdate = table.cell(cellLookup.row, col2ToUpdate+1)
    cell5ToUpdate = table.cell(cellLookup.row, col5ToUpdate+1)
    cell6ToUpdate = table.cell(cellLookup.row, col6ToUpdate+1)
    cell7ToUpdate = table.cell(cellLookup.row, col7ToUpdate+1)

    # update the cell's value

    cellToUpdate.value = int(cellToUpdate.value) +3
    cell2ToUpdate.value = int(cell2ToUpdate.value) + 1
    cell5ToUpdate.value = team_two_score
    cell6ToUpdate.value = team_one_score
    cell7ToUpdate.value = int(team_two_score) - int(team_one_score)

    # put it in the queue

    cell_list.append(cellToUpdate)
    cell_list.append(cell2ToUpdate)
    cell_list.append(cell5ToUpdate)
    cell_list.append(cell6ToUpdate)
    cell_list.append(cell7ToUpdate)

    # now, do it

    table.update_cells(cell_list)

    table.sort((2, 'des'), range='A2:H21')

get_match_winner()