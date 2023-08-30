# Premier League Table
English Premier League Table is a Python terminal program that runs in the Code Institute mock terminal Heroku. 

When the results of the games are finalised after each match week, a user can update the scores for each game thereby updating the league table. This can be done continuously over the season until all the match results are entered and the champions are determined. The table can be viewed at any point over the season. The data is saved so the program can be exited. The results can be cleared and the process can start again at any point.

The program utilizes the 2023/2024 English Premier League season. However, the program could run any soccer league by updating the associated spreadsheet. 

[Premier League Table](link)

![image of the program running on Heroku on different devices](image.jpg)

## Owner Goals

My goal for this project was to provide the user with a program with the ability to update a league table throughout a season whenever the results come in. I wanted the user to even potentially use speculative results to be able to update a fantasy league table. Fantasy results could be inputted as results of a fantasy match. In its current form, the program runs a specific year in a specific league - the English League in its 2023/2024 season. The malleable nature of the spreadsheet means it can be updated to include any league - even fake teams, in fake leagues with fake results. The program sorts the games in the style of a round-robin tournament where every team meets each other twice. This opposes the elimination tournament found in World Cups or other head-to-head Cup tournaments.

## Features 
### How to Use

![image of the menu](documents/readme%20images/menu.png)

When the program runs, you user is given four menu options - view table, enter results, clear the results and table, and exit the program. Viewing the table will ask the user if they want to see the top four teams, the bottom three teams, or the entire table. At the start, the table will have no resulting values. By the end of the season with all results in, the table will have the result of all the games. 

![image of results entry](documents/readme%20images/match_day_entry.png)

Choosing to enter the results will ask the user to enter the goals scored by each team for each of the fixtures. Firstly, the goals scored by the team playing at home; secondly, the goals scored by the team playing away from home. After the results from each matchday are entered, the option is presented to view the table. However, data is saved and the table can be viewed at any point by returning to the menu. 

![image of the top four](documents/readme%20images/top_four.png)

![image of the whole table](documents/readme%20images/full_table.png)

The third option from the menu is to clear the saved data and clear the table - this will bring the program back to the beginning by removing text from the progress.txt file and data from the associated spreadsheets. When entering results again, you will be brought back to matchday one.

![image of the the end of the season function](documents/readme%20images/end_of_season.png)

In this English example, 380 games are played for 38 matchdays with ten games per matchday. At the end of the season, when all the games of rows have been looped through, the champions and runners-up are printed to the terminal with the option to view to entire table again.

![image of the choosing to 'clear results'](documents/readme%20images/clear_results.png)

### Existing Features
#### Google Sheet Integration 
- The program interacts with a Google Sheet document titled *League table*. The document contains two worksheets titled *standings* and *fixtures*. Data is taken from the *fixtures* worksheet. Resulting data updates both the *fixtures* and *standings* worksheet. *Standings* maintains the sorted league. 
- The *fixtures* sheet stores the values for the goals scored for each team and the goal difference for each team for each game.
- The *standings* sheet stores the points for each team and the goal difference over the course of the entire season.

#### Interface and Interaction
- The menu will provide users with an interface with different options. Each option has further options to choose from i.e. entering match results. The option to return to the menu is available at any point while running the program.
- Choosing the option to view the table as it stands will give the user the ability to choose to see the entire table or the top or bottom teams.
- The 'tabulate' library is used to format the table data in the terminal.

#### Match Result Entry 
- The program presents the user with a match to enter the results. The user is asked to input the goals scored by each team separately. 
- The user is made aware of the specific matchday and is prompted to view the table at the end of every matchday.
  
#### Saving Progress
The progress automatically saves and loads progress into a file in the directory of the program. This allows for data to be saved when the program is exited. This means the user can return and enter results from where they left off. It can be cleared at any point. 

#### Input Validation

The program contains checks to make sure that the data entered is correct. If it is incorrect, the user will be prompted to re-enter the data. If an integer is required, the program will check for an integer. If a word is required, the program will check if the string is equal to a value. 

### Future Features 

- The game should be more easily adaptable for other leagues. For example, two teams with level points are not sorted by goal difference in other leagues. In the German league, for example, the position of two teams with equal points is determined by the result of their head-to-head matches. The program should also allow for the entry of data into the spreadsheet for other leagues rather than using manual input.

- More variables could be added to get more specific with input values such as top-scoring player. If the program allowed for entry of who scored the goals, the program could determine the top scorer. 

- Rather than displaying the Home team or the Away team, the program could simply ask for the ground in which the match is played. Rather than displaying "Home team: ManCity, Away team: Newcastle", the program could ask "Ground to be played by ManCity vs Newcastle" and the answer would determine who played at home. If "St. James Park" is entered, Newcastle is the Home team. If "Etihad Stadium" is entered, ManCity is at home. 

- There are many other statistics from soccer games that could be added and utilized: possession of the ball for each time, expected goals, red cards, yellow cards, and substitutions that could be integrated. 

## Data Model

Google Sheets were used to model the data for this program. Google Sheets allowed for the match fixtures, results and standings to be represented. 

### Fixtures Worksheet

The fixtures worksheet contains rows for each game of the season. 

There are nine headers in the fixtures worksheet:

1. The match number
2. The matchday number
3. Home team
4. Away team
5. Date played 
6. Home team goals
7. Away team goals
8. Home team goal difference
9. Away team goal difference

![image of the fixtures spreadsheet](documents/readme%20images/fixtures_sheet.png)
### Standings Worksheet

The standings worksheet contains the table itself. The row values are for each team. There are no headers. Each of the columns contains values for:

1. Team name
2. Overall goal difference
3. Overall points

![image of the standings spreadsheet](documents/readme%20images/standing_stable.png)

### Progress tracking and saving

There is a progress.txt file in the same directory of the program that will save data. Specifically, it saves the row number of the last match that was updated. When the program runs again it takes off from there. 

### Data processing

The program processes goal differences, updates the standings, updates the points and then sorts by these values. A user interacts with the command-line interface (CLI) to input the values, view the league, and clear the results. 

## Testing

I have manual tested the program by running it the whole way through. The progress.txt file can be edited to enter a later row value to test the later sections of the end_of_season function by entering a row value nearer to the end. I found no bugs when I tested the project manually.

### Bugs
#### Solved Bugs

- There were many bugs in both the functions to update the spreadsheets. Wrong values were inputted in the right places. The right values were inputted in the wrong places. It took a combing with a fine toothcomb but the values entered for each cell are correct.

- I ran into bugs whenever I tried to validate code. I would use a While loop in a function and break it at the wrong point. I could continue at the wrong point. This kept on happened whenever I tried to validate an input and ask for the input again. This was the case for the table function, all_matches function and menu functions. I used Stack Overflow to resolve these issues. I sometimes created separate functions to validate an input such as creating the validate_integer_input function.
  
#### Remaining Bugs

- A bug I noticed just before deployment occurs when using the validate_input
  
### Validator Testing

The code was run through the Code Institute Python linter with a few issues initially. The lines of some of the code exceeded the cut-off point. In most cases, these were print functions whose strings I needed to reduce. This is especially true when I added simple_colors and Colorama modules to try to colour the code in the terminal. In these cases, I set new variables with the strings for printing and printed the strings. 

Now the code passes through the linter with no issues. 

![image of the run.py code ran through the Code Institute Linter](documents/readme%20images/linter_checker.png)

## Libraries & Technologies User
### Python Libraries 
I installed a lot of different libraries while making this program. The ones used in the end are as follows:

- **gspread** to communicate with Google Sheets
  
- **Colorama** was used to colour text in the terminal
  
- **simple_colors** was used to colour tables in the terminal.
  
- **Tabulate** was used to display terminals with an appealing design.

### Programs Used

- **GitHub** was used for version control

- **Heroku** was used to display the project live. 
  
- **CI Python Linter** was used to validate Python code. 

## Deployment

The project was deployed using Code Institute's mock terminal for Heroku. 

## Credits & Acknowledgements

- This YouTube video from Tech With Tim with help using the Colorama module: https://www.youtube.com/watch?v=u51Zjlnui4Y

- The vast majority of solutions to issues I ran into came from Stack Overflow, especially regarding While loop issues and Try, Except statements.

- This YouTube video with help with saving to a file and loading from a file. The code was adapted directly from this video: https://www.youtube.com/watch?v=Uh2ebFW8OYM

- I used this YouTube video to help refactor and standardise my code: https://www.youtube.com/watch?v=u3yo-TjeIDg

- My tutor Antonio with advice and help along the way.