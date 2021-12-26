from Event import Event
import log
from datetime import datetime


def Specify_ticket():
    """
    Specify the types of event tickets for teachers etc.
    are based on the cost of the original ticket
    :return:
    """
    global amount01, payable01, payable02, payable03, discount_code03, payable04, discount_code04, \
        payable05, discount_code05, payable06, discount_code06

    print("Specify the tickets you want for this event by entering + or -"
          "\n  🔔 Note that the original ticket must be available")
    type01 = "original ticket"
    while True:
        try:
            amount01 = float(input('Enter the amount original ticket : '))
        except Exception as E:
            print(E)
        else:
            break
    while True:
        try:
            discount01 = int(input("Discount amount : "))
        except Exception as E:
            print(E)
        else:
            break
    while discount01 > 100:
        print("The discount rate is 0 to 100% ")
        while True:
            try:
                discount01 = int(input("re_enter Discount amount : "))
            except Exception as E:
                print(E)
            else:
                break
    payable01 = amount01 - (amount01 * discount01 / 100)
    print(f"The amount payable for Ticket {type01} : {payable01}$")
    type02 = input("VIP +/- :")
    if type02 == '+':
        while True:
            try:
                amount02 = float(input('Enter the amount :'))
            except Exception as E:
                print(E)
            else:
                break
        while True:
            try:
                discount02 = int(input("Discount amount :"))
            except Exception as E:
                print(E)
            else:
                break
        while discount02 > 100:
            print("The discount rate is 0 to 100% ")
            while True:
                try:
                    discount02 = int(input("re_enter Discount amount :"))
                except Exception as E:
                    print(E)
                else:
                    break
        payable02 = amount02 - (amount02 * discount02 / 100)
        print(f"The amount payable for Ticket {type02} : {payable02}$")
    elif type02 == '-':
        payable02 = None
    else:
        log.logger.warning('The entered phrase is incorrect', exc_info=True)
    type03 = input("Student +/- :")
    if type03 == '+':
        while True:
            try:
                discount03 = int(input("Discount amount :"))
            except Exception as E:
                print(E)
            else:
                break
        while discount03 > 100:
            print("The discount rate is 0 to 100% ")
            while True:
                try:
                    discount03 = int(input("re_enter Discount amount :"))
                except Exception as E:
                    print(E)
                else:
                    break
        discount_code03 = input("Discount code :")
        payable03 = amount01 - (amount01 * discount03 / 100)
        print(f"The amount payable for Ticket {type03} : {payable03}$")
    elif type03 == '-':
        payable03 = None
        discount_code03 = None
    else:
        log.logger.warning('The entered phrase is incorrect', exc_info=True)
    type04 = input("Cultural +/- :")
    if type04 == '+':
        while True:
            try:
                discount04 = int(input("Discount amount :"))
            except Exception as E:
                print(E)
            else:
                break
        while discount04 > 100:
            print("The discount rate is 0 to 100% ")
            while True:
                try:
                    discount04 = int(input("re_enter Discount amount :"))
                except Exception as E:
                    print(E)
                else:
                    break
        discount_code04 = input("Discount code :")
        payable04 = amount01 - (amount01 * discount04 / 100)
        print(f"The amount payable for Ticket {type04} : {payable04}$")
    elif type04 == '-':
        payable04 = None
        discount_code04 = None
    else:
        log.logger.warning('The entered phrase is incorrect', exc_info=True)
    type05 = input("Last Moment +/- :")
    if type05 == '+':
        while True:
            try:
                discount05 = int(input("Discount amount :"))
            except Exception as E:
                print(E)
            else:
                break
        while discount05 > 100:
            print("The discount rate is 0 to 100% ")
            while True:
                try:
                    discount05 = int(input("re_enter Discount amount :"))
                except Exception as E:
                    print(E)
                else:
                    break
        discount_code05 = input("Discount code :")
        payable05 = amount01 - (amount01 * discount05 / 100)
        print(f"The amount payable for Ticket {type05} : {payable05}$")
    elif type05 == '-':
        payable05 = None
        discount_code05 = None
    else:
        log.logger.warning('The entered phrase is incorrect', exc_info=True)
    Event.Recorded_events['Original_ticket_price'] = payable01
    Event.Recorded_events['Vip_ticket_price'] = payable02
    Event.Recorded_events['Student_ticket_price'] = payable03
    Event.Recorded_events['Student_ticket_discount_code03'] = discount_code03
    Event.Recorded_events['Cultural_ticket_price'] = payable04
    Event.Recorded_events['Cultural_ticket_discount_code03'] = discount_code04
    Event.Recorded_events['Last Moment_ticket_price'] = payable05
    Event.Recorded_events['Last Moment_ticket_discount_code03'] = discount_code05

    return payable01, payable02, payable03, discount_code03, payable04, discount_code04, payable05, discount_code05


def time_comparison(date1, date2, date3):
    """

    :param date1: Input date
    :param date2: Benchmark Date ---> Registration end date
    :param date3: Benchmark Date ---> Registration start date
    :return: True / False
    """

    var1 = date1 > date2
    var2 = date1 < date3
    if var1:
        return False
    elif var2:
        return False
    else:
        return True


list_special_days = []
list_discount = []


def special_days():
    """
    With this function, the admin can give discounts for all tickets on special days
    :return:
    """
    print("   🔔 Note that the date you specify must be in the registration period")
    while True:
        S_day = input("Do you have a discount for special days? +/- : ")
        if S_day == '+':
            date_entry = input('Enter a date (i.e. 2017-7-1) : ')
            year, month, day = map(int, date_entry.split('-'))
            date1 = datetime(year=year, month=month, day=day, hour=0, minute=0, second=0)
            print(date1)
            while not time_comparison(date1, Event.Recorded_events['end_date'], Event.Recorded_events['start_date']):
                date_entry = input('❌ Date is not valid, Must be in the registration period !'
                                   're_enter (i.e. 2017-7-1) : ')
                year, month, day = map(int, date_entry.split('-'))
                date1 = datetime(year=year, month=month, day=day, hour=0, minute=0, second=0)
                print(date1)
            list_special_days.append(date1)
            d_S_day = int(input("What percentage discount do you have for this day? "))
            # d_S_day ---> Discount code for special day
            list_discount.append(d_S_day)
        elif S_day == '-':
            break
        else:
            log.logger.warning('The entered phrase is incorrect', exc_info=True)
    Event.Recorded_events['List_of_dates_for_special_days'] = list_special_days
    Event.Recorded_events['List_of_discount_dates_for_special_days'] = list_discount
    return list_special_days, list_discount
