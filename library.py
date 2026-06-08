def library_management_system():
    print("welcome to the library management system")
    a = (input("enter the name of book you want"))
    h = input("do you have a pending book to return? (yes/no)")
    if h.lower == "yes":
        print("please return the pending book before borrowing a new one")
    if h.lower=="no":
        print("ok, you can borrow the book",a)
        i=int(input("do you returning the book before 15 days (1 for yes, 0 for no)"))
        if i==1:
            print("thank you for returning the book on time")
        if i==0:
                print("you have to pay late fees of 10 ruppes per day after the due date")
        fine=int(input("enter the number of days you are late"))
        if fine>0:
                print("you have to pay",fine*10,"rupees as late fees")
        else:
                print("you have no late fees to pay please don't play with the system")
                print("you are ready to borrow the book",a)
    try:
        b=int(input("enter the number of books you want"))
        if b==3:
            print("you can borrow",b,"books")
        else:
            print("you can only borrow 3 books at a time")
    except:
        raise ValueError("please enter a valid number")
    print("the name of books you want is",a,"and the number of books you want is",b)

    try:
        c=int(input("enter you class"))
        if c<=5:
            print("you are eligible to borrow books")
        else:
            print("you are not eligible to borrow books")
    except:
        raise ValueError("please enter a valid class")
    try:
        d=int(input("enter the number of days you want to borrow the book"))
        if d<=15:
            print("you can borrow the book for",d,"days")
        else:
            print("you cannot borrow the book for more than 15 days")
    except:
        raise ValueError("please enter a valid number of days")

    e=input("enter your name")
    print("ok",e," so you want to borrow the book",a,"for",d,"days")

    try:
        f=int(input("enter your roll number"))
        if len(str(f))==4:
            print("your roll number is",f)
        else:
            print("please enter a valid roll number roll number is normally 4 digits")
    except:
        raise ValueError("please enter a valid integer roll number")

    print("thank you for using the library management system")
    print("have a nice day")
    print("return the book on time to avoid late fees")
    print("late fees are 10 rupees per day after the due date")
    print("if you have any questions please contact the library staff")
    print("goodbye")
library_management_system()
def start_again():
    g=input("do you want to borrow or return another book? (yes/no)")
    if g.lower()=="yes":
        print("ok, please start again")
        library_management_system()
    if g.lower()=="no":
        print("thank you for using the library management system")
        print("return the book after 15 days")
start_again()