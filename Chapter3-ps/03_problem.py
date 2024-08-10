#program to detect double spaces in the program and replace them
input_sample = input("enter the input sample : ");
doubleSpaces = input_sample.count("  ");
print("Double spaces :  ", doubleSpaces);
updated_sample = input_sample.replace("  ", " ");
print("updated sample : ", updated_sample);
