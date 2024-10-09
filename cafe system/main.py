dic={
    "pasta":60,"pizza":120,"chawmin":60,"burger":50,"coffee":30,"tea":20,"smoothie":90
}
print("Our menu:")
print("pasta:60\npizza:120\nchawmin:60\nburger:50\ncoffee:30\ntea:20\nsmoothie:90")
amount=0
print("Welcome! to our cafe ")
item=input("what would you like to order: ")
if item in dic:
    print(f"your {item} is added")
    amount+=dic[item]
    
else:
    print(f"{item} is not available yet") 
     
flag=True    
while flag ==True:    
 another_order=input("Do you want to add another item  {yes/no only}") 
 if another_order=="yes":
    item2=input("what would you like to order: ")
    if item2 in dic:
        print(f"your {item2} is added")
        amount+=dic[item2]
    else:
       print(f"{item} is not available yet")  

 else:
    print("your total is:",amount) 
    flag==False 
    break

print("Thanks for ordering sir ")
      