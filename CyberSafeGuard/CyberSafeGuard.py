'''This code was created by Shrut Chokshi and Darius and in this code these people will have to go through levels that each have a topic surrounding internet safety. Internet safety is a really big problem that is occurring today with the ongoing use of technology. This program is designed to help our target market of kids to learn about internet safety . More information will be provided on all the game demos, slide presentation and research doc. Enjoy the code and work through how to solve these challenges and level. All these levels have a unique and different aspect towards internet safety. Concluding, there will be many opportunities for our users to learn at.

Course: Dig. Tech and Innovations in the changing world
Date started: December 19, 2023
Date Finsihed: January 12, 2024'''

import pgzrun
from time import sleep
from random import randint

# Play the background music
music.play("jazz")

# Add images for the menu page
start = Actor("startscreen.png")
instructions = Actor("instructions.png")
exit = Actor("exitscreen.png")
goodluck = Actor("goodluck.png")

# Add images for the new level animation
newlevel1 = Actor("newlevel1.png")
newlevel2 = Actor("newlevel2.png")
newlevel3 = Actor("newlevel3.png")
newlevel4 = Actor("newlevel4.png")
newlevel5 = Actor("newlevel5.png")

#Add the images for each of the hearts from 1-5
heart1 = Actor("heart1.png")
heart2 = Actor("heart2.png")
heart3 = Actor("heart3.png")
heart4 = Actor("heart4.png")
heart5 = Actor("heart5.png")

#Add the images for the password level
password = Actor("bestpassword.png")
correctpassword = Actor("correctanswer.png")
wrongpassword = Actor("wrongpassword.png")

#Add the images for the gmail level
gmailintro = Actor("gmailintro.png")
gmail1 = Actor("gmail1.png")
gmail2 = Actor("gmail2.png")
gmail3 = Actor("gmail3.png")
gmail4 = Actor("gmail4.png")
explanationgmail = Actor("explanationgmail.png")

#Add the background
background = Actor("background.png")

#Add the images for the tweets for digital footprint safety
tweet1 = Actor("tweet1.png")
tweet2 = Actor("tweet2.png")
tweet3 = Actor("tweet3.png")

#Add the images for the virus detecting level
introvirus = Actor("introvirus.png")
virus = Actor("virus.png")

#Add the image for the ending page
end = Actor("end.png")

#Make the starting image width and height the size of the start image
WIDTH = start.width
HEIGHT = start.height

#Add the boxes for the quiz later on
main_box = Rect(0, 0, 820, 240)
timber_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

# Set initial positions for the rectangles
main_box.move_ip(50, 40)
timber_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

# Store the answer boxes in a list
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

# Initialize time_left variables
time_left = "∞"

# Define questions and answers
q1 = ["What is needed in a good password?", "Thinking", "Symbols/Lowercase/Uppercase", "B", "1234", 2]
q2 = ["What do you NOT share online?", "Drug prescriptions", "Personal Information", "Terrorist Attacks", "Family", 2]
q3 = ["Who should you only accept emails from?", "Presidents", "Schools", "People", "Those you know", 4]
q4 = ["What should you check for on a website?", "Privacy", "Cookies", "A HTTPS URL Link", "Terms & Conditions", 3]
q5 = ["What should you do when you are being threatened online?", "Tell a trusted adult & block the user", "Ignore the message", "Go to France", "Threaten back", 1]
q6 = ["Why is cybersecurity important?", "Scary people can get you", "You need to protect yourself", "So you learn the responsibility to protect yourself on the internet", "So you don't go on the dark web", 3]
q7 = ["What are the consequences of sharing personal information online", "Risk of losing personal information", "Risk of stolen identity", "Risk of stolen data", "All of the above", 4]
q8 = ["Should you learn to keep yourself and others safe on the internet", "Yes", "No", "Yes but with caution", "Prioritize yourself", 3]
q9 = ["What should you do when you gain access to dangerous or illegal information", "Delete the information", "Report this information to the police", "Stay away from the information source", "All of the above", 4]
q10 = ["Should you share your own passwords", "Yes", "No", "Only if you want to", "Keep it with trusted sources", 2]
q11 = ["Did you enjoy this program", "Yes", "Yes", "Yes", "Yes", 1]

