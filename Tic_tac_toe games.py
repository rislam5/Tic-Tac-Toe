#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

for i in range(10):
    clear_output(wait=True)   #to print the last output we are using this
    print("Hello World!")


# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**
# 

# In[2]:


from IPython.display import clear_output
def display_board(board):
    print('   |   |  ')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |  ')
    print('---|---|--')
    print('   |   |  ')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |  ')
    print('---|---|--')
    print('   |   |  ')
    print(f' { board[1]} | {board[2]} | {board[3]}')
    print('   |   |  ')


# In[3]:


#to test the previous cell
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[4]:


def player_input():
    player_1=input('player 1, choose "x" or "O": ')
    while player_1!='x' and player_1!='o':
        player_1=input('player 1, choose "x" or "O": ')
        
    if player_1=='x':
        player_2='o'
    else:
        player_2='x'
    return(player_1,player_2)


# In[5]:


#to test the previous cell
player_input()


# In[6]:


player_1, player_2=player_input()


# In[7]:


player_1


# In[8]:


player_2


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[9]:


def place_marker(board, marker, position):
    board[position]=marker


# In[10]:


#to test the previous cell
place_marker(test_board,'#',4)
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[11]:


def win_check(board,mark):
    return (board[7]==board[8]==board[9]==mark) or (board[4]==board[5]==board[6]==mark) or (board[1]==board[2]==board[3]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)


# In[12]:


#to test the previous cell
place_marker(test_board,'X',2)
win_check(test_board,'X')


# In[13]:


#to test the previous cell
place_marker(test_board,'X',2)
win_check(test_board,'O')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[14]:


import random
def choice_first():
    string=['player_1','player_2']                    
    return string[random.randint(0,len(string)-1)]


# In[15]:


#to test the previous cell
choice_first()


# In[16]:


#to test the previous cell
choice_first()


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[17]:


def space_check(board, position):
    return board[position]==' '


# In[18]:


#to test the previous cell
space_check(test_board,8)


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[19]:


def full_board_check(board):
    for i in range(1,len(test_board)):
        if board[i]==' ':
            return False
            break
    return True
            


# In[20]:


#to test the previous cell
full_board_check(test_board)


# In[21]:


#to test the previous cel
another_board= ['#','X','O','X','O','X','O','X',' ','X']
full_board_check(another_board)


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[22]:


def player_choice(board):
    i=int(input('type next position: '))
    if space_check(board, i):
        return i


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[23]:


def replay():
    ask=input('if want to play again, type "yes" otherwise "no": ').lower()
    return ask=='yes'


# In[24]:


#to test the previous cell
replay()


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[27]:


from IPython.display import clear_output
print('     welcome to tic tac toe game!    ')
print('********')
print('please turn off caps lock on your keyboard')
print('*********')
while True:
    board=[' ']*10
    #display_board(board)      #step1
    player_1, player_2 = player_input()#step2
    player=choice_first()  #step5
    print('********')
    print(f'{player} will go first')
    print('********')
    answer=input('do you want to start? "Yes" or "No": ')
    if answer=='yes':
        game_on= True
    elif answer=='no':
        game_on= False
    else:
        print('********')
        print('please, type "yes" or "no", not number or any symbol ')
    while game_on:
        if player=='player_1':
            clear_output()
            display_board(board)
            position=player_choice(board) #step8 ans which is connected to step6
            place_marker(board,player_1,position)  #step3
            if win_check(board,player_1):
                clear_output()
                display_board(board)
                print(f'{player} has won the game. congratulations!')
                game_on= False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('the game is a tie')
                    break
                else:
                    player='player_2'
        elif player=='player_2':
            clear_output()
            display_board(board)
            position=player_choice(board)
            place_marker(board,player_2,position)
            if win_check(board,player_2):
                clear_output()
                display_board(board)
                print(f'{player} has won the game. congratulations!')
                game_on= False
            else:
                if full_board_check(board):
                    clear_output()
                    display_board(board)
                    print('the game is a tie')
                    break
                else:
                    player='player_1'
    if not replay():
        break


# In[ ]:





# In[ ]:




