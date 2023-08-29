# Premier League Table
English Premier League Table is a Python terminal program which runs in the Code Institute mock terminal Heroku. 

A user can update the league table by entering the goals scored in each of the weekend's soccer games. The table will sort the results by points and goal difference. The table can be viewed at any point over the season. The data is saved so the program can be exited and returned to. The results can be cleared and the process can start again. 

The program utilizes the 2023/2024 English Premier League season. However, the program could run any soccer league by updating the associated spreadsheet. 

[Premier League Table](link)

![image of the program running on Heroku on different devices](image.jpg)

## How to use
When the program runs, you user is given four menu options - view table, enter results, clear the results and table, and exit the program. 

![image of the menu](menu.jpg)

Viewing the table will ask the user if they want to see the top four teams, the bottom three teams or the entire table. At the start, the table will have no resulting values. By the end of the season with all results in, the table will have the result of all the games. 

![image of the table](view_table.jpg)

Choosing to enter the results will ask the user to enter the goals scored by each team for each of the fixtures - first the goals scored by the team playing at home, secondly the goals scored by the team playing away from home. After the results from each matchday is entered, the option is presented to view the table. However, data is saved and the table can be viewed at any point by returning to the menu. 

![image of results entry](enter_results.jpg)

The third option from the menu is to clear the saved data and clear the table - this will bring the program back to the beginning by clearing both the saved data and the associated spreadsheets. When entering results again, you will be brought back to matchday one.

![image of the clear_results](clear_results.jpg)

In this English example, 380 games are played over the course of 38 matchdays with ten games per matchday. This program could be adapted to any other soccer league which uses a round-robin system by updating the two associated spreadsheets. 

![image of the standings spreadsheet](standings.jpg)

![image of the fixtures spreadsheet](fixtures.jpg)
The first spreadsheet is for the fixtures from which the match data is taken from. The second spreadsheet is the table in which the match data results are sorted. 

## Features
### Existing Features
#### Google Sheet Integration 
- The program interacts with a Google Sheet document titled *league table*. The document contains two worksheets titled *standings* and *fixtures*. Data is taken from the *fixtures* worksheet. Resulting data updates both the *fixtures* and *standings* worksheet. *Standings* maintains the sorted league. 
- The *fixtures* sheet stores the values for the goals scored for each team and the goal difference for each team for each game.
- The *standings* sheet stores the points for each team and the goal difference over the course of the entire season.

#### Interface and Interaction
- The menu will provide users with an interface with different options. Each option has further options to choose from i.e entering match results. The option to return to the menu is available at any point while running the program.
- Choosing the option to view the table as it stands will give the user the ability to choose to see the entire table or the top or bottom teams.
- The 'tabulate' library is used to format the table data in the terminal.

#### Match Result Entry 
- The program presents the user with a match to enter the results from. The user is asked to input the goals scored by each team separately. 
- The user is made aware of the specific matchday and is prompted to view the table at the end of every matchday.
  
#### Saving Progress
The progress automatically saves and loads progress into a file in the programs directory. This allows for data to be saved when the program is exited. This means the user can return and enter results from where they left off. It can be cleared at any point. 

#### Input Validation

The program contains checks to make sure that the data entered is correct. If it is incorrect, the user will be prompted to re-enter the data. If an integer is required, the program will check for an integer. If a word is required, the program will check if the string is equal to a value. 

### Future Features 

- The game should be more easily adaptable for other leagues. This would require different functions and sorting methods. For example, two teams with level points are not sorted by goal difference in other leagues. In the German league for example, the position of two teams with equal points is determined by the result of their head to head matches. The program should also allow for the entry of data into the spreadsheet for other leagues rather than using manual input.
- More variables could be added to get more specific with input values such as top scoring player. If the program allowed for entry of who scored the goals, the program could determine the top scorer. 
- Rather than displaying Home team or Away team, the program could simply ask for the ground in which the match is played. Rather than displaying "Home team: ManCity, Away team: Newcastle", the program could ask "Ground to be played by ManCity vs Newcastle" and the answer would determine who played at home. If "St. James Park" is entered, Newcastle is the Home team. If "Etihad Stadium" is entered, ManCity are at home. 
- There are many other statistics from soccer games that could be added and utilized: possession of the ball for each time, expected goals, red cards, yellow cards, substitutions that could be integrated. 

## Data Model

Google Sheets were used to model the data for this program. Google Sheets allowed for the match fixtures, results and standings to be represented. 

### Fixtures Worksheet

The fixtures worksheet contains rows for each game of the season. 

There are nine headers in the fixtures worksheet.
1. The match number
2. The matchday number
3. Home team
4. Away team
5. Date played 
6. Home team goals
7. Away team goals
8. Home team goal difference
9. Away team goal difference
    
### Standings Worksheet

The standings worksheet contains the table itself. The row values are for each team. 

The headers are three headers to sort the table:
1. Team name
2. Overall goal difference
3. Overall points

### Progress tracking and saving

There is a progress.txt file in the same directory of the program that will save data. Specifically, it saves the row number of the last match that was updated. When the program runs again it takes off from there. 

### Data processing

The program processes goal differences, updates the standings, updates the points and then sorts by these values. A user interacts with the command-line interface (CLI) to input the values, view the league and clear the results. 

## Testing

I have manual tested the project by doing the following: 

### Bugs
#### Solved Bugs

#### Remaining Bugs
### Validator Testing

## Deployment

The project was deployed using Code Institute's mock terminal for Heroku. 

## Credits & Acknowledgements

- This YouTube video from Tech With Tim with help using the colorama module: https://www.youtube.com/watch?v=u51Zjlnui4Y

- This Stack Overflow user with help with colouring tables: https://stackoverflow.com/questions/76734963/colorama-not-working-with-tabulate-to-display-colored-output-in-python

- The vast majority of solutions to issues I ran into came from Stack Overflow especially regarding While loop issues and Try, Except statements.

- This YouTube video with help regarding saving to a file and loading from a file: https://www.youtube.com/watch?v=Uh2ebFW8OYM