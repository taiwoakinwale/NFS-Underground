# Lab 4
# CS 20
# John and Taiwo
# ------------------------------------- Beginning of code --------------------------------------------------
import random

speed = 0
handling = 0
acceleration = 0
traction = 0

body_rigidity = 0
nos = 0
fuel = 0
distance_covered = 0
total_distance_covered = 0
distance_left = 0
engine_heat = 0
racers_and_cops = 0
chance_of_hitting_cars = 0

# 13 ---------------------- This is where the game will actually start playing ------------------------
# 14 ----------------------------------------- easy mode ----------------------------------------------


def game_play_easy():
   chance_of_hitting_cars = 10
   engine_heat = 100
   body_rigidity = 100
   nos = 100
   fuel = 100
   distance_covered = 0
   total_distance_covered = 0
   distance_left = 50

   racers_and_cops = -1
   random.randrange(10)
   print("The race is about to start!")
   print("\nThe instructions:"
         "\n1. Inject fuel to raise your fuel level"
         "\n   (This will slow you down.)"
         "\n2. Inject Nos to increase your speed dramatically."
         "\n   (This will decrease your Nos and fuel level)"
         "\n3. Slow pace"
         "\n   (This doesn't burn very much fuel.)"
         "\n4. Normal pace"
         "\n   (This burns a moderate amount of fuel.)"
         "\n5. Push the pace"
         "\n   (This burns a greater amount of fuel.)"
         "\n6. Stop"
         "\n   (This will allow you to stop to let your engine to cool down. "
         "\n7. Status"
         "\n   (This is to check your current status"
         "\n8.  Quit"
         "\n   (This is to exit the game)")
   print("\nPro Tip! \nYou should check your status so to check your engine temperature.")
   input("\npress enter to continue. ")
   start_engine = input("\nStart your engine! "
                        "\npress 'e' to start your engine ")
   if start_engine.lower() == "e":
       print("\n3, 2, 1, GO!!!")
   else:
       while start_engine.lower() != "e":
           print("You pressed the wrong button.")
           why_not_try_again = input("Try Again! ")
           if why_not_try_again.lower() == "e":
               print("\n3, 2, 1, GO!!!")
               break
   done = False
   while not done:
       user_choice = int(input(" \n1. Inject fuel to raise your fuel level"
                               "\n2. Inject Nos to increase your speed dramatically."
                               "\n3. Slow pace"
                               "\n4. Normal pace"
                               "\n5. Push the pace"
                               "\n6. Stop"
                               "\n7. Status"
                               "\n8. Quit "
                               "\nYour choice: "))
       if user_choice == 1:

           print("You have injected fuel your fuel level is now at " + str(fuel) + "%")

       elif user_choice == 2:

           print("You have activated your Nos and push the car to the limit, your nos level"
                 "has reduced to " + str(nos) + "% and you have covered " + str(distance_covered)
                 + "km")

       elif user_choice == 3:

           print("You go at a slow pace covering " + str(distance_covered) + "km")

       elif user_choice == 4:

           print("You go at a normal pace covering " + str(distance_covered) + "km")

       elif user_choice == 5:

           print("You push the pace and cover " + str(distance_covered) + "km")

       elif user_choice == 6:

           print("You stop and you engine cools down to " + str(engine_heat) + "C")

       elif user_choice == 7:
           print("\nBody Rigidity: " + str(body_rigidity) + "%"+ "\nNos: " + str(nos) + "%"
                 + "\nFuel: " + str(fuel) + "%" + "\nDistance covered: "
                 + str(total_distance_covered) + "km" + "\nDistance left: " + str(distance_left) + "km"
                 + "\nOther racers: " + str(racers_and_cops) + "km" + "\nEngine heat: " + str(engine_heat) + "C")
           if engine_heat >= 130:
               print("Your engine temperature is high be careful not to have it overheat.")

       elif user_choice == 8:
           print("You have quit the game")
           done = True

# 15 ----------------------------------------- medium mode ----------------------------------------------


def game_play_medium():
   track_size = 100
   your_current_location = 0
   lots = input("1")
   if lots == "1":
       track_size -= 50
       your_current_location += 50
   print("you have this many km left:" + str(track_size))
   print("you have traveled this far:" + str(your_current_location))


# 16 ----------------------------------------- hard mode ------------------------------------------------

def game_play_hard():
   track_size = 100
   your_current_location = 0
   lots = input("1")
   if lots == "1":
       track_size -= 50
       your_current_location += 50
   print("you have this many km left:" + str(track_size))
   print("you have traveled this far:" + str(your_current_location))


# 4 --------------------------- Game code for easy mode ---------------------------------------------

def easy_diff():
   go_on = input("\nTo continue, press enter. ")
   done = False
   if go_on.lower() == "":
       print("\nYour game is loading...")
       print("\nPro tip: Nos is Nitrous oxide, it makes you go faster, but is also "
             "\nflammable and explosive. so be careful how you use it.")
       print()
       next_message = input("To continue, press enter. ")
       if next_message.lower() == "":
           print("\nHere is a $100,000, you can choose your first car.")
           go_on = input("\nTo continue, press enter. ")
           if go_on.lower() == "":
               print("\nThese are your choices:")
   else:
       next_message = input("To continue, press enter, otherwise type 'exit' to quit.")
       if next_message.lower() == "next":
           go_on = input("To continue, type next. ")
           if go_on.lower() == "next":
               print("\nHere is a $100,000, you can choose your first car.")
           go_on = input("To continue, type next. ")
           if go_on.lower() == "next":
               print("\nThese are your choices:")

       elif next_message.lower() == "exit":
           print("You've exited the game.")
           done = True

# 5 ------------------------------------- Types of cars ----------------------------------------------
# 6 -------------------------- Car 1 for easy difficulty ---------------------------------------------
   if go_on == "":
       print("\n2016 Mazda Miata MX-5")
       print("\nThis car is very balanced and you should probably use it to get a feel for the game "
             "\nif you are a beginner. "
             "This car is only meant for true beginners!")

       print("\nSpeed = 50 \nHandling = 50 \nAcceleration = 50 \nTraction = 50 "
             "\nReliability = 100% \nInitial body rigidity = 100%"
             "\nInitial Nos = 100% \nInitial fuel = 100%")
       print()
       go_on = input("press enter to continue. ")
# 7 -------------------------- Car 2 for easy difficulty ---------------------------------------------
   if go_on == "":
       print("\n2016 Chevrolet Corvette Z06")
       print("\nThis car has more speed but everything else is slightly lowered."
             "\nDriving on straights with this car will make you go much faster "
             "\nthan other racers and help you reach"
             "\nthe finish line quicker.")

       print("\nSpeed = 75 \nHandling = 43.33333333333333 "
             "\nAcceleration = 43.33333333333333 \nTraction = 43.33333333333333"
             "\nReliability = 95% \nInitial body rigidity = 100% "
             "\nInitial Nos = 100% \nInitial fuel = 100%")
       go_on = input("\npress enter to continue. ")

# 8 -------------------------- Car 3 for easy difficulty ---------------------------------------------
   if go_on == "":
       print("\n2016 Ford Mustang Shelby GT350R.")
       print("\nThis car has better acceleration but everything else is slightly lowered."
             "\nHaving higher acceleration will help you to get an explosive start off faster, "
             "\nand get out of turns quicker.")

       print("\nSpeed = 43.33333333333333 \nHandling = 43.33333333333333 "
             "\nAcceleration = 75 \nTraction = 43.33333333333333"
             "\nReliability = 95% \nInitial body rigidity = 100% "
             "\nInitial Nos = 100% \nInitial fuel = 100%")
   go_on = input("\npress enter to continue. ")
# 9 -------------------------- Car 4 for easy difficulty ---------------------------------------------
   if go_on == "":
       print("\n2016 FIAT 500 Abarth")
       print("\nThis car has higher handling and traction but everything else is slightly lowered."
             "\nHaving higher handling and traction will help you to slow down and stop quicker, "
             "while also improving your maneuverability around obstacles.")

       print("\nSpeed = 37.5 \nHandling = 65 "
             "\nAcceleration = 37.5 \nTraction = 65"
             "\nReliability = 95% \nInitial body rigidity = 100% "
             "\nInitial Nos = 100% \nInitial fuel = 100%")
   go_on = input("\npress enter to continue. ")
# 10 -------------------------- car selection code ---------------------------------------------
   if go_on == "":
       car_choice_for_easy = input("\nType '1' for car number one, '2' for number two,"
                                   "\n'3' for number three, and '4' for number four. ")
       if car_choice_for_easy == "1":
           print("\nYou picked the 2016 Mazda Miata MX-5. "
                 "\n\nStats:")
           print("Speed: " + str(speed + 50))
           print("Handling: " + str(handling + 50))
           print("Acceleration: " + str(acceleration + 50))
           print("Traction: " + str(traction + 50))
           print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
           print("Initial fuel: " + str(fuel + 100) + "%")
           print("Initial Nos: " + str(nos + 100) + "%")
           game_play_easy()

       elif car_choice_for_easy == "2":
           print("\nYou picked the 2016 Chevrolet Corvette Z06. "
                 "\n\nStats:")
           print("Speed: " + str(speed + 75))
           print("Handling: " + str(handling + 43.33333333333333))
           print("Acceleration: " + str(acceleration + 43.33333333333333))
           print("Traction: " + str(traction + 43.33333333333333))
           print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
           print("Initial fuel: " + str(fuel + 100) + "%")
           print("Initial Nos: " + str(nos + 100) + "%")

       elif car_choice_for_easy == "3":
           print("\nYou picked the 2016 Ford Mustang Shelby GT350R. "
                 "\n\nStats:")
           print("Speed: " + str(speed + 43.33333333333333))
           print("Handling: " + str(handling + 43.33333333333333))
           print("Acceleration: " + str(acceleration + 75))
           print("Traction: " + str(traction + 43.33333333333333))
           print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
           print("Initial fuel: " + str(fuel + 100) + "%")
           print("Initial Nos: " + str(nos + 100) + "%")

       elif car_choice_for_easy == "4":
           print("\nYou picked the 2016 FIAT 500 Abarth. "
                 "\n\nStats:")
           print("Speed: " + str(speed + 37.5))
           print("Handling: " + str(handling + 65))
           print("Acceleration: " + str(acceleration + 37.5))
           print("Traction: " + str(traction + 65))
           print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
           print("Initial fuel: " + str(fuel + 100) + "%")
           print("Initial Nos: " + str(nos + 100) + "%")

# 11 ---------------------- If an invalid option was chosen ------------------------------------------

       else:
           while car_choice_for_easy != "1" or "2" or "3" or "4":
               try_again_for_easy = input("\nThat's an invalid choice, try again! ")
               if try_again_for_easy == "1":
                   print("\nYou picked the 2016 Mazda Miata MX-5. "
                         "\n\nStats:")
                   print("Speed: " + str(speed + 50))
                   print("Handling: " + str(handling + 50))
                   print("Acceleration: " + str(acceleration + 50))
                   print("Traction: " + str(traction + 50))
                   print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
                   print("Initial fuel: " + str(fuel + 100) + "%")
                   print("Initial Nos: " + str(nos + 100) + "%")
                   break
               elif try_again_for_easy == "2":
                   print("\nYou picked the 2016 Chevrolet Corvette Z06. "
                         "\n\nStats:")
                   print("Speed: " + str(speed + 75))
                   print("Handling: " + str(handling + 43.33333333333333))
                   print("Acceleration: " + str(acceleration + 43.33333333333333))
                   print("Traction: " + str(traction + 43.33333333333333))
                   print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
                   print("Initial fuel: " + str(fuel + 100) + "%")
                   print("Initial Nos: " + str(nos + 100) + "%")

                   break
               elif try_again_for_easy == "3":
                   print("\nYou picked the 2016 Ford Mustang Shelby GT350R. "
                         "\n\nStats:")
                   print("Speed: " + str(speed + 43.33333333333333))
                   print("Handling: " + str(handling + 43.33333333333333))
                   print("Acceleration: " + str(acceleration + 75))
                   print("Traction: " + str(traction + 43.33333333333333))
                   print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
                   print("Initial fuel: " + str(fuel + 100) + "%")
                   print("Initial Nos: " + str(nos + 100) + "%")
                   break
               elif try_again_for_easy == "4":
                   print("\nYou picked the 2016 FIAT 500 Abarth. "
                         "\n\nStats:")
                   print("Speed: " + str(speed + 37.5))
                   print("Handling: " + str(handling + 65))
                   print("Acceleration: " + str(acceleration + 37.5))
                   print("Traction: " + str(traction + 65))
                   print("Initial body rigidity: " + str(body_rigidity + 100) + "%")
                   print("Initial fuel: " + str(fuel + 100) + "%")
                   print("Initial Nos: " + str(nos + 100) + "%")
                   break
       game_play_easy()

# 12 --------------------------------- Game code for medium mode --------------------------------------


def medium_diff():
   print("\nHere is a $300,000, you can choose your first car.")
   print("\nThese are your choices:")

   print("\ncar one")
   print("\n")

   print("\nSpeed = 172.5 \nHandling = 172.5 \nAcceleration = 172.5 \nTraction = 172.5 "
         "\nReliability = 85% \nInitial body rigidity = 75%"
         "\nInitial Nos = 75% \nInitial fuel = 75% how though")

   print("\nCar two:")
   print("\nThis car has more speed but everything else is slightly lowered.")

   print("\nSpeed = 402 \nHandling = 102.6666666666666667 "
         "\nAcceleration = 102.6666666666666667 \nTraction = 102.6666666666666667"
         "\nReliability = 65% \nInitial body rigidity = 75% "
         "\nInitial Nos = 75% \nInitial fuel = 75%")

   print("\nCar three:")
   print("\nThis car has better acceleration but everything else is slightly lowered."
         "\nHaving higher acceleration will help you be able to get out of turns quicker")

   print("\nSpeed = 102.6666666666666667 \nHandling = 102.6666666666666667 "
         "\nAcceleration = 402 \nTraction = 102.6666666666666667"
         "\nReliability = 65% \nInitial body rigidity = 75% "
         "\nInitial Nos = 75% \nInitial fuel = 75%")

   print("\nCar four:")
   print("\nThis car has higher handling and traction but everything else is slightly lowered."
         "\nHaving higher handling and traction will help you be able to be faster on turns")

   print("\nSpeed = 154 \nHandling = 201 "
         "\nAcceleration = 201 \nTraction = 154"
         "\nReliability = 65% \nInitial body rigidity = 75% "
         "\nInitial Nos = 75% \nInitial fuel = 75%")

# 13 --------------------------------- Game code for hard mode --------------------------------------


def hard_diff():
   print("\nHere is $600,000, you can choose your first car.")
   print("\nThese are your choices:")

   print("\nCar one:")
   print()

   print("\nSpeed = 318.75 \nHandling = 318.75 \nAcceleration = 318.75 \nTraction = 318.75 "
         "\nReliability = 50% \nInitial body rigidity = 25%"
         "\nInitial Nos = 25% \nInitial fuel = 25%")

   print("\nCar two:")
   print("\nThis car has more speed but everything else is slightly lowered.")

   print("\nSpeed = 75 \nHandling = 43.33333333333333 "
         "\nAcceleration = 43.33333333333333 \nTraction = 43.33333333333333"
         "\nReliability = 95% \nInitial body rigidity = 100% "
         "\nInitial Nos = 100% \nInitial fuel = 100%")

   print("\nCar three:")
   print("\nThis car has better acceleration but everything else is slightly lowered."
         "\nHaving higher acceleration will help you be able to get out of turns quicker")

   print("\nSpeed = 43.33333333333333 \nHandling = 43.33333333333333 "
         "\nAcceleration = 75 \nTraction = 43.33333333333333"
         "\nReliability = 95% \nInitial body rigidity = 100% "
         "\nInitial Nos = 100% \nInitial fuel = 100%")

   print("\nCar four:")
   print("\nThis car has higher handling and traction but everything else is slightly lowered."
         "\nHaving higher handling and traction will help you be able to be faster on turns")

   print("\nSpeed = 37.5 \nHandling = 65 "
         "\nAcceleration = 37.5 \nTraction = 65"
         "\nReliability = 95% \nInitial body rigidity = 100% "
         "\nInitial Nos = 100% \nInitial fuel = 100%")


# 1 ----------------------------------- Main Menu -----------------------------------------------------
# 2 ------------------- Code will make sense if read from here first ----------------------------------

def main_game():
   done = False
   print()
   print("So " + user_name + ", you think you're ready for what it takes to become street king?")
   print()

   difficulty_lv = input("Go ahead and pick your difficulty level. Your choices are 'easy', 'medium' or 'hard'. ")

   if difficulty_lv.lower() == "easy":
       print()
       print("You chose easy, so it will be easy.")
       easy_diff()

   elif difficulty_lv.lower() == "medium":
       print()
       print("You chose the medium difficulty. This may give you bit more of a challenge.")
       medium_diff()

   elif difficulty_lv.lower() == "hard":
       print()
       print("You chose the hard difficulty. So you think you're an expert huh?.")
       hard_diff()

   else:
       while difficulty_lv != "easy" or "medium" or "hard":
           set_difficulty = input("\nThat's an invalid choice, if you want to quit the game, type 'exit'. Otherwise"
                                  "\nplease pick a difficulty. ")
           if set_difficulty.lower() == "exit":
               print()
               print("You've exited the game.")
               done = True
           elif set_difficulty.lower() == "easy" or "medium" or "hard":
               print()
               if set_difficulty == "easy":
                   print("You chose easy, so it will be easy.")
                   easy_diff()
               elif set_difficulty == "medium":
                   print()
                   print("You chose the medium difficulty. This may give you bit more of a challenge.")
                   medium_diff()
               elif set_difficulty == "hard":
                   print()
                   print("You chose the hard difficulty. So you think you're an expert huh?.")
                   hard_diff()


# 3 ----------------------------------- Game Intro -----------------------------------------------------
done = False
while not done:
   print()
   print("Welcome to Need for Speed Underground or NFS for short, "
         "here you can test your skills against other street racers, and "
         "build up your reputation to potentially become street king!\n")

   user_name = input("To begin, please enter your name. ")
   print()
   user_input = input("Welcome " + user_name + ", to NFS, to begin type 'start'. Otherwise type 'exit' to quit. ")

   if user_input.lower() == "start":
       main_game()
   elif user_input.lower() == "exit":
       print()
       print("You've exited the game.")
       done = True
   else:
       while user_input.lower() != "start" or "exit":
           try_again = input("\nThat's an invalid choice, if you want to quit the game, type 'exit'"
                             "\nand if you would like to continue type 'start'. ")
           if try_again.lower() == "start":
               main_game()
           elif try_again.lower() == "exit":
               print()
               print("You've exited the game.")
               done = True
               break

