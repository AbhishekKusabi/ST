def nextDate(month, day, year):
    if month == 2:
        if day < 28:
            return month, day + 1, year
        elif day == 28:
            if year % 4 == 0:
                return month, day + 1, year
            else:
                return 3, 1, year
        else:
            return 3, day, year
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day < 30:
            return month, day + 1, year
        else:
            return month + 1, 1, year
    else:
        if day < 31:
            return month, day + 1, year
        else:
            if month == 12:
                return 1, 1, year + 1
            else:
                return month + 1, 1, year
            
def main():
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    
    month, day, year = nextDate(month, day, year)
    print("Next date: ", day, "/", month, "/", year)
    
if __name__ == "__main__":
    main()