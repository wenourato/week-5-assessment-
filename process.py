#this command is opening a .txt file.  you can also use this command to open .csv files!

log_file = open("um-server-01.txt")

#this is  a function in plthon.  the def keyword is the function declaration
def sales_reports(log_file):
    for line in log_file:   #this is a python for loop. it is looping over the lines in the .txt file 
        line = line.rstrip()  #rstip is a command to take out certtain characters
        day = line[0:3]  #this is identifying the index of the text list 
        if day == "Tue":  # this is a python if statement.  in python, we only use 2 equal signs, and must capitolize the first letter of the boolean statement 
            print(line)  #pring, is the console log of python.  in this block, (since it is indented and not part of the function,) will execute the line variable


sales_reports(log_file)  #this is reassigning the variable name 
