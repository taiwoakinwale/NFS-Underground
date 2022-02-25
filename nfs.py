# Lab 4
# CS 20
# John and Taiwo
# ------------------------------------- Beginning of code --------------------------------------------------
import random
# 13 ---------------------- This is where the game will actually start playing ----------------------------
# 14 ----------------------------------------- easy mode --------------------------------------------------


def helping_tips():
   the_helping_tips = random.randrange(1, 11)
   if the_helping_tips == 1:
       print("\nPro Tip: You should check your status so you can check for things like your engine temperature!")
   elif the_helping_tips == 2:
       print("\nPro Tip: Nos is Nitrous oxide, it makes you go faster, but is also "
             "\nflammable and explosive. So be careful how you use it!")
   elif the_helping_tips == 3:
       print("\nPro Tip: Don't forget that you're not just trying to stay ahead of the cops,"
             "you are also trying to beat the other racers!")
   elif the_helping_tips == 4:
       print("\nPro Tip: The other racers specific distances covered in a turn aren't shown, but if you "
             "if you check your status it will show whether or not you traveled further than them!")
   elif the_helping_tips == 5:
       print("\nPro Tip: Don't use slow pace as your first move, you are very likely to get caught!")
   elif the_helping_tips == 6:
       print("\nPro Tip: ")
   elif the_helping_tips == 7:
       print("\nPro Tip:")
   elif the_helping_tips == 8:
       print("\nPro Tip:")
   elif the_helping_tips == 9:
       print("\nPro Tip:")
   elif the_helping_tips == 10:
       print("\nPro Tip:")
# --------------------------------------------------------------------------------------------------------