# Store questions in a list
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]

# Flag to check if sounds are playing
correct_sound_playing = False
incorrect_sound_playing = False

#set the score to 5, in other words the lives
score = 5

#get the box of the instruction
instruction_x = 146
instruction_y = 303
instruction_width = 93
instruction_height = 30

#get the box of start
start_x = 318
start_y = 302
start_width = 93
start_height = 30

#get the box of exit
exit_x = 494
exit_y = 302
exit_width = 93
exit_height = 30

#get the box of main menu
mainmenu_x = 219
mainmenu_y = 320
mainmenu_width = 271
mainmenu_height = 74

#get the box for continue
continue_x = 208
continue_y = 374
continue_width = 316
continue_height = 62

#get the box for password
password_x = 79
password_y = 230
password_width = 565
password_height = 88

#get the box for password2
password2_x = 79
password2_y = 342
password2_width = 565
password2_height = 84

#get the box for try again when they click the wrong password
tryagainpass_x = 191
tryagainpass_y = 318
tryagainpass_width = 302
tryagainpass_height = 86

#get the box when they need to click the correct password
correctpassword_x = 152
correctpassword_y = 448
correctpassword_width = 414
correctpassword_height = 86

#get the box if they click continue (1)
continue1_x = 218
continue1_y = 346
continue1_width = 263
continue1_height = 49

#get the box if they click continue (2)
continue2_x = 225
continue2_y = 575
continue2_width = 312
continue2_height = 37

#get the box if they click accept for the gmail
accept_x = 72
accept_y = 468
accept_width = 164
accept_height = 47

#get the box if they click deny for the gmail
deny_x = 400
deny_y = 469
deny_width = 163
deny_height = 47

#get the box if they click continue for the gmail
continuegmail_x = 380
continuegmail_y = 302
continuegmail_width = 285
continuegmail_height = 37

#get the box if they want to send the tweet
send_x = 36
send_y = 409
send_width = 161
send_height = 145

#get the box if they do not want to send the tweet (dont send (ds))
ds_x = 470
ds_y = 401
ds_width = 156
ds_height = 145

#get the box if they want to continue to find the virus
findvirus_x = 355
findvirus_y = 456
findvirus_width = 310
findvirus_height = 44

#get the box of the virus
virus_x = 347
virus_y = 276
virus_width = 58
virus_height = 49

#get the box of the quiz option
quiz_x = 362
quiz_y = 266
quiz_width = 203
quiz_height = 97

#get the box of the exit option at the end
exit2_x = 85
exit2_y = 267
exit2_width = 190
exit2_height = 100


#set the start image to show
startshow = True

#set all the other variables we plan to use to false

exitscreen = False
show_instructions = False
goodluckshow = False
newlevel1show = False
newlevel2show = False
newlevel3show = False
newlevel4show = False
newlevel5show = False
passwordshow = False
show_heart = False
showcorrectpassword = False
showwrongpassword = False
showgmailpage = False
placegmail1 = False
placegmail2 = False
placegmail3 = False
placegmail4 = False
explaingmail = False
placegmailexplain = False
drawthedot = False
tweet_1 = False
tweet_2 = False
tweet_3 = False
endingscreen = False
placeintrovirus = False
placevirus = False
quizclicked = False

#set the current level to 1 and the delay to 1 for the new level animation
current_level = 1
delay_seconds = 0.5 # Set the delay between levels

screenai = 1

# Define the custom number pattern
number_pattern = [8, 3, 1, 6, 7, 5, 9, 2, 4 ]
dots = []
dot2_list = []
lines = []
next_dot = 0

dot_count = 0
dot2_count = 5  # Adjust the number of dot2 instances

