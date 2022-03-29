
def countDayOfTheWeek():
    # This first line is provided for you

    weekdays = dict() 

    file_name = input("Enter a file name: ")
    try:
        file_handle = open(file_name)
    except:
        print("Please enter a valid file.")
        exit()
    
    for line in file_handle:
        words = line.split()
        if len(words) <3 or words[0] != 'From':
            continue
        else:
            if words[2] not in weekdays:
                weekdays[words[2]] = 1
            else:
                weekdays[words[2]] += 1
    
    print (weekdays)
        # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#countDayOfTheWeek()