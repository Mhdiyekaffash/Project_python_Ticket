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
    def __init__(self, name, start_date, end_date, holding_date, location, total_capacity, remaining_capacity, type):
        """
        :param holding_date: holding_date event
        :param start_date: Registration start date
        :param end_date: Registration end date
        :param end_date: Security or public
        """
        self.name_event = name
        self.start_date = start_date
        self.holding_date = holding_date
        self.end_date = end_date
        self.location = location
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.type = type

    @classmethod
    def add_event(cls):
        name_event = input("Event name : ")
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
        total_capacity = int(input("Total capacity : "))
        r_d = int(input("registration deadline ? "))  # r_d ---> registration deadline
        start_date = holding_date - timedelta(days=r_d)
        print(f"Start registration {start_date}")
        end_date = holding_date - timedelta(days=1)
        print(f"finish registration {end_date}")
        type_event = input("Security or public :")
        print("This event was successfully registered ✔ Thanks. ")
        logger.info('Event registration !', exc_info=True)
        return name_event, holding_date, total_capacity, start_date, end_date, type_event

    @classmethod
    def location(cls):
        city = input("City : ")
        street = input("Street : ")
        building = input("Building name :")
        return city, street, building

    # @staticmethod
    # def check_date(date_event):
    #     date_pattern = r"(?<=\D|^)(?<year>\d{4})(?<sep>[^\w\s])(?<month>1[0-2]|0[1-9])\k<sep>(?<day>0[1-9]|
    #     [12][0-9]|(?<=11\k<sep>|[^1][4-9]\k<sep>)30|(?<=1[02]\k<sep>|[^1][13578]\k<sep>)3[01])(?=\D|$)"
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
    def check_int(value):
        try:
            if isinstance(value, int):
                return True
            else:
                raise Exception
        except Exception as e:
            logger.error("The entered phrase is not a int", exc_info=True)

    def __repr__(self):
        """
        If the user wants to know the remaining capacity of the event and
         the time remaining until the end of to Event registration
        :return: string
        """
        return f"The {Event.add_event()[0]} event was recorded at the place of {Event.location()} " \
               f"in time {Event.add_event()[1]} with a capacity of {Event.add_event()[2]} people." \
               f" Registration for the event starts from {Event.add_event()[3]} to {Event.add_event()[4]}"

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

    def file_events(self):  # for submit Happens
        print("for submit Happens")