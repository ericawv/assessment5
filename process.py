

#  Opens the 'um-server-01.txt' file by declaring the log_file variable and assigning it to the open function that passes in the um-server-01.txt parameter. 
log_file = open("um-server-01.txt") 

# Using the 'def' keyword to define the 'sales_report' function and that passes the log_file variable as a paramenter for the 'um-server-01.txt' file.
def sales_reports(log_file):
     
# Using the 'for' keyword to loop through each line of the um-server-01.txt file. 
        for line in log_file:   
# Using the dot notation to and the rstrip function to remove the trailing characters and whitespace on the right-side in each line of the um-server-01.txt file.
            line = line.rstrip()
# Assigning day to the first [0] through fourth [3] places (or the first through fourth columns) in each line of the um-server-01.txt file.
            day = line[0:3]
# Using an if-statement to determine if any line in the um-server-01.txt file equals (or has) has a "Tues" (represents Tuesday) stated. Changed "Tues" to "Mon" to determine if any line in the um-server-01.txt file equals (or has) has a "Tues" (represents Tuesday) stated.
            if day == "Mon":
# Using the print function to print the entire line (includes the first through fourth columns) of each line in  the um-server-01.txt file that states "Tues" (initally). 
                print(line)


#Invoking the "sales_reports" function to pass the log_file variable to return the output values of the um-server-01.txt file. 
sales_reports(log_file)
