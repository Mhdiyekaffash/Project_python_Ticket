import logging
from File_Handler import FileHandler
from datetime import date, time, datetime, timedelta
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create handlers and set level
file_handler = logging.FileHandler('Administrator_user')
file_handler.setLevel(level=logging.INFO)
# create formatters and add it to handlers
file_format = logging.Formatter('%(asctime)s ::%(levelname)s - %(filename)s  - %(message)s')
file_handler.setFormatter(file_format)
# add handlers to the logger
logger.addHandler(file_handler)


class Event:
    def __init__(self, name, start_date, end_date, start_time, end_time, holding_time, holding_date, location,
                 total_capacity, remaining_capacity):
        """
        :param start_date: Registration start date
        :param end_date: Registration end date
        :param start_time: Registration start time
        :param end_time: Registration end time
        :param holding_time: holding_time event
        :param holding_date: holding_date event

        """
        self.name_event = name
        self.start_date = start_date
        self.holding_time = holding_time
        self.holding_date = holding_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity

    @classmethod
    def add_happen(cls):
        name_event = input("Event name : ")
        holding_date = input("Holding date : ")
        while not cls.check_date(holding_date):
            holding_date = input("Please follow the date format , for example ---> 2020/10/10")
        holding_time = input("Holding time : ")
        while not cls.check_date(holding_time):
            holding_time = input("Please follow the time format , for example ---> 09:10")
        location = input("Venue of the event :")
        total_capacity = int(input("Total capacity : "))
        ticket_fee = int(input("Ticket fee :"))
        start_date = input("Registration start date : ")
        while not cls.check_date(start_date):
            start_date = input("Please follow the date format , for example ---> 2020/10/10")
        start_time = input("Registration start time : ")
        while not cls.check_date(start_time):
            start_date = input("Please follow the time format , for example ---> 09:10")
        end_date = input("Registration end date : ")
        while not cls.check_date(start_date):
            start_date = input("Please follow the date format , for example ---> 2020/10/10")
        end_time = input("Registration end time : ")
        while not cls.check_date(end_time):
            start_date = input("Please follow the time format , for example ---> 09:10")
        print("This event was successfully registered ✔ Thanks. ")
        logger.info('Event registration !', exc_info=True)
        return name_event, holding_date, holding_time, location, total_capacity, ticket_fee, start_date, \
               start_time, end_date, end_time

    @staticmethod
    def check_date(date_event):
        regex_date = r"(?P<LongDate>(?P<Year>\d{4})[\/ ]+(?P<Month>[1-9]|[01][012])[\/ ]+)(?P<Day>\d+)"
        matches1 = re.finditer(regex_date, date_event, re.IGNORECASE | re.UNICODE)
        if matches1:
            return True
        else:
            return False

    @staticmethod
    def check_time(time_event):
        regex_time = r"/([0-1]{0,1}[0-9]{1}):([0-6]{0,1}[0-9]{1})$/"
        matches2 = re.finditer(regex_time, time_event)
        if matches2:
            return True
        else:
            return False

    @staticmethod
    def date_registration(end_date, end_time):
        """
        display Date and time of user registration user
        """
        now = datetime.now()
        now_date = now.date()
        if now_date.year > end_date[0:4]:
            print("Registration deadline has expired ")
        elif now_date.month > end_date[5:7]:
            print("Registration deadline has expired ")
        elif now_date.day > end_date[9:11]:
            print("Registration deadline has expired ")
        now_time = time(now.hour, now.minute, now.second)
        return now_date, now_time

    def file_happens(self):  # for submit Happens
        print("for submit Happens")

    def __repr__(self):
        """
        If the user wants to know the remaining capacity of the event and
         the time remaining until the end of to Event registration
        :return: string
        """
        return f"The remaining capacity of the {self.name_event} Event is : {self.remaining_capacity} and " \
               f"time remaining until the end of to Event registration : min"

    def type_ticket(self):  # display types tickets and Selected by the customer.
        print("Choose your ticket type 🙂")
        menu01 = input("""\n1.Normal\n2.vip\n3.Student\n4.Cultural\n5.special place\n6.Last Moment\n...? """)
        number_ticket = int(input("How many tickets do you want ? "))
        while not Event.check_capacity(self.remaining_capacity, number_ticket):
            a = input("Are you still interested in registering for the event? yes/no")
            if a == 'yes':
                number_ticket = int(input("Re-enter the number of tickets you requested : "))
                if not Event.check_capacity(self.remaining_capacity, number_ticket):
                    print(f"why :| ?????? my Dear {number_ticket} > {self.remaining_capacity}  :|")
                else:
                    self.remaining_capacity -= number_ticket
                    print("✔")
                    break
            elif a == 'no':
                break
        if menu01 == '1':
            print("Display discount code and payable")
        elif menu01 == '2':
            print("Display discount code and payable")
        elif menu01 == '3':
            print("Display discount code and payable")
        elif menu01 == '4':
            print("Display discount code and payable")

    @staticmethod
    def check_capacity(num1, num2):
        """

        :param num1: Number of tickets remaining from the Event
        :param num2: Number of tickets requested by the user
        :return: true or false
        """
        if num2 > num1:
            print(f"The remaining capacity of the Event is : {num1} ,"
                  f" Sorry but we can only deliver {num1} tickets to you")
            return False
        else:
            print("✔")
            return True

    def discount_code(self):  # Specify a discount code for each type of ticket
        print("View the types of tickets and set the discount code for each type of ticket by the administrator user")

    @staticmethod
    def calculate_cost(amount, number, discount_code):  # Calculate the cost payable
        """

        :param amount: The principal amount ticket
        :param number: Number of tickets requested by the user
        :param discount_code: discount_code
        :return: payable
        """
        pass
