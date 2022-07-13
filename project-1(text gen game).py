print("               WELCOME TO MY FIRST GAME !         ")
print("    ")
name=input("What is your name :")
age=int(input("What is your Age:"))
print("\nhello",name,"you are",age,"years old.")

health=10
print("\nyou are starting with health :",health)
if age >=18:
    print("you are old enough!")

    wants_to_play=input("\nDo you want to play? (yes/no)").lower()

    if wants_to_play =="yes":
      print("let's play!")
      left_or_right=input("\nFrist choice... left or right (left/right)?")
      if left_or_right == "left" :
          ans = input("\nNice,you follow the path and reach a lake...Do you swim across or go around (across/around)?")
          if ans == "around":
              print(" you went around and reached the other side of the lake and stucked")
          elif ans == "across":
              print("you managed to get across,but were bit by a fish and lost 5 health.")
              health -= 5
              ans1=input("\nyou notice a house and a river. which do you go to (river/house)?")
              if ans1 == "house":
                  print("you go to the house and are greted by the owner...he dosen't like you and you lose 5 health")
                  health -=5
                  if health <= 0:
                      print("you have no health and you lost the game...")
                  else:
                      print("you have survived...")
              elif ans1 == "river":
                  print("you choose the crt path ")
              else:
                  print("you down and lost....")
          else:
              print("You lost...")
      else:
          print("you fell down and lost....")    
    else:
      print("bye......")
else :
   print("you are not old enough to play the GAME!")
  