#Get the draw funtion to draw all the images
def draw():

    #clear the screen
    screen.clear()

    #check if the startshow is true and draw the corresponding image
    if startshow:
        start.draw()

    #check if the show instructions is true and draw the corresponding image
    if show_instructions:
        instructions.draw()

    #check if the exitscreen is true and draw the corresponding image
    if exitscreen:
        exit.draw()

    #check if the goodluck showing screen is true and draw the corresponding image
    if goodluckshow:
        goodluck.draw()

    #check if the newlevel image 1 is true and draw the corresponding image
    if newlevel1show:
        newlevel1.draw()

   #check if the newlevel image 2 is true and draw the corresponding image
    if newlevel2show:
        newlevel2.draw()

   #check if the newlevel image 3 is true and draw the corresponding image
    if newlevel3show:
        newlevel3.draw()

   #check if the newlevel image 4 is true and draw the corresponding image
    if newlevel4show:
        newlevel4.draw()

   #check if the newlevel image 5 is true and draw the corresponding image
    if newlevel5show:
        newlevel5.draw()

   #check if the password screen is true then draw the corresponding image
    if passwordshow:
        screen.fill("dim gray")
        password.draw()

   #check if show heart and score is equal to that corresponding number to draw the image based on the lives
    if show_heart and score == 5:
        heart5.draw()

   #check if show heart and score is equal to that corresponding number to draw the image based on the lives

    if show_heart and score == 4:
        heart4.draw()

   #check if show heart and score is equal to that corresponding number to draw the image based on the lives

    if show_heart and score == 3:

        heart3.draw()

   #check if show heart and score is equal to that corresponding number to draw the image based on the lives

    if show_heart and score == 2:
        heart2.draw()

   #check if show heart and score is equal to that corresponding number to draw the image based on the lives

    if show_heart and score == 1:
        heart1.draw()

#check if the correct password is set to true and draw the image for it
    if showcorrectpassword:
        correctpassword.draw()

#check if the wrong password is set to true and draw the image for it
    if showwrongpassword:
        wrongpassword.draw()

#check if the gmail intro page is set to true and draw the image for it
    if showgmailpage:
        gmailintro.draw()

#check if the placegmail 1 is set to true and draw the image for it
    if placegmail1:
        gmail1.draw()

#check if the placegmail 2 is set to true and draw the image for it
    if placegmail2:
        gmail2.draw()

#check if the placegmail 3 is set to true and draw the image for it
    if placegmail3:
        gmail3.draw()

#check if the placegmail 4 is set to true and draw the image for it
    if placegmail4:
        gmail4.draw()

#check if the explanation of the gmail is set to true and draw the image for it
    if explaingmail:
        explanationgmail.draw()

#check if we can draw the dots and if it is set to true
    if drawthedot == True:
        draw_dots()

#check if the tweet 1 is set to true and draw the image for it
    if tweet_1:
        tweet1.draw()

#check if the tweet 2 is set to true and draw the image for it
    if tweet_2:
        tweet2.draw()

#check if the tweet 3 is set to true and draw the image for it
    if tweet_3:
        tweet3.draw()

#check if the place intro for the virus screen is set to true and draw the image for it
    if placeintrovirus:
        screen.fill("red")
        introvirus.draw()

#check if the place virus for the virus screen is set to true and draw the image for it

    if placevirus:
        virus.draw()

#check if the ending screen is set to true and draw it
    if endingscreen:
        end.draw()

#check if the quiz is being drawn and call the function for it
    if quizclicked:
        draw_quiz()

#draw the quiz and get the function draw quiz
def draw_quiz():

    #get the global variables
    global time_left, questions, answer_boxes

    #edit the screen
    screen.fill("black")
    screen.draw.filled_rect(main_box, "white")
    screen.draw.filled_rect(timber_box, "dark gray")

    # Draw the answer boxes
    for box in answer_boxes:
        screen.draw.filled_rect(box, "dark gray")

    if questions:
        # Display the time left and the current question
        screen.draw.textbox(str(time_left), timber_box, color=("black"))
        screen.draw.textbox(questions[0][0], main_box, color=("black"))

        index = 1
        # Display answer choices in the answer boxes
        for box in answer_boxes:
            screen.draw.textbox(questions[0][index], box, color=("black"))
            index = index + 1
    else:
        # Display game over message
        screen.draw.textbox("Good thinking! The quiz has been completed.", main_box, color=("black"))

