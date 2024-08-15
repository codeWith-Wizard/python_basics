#basic menu type question for adding names and their languages

friends = {}

for i in range(4):
    name = input("enter your name : ")
    lang = input("enter your fav. language : ")
    friends.update({name : lang})

print(friends);
