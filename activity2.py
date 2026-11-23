hour=int(input("Enter the hour of the day in 24-hour format: "))
terminal=int(input("Enter the  terminal number: "))
if 9<=hour<=16 and terminal<50:
    print("Connection Allowed")
else:
    print("Session Rejected ")