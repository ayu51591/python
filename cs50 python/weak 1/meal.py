def main():

    time = input("Enter the time in 24-hour format (7:30 or 12:00): ")
    
    hours_float = convert(time)
    
    if 7.0 <= hours_float <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= hours_float <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= hours_float <= 19.0:
        print("It's dinner time!")
    else:
        pass

def convert(time):
    hours, minutes = map(int, time.split(':'))
    
    total_hours = hours + minutes / 60.0
    
    return total_hours

if __name__ == "__main__":
    main()