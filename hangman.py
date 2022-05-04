# imports that were needed
import random
from tkinter import *
from tkinter import messagebox
import c1 as c1

# score starts at zero. When you win the game your score increases
score = 0
run = True

# loop to run the game
while run:
    # root is where all the functions go to pop on screen
    root = Tk()
    root.geometry('915x700')
    root.title('HANG-MAN')
    root.config(bg='#FFFFFF')
    # variable for wrong guess
    wrong_guess = 0
    # variable for if guess is correct
    right_guess = 0

    # choose word at random from the list
    index = random.randint(0, 1)
    # text file where the words are stored
    file = open('words.txt', 'r')
    # reads the words file
    l2 = file.readlines()
    # takes away the \n from the word in wordlist
    selected_word = l2[index].strip('\n')

    # this creates the dashes, creates first dash then moves each dash after by a certain length
    x = 250
    for i in range(0, len(selected_word)):
        x += 60
        # sets properties of dashes and letters that display
        exec('d{}=Label(root,text="_",bg="#FFFFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i, x, 450))

    # this creates all letter icons ( created with https://buttonoptimizer.com/)
    # list of all letters in alphabet
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    # for each letter in list assigns file
    for alpha in al:
        exec('{}=PhotoImage(file="{}.png")'.format(alpha, alpha))

    # creates the hangman images as you play
    # list to use to create them
    hm = ['hm1', 'hm2', 'hm3', 'hm4', 'hm5', 'hm6', 'hm7']
    # for each spot in the list a png is assigned.
    for hangman in hm:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman, hangman))

    # the placement of all buttons for the letters
    button = [['b1', 'a', 0, 595], ['b2', 'b', 70, 595], ['b3', 'c', 140, 595], ['b4', 'd', 210, 595],
              ['b5', 'e', 280, 595], ['b6', 'f', 350, 595], ['b7', 'g', 420, 595], ['b8', 'h', 490, 595],
              ['b9', 'i', 560, 595], ['b10', 'j', 630, 595], ['b11', 'k', 700, 595], ['b12', 'l', 770, 595],
              ['b13', 'm', 840, 595], ['b14', 'n', 0, 645], ['b15', 'o', 70, 645], ['b16', 'p', 140, 645],
              ['b17', 'q', 210, 645], ['b18', 'r', 280, 645], ['b19', 's', 350, 645], ['b20', 't', 420, 645],
              ['b21', 'u', 490, 645], ['b22', 'v', 560, 645], ['b23', 'w', 630, 645], ['b24', 'x', 700, 645],
              ['b25', 'y', 770, 645], ['b26', 'z', 840, 645]]
    
    for q1 in button:
        exec(
            '{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#FFFFFF",activebackground="#FFFFFF",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

    # code to place the hangman
    han = [['c1', 'hm1'], ['c2', 'hm2'], ['c3', 'hm3'], ['c4', 'hm4'], ['c5', 'hm5'], ['c6', 'hm6'], ['c7', 'hm7']]
    for p1 in han:
        exec('{}=Label(root,bg="#FFFFFF",image={})'.format(p1[0], p1[1]))

    c1.place(x=300, y=- 50)

    # end game button, this will close the window
    def close():
        global run
        answer = messagebox.askyesno('ENDING', 'DO YOU WANT TO END THE GAME?')

        if answer:
            run = False
            root.destroy()

    # end the game button
    e1 = PhotoImage(file='end.png')
    ex = Button(root, bd=0, command=close, bg="#FFFFFF", activebackground="#FFFFFF", font=10, image=e1)
    ex.place(x=770, y=10)
    s2 = 'SCORE:' + str(score)
    s1 = Label(root, text=s2, bg="#FFFFFF", font=("arial", 25))
    s1.place(x=10, y=10)

    # button press check function
    def check(letter, button1):
        global wrong_guess, right_guess, run, score
        exec('{}.destroy()'.format(button1))
        if letter in selected_word:
            for i2 in range(0, len(selected_word)):
                if selected_word[i2] == letter:
                    right_guess += 1
                    exec('d{}.config(text="{}")'.format(i2, letter.upper()))
            # if you win the game score increases and asks player to play again
            if right_guess == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER', f'WINNER!\nthe word was: {selected_word.upper()}\nWANT TO PLAY AGAIN?')
                # if answer is true statement
                if answer:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        else:
            wrong_guess += 1
            exec('c{}.destroy()'.format(wrong_guess))
            exec('c{}.place(x={},y={})'.format(wrong_guess + 1, 300, -50))
            # if you guess wrong 6 times, lets you know game over and asks if you want to play again
            if wrong_guess == 6:
                answer = messagebox.askyesno('GAME OVER', f'YOU LOST!\nthe word is: {selected_word.upper()}\nWANT TO PLAY AGAIN?')
                if answer:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()
    # ends main loop
    root.mainloop()