def game_play_easy():
   finished = False
   while not finished:
       engine_heat = 90
       nos = 100
       fuel = 100
       total_distance_covered = 0
       distance_left = 100
       racers_distance = 0
       racers_total = 0
       cops = -5
       distance_covered = 0
       print("\nThe race is about to start!")
       input("\nPress enter to continue. ")
       print("\nThe instructions:"
             "\n1. Inject fuel to raise your fuel level"
             "\n   (This will slow you down.)"
             "\n2. Activate Nos to increase your speed dramatically."
             "\n   (This will decrease your Nos and fuel level)"
             "\n3. Slow pace"
             "\n   (This doesn't burn very much fuel.)"
             "\n4. Moderate pace"
             "\n   (This burns a moderate amount of fuel.)"
             "\n5. Push the pace"
             "\n   (This burns a greater amount of fuel.)"
             "\n6. Stop"
             "\n   (This will allow you to stop to let your engine to cool down. "
             "\n7. Status"
             "\n   (This is to check your current status"
             "\n8.  Quit"
             "\n   (This is to exit the game)")
       print()
       helping_tips()
       input("\npress enter to continue. ")
       start_engine = input("\nStart your engine! "
                            "\n\npress 'e' to start your engine ")
       if start_engine.lower() == "e":
           print("\n3, 2, 1, GO!!!")
       else:
           while start_engine.lower() != "e":
               print("\nYou pressed the wrong button.")
               why_not_try_again = input("\nTry Again! ")
               if why_not_try_again.lower() == "e":
                   print("\n3, 2, 1, GO!!!")
                   break
       finished = False
       while not finished:
           user_choice = (input("\n1. Inject fuel"
                                "\n2. Activate Nos"
                                "\n3. Slow pace"
                                "\n4. Moderate pace"
                                "\n5. Push the pace"
                                "\n6. Stop"
                                "\n7. Status"
                                "\n8. Quit "
                                "\n\nYour choice: "))
           # 1 ----------------------------------------- Inject Fuel ----------------------------------------------
           if user_choice == "1":
               if fuel < 100:
                   fuel += random.randrange(5, 11)
                   distance_covered = random.randrange(1, 3)
                   total_distance_covered += distance_covered
                   engine_heat -= random.randrange(1, 6)
                   cops += random.randrange(2, 5)
                   racers_distance = random.randrange(2, 7)
                   racers_total += racers_distance
                   distance_left -= distance_covered
                   if cops >= total_distance_covered:
                       print("\nThe cops have caught up to you!"
                             "\nYou lose.")
                       finished = True
                       break
                   elif distance_left <= 0:
                       print("\nYOU WON!!!")
                       finished = True
                       break
                   print("\nYou injected fuel, your fuel level is now at " + str(fuel) + "% and you covered "
                         + str(distance_covered) + "km.")
                   if fuel <= 0:
                       print("\nYou ran out of fuel!"
                             "\nYou lose.")
                       print(str(total_distance_covered) + "km")
                       finished = True
                       break
                   elif racers_total >= 100:
                       print("The other racers have gotten to the finish line before you."
                             "\nYou lose.")
                       finished = True
                       break
               elif fuel >= 100:
                   print("\nYou tried to inject fuel, but your fuel level is already filled up! ")
           # 2 ----------------------------------------- Activate Nos ----------------------------------------------
           elif user_choice == "2":
               if nos > 0:
                   nos -= random.randrange(10, 16)
                   if nos < 0:
                       nos = 0
                   distance_covered = random.randrange(11, 16)
                   total_distance_covered += distance_covered
                   engine_heat += random.randrange(10, 16)
                   cops -= random.randrange(5, 11)
                   racers_distance = random.randrange(2, 7)
                   racers_total += racers_distance
                   distance_left -= distance_covered
                   fuel -= random.randrange(11, 16)
                   print("\nYou have activated your Nos and push the car to the limit, your nos level "
                         "has reduced to " + str(nos) + "% and you have covered " + str(distance_covered)
                         + "km.")
                   if cops >= total_distance_covered:
                       print("\nThe cops have caught up to you!"
                             "\nYou lose.")
                       finished = True
                       break
                   elif distance_left <= 0:
                       print("\nYOU WON!!!")
                       finished = True
                       break
                   elif fuel <= 0:
                       print("\nYou ran out of fuel!"
                             "\nYou lose.")
                       print(str(total_distance_covered) + "km")
                       finished = True
                       break
                   elif engine_heat >= 150:
                       print("\nYour engine overheated!"
                             "\nYou lose.")
                       finished = True
                       break
                   elif engine_heat >= 130:
                       if engine_heat < 150:
                           print("Your engine temperature is high be careful not to have it overheat.")
                   elif racers_total >= 100:
                       print("The other racers have gotten to the finish line before you."
                             "\nYou lose.")
                       finished = True
                       break
               else:
                   print("\nYou have ran out of Nos, this option, is no longer available.")
           # 3 ----------------------------------------- Slow Pace ----------------------------------------------
           elif user_choice == "3":
               distance_covered = random.randrange(1, 3)
               total_distance_covered += distance_covered
               engine_heat += random.randrange(1, 4)
               cops += random.randrange(3, 6)
               racers_distance = random.randrange(2, 7)
               racers_total += racers_distance
               distance_left -= distance_covered
               fuel -= random.randrange(1, 5)
               print("\nYou go at a slow pace covering " + str(distance_covered) + "km.")
               if cops >= total_distance_covered:
                   print("\nThe cops have caught up to you!"
                         "\nYou lose.")
                   finished = True
                   break
               elif distance_left <= 0:
                   print("\nYOU WON!!!")
                   finished = True
                   break
               elif fuel <= 0:
                   print("\nYou ran out of fuel!"
                         "\nYou lose.")
                   print(str(total_distance_covered) + "km")
                   finished = True
                   break
               elif engine_heat >= 150:
                   print("\nYour engine overheated!"
                         "\nYou lose.")
                   finished = True
                   break
               elif engine_heat >= 130:
                   if engine_heat < 150:
                       print("Your engine temperature is high be careful not to have it overheat.")
               elif racers_total >= 100:
                   print("The other racers have gotten to the finish line before you."
                         "\nYou lose.")
                   finished = True
                   break
           # 4 ----------------------------------------- Moderate Pace ----------------------------------------------
           elif user_choice == "4":
               distance_covered = random.randrange(3, 7)
               total_distance_covered += distance_covered
               engine_heat += random.randrange(4, 7)
               cops += random.randrange(1)
               racers_distance = random.randrange(2, 7)
               racers_total += racers_distance
               distance_left -= distance_covered
               fuel -= random.randrange(5, 9)
               print("\nYou go at a normal pace covering " + str(distance_covered) + "km.")
               if cops >= total_distance_covered:
                   print("\nThe cops have caught up to you!"
                         "\nYou lose.")
                   finished = True
                   break
               elif distance_left <= 0:
                   print("\nYOU WON!!!")
                   finished = True
                   break
               elif fuel <= 0:
                   print("\nYou ran out of fuel!"
                         "\nYou lose.")
                   print(str(total_distance_covered) + "km")
                   finished = True
                   break
               elif engine_heat >= 150:
                   print("\nYour engine overheated!"
                         "\nYou lose.")
                   finished = True
                   break
               elif engine_heat >= 130:
                   if engine_heat < 150:
                       print("Your engine temperature is high be careful not to have it overheat.")
               elif racers_total >= 100:
                   print("The other racers have gotten to the finish line before you."
                         "\nYou lose.")
                   finished = True
                   break
           # 5 ----------------------------------------- Push The Pace ----------------------------------------------
           elif user_choice == "5":
               distance_covered = random.randrange(6, 13)
               total_distance_covered += distance_covered
               engine_heat += random.randrange(7, 11)
               cops -= random.randrange(1, 3)
               racers_distance = random.randrange(2, 7)
               racers_total += racers_distance
               distance_left -= distance_covered
               fuel -= random.randrange(9, 12)
               print("\nYou push the pace and cover " + str(distance_covered) + "km.")
               if cops >= total_distance_covered:
                   print("\nThe cops have caught up to you!"
                         "\nYou lose.")
                   finished = True
                   break
               elif distance_left <= 0:
                   print("\nYOU WON!!!")
                   finished = True
                   break
               elif fuel <= 0:
                   print("\nYou ran out of fuel!"
                         "\nYou lose.")
                   print(str(total_distance_covered) + "km")
                   finished = True
                   break
               elif engine_heat >= 150:
                   print("\nYour engine overheated!"
                         "\n You lose.")
                   finished = True
                   break
               elif engine_heat >= 130:
                   if engine_heat < 150:
                       print("Your engine temperature is high be careful not to have it overheat.")
               elif racers_total >= 100:
                   print("The other racers have gotten to the finish line before you."
                         "\nYou lose.")
                   finished = True
                   break
           # 6 ----------------------------------------- Stop ----------------------------------------------
           elif user_choice == "6":
               cops += random.randrange(4, 9)
               racers_distance = random.randrange(2, 7)
               racers_total += racers_distance
               engine_heat -= random.randrange(10, 16)
               print("\nYou stop and your engine cools down to " + str(engine_heat) + "°C.")
               if racers_total >= 100:
                   print("The other racers have gotten to the finish line before you."
                         "\nYou lose.")
                   finished = True
                   break
               elif cops >= total_distance_covered:
                   print("\nThe cops have caught up to you!"
                         "\nYou lose.")
                   finished = True
           # 7 ----------------------------------------- Status ----------------------------------------------
           elif user_choice == "7":
               helping_tips()
               print("\nNos: " + str(nos) + "% "
                     "\nFuel: " + str(fuel) + "% "
                     "\nDistance covered: " + str(total_distance_covered) + "km "
                     "\nDistance left: " + str(distance_left) + "km "
                     "\nOther racers distance from you: " + str(racers_total - total_distance_covered) + "km "
                     "\nEngine heat: " + str(engine_heat) + "°C")
               print("\nThis is how far you went on your last turn driving " + str(distance_covered) + "km ")
               if distance_covered == racers_distance:
                   print("and the other racers also covered the same distance in the last turn.")
               elif distance_covered <= racers_distance:
                   print("and the other racers also travelled a greater distance than you.")
               elif distance_covered >= racers_distance:
                   print(" and you covered a greater distance than the other racers.")
           # 8 ----------------------------------------- Exit The Game ----------------------------------------------
           elif user_choice == "8":
               print("\nYou have exited the game.")
               finished = True
               break
           # ----------------------------------------- If Invalid Choice ----------------------------------------------
           else:
               print("\nInvalid choice, try again!")
       return finished
   return finished
# 15 ----------------------------------------- medium mode ----------------------------------------------


"""def game_play_medium():
   track_size = 100
   your_current_location = 0
   lots = input("1")
   if lots == "1":
       track_size -= 50
       your_current_location += 50
   print("you have this many km left:" + str(track_size))
   print("you have traveled this far:" + str(your_current_location))
"""

# 16 ----------------------------------------- hard mode ------------------------------------------------


"""def game_play_hard():
   track_size = 100
   your_current_location = 0
   lots = input("1")
   if lots == "1":
       track_size -= 50
       your_current_location += 50
   print("you have this many km left:" + str(track_size))
   print("you have traveled this far:" + str(your_current_location))
"""

# 4 --------------------------- Game code for easy mode ---------------------------------------------


def easy_diff():
   speed = 0
   handling = 0
   acceleration = 0
   traction = 0
   body_rigidity = 0
   nos = 0
   fuel = 0

   input("\npress enter to continue. ")
   print("\nYour game is loading...")
   helping_tips()
   print("\nHere is a $100,000, you can choose your first car.")
   print("\nThese are your choices:")

# 5 ------------------------------------- Types of cars ----------------------------------------------
# 6 -------------------------- Car 1 for easy difficulty ---------------------------------------------
   input("\npress enter to continue. ")
   print("\n2016 Mazda Miata MX-5")
   print("\nThis car is very balanced and you should probably use it to get a feel for the game "
         "\nif you are a beginner. "
         "This car is only meant for true beginners!")

   print("\nSpeed = 50 \nHandling = 50 \nAcceleration = 50 \nTraction = 50 "
         "\nReliability = 100% \nInitial body rigidity = 100%"
         "\nInitial Nos = 100% \nInitial fuel = 100%")
   input("\npress enter to continue. ")
# 7 -------------------------- Car 2 for easy difficulty ---------------------------------------------
   print("\n2016 Chevrolet Corvette Z06")
   print("\nThis car has more speed but everything else is slightly lowered."
         "\nDriving on straights with this car will make you go much faster "
         "\nthan other racers and help you reach"
         "\nthe finish line quicker.")

   print("\nSpeed = 75 \nHandling = 43.33333333333333 "
         "\nAcceleration = 43.33333333333333 \nTraction = 43.33333333333333"
         "\nReliability = 95% \nInitial body rigidity = 100% "
         "\nInitial Nos = 100% \nInitial fuel = 100%")
# 8 -------------------------- Car 3 for easy difficulty ---------------------------------------------
   input("\npress enter to continue. ")
   print("\n2016 Ford Mustang Shelby GT350R.")
   print("\nThis car has better acceleration but everything else is slightly lowered."
         "\nHaving higher acceleration will help you to get an explosive start off faster, "
         "\nand get out of turns quicker.")

   print("\nSpeed = 43.33333333333333 \nHandling = 43.33333333333333 "
         "\nAcceleration = 75 \nTraction = 43.33333333333333"
         "\nReliability = 95% \nInitial body rigidity = 100% "
         "\nInitial Nos = 100% \nInitial fuel = 100%")
# 9 -------------------------- Car 4 for easy difficulty ---------------------------------------------
   input("\npress enter to continue. ")
   print("\n2016 FIAT 500 Abarth")
   print("\nThis car has higher handling and traction but everything else is slightly lowered."
         "\nHaving higher handling and traction will help you to slow down and stop quicker, "
         "\nwhile also improving your maneuverability around obstacles.")

   print("\nSpeed = 37.5 \nHandling = 65 "
         "\nAcceleration = 37.5 \nTraction = 65"
         "\nReliability = 95% \nInitial body rigidity = 100% "
         "\nInitial Nos = 100% \nInitial fuel = 100%")
# 10 -------------------------- car selection code ---------------------------------------------
   input("\npress enter to continue. ")
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
   return game_play_easy()

# 12 --------------------------------- Game code for medium mode --------------------------------------


"""def medium_diff():
   print("\nHere is a $300,000, you can choose your first car.")
   print("\nThese are your choices:")

   print("\ncar one")
   print()
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
         "\nInitial Nos = 75% \nInitial fuel = 75%")"""

# 13 --------------------------------- Game code for hard mode --------------------------------------


"""def hard_diff():
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
         "\nInitial Nos = 100% \nInitial fuel = 100%")"""


# 3 ----------------------------------- Main Menu -----------------------------------------------------
def main_game():
   finished = False
   while not finished:
       print()
       print("So " + user_name + ", you think you're ready for what it takes to become street king?")
       print()

       difficulty_lv = input("Go ahead and pick your difficulty level. Your choices are 'easy',"
                             " 'medium(Coming soon)' or"
                             " 'hard'(Coming soon). ")

       if difficulty_lv.lower() == "easy":
           print()
           print("You chose easy, so it will be easy.")
           finished = easy_diff()

       elif difficulty_lv.lower() == "medium":
           print()
           print("This mode isn't available right now, please enjoy the easy mode for now.")
           player_choice = input("\npress 'e' for easy mode or type 'exit' to quit. ")
           if player_choice.lower() == "exit":
               print()
               print("You have exited the game.")
               finished = True
           elif player_choice.lower() == "e":
               easy_diff()
           else:
               while player_choice.lower() != "e" or "exit":
                   player_choice = input("\nThat's an invalid choice, try again. ")
                   if player_choice == "e":
                       easy_diff()
                   elif player_choice == "exit":
                       print("\nYou have exited the game.")
                       finished = True
                       break
           # print("You chose the medium difficulty. This may give you bit more of a challenge.")
           # medium_diff()

       elif difficulty_lv.lower() == "hard":
           print()
           print("This mode isn't available right now, please enjoy the easy mode for now.")
           player_choice = input("\nPress 'e' for easy mode or type 'exit' to quit. ")
           if player_choice.lower() == "e":
               easy_diff()
           elif player_choice.lower() == "exit":
               print()
               print("You have exited the game.")
               finished = True
           else:
               while player_choice.lower() != "e" or "exit":
                   player_choice = input("\nThat's an invalid choice, try again. ")
                   if player_choice == "e":
                       easy_diff()
                   elif player_choice == "exit":
                       print("\nYou have exited the game.")
                       finished = True
                       break
           # print("You chose the hard difficulty. So you think you're an expert huh?.")
           # hard_diff()

       else:
           while difficulty_lv != "easy" or "medium" or "hard" or "exit":
               difficulty_lv = input("\nThat's an invalid choice, if you want to quit the game,"
                                     " type 'exit'. \nOtherwise"
                                     "please pick a difficulty. ")
               if difficulty_lv.lower() == "exit":
                   print()
                   print("You've exited the game.")
                   finished = True
                   break
               elif difficulty_lv.lower() == "easy" or "medium" or "hard":
                   if difficulty_lv == "easy":
                       print()
                       print("You chose easy, so it will be easy.")
                       easy_diff()
                   elif difficulty_lv == "medium":
                       print()
                       print("This mode isn't available right now, please enjoy the easy mode for now.")
                       player_choice = input("\npress 'e' for easy mode or type 'exit' to quit. ")
                       if player_choice.lower() == "e":
                           easy_diff()
                       elif player_choice.lower() == "exit":
                           print("\nYou have exited the game.")
                           finished = True
                           break
                       # print("You chose the medium difficulty. This may give you bit more of a challenge.")
                       # medium_diff()
                   elif difficulty_lv == "hard":
                       print()
                       print("This mode isn't available right now, please enjoy the easy mode for now.")
                       player_choice = input("\npress 'e' for easy mode or type 'exit' to quit. ")
                       if player_choice.lower() == "e":
                           easy_diff()
                       elif player_choice.lower() == "exit":
                           print()
                           print("You have exited the game.")
                           finished = True
                           break
                       else:
                           while player_choice.lower() != "e" or "exit":
                               player_choice = input("\nThat's an invalid choice, try again. ")
                               if player_choice == "e":
                                   easy_diff()
                               elif player_choice == "exit":
                                   print("\nYou have exited the game.")
                                   finished = True
                                   break
                       # print("You chose the hard difficulty. So you think you're an expert huh?.")
                       # hard_diff()
   return finished
# 1 ----------------------------------- Main Menu -----------------------------------------------------
# 2 ------------------- Code will make sense if read from here first ----------------------------------


done = False
while not done:
   print()
   print("Welcome to Need for Speed Underground or NFS for short, "
         "here you can test your skills against other street racers, and "
         "build up your reputation to potentially become street king!")
   user_name = input("\nTo begin, please enter your name. ")

   user_input = input("\nWelcome " + user_name + ", to NFS, to begin type 'start'. Otherwise type 'exit' to quit. ")
   if user_input.lower() == "start":
       done = main_game()
   elif user_input.lower() == "exit":
       print()
       print("You've exited the game.")
       done = True
   else:
       while user_input.lower() != "start" or "exit":
           user_input = input("\nThat's an invalid choice, if you want to quit the game, type 'exit'"
                              "\nand if you would like to continue type 'start'. ")
           if user_input.lower() == "start":
               done = main_game()
           elif user_input.lower() == "exit":
               print("\nYou've exited the game.")
               done = True
               break
