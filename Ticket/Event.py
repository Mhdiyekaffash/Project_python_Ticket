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
    def add_event(cls):
        name_event = input("Event name : ")
        # holding_date = input("Holding date : ")
        # date_entry = input('Holding date : i.e. --->  2017-7-1')
        # while not cls.check_date(date_entry):
        #     date_entry = input("Please follow the date format , i.e. ---> 2020-10-10")
        # year, month, day = map(int, date_entry.split('-'))
        # holding_date = datetime(year, month, day)
        # print(date)
        # while not cls.check_date(holding_date):
        #     holding_date = input("Please follow the date format , i.e. ---> 2020/10/10")
        #---------------------holding_date-----------------------------------------------------------------

        print("Enter the date and time of the event 📆")
        year = int(input("Year :"))
        month = int(input("Month :"))
        while month > 12:
            month = int(input("month must be in 1..12"))
        day = int(input("d:"))
        while day > 31:
            day = int(input("day must be in 1..31"))
        hour = int(input("Hour :"))
        while hour > 24:
            hour = int(input("hour must be in 1..24"))
        minute = int(input("Minute :"))
        while minute > 59:
            minute = int(input("minute must be in 1..59"))
        holding_date = datetime(year, month, day, hour=hour, minute=minute, second=0)
        print(f"holding_date : {holding_date}")
        # -------------------------------------------
        location = input("Venue of the event :")
        total_capacity = int(input("Total capacity : "))
        # ticket_fee = int(input("Ticket fee :"))
        #--------Registration start date--------------------------------------------------------------

        # print("Enter the start date for registration :")
        # year_r_s = int(input("Year :"))
        # if year_r_s > year:
        #     while year_r_s > year:
        #         year_r_s = int(input(f"{year_r_s} > {year} !!!!!!!!!, enter again:"))
        #     month_r_s = int(input("Month :"))
        #     while month_r_s > 12:
        #         month_r_s = int(input("month must be in 1..12"))
        #     day_r_s = int(input("d:"))
        #     while day_r_s > 31:
        #         day_r_s = int(input("day must be in 1..31"))
        #     hour_r_s = int(input("Hour :"))
        #     while hour_r_s > 24:
        #         hour_r_s = int(input("hour must be in 1..24"))
        #     start_date = datetime(year_r_s, month_r_s, day_r_s, hour_r_s, 0, 0)
        #     print(f"start date : {start_date}")
        # else:
        #     month_r_s = int(input("Month :"))
        #     while month_r_s > 12:
        #         month_r_s = int(input("month must be in 1..12"))
        #     if month_r_s > month:
        #         while month_r_s > month:
        #             month_r_s = int(input(f"{month_r_s} > {month} !!!!!!!!!, enter again:"))
        #         day_r_s = int(input("d:"))
        #         while day_r_s > 31:
        #             day_r_s = int(input("day must be in 1..31"))
        #         hour_r_s = int(input("Hour :"))
        #         while hour_r_s > 24:
        #             hour_r_s = int(input("hour must be in 1..24"))
        #         start_date = datetime(year_r_s, month_r_s, day_r_s, hour_r_s, 0, 0)
        #         print(f"start date : {start_date}")
        #
        # #-----------------------------------------------------------------------
        # # start_date = input("Registration start date : ")
        # # while not cls.check_date(start_date):
        # #     start_date = input("Please follow the date format , for example ---> 2020/10/10")
        # # start_time = input("Registration start time : ")
        # # while not cls.check_date(start_time):
        # #     start_date = input("Please follow the time format , for example ---> 09:10")
        # #----------------Registration end date-----------------------------------------------
        # deadline = int(input("Event registration deadline? few days ?"))
        # end_date = start_date + timedelta(days=deadline)
        # print(f"end_date : {end_date}")

        # end_date = input("Registration end date : ")
        # while not cls.check_date(start_date):
        #     start_date = input("Please follow the date format , for example ---> 2020/10/10")
        # end_time = input("Registration end time : ")
        # while not cls.check_date(end_time):
        #     start_date = input("Please follow the time format , for example ---> 09:10")
        r_d = int(input("registration deadline ? "))  # r_d ---> registration deadline
        start_date = holding_date - timedelta(days=r_d)
        print(f"Start registration {start_date}")
        end_date = holding_date - timedelta(days=1)
        print(f"finish registration {end_date}")
        print("This event was successfully registered ✔ Thanks. ")
        logger.info('Event registration !', exc_info=True)
        # return name_event, holding_date, holding_time, location, total_capacity, ticket_fee, start_date, \
        #        start_time, end_date, end_time
        return name_event, holding_date, location, total_capacity, start_date, end_date

    # @staticmethod
    # def check_date(date_event):
    #     date_pattern = r"(?<=\D|^)(?<year>\d{4})(?<sep>[^\w\s])(?<month>1[0-2]|0[1-9])\k<sep>(?<day>0[1-9]|[12][0-9]|(?<=11\k<sep>|[^1][4-9]\k<sep>)30|(?<=1[02]\k<sep>|[^1][13578]\k<sep>)3[01])(?=\D|$)"
    #     matches1 = re.finditer(date_pattern, date_event, re.IGNORECASE | re.UNICODE)
    #     if matches1:
    #         return True
    #     else:
    #         return False

    # @staticmethod
    # def check_time(time_event):
    #     time_pattern = r"/([0-1]{0,1}[0-9]{1}):([0-6]{0,1}[0-9]{1})$/"
    #     matches2 = re.finditer(time_pattern, time_event)
    #     if matches2:
    #         return True
    #     else:
    #         return False

    @staticmethod
    def date_registration():
        """
        display Date and time of user registration user
        """
        now = datetime.now()
        now_date = now.date()
        now_time = time(now.hour, now.minute, now.second)
        if now_date.year > Event.add_event()[5].year:
            print("Registration deadline has expired ")
        elif now_date.year == Event.add_event()[5].year & now_date.month > Event.add_event()[5].month:
            print("Registration deadline has expired ")
        elif now_date.year == Event.add_event()[5].year & now_date.month == Event.add_event()[5].month & \
                now_date.day > Event.add_event()[5].day:
            print("Registration deadline has expired ")
        else:
            return now_date, now_time

    @staticmethod
    def check_int(value):
        try:
            if isinstance(value, int):
                return True
            else:
                raise Exception
        except Exception as e:
            logger.error("The entered phrase is not a int", exc_info=True)


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


    def type_ticket(self):  # display types tickets payable for the customer.
        print("Choose your ticket type 🙂")
        menu01 = input("""\n1.Normal\n2.vip\n3.Student\n4.Cultural\n5.Last Moment\n What is your choice? """)
        number_ticket = int(input("How many tickets do you want ? "))
        while not Event.check_capacity(self.remaining_capacity, number_ticket):
            a = input("Are you still interested in registering for the event? yes/no")
            if a == 'yes':
                number_ticket = int(input("Re-enter the number of tickets you requested : "))
                # if not Event.check_capacity(self.remaining_capacity, number_ticket):
                #     print(f"why :| ?????? my Dear {number_ticket} > {self.remaining_capacity}  :|")
                # else:
                #     self.remaining_capacity -= number_ticket
                #     print("✔")
                #     break
            elif a == 'no':
                self.remaining_capacity -= number_ticket
                print("✔")
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
