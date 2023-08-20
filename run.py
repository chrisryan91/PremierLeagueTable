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


team_a = (WestHam, Arsenal, ManCity, ManUnited, Chelsea)

team_b = (Wolves, Sheffield, Burnley, Liverpool)

def get_match_winner():

    for (a, b) in zip(team_a, team_b):
        team_one_score = input(f"Enter {a} score here: \n")
        team_two_score = input(f"Enter {b} score here: \n")

        if team_one_score > team_two_score:
            cell_list = []
            #get the headers from row #1
            headers = table.row_values(1)
            # find the column "Weight", we will remember this column #
            colToUpdate = headers.index('Points')

            # task 1 of 2
            cellLookup = table.find(a)
            # get the cell to be updated
            cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
            # update the cell's value
            cellToUpdate.value = 3
            # put it in the queue
            cell_list.append(cellToUpdate)

            # task 2 of 2
            cellLookup = table.find(b)
            # get the cell to be updated
            cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
            # update the cell's value
            cellToUpdate.value = 0
            # put it in the queue
            cell_list.append(cellToUpdate)

            # now, do it
            table.update_cells(cell_list)

        elif team_one_score == team_two_score:
            cell_list = []
            #get the headers from row #1
            headers = table.row_values(1)
            # find the column "Weight", we will remember this column #
            colToUpdate = headers.index('Points')

            # task 1 of 2
            cellLookup = table.find(a)
            # get the cell to be updated
            cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
            # update the cell's value
            cellToUpdate.value = +1
            # put it in the queue
            cell_list.append(cellToUpdate)

            # task 2 of 2
            cellLookup = table.find(b)
            # get the cell to be updated
            cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
            # update the cell's value
            cellToUpdate.value = +1
            # put it in the queue
            cell_list.append(cellToUpdate)

            # now, do it
            table.update_cells(cell_list)
            
        else:
            cell_list = []
            #get the headers from row #1
            headers = table.row_values(1)
            # find the column "Weight", we will remember this column #
            colToUpdate = headers.index('Points')

            # task 1 of 2
            cellLookup = table.find(a)
            # get the cell to be updated
            cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
            # update the cell's value
            cellToUpdate.value = +0
            # put it in the queue
            cell_list.append(cellToUpdate)

            # task 2 of 2
            cellLookup = table.find(b)
            # get the cell to be updated
            cellToUpdate = table.cell(cellLookup.row, colToUpdate+1)
            # update the cell's value
            cellToUpdate.value = +3
            # put it in the queue
            cell_list.append(cellToUpdate)

            # now, do it
            table.update_cells(cell_list)

get_match_winner()