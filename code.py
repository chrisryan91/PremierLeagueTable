



""""
team_one = fixtures.get('C2:C381')
team_two = fixtures.get('D2:D381')

def get_match_winner():

    for (a, b) in zip(team_a, team_b):
        team_one_score = input(f"Enter {a} score here: \n")
        team_two_score = input(f"Enter {b} score here: \n")

        if team_one_score > team_two_score:

            first_cell_values = [[str(a), +1 , +1, +0, +0, int(team_one_score), int(team_two_score), +(int(team_one_score)-int(team_two_score)), +3 ]]
            
            cell_list = table.range('A1:H1')

            for i, val in enumerate(first_cell_values):  #gives us a tuple of an index and value
                cell_list[i].value = val    #use the index on cell_list and the val from cell_values

            table.update_cells(cell_list)
            #a_notation = "A" + str(Luton.row) + ":AT"+ str(Luton.row)
                
            #table.update(a_notation, first_cell_values)

        elif team_one_score == team_two_score:
            first_cell_list = table.range('A2:I2')
            first_cell_values = [str(a), +1 , +0, +0, +1, int(team_one_score), int(team_two_score), +(int(team_one_score)-int(team_two_score)), +1]

            for i, val in enumerate(first_cell_values):  #gives us a tuple of an index and value
                first_cell_list[i].value = val    #use the index on cell_list and the val from cell_values

            table.update_cells(first_cell_list)

            second_cell_list = table.range('A3:I3')
            second_cell_values = [str(b), +1, +0, +0, +1, int(team_two_score), int(team_one_score), +(int(team_two_score)-int(team_one_score)), +1]

            for i, val in enumerate(second_cell_values):  #gives us a tuple of an index and value
                second_cell_list[i].value = val    #use the index on cell_list and the val from cell_values

            table.update_cells(second_cell_list)
        else:
            first_cell_list = table.range('A2:I2')
            first_cell_values = [str(a), +1 , +0, +1, +0, int(team_one_score), int(team_two_score), +(int(team_one_score)-int(team_two_score)), +0 ]

            for i, val in enumerate(first_cell_values):  #gives us a tuple of an index and value
                first_cell_list[i].value = val    #use the index on cell_list and the val from cell_values

            table.update_cells(first_cell_list)

            second_cell_list = table.range('A3:I3')
            second_cell_values = [str(b), +1 , +1, +0, +0, int(team_two_score), int(team_one_score), +(int(team_two_score)-int(team_one_score)), +3 ]

            for i, val in enumerate(second_cell_values):  #gives us a tuple of an index and value
                second_cell_list[i].value = val    #use the index on cell_list and the val from cell_values

            table.update_cells(second_cell_list)

get_match_winner()


"""