#have a function to place the start screen
def place_start():

    #center the start screen
    start.center = (WIDTH // 2, HEIGHT // 2)

#get the function to place the end
def place_end():

    #get the global variables
    global show_heart, endingscreen, HEIGHT

    #center the end screen
    end.center = (WIDTH // 2, HEIGHT // 2)
    #set the height to the given height
    HEIGHT = 424
    #set show_heart to false and ending screen to true
    show_heart = False
    endingscreen = True

#get the function for place_instruction
def place_instructions():
    #get the global variables
    global show_instructions
    #draw instructions
    show_instructions = True

#get the function to place correctpassword
def place_correctpassword():

    #set global variables
    global showcorrectpassword, WIDTH, HEIGHT

    #set correctpassword to true
    showcorrectpassword = True

    #line up the frame and image
    WIDTH, HEIGHT = 750, 400
    correctpassword.x = 400
    correctpassword.y = 250

#get the function to place a wrong password
def place_wrongpassword():
    #get the global variables
    global showwrongpassword, WIDTH, HEIGHT

    #fix the frame
    showwrongpassword = True
    WIDTH, HEIGHT = 700, 450
    wrongpassword.x = 400
    wrongpassword.y = 250

#get the function to place_exit
def place_exit():

    #get the global variables
    global exitscreen, WIDTH, HEIGHT

    #fix the screen
    exitscreen = True
    WIDTH, HEIGHT = 500, 220
    exit.center = (WIDTH // 2, HEIGHT // 2)  # Center the exit screen
    quit()

#get the function to place the good luck screen
def place_goodluck():

    #get the global variables
    global goodluckshow, WIDTH, HEIGHT

    #fix the frame
    goodluckshow = True
    WIDTH, HEIGHT = 700, 450
    goodluck.x = 400
    goodluck.y = 400

#get the function to place new level screen
def place_newlevel():

    #get all the global variables needed for the function
    global newlevel1show, newlevel2show, newlevel3show, newlevel4show, newlevel5show, WIDTH, HEIGHT, current_level, show_heart, screenai, score, dot_count, lines, score, dots, dot2_list, number_pattern, next_dot, dot2_count, drawthedot

    #check if the increment is equal to 0 and set all the drawings to false
    if current_level == 0:
        newlevel1show = False
        newlevel2show = False
        newlevel3show = False
        newlevel4show = False
        newlevel5show = False

#check if the current level is 1 and set the drawings corresponding to that
    if current_level == 1:
        newlevel1show = True
        WIDTH, HEIGHT = 650, 350
        newlevel1.x = 350
        newlevel1.y = 250
        show_heart = False

#check if the current level is 2 and set the drawings corresponding to that
    elif current_level == 2:
        newlevel2show = True
        WIDTH, HEIGHT = 650, 350
        newlevel2.x = 350
        newlevel2.y = 250
        show_heart = False

#check if the current level is 3 and set the drawings corresponding to that
    elif current_level == 3:
        newlevel3show = True
        WIDTH, HEIGHT = 650, 350
        newlevel3.x = 350
        newlevel3.y = 250
        show_heart = False

#check if the current level is 4 and set the drawings corresponding to that
    elif current_level == 4:
        newlevel4show = True
        WIDTH, HEIGHT = 650, 350
        newlevel4.x = 350
        newlevel4.y = 250
        show_heart = False

#check if the current level is 5 and set the drawings corresponding to that

    elif current_level == 5:
        newlevel5show = True
        WIDTH, HEIGHT = 650, 350
        newlevel5.x = 350
        newlevel5.y = 250
        show_heart = False

#check if the current level is finished and set the drawings to false

    elif current_level == 6:
        newlevel1show = False
        newlevel2show = False
        newlevel3show = False
        newlevel4show = False
        newlevel5show = False
        if screenai == 3:
            drawthedot = True

        #place the new image based on the screenai it was set to
        if screenai == 1:
            place_password()

         #place the new image based on the screenai it was set to
        if screenai ==2:
            place_gmailcheck()

        #place the new image based on the screenai it was set to
        if drawthedot:

            WIDTH = 800
            HEIGHT = 500

            for dot_number in number_pattern:
                actor = Actor("dot")
                actor.pos = randint(20, 400 - 20), randint(50, 500 - 20)
                dots.append(actor)
                dot_count += 1

            for _ in range(dot2_count):
                dot = Actor("dot1")
                dot.pos = randint(20, 400 - 20), randint(50, 500 - 20)
                dot2_list.append(dot)

            background = Actor("background")

        #place the new image based on the screenai it was set to
        if screenai == 4:
            place_tweet1()

        #place the new image based on the screenai it was set to
        if screenai == 5:
            place_introvirus()

        #place the new image based on the screenai it was set to
        if screenai == 6:
            place_end()

#get the function to draw the dots
def draw_dots():

    #get the global variables
    global dot_count, lines, score, dots, dot2_list, number_pattern, next_dot, dot2_count, show_heart, screenai, drawthedot

    #check if we can draw the dot
    if drawthedot == True:

        #draw the background and the hearts
        background.draw()
        show_heart = True

        #draw the dots for 1
        for i in range(min(dot_count, len(number_pattern))):  # Use min to avoid going out of range
            dot_number = number_pattern[i]
            dot = dots[i]
            screen.draw.text(str(dot_number), (dot.pos[0], dot.pos[1] + 12))
            dot.draw()

        #draw the lines to connect them
        for line in lines:
            screen.draw.line(line[0], line[1], (100, 0, 0))




    #screen.draw.text("Score: " + str(score), (10, 10), color="white")

    # Draw all instances of dot2
        for dot in dot2_list:
            dot.draw()



#get the place gmail check function and fix the screen
def place_gmailcheck():

    global WIDTH, HEIGHT, showgmailpage, show_heart
    showgmailpage = True
    show_heart = False
    WIDTH, HEIGHT = 600, 650
    gmailintro.x = 400
    gmailintro.y = 350

#get the place password function and fix the screen
def place_password():

    global passwordshow, WIDTH, HEIGHT, show_heart

    show_heart = True
    passwordshow = True
    WIDTH, HEIGHT = 700, 600
    password.x = 400
    password.y = 350

#get the place gmail1 function and fix the screen
def place_gmail1():
    global placegmail1, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675,650
    placegmail1 = True
    show_heart = True
    gmail1.x = 375
    gmail1.y = 350

#get the place gmail2 function and fix the screen
def place_gmail2():
    global placegmail2, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675,650
    placegmail2 = True
    show_heart = True
    gmail2.x = 375
    gmail2.y = 350

#get the place gmail3 function and fix the screen
def place_gmail3():
    global placegmail3, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675,650
    placegmail3 = True
    show_heart = True
    gmail3.x = 375
    gmail3.y = 350

#get the place gmail4 function and fix the screen
def place_gmail4():
    global placegmail4, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675,650
    placegmail4 = True
    show_heart = True
    gmail4.x = 375
    gmail4.y = 350

#get the place gmailexplain function and fix the screen

def place_gmailexplain():
    global explaingmail, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675,400
    explaingmail = True
    show_heart = False
    explanationgmail.x = 375
    explanationgmail.y = 275

#get the place tweet1 function and fix the screen - also fix the position of the hearts
def place_tweet1():

    global tweet_1, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675, 600
    tweet_1 = True
    tweet1.x = 375
    tweet1.y = 350
    show_heart = True
    if show_heart and score == 5:
        heart5.x = 190
        heart5.y = 25

#get the place tweet2 function and fix the screen - also fix the position of the hearts

def place_tweet2():

    global tweet_2, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675, 600
    tweet_2 = True
    tweet2.x = 375
    tweet2.y = 350
    show_heart = True
    if show_heart and score == 5:
        heart5.x = 190
        heart5.y = 25

#get the place tweet3 function and fix the screen - also fix the position of the hearts

def place_tweet3():

    global tweet_3, WIDTH, HEIGHT, show_heart

    WIDTH, HEIGHT = 675, 600
    tweet_3 = True
    tweet3.x = 375
    tweet3.y = 350
    show_heart = True

#get the place intro virus function and fix the screen

def place_introvirus():

    global placeintrovirus, WIDTH, HEIGHT, show_heart


    WIDTH, HEIGHT = 750, 600
    placeintrovirus = True
    show_heart = True
    introvirus.x = 375
    introvirus.y = 350

#get the place find virus function and fix the screen

def place_findvirus():

    global placevirus, WIDTH, HEIGHT, show_heart


    WIDTH, HEIGHT = 750, 750
    placevirus = True
    show_heart = True

    if show_heart and score == 5:
        heart5.x = 190
        heart5.y = 25

    virus.x = 375
    virus.y = 430

# Function to handle game over scenario and display final score
def game_over():
    global questions, time_left, score, correct_sound_playing, incorrect_sound_playing
    # Display game over message and final score
    message = "The quiz is over. You got %s questions correct out of 11" % str(score)
    questions = [[message, "-", "-", "-", "-", 10]]  # Wrap the message in a list
    time_left = 0
    correct_sound_playing = False
    incorrect_sound_playing = False

# Function to handle correct answers
def correct_answer():
    global questions, score, time_left, correct_sound_playing
    # Increase the score and move to the next question
    score = score + 1
    if questions:
        questions = questions[1:]  # Remove the current question
        time_left = "∞"
        if not correct_sound_playing:
            music.play("correct")  # Play the correct sound
            sleep(1)
            music.play("jazz")
    else:
        print("End of questions")
        game_over()

# Function to handle incorrect answers
def incorrect_answer():
    global questions, time_left, score, incorrect_sound_playing
    if not incorrect_sound_playing:
        music.play("incorrect")  # Play the incorrect sound
        sleep(1)
        music.play("jazz")


#get the mouse down function to see if the mouse was pushed down
def on_mouse_down(pos, button):

    #define all the global variables needed for this method
    global instruction_x, instruction_y, instruction_width, instruction_height, startshow, show_instructions, goodluckshow, current_level, score, passwordshow, showwrongpassword, showcorrectpassword, screenai, showgmailpage, placegmail1, placegmail2, placegmail3, placegmail4, placegmailexplain, explaingmail, dot_count, drawthedot, show_heart, tweet_1, tweet_2, tweet_3, placeintrovirus, placevirus, quizclicked
    global next_dot
    global lines
    global score
    global WIDTH, HEIGHT


    #check if startshow is true
    if startshow:

        #check if the instructions box was clicked
        if instruction_x < pos[0] < instruction_x + instruction_width and instruction_y < pos[1] < instruction_y + instruction_height:
            place_instructions()
            startshow = False

        #check if the start box was clicked
        if start_x < pos[0] < start_x + start_width and start_y < pos[1] < start_y + start_height:
            place_goodluck()
            startshow = False

        #check if the exit box was clicked
        if exit_x < pos[0] < exit_x + exit_width and exit_y < pos[1] < exit_y + exit_height:
            place_exit()
            startshow = False

    #check if show instructions is true
    if show_instructions:

        #check if main menu is clicked and perform the code
        if mainmenu_x < pos[0] < mainmenu_x + mainmenu_width and mainmenu_y < pos[1] < mainmenu_y + mainmenu_height:
            show_instructions = False
            startshow = True

    #check if the good luck screen is being shown
    if goodluckshow:

        #check if the continue button was clicked
        if continue_x < pos[0] < continue_x + continue_width and continue_y < pos[1] < continue_y + continue_height:

            #add everything needed in this
            goodluckshow = False
            place_newlevel()
            screenai = 1
            clock.schedule_interval(next_level, delay_seconds)

    #check if passwordshow is true
    if passwordshow:

        #check if any other place was clicked
        if password_x < pos[0] < password_x + password_width and password_y < pos[1] < password_y + password_height or password2_x < pos[0] < password2_x + password2_width and password2_y < pos[1] < password2_y + password2_height:

            #add the code for the wrong answer
            place_wrongpassword()
            passwordshow = False
            score = score - 1
            if score == 0:
                place_exit()

        #check if the correct password was clicked
        if correctpassword_x < pos[0] < correctpassword_x + correctpassword_width and correctpassword_y < pos[1] < correctpassword_y + correctpassword_height:

            #add the code for the right answer
            place_correctpassword()
            passwordshow = False


    #check if this is true
    if showwrongpassword:

        #check if the try again button was clicked
        if tryagainpass_x < pos[0] < tryagainpass_x + tryagainpass_width and tryagainpass_y < pos[1] < tryagainpass_y + tryagainpass_height:

            showwrongpassword = False
            passwordshow = True
            place_password()

    #check if show correct password is true
    if showcorrectpassword:

        #check if the continue button was clicked
        if continue1_x < pos[0] < continue1_x + continue1_width and continue1_y < pos[1] < continue1_y + continue1_height:

            #add the corresponding code for it
            show_heart = False
            place_newlevel()
            current_level = 0
            screenai = 2
            clock.schedule_interval(next_level, 1)
            showcorrectpassword = False

    #check if the show gmail page is true
    if showgmailpage:

        #check if the continue button was clicked
        if continue2_x < pos[0] < continue2_x + continue2_width and continue2_y < pos[1] < continue2_y + continue2_height:

            #add the corresponding code
            showgmailpage = False
            place_gmail1()

    #check if place gmail is true
    if placegmail1:

        #check if they clicked deny and add the corresponding code
        if deny_x < pos[0] < deny_x + deny_width and deny_y < pos[1] < deny_y + deny_height:
            placegmail1 = False
            place_gmail2()
            score = score+ 1

        #check if they clicked accept and add the corresponding code
        if accept_x < pos[0] < accept_x + accept_width and accept_y < pos[1] < accept_y + accept_height:
            score = score - 1
            if score == 0:
                place_exit()

    #check if place gmail1 is true
    if placegmail2:

        #check if they clicked deny and add the corresponding code
        if deny_x < pos[0] < deny_x + deny_width and deny_y < pos[1] < deny_y + deny_height:
            score = score - 1
            if score == 0:
                place_exit()

        #check if they clicked accept and add the corresponding code
        if accept_x < pos[0] < accept_x + accept_width and accept_y < pos[1] < accept_y + accept_height:
            placegmail2 = False
            place_gmail3()
            score = score+ 1

    #check if place gmail1 is true
    if placegmail3:

        #check if they clicked deny and add the corresponding code
        if deny_x < pos[0] < deny_x + deny_width and deny_y < pos[1] < deny_y + deny_height:
            placegmail3 = False
            place_gmail4()
            score = score+ 1

        #check if they clicked accept and add the corresponding code
        if accept_x < pos[0] < accept_x + accept_width and accept_y < pos[1] < accept_y + accept_height:
            score = score - 1
            if score == 0:
                place_exit()

    #check if place gmail1 is true
    if placegmail4:

        #check if they clicked deny and add the corresponding code
        if deny_x < pos[0] < deny_x + deny_width and deny_y < pos[1] < deny_y + deny_height:
            score = score - 1
            if score == 0:
                place_exit()


        #check if they clicked accept and add the corresponding code
        if accept_x < pos[0] < accept_x + accept_width and accept_y < pos[1] < accept_y + accept_height:
            placegmail4 = False
            place_gmailexplain()
            placegmailexplain = True

    #check if place gmail explain is true
    if placegmailexplain:

        #check if the continue button was clicked
        if continuegmail_x < pos[0] < continuegmail_x + continuegmail_width and continuegmail_y < pos[1] < continuegmail_y + continuegmail_height:

            #add the corresponding code for it
            current_level = 1
            place_newlevel()
            clock.schedule_interval(next_level, 1)
            explaingmail = False
            show_heart = False
            screenai = 3
            score += 1

    #check if screenai is equal to 3
    if screenai == 3:

        #check if the dots colldie with each other
        if next_dot < dot_count and dots[next_dot].collidepoint(pos):

            #if they do set the next_dot + 1
            if next_dot:
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot += 1

            #if the next_dot is the last dot then that means they finished it
            if next_dot == dot_count:

                #add the corresponding code
                screenai = 4
                current_level = 1
                place_newlevel()
                clock.schedule_interval(next_level, 1)
                show_heart = False
                drawthedot = False

        #if it was false then reset it back to 0 and make them loose a life
        else:
            lines = []
            next_dot = 0
            score -= 1  # Decrease the score by 1 for a wrong click
            if score == 0:
                place_exit()

    #check if the tweet 1 is true
    if tweet_1 == True:

        #check if they clicked dont send and add the corresponding code
        if ds_x < pos[0] < ds_x + ds_width and ds_y < pos[1] < ds_y + ds_height:
            tweet_1 = False
            place_tweet2()
            score+=1

        #check if they clicked send and add the corresponding code
        if send_x < pos[0] < send_x + send_width and send_y < pos[1] < send_y + send_height:
            score = score - 1
            if score == 0:
                place_exit()

    #check if the tweet 1 is true
    if tweet_2 == True:

        #check if they clicked dont send and add the corresponding code
        if ds_x < pos[0] < ds_x + ds_width and ds_y < pos[1] < ds_y + ds_height:
            score = score - 1
            if score == 0:
                place_exit()

        #check if they clicked send and add the corresponding code
        if send_x < pos[0] < send_x + send_width and send_y < pos[1] < send_y + send_height:
            score+=1
            tweet_2 = False
            place_tweet3()

    #check if the tweet 1 is true
    if tweet_3 == True:

        #check if they clicked dont send and add the corresponding code
        if ds_x < pos[0] < ds_x + ds_width and ds_y < pos[1] < ds_y + ds_height:

            tweet_3 = False
            screenai = 5
            current_level = 1
            place_newlevel()
            clock.schedule_interval(next_level, 1)
            show_heart = False

        #check if they clicked send and add the corresponding code
        if send_x < pos[0] < send_x + send_width and send_y < pos[1] < send_y + send_height:
            score = score - 1
            if score == 0:
                place_exit()

    #check if place intro virus is set to true
    if placeintrovirus:


        #if they click continue let them find the virus
        if findvirus_x < pos[0] < findvirus_x + findvirus_width and findvirus_y < pos[1] < findvirus_y + findvirus_height:
            placeintrovirus = False
            place_findvirus()
            score += 1;

    #check if placevirus is set to true
    if placevirus:

        #check if the correct virus box area was clicked
        if virus_x < pos[0] < virus_x + virus_width and virus_y < pos[1] < virus_y + virus_height:

            #add the corresponding code for it
            placevirus = False
            screenai = 6
            current_level = 1
            place_newlevel()
            clock.schedule_interval(next_level, 1)
            show_heart = False

        #reduce a score if they click anywhere else
        else:
            score = score - 1
            if score == 0:
                place_exit()

    #check if ending screen is true
    if endingscreen:

        #check if exit is clicked and quit the program
        if exit2_x < pos[0] < exit2_x + exit2_width and exit2_y < pos[1] < exit2_y + exit2_height:
             quit()

        #check if quiz is clicked and run the quiz
        if quiz_x < pos[0] < quiz_x + quiz_width and quiz_y < pos[1] < quiz_y + quiz_height:
            quizclicked = True

    #check if quiz is clicked
    if quizclicked:

        #adjuct frame size
        WIDTH = 1280
        HEIGHT = 720

        index = 1
    # Check which answer box was clicked
        for box in answer_boxes:
            if box.collidepoint(pos):
                print("Clicked on answer" + str(index))
                # Check if the clicked answer is correct
                if index == questions[0][5]:  # Use questions[0][5] instead of questions[0][11]
                    print("You got it correct!")
                    correct_answer()

            index = index + 1

#use this function for the next level animaiton
def next_level():

    #get global variables
    global current_level, screenai

    #add the current level by 1 when the clock is working
    current_level += 1

    #place new level
    place_newlevel()


#place start
place_start()

#run the code
pgzrun.go()