import random

def decide(user,computer) :
  if((user=="p" and computer=="r")or(user=="s" and computer=="p")or(user=="r" and computer=="s")) :
    return 0
  elif((computer=="p" and user=="r")or(computer=="s" and user=="p")or(computer=="r" and user=="s")) :
    return 1
  else :
    return -1

def start_game() :
  computer_score=0
  user_score=0
  t=1
  while(1) :
      possibilities=["r","p","s"]
      print("\nEnter you choice :\nr for rock\np for paper\ns for scissor\n")
      user_choice=input()
      computer_choice=random.choice(possibilities)
      print("\nYou : ",user_choice,"\nComputer : ",computer_choice,"\n")
      if(decide(user_choice,computer_choice)==1) :
          print("\nComputer got one point\n")
          computer_score+=1
      elif(decide(user_choice,computer_choice)==0) :
          user_score+=1
          print("\nYou got one point\n")
      else :
          print("\nNobody won in this round\n")
          pass
      print("\nYour score : ",user_score,"\nComputer score : ",computer_score,"\n")
      print("\n",t,"Round completed\n-----------------------------------------------------------\n")
      t+=1
      print("\nIf you want to play again enter yes Else enter no :\n")
      ch=input()
      if(ch=="no") :
        break

  print("\n****************************************************\nYour score :",user_score,"\nComputer score :",computer_score,"\n")
  if (user_score > computer_score) :
      print("Hey ! You won the game\n**************************************\n")
  elif(computer_score > user_score) :
      print("Sorry! You lost the game\n*******************************\n")
  else :
      print("It is a draw\n******************************************\n")

start_game()