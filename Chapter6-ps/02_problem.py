subject_marks = {
    "chemistry" : 0,
    "mathematics" : 0,
    "physics" : 0
}

subjects = list(subject_marks.keys());

for sub in subjects:
    marks = int(input(f"enter {sub} marks : "))
    subject_marks.update({sub : marks})

chem_marks = subject_marks.get("chemistry");
phy_marks = subject_marks.get("physics");
math_marks = subject_marks.get("mathematics");

sum_marks = chem_marks + phy_marks + math_marks;

avg = float(sum_marks/3)

if (sum_marks >= 40):
    if(chem_marks > 33 and phy_marks > 33 and math_marks > 33 ):
        print("Congrats, passed with ", avg , "% !!" )
    else:
        print("You failed to pass the minimum passing criteria !!", avg ,"% !!")

else:
    print("Failed !! ",avg ,"%")

                                                                                                                            

