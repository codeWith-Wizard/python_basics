# hindi to english dictionary 
hindi_dict ={
            "chor" : "thief",
            "bakri" : "sheep",
            "kitab" : "book",
            "mej" : "table",
            "pakshi" : "bird",
            "udna" : "fly",
            }

hindi_keys = list(hindi_dict.keys());
counter = 1;
choice = -1; #random value

for i in hindi_keys:
    print(i," : ",counter)
    counter +=1

choice = int(input("\nplease enter choosen choice : "));

selected_key = hindi_keys[choice-1];
english_value = hindi_dict.get(selected_key);
print(selected_key," : ", english_value);
