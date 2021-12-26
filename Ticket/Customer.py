from datetime import datetime
from Ticket import Ticket_types
from Ticket_types import list_special_days, list_discount
from Event import Event
from Administrator_user import Administrator_user
import log

list_n_c_p = []  # ----> List of national code of participants


def type_event():
    """
    This method is executed if type event == security
    :return: True / False
    """
    national_code = input("please enter your national_code :")
    while not Administrator_user.check_national_code(national_code):
        national_code = input("The national_Code is incorrect, Must be 10 digits. please enter again :")
    if national_code is not list_n_c_p:
        list_n_c_p.append(national_code)
        return True
    else:
        return False


def date_registration(d1, d2):
    """
    :param d1: Registration end date
    :param d2: Registration start date
    display Date and time of user registration user
    """
    now = datetime.now()
    if Ticket_types.time_comparison(now, d1, d2):
        return True
    else:
        return False


# if methode ⬆ False methode ⬇ not done

list_num_ticket = []


def num_ticket(event_type, remaining_capacity):
    if event_type == 'Security':
        number_ticket = 1
        list_num_ticket.append(number_ticket)
    else:
        while True:
            try:
                number_ticket = int(input("How many tickets do you want ? "))
            except Exception as E:
                print(E)
            else:
                break
        while not Event.check_capacity(remaining_capacity, number_ticket):
            a = input("Are you still interested in registering for the event? 1.yes  2.no : ")
            if a == '1':
                while True:
                    try:
                        number_ticket = int(input("How many tickets do you want ? "))
                    except Exception as E:
                        print(E)
                    else:
                        break
            elif a == '2':
                number_ticket = 0
                break
            else:
                log.logger.warning('The entered phrase is incorrect', exc_info=True)
        list_num_ticket.append(number_ticket)
        remaining_capacity -= number_ticket
    return number_ticket


# if methode ⬆ number_ticket = 0 methode ⬇ not done


def type_ticket(dic):
    """
    1 ---> display types tickets
    2 ---> Select the type of ticket
    3 ---> display payable for the customer.
    """
    print("welcome ! Choose your ticket type ")
    menu01 = input("""\n1.Ordinary ticket\n2.vip\n3.Student\n4.Cultural\n5.Last Moment\n What is your choice? """)
    if menu01 == '1':
        now = datetime.now()
        s_d_d = [list_discount[i] for i in range(len(list_special_days))
                 if list_special_days[i] == now]
        # s_d_d is ----> Special day discount
        if s_d_d:
            pay = int(float(dic['Original_ticket_price'])) - int(float(dic['Original_ticket_price'])) * s_d_d[0] / 100
            payable = pay * list_num_ticket[0]
            print(f"You have a special day discount. You have to pay {payable} $ for {list_num_ticket[0]} tickets")
            return payable
        else:
            pay = int(float(dic['Original_ticket_price']))
            payable = pay * list_num_ticket[0]
            print(f"You have to pay {payable} $ for {list_num_ticket[0]} tickets")
            return payable
    elif menu01 == '2':
        if dic['Vip_ticket_price'] is not '':
            now = datetime.now()
            s_d_d = [list_discount[i] for i in range(len(list_special_days))
                     if list_special_days[i] == now]
            if s_d_d:
                pay = int(float(dic['Vip_ticket_price'])) - int(float(dic['Vip_ticket_price'])) * s_d_d[
                    0] / 100
                payable = pay * list_num_ticket[0]
                print(f"You have a special day discount. You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                return payable
            else:
                pay = int(float(dic['Vip_ticket_price']))
                payable = pay * list_num_ticket[0]
                print(f"You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                return payable
        else:
            print("Sorry, this ticket does not exist !")
            return False
    elif menu01 == '3':
        if dic['Student_ticket_price'] is not '':
            for i in range(1, 4):
                Code_Special = input("Enter the special code for this ticket :")
                if Code_Special == dic['Student_ticket_discount_code03']:
                    now = datetime.now()
                    s_d_d = [list_discount[i] for i in range(len(list_special_days))
                             if list_special_days[i] == now]
                    if s_d_d:
                        pay = int(float(dic['Student_ticket_price'])) - int(float(dic['Student_ticket_price'])) * s_d_d[
                            0] / 100
                        payable = pay * list_num_ticket[0]
                        print(
                            f"You have a special day discount. You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                        return payable
                    else:
                        pay = int(float(dic['Student_ticket_price']))
                        payable = pay * list_num_ticket[0]
                        print(f"You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                        return payable
                else:
                    if i == 3:
                        print("sorry ! Your access to the site has been blocked")
                    else:
                        print(f"The entered code is invalid, You can enter {3 - i} more times")
        else:
            print("Sorry, this ticket does not exist !")
            return False
    elif menu01 == '4':
        if dic['Cultural_ticket_price'] is not '':
            for i in range(1, 4):
                Code_Special = input("Enter the special code for this ticket :")
                if Code_Special == dic['Cultural_ticket_discount_code03']:
                    now = datetime.now()
                    s_d_d = [list_discount[i] for i in range(len(list_special_days))
                             if list_special_days[i] == now]
                    if s_d_d:
                        pay = int(float(dic['Cultural_ticket_price'])) - int(float(dic['Cultural_ticket_price'])) * s_d_d[
                            0] / 100
                        payable = pay * list_num_ticket[0]
                        print(
                            f"You have a special day discount. You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                        return payable
                    else:
                        pay = int(float(dic['Cultural_ticket_price']))
                        payable = pay * list_num_ticket[0]
                        print(f"You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                        return payable
                else:
                    if i == 3:
                        print("sorry ! Your access to the site has been blocked")
                    else:
                        print(f"The entered code is invalid, You can enter {3 - i} more times")
        else:
            print("Sorry, this ticket does not exist !")
            return False
    elif menu01 == '5':
        if dic['Last Moment_ticket_price'] is not '':
            for i in range(1, 4):
                Code_Special = input("Enter the special code for this ticket :")
                if Code_Special == dic['Last Moment_ticket_discount_code03']:
                    now = datetime.now()
                    s_d_d = [list_discount[i] for i in range(len(list_special_days))
                             if list_special_days[i] == now]
                    if s_d_d:
                        pay = int(float(dic['Last Moment_ticket_price'])) - int(float(dic['Last Moment_ticket_price'])) * \
                              s_d_d[
                                  0] / 100
                        payable = pay * list_num_ticket[0]
                        print(
                            f"You have a special day discount. You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                        return payable
                    else:
                        pay = int(float(dic['Last Moment_ticket_price']))
                        payable = pay * list_num_ticket[0]
                        print(f"You have to pay {payable} $ for {list_num_ticket[0]} tickets")
                        return payable
                else:
                    if i == 3:
                        print("sorry ! Your access to the site has been blocked")
                    else:
                        print(f"The entered code is invalid, You can enter {3 - i} more times")
        else:
            print("Sorry, this ticket does not exist !")
            return False
    else:
        log.logger.warning('The entered phrase is incorrect', exc_info=True)


