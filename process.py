log_file = open("um-server-01.txt") # Opens the 'um-server-01.txt' file.


def sales_reports(log_file): # Defining the 'sales_report' function for the 'um-server-01.txt' file.
    for line in log_file:    #   
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)
