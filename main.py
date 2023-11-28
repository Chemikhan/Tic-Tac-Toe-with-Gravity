# The Tic-Tac-Toe game with gravity code

# By changing table_length, table_width you can change the size of the table
# Variable chars_in_a_row is responsible for the 'win' condition,i.e. how many characters in a row player should collect to win.
# gamers list shows us how many players can play this game and what characters they use.

table_length = 6
table_width = 7
chars_in_a_row = 4
gamers = ['X','O']

def create_table(l:int,w:int)->list:
    """
    Create a table

    :param int l: length of the table, i.e. amount of rows
    :param int w: width of the table, i.e. amount of columns
    """
    table = []
    for _ in range(l):
        row = []
        for _ in range(w):
            row.append(None)
        table.append(row)
    return table

def table_full_check(table:list)->bool:
    """
    Check if the table has no space to put one more sign in it

    :param list table: table to check
    """
    counter = 0 
    for row in table:
        counter += row.count(None)
    if counter == 0:
        return True
    else:
        return False

def print_game_table(table:list)->None:
    """
    Print the table, adding special characters for a more visual representation.    

    :param list table: table to print
    """
    #creating and filling the table with special chars
    game_table = []
    upperline = ['-']
    for r_n,row in enumerate(table):
        row_string = '|'
        upperline = ['-']
        for c_n,column in enumerate(row):
            if table[r_n][c_n] is None:
                row_string = row_string + ' ' + '|'
            else:
                row_string = row_string + str(table[r_n][c_n]) + '|'
            upperline.append('--')
        game_table.append(upperline)
        game_table.append(row_string)
    game_table.append(upperline)

    #printing the table
    for row in game_table:
        row_string = ''
        for column in row:
            row_string+=column
        print(row_string)

def get_column(current_gamer:str,width:int)->(int|None):
    """
    Getting from the gamer the number of column to put there the gamer's charachter.
    The number should be between 1 and width, gamer has 10 attempts to input it.

    :param str current_gamer: gamer's charachter
    :param int width: table width
    """
    column = None
    counter = 10
    while column is None:
        
        try:
            column = int(input(f'Choose the column to put {current_gamer} (from 1 to {width}): '))
            #check if the gamer input correct number
            if column>width or column<1:
                column = None
                raise 
        except KeyboardInterrupt:
            #allowing the gamer to finish the game by KeyboardInterrupt
            print("\nThe Program is terminated manually!")
            quit()
        except:
            #if the number(or other char) is incorrect, decrement the counter 
            counter -= 1
            print(f'Please, write number from 1 to {width+1}. Attempts left: {counter}')
            if counter==0:
                print('Closing the game...')
                break
    return column

def check_winner(row:int,column:int,gamer:str,actual_table:list,chars_in_a_row:int):
    """
    Checking if current gamer wins by adding last char to the table.

    :param int row: row of the last  gamer's charachter
    :param int column: column of the last  gamer's charachter    
    :param str gamer: gamer's charachter
    :param list actual_table: current state of the  table
    :param int chars_in_a_row: win condition
    """
    #cheching if there is any winning sequence in every direction (horizontally, vertically or diagonally)
    #[1,0] - horizontally 
    #[0,1] - vertically
    #[1,1],[-1,1] - diagonally
    for direction in [[1,0],[1,1],[0,1],[-1,1]]:
        counter = 1
        for step_positive in range(1,5):
            try:
                current_row = row+step_positive*direction[0]
                current_column = column+step_positive*direction[1]
                current_sign = actual_table[current_row][current_column]
                if current_sign==gamer:
                    counter+=1
                else:
                    break
            except IndexError:
                break
        for step_negative in range(-1,-5,-1):
            try:
                current_row = row+step_negative*direction[0]
                current_column = column+step_negative*direction[1]
                current_sign = actual_table[current_row][current_column]
                if current_sign==gamer:
                    counter+=1
                else:
                    break
            except IndexError:
                break
        if counter == chars_in_a_row:
            return gamer
    return None

def update_table(current_gamer:str,actual_table:list, chars_in_a_row:int):
    """
    Update the current state of the table

    :param str gamer: gamer's charachter
    :param list actual_table: current state of the table
    :param int chars_in_a_row: win condition
    """
    counter = 3
    while counter!=0:
        choosen_column = get_column(current_gamer,len(actual_table[0]))-1
        for row in range(len(actual_table)-1,-1,-1):
            if actual_table[row][choosen_column] is None:
                actual_table[row][choosen_column] = current_gamer
                gamer = check_winner(row,choosen_column,current_gamer,actual_table,chars_in_a_row)
                return gamer
        counter -=1
        print(f'Column is full. Choose another one. Attempts left: {counter}')
        
def start_game(length:int,width:int,chars_in_a_row:int, gamers_list:list):
    """
    Run the game

    :param int length: length of the table, i.e. amount of rows
    :param int width: width of the table, i.e. amount of columns
    :param int chars_in_a_row: win condition
    :param list gamers_list: win condition
    """
    winner = None
    gamers = gamers_list
    current_gamer = 0
    actual_table = create_table(l=length,w=width)

    print(f'Game "Tic-Tac-Toe" started. Table size: {width}x{length}.')
    print(f'The winner must collect {chars_in_a_row} characters in a row (horizontally, vertically or diagonally) ')
    print_game_table(actual_table)

    while winner is None:
        winner = update_table(gamers[current_gamer],actual_table,chars_in_a_row)
        print_game_table(actual_table)
        #check if the winner is determined
        if winner is not None:
            print(f'The winner is {winner} gamer')
            break
        #check if game table is full
        if table_full_check(actual_table):
            print(f'Table is full. Noone wins')
            break
        #change the gamer
        current_gamer+=1
        if current_gamer==len(gamers):
            current_gamer=0


    
if __name__ == "__main__":
    start_game(table_length,table_width,chars_in_a_row,gamers)