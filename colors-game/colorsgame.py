import tkinter
import random

# Driver Code 
# Create a GUI window
colordisplay = tkinter.Tk()

# set the title
colordisplay.title("Color-Game")

# Set the size
colordisplay.geometry("750x400")

# add an instructions label
instructions = tkinter.Label(colordisplay, text = "Type in the color"
                             "of the words, and not  the word text!", font = ('Helvetica', 12))

instructions.pack()

# score label
scoreLabel = tkinter.Label(colordisplay, text = "Press enter to start",
                           font = ('Helvetica', 12))
scoreLabel.pack()

# Time left label
timeLabel = tkinter.Label(colordisplay, text = "Time left: " +
                          str(timeleft), font = ('Helvetia', 12))
timeLabel.pack()

# label to display the colors
label = tkinter.Label(colordisplay, font = ('Helvetia', 60))
label.pack()

# Text entry box for typing in colors
e = tkinter.Entry(colordisplay)

# run the 'startGame' function when the enter key is pressed
colordisplay.bind('<Return>', startGame())
e.pack()
# Set focus on the entry box
e.focus_set()

# Start the GUI
colordisplay.mainloop()

# Declaration of variables
# List of possible color.
colors = ['Red','Blue','Green','Pink','Black','Yellow',
          'orange','White','Purple','Brown']
score = 0

# The game time left in seconds
timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColor()

def nextColor():
    global score
    global timeleft

    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the color typed is equal to the color of the text
        if e.get().lower() == colors[1].lower():
            sore += 1
        # clear the text entry box
        e.delete(0, tkinter.END)
        random.shuffle(colors)

        # change the color to type, by changing the 
        # text _and_ the color to a random color value
        label.config(fg = str(colors[1]), text = str(colors[0]))

        # update the score
        scoreLabel.config(text = "score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft
    
    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1
        
        # update the time left label
        timeLabel.config(text = "Time left: " + str(timeleft))

        # run the function again after 1 second
        timeLabel.after(1000, countdown)