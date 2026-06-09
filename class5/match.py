
# role = "admin";
role = input("Enter your role (admin/user/guest):")

match role:
    case "admin":
        print("Your role is admin")
    case "user":
        print("Your role is user")
    case "guest":
        print("Your role is guest")
    case _:  # Default case if none of the above cases match
        print("Your role is unknown")


day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today  is a Weekday",day)
    case 6 | 7:
        print("I Love weekends!", day)
    case _:
        print("Invalid day")