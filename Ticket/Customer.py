from datetime import date, time, datetime, timedelta
import Event
import Administrator_user
import Types_ticket


def type_event():
    """
    This method is executed if type event == security
    :return: True / False
    """
    list_n_c = []  # ----> List of national code of participants
    national_code = int(input("please enter your national_code :"))
    while not Administrator_user.Administrator_user.check_national_code(national_code):
        national_code = int(input("The national_Code is incorrect, Must be 10 digits. please enter again :"))
    if national_code is not list_n_c:
        list_n_c.append(national_code)
        print("welcome")
        return True
    else:
        print("A user has already registered with this national code")
        return False


def date_registration():
    """
    display Date and time of user registration user
    """
    now = datetime.now()
    if Types_ticket.time_comparison(now, Event.Event.add_event()[4], Event.Event.add_event()[3]):
        return now
    else:
        print(" Registration deadline has expired .")
        return False


# if methode ⬆ False methode ⬇ not done

def num_ticket():
    if Event.Event.add_event()[5] == 'security':
        number_ticket = 1
    else:
        number_ticket = int(input("How many tickets do you want ? "))
        while not Event.Event.check_capacity(Event.Event.add_event()[2], number_ticket):
            a = input("Are you still interested in registering for the event? yes/no")
            if a == 'yes':
                number_ticket = int(input("Re-enter the number of tickets you requested : "))
            elif a == 'no':
                number_ticket = 0
                break
        Event.Event.add_event()[2] -= number_ticket
    return number_ticket


# if methode ⬆ number_ticket = 0 methode ⬇ not done


def type_ticket():
    """
    1 ---> display types tickets
    2 ---> Select the type of ticket
    3 ---> display payable for the customer.
    """
    print("welcome ! Choose your ticket type ")
    menu01 = input("""\n1.Normal\n2.vip\n3.Student\n4.Cultural\n5.Last Moment\n What is your choice? """)
    if menu01 == '1':
        s_d_d = [Types_ticket.special_days()[1][i] for i in range(len(Types_ticket.special_days()[0]))
                 if Types_ticket.special_days()[0][i] == date_registration()]
        # s_d_d is ----> Special day discount
        if s_d_d:
            pay = Types_ticket.Specify_ticket()[0] - Types_ticket.Specify_ticket()[0] * s_d_d[0] / 100
            print(f"You have a special day discount. You have to pay {pay} $ for {num_ticket()} tickets")
            return pay
        else:
            print(f"You have to pay {Types_ticket.Specify_ticket()[0]} $ for {num_ticket()} tickets")
            return Types_ticket.Specify_ticket()[0]
    elif menu01 == '2':
        if Types_ticket.Specify_ticket()[1] is not None:
            s_d_d = [Types_ticket.special_days()[1][i] for i in range(len(Types_ticket.special_days()[0]))
                     if Types_ticket.special_days()[0][i] == date_registration()]
            if s_d_d:
                pay = Types_ticket.Specify_ticket()[1] - Types_ticket.Specify_ticket()[1] * s_d_d[0] / 100
                print(f"You have a special day discount. You have to pay {pay} $ for {num_ticket()} tickets")
                return pay
            else:
                print(f"You have to pay {Types_ticket.Specify_ticket()[1]} $ for {num_ticket()} tickets")
                return Types_ticket.Specify_ticket()[1]
        else:
            print("Sorry, this ticket does not exist !")
    elif menu01 == '3':
        if Types_ticket.Specify_ticket()[2] is not None:
            for i in range(1, 4):
                Code_Special = input("Enter the special code for this ticket :")
                if Code_Special == Types_ticket.Specify_ticket()[3]:
                    s_d_d = [Types_ticket.special_days()[1][i] for i in range(len(Types_ticket.special_days()[0]))
                             if Types_ticket.special_days()[0][i] == date_registration()]
                    if s_d_d:
                        pay = Types_ticket.Specify_ticket()[2] - Types_ticket.Specify_ticket()[2] * s_d_d[0] / 100
                        print(f"You have a special day discount. You have to pay {pay} $ for {num_ticket()} tickets")
                        return pay
                    else:
                        print(f"You have to pay {Types_ticket.Specify_ticket()[2]} $ for {num_ticket()} tickets")
                        return Types_ticket.Specify_ticket()[2]
                else:
                    if i == 3:
                        print("sorry ! Your access to the site has been blocked")
                    else:
                        print(f"The entered code is invalid, You can enter {3 - i} more times")
        else:
            print("Sorry, this ticket does not exist !")
    elif menu01 == '4':
        if Types_ticket.Specify_ticket()[4] is not None:
            for i in range(1, 4):
                Code_Special = input("Enter the special code for this ticket :")
                if Code_Special == Types_ticket.Specify_ticket()[5]:
                    s_d_d = [Types_ticket.special_days()[1][i] for i in range(len(Types_ticket.special_days()[0]))
                             if Types_ticket.special_days()[0][i] == date_registration()]
                    if s_d_d:
                        pay = Types_ticket.Specify_ticket()[4] - Types_ticket.Specify_ticket()[4] * s_d_d[0] / 100
                        print(f"You have a special day discount. You have to pay {pay} $ for {num_ticket()} tickets")
                        return pay
                    else:
                        print(f"You have to pay {Types_ticket.Specify_ticket()[4]} $ for {num_ticket()} tickets")
                        return Types_ticket.Specify_ticket()[4]
                else:
                    if i == 3:
                        print("sorry ! Your access to the site has been blocked")
                    else:
                        print(f"The entered code is invalid, You can enter {3 - i} more times")
        else:
            print("Sorry, this ticket does not exist !")
    elif menu01 == '5':
        if Types_ticket.Specify_ticket()[6] is not None:
            for i in range(1, 4):
                Code_Special = input("Enter the special code for this ticket :")
                if Code_Special == Types_ticket.Specify_ticket()[7]:
                    s_d_d = [Types_ticket.special_days()[1][i] for i in range(len(Types_ticket.special_days()[0]))
                             if Types_ticket.special_days()[0][i] == date_registration()]
                    if s_d_d:
                        pay = Types_ticket.Specify_ticket()[6] - Types_ticket.Specify_ticket()[6] * s_d_d[0] / 100
                        print(f"You have a special day discount. You have to pay {pay} $ for {num_ticket()} tickets")
                        return pay
                    else:
                        print(f"You have to pay {Types_ticket.Specify_ticket()[6]} $ for {num_ticket()} tickets")
                        return Types_ticket.Specify_ticket()[6]
                else:
                    if i == 3:
                        print("sorry ! Your access to the site has been blocked")
                    else:
                        print(f"The entered code is invalid, You can enter {3 - i} more times")
        else:
            print("Sorry, this ticket does not exist !")


def Return():
    """
    Possibility of return
    :return:
    """
    Event.Event.add_event()[2] = Event.Event.add_event()[2] + num_ticket()
    print(f"{type_ticket()} was paid to your account")