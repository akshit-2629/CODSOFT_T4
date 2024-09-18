import random 
zzz = int(input("choose 0 for rock /n choose 1 for scissors /n choose 2 for paper :"))

if zzz == 0:
    print("""_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
elif zzz == 1 :
 print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___))  
      """) 
 
else :
   print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")






print("computer choice: ")
randomzz= random.randint(0,2)

if randomzz == 0:
    print("""_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
elif randomzz == 1 :
 print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___))  
      """) 
 
else :
   print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

if zzz == 0 and randomzz == 1 :
  print("you won bro ")

elif zzz == 1 and randomzz == 2 : 
   print("you won bro ")


elif zzz == 2 and randomzz == 0 :
   print("you won bro ")

elif zzz == randomzz :
   print("come on...lets play again")
else :
   print("you lose")   