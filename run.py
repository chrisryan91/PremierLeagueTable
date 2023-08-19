import gspread 
from google.oauth2.service_account import Credentials


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


arsenal = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

aston_villa = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

bournemouth = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

brentford = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

brighton = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

burnley = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

chelsea = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

crystal_palace = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

everton = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

fulham = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

liverpool = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

luton_town = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

manchester_city = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

manchester_united = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

newcastle = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

nottingham_forest = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

sheffield_united = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

tottenham = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

west_ham = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

wolves = {
  "Matches Played": 0,
  "Win": 0,
  "Draw": 0,
  "Loss": 0,
  "Goals Scored": 0,
  "Goals Against": 0,
  "Goal Difference": 0,
  "Points": 0
}

def get_match_winner():
    team_one = fixtures.get('C2:C381')
    team_two = fixtures.get('D2:D381')
    for (a, b) in zip(team_one, team_two):
        print(a, b)
        print(f"Please enter the result of {a} against {b} \n")
        print("Data should be two numbers seperated by a comma \n")
        print("Example: 2,2 \n")
        score_data = input("Enter the result here: \n")
        
get_match_winner()
