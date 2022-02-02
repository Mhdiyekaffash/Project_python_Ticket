import log
from datetime import datetime, timedelta


class Event:
    Recorded_events = {}

    def __init__(self, name, start_date, end_date, holding_date, location, total_capacity, remaining_capacity, type):
        """
        :param holding_date: holding_date event
        :param start_date: Registration start date
        :param end_date: Registration end date
        :param end_date: Security or public
        """
        self.event_name = name
        self.start_date = start_date
        self.holding_date = holding_date
        self.end_date = end_date
        self.location = location
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.type = type

    @classmethod
    def add_event(cls):
        global holding_date
        event_name = input("Event name : ")
        event_place = input("Event place : ")
        print("Enter the date and time of the event 📆")
        while True:
            try:
                year = int(input("Year (i.e ---> 2020 ):"))
            except Exception as E:
                print(E)
            else:
                break
        while True:
            try:
                month = int(input("Month :"))
            except Exception as E:
                print(E)
            else:
                break
        while month > 12:
            month = int(input("month must be in 1..12"))
        while True:
            try:
                day = int(input("day :"))
            except Exception as E:
                print(E)
            else:
                break
        while day > 31:
            day = int(input("day must be in 1..31"))
        while True:
            try:
                hour = int(input("Hour :"))
            except Exception as E:
                print(E)
            else:
                break
        while hour > 24:
            hour = int(input("hour must be in 1..24"))
        while True:
            try:
                minute = int(input("Minute :"))
            except Exception as E:
                print(E)
            else:
                break
        while minute > 59:
            minute = int(input("minute must be in 1..59"))
        try:
            holding_date = datetime(year, month, day, hour=hour, minute=minute, second=0)
        except Exception as E:
            print(E)
        print(f"holding_date : {holding_date}")
        while True:
            try:
                r_d = int(input("registration deadline ? "))  # r_d ---> registration deadline
            except Exception as E:
                print(E)
            else:
                break
        start_date = holding_date - timedelta(days=r_d)
        print(f"Start registration {start_date}")
        end_date = holding_date - timedelta(days=1)
        print(f"finish registration {end_date}")
        while True:
            try:
                total_capacity = int(input("Total capacity : "))
            except Exception as E:
                print(E)
            else:
                break
        while True:
            try:
                remaining_capacity = total_capacity
            except Exception as E:
                print(E)
            else:
                break
        event_type = input("1.Security  2.public :")
        if event_type == '1':
            event_type = 'Security'
        elif event_type == '2':
            event_type = 'public'
        else:
            log.logger.warning('The entered phrase is incorrect', exc_info=True)
        cls.Recorded_events = {'event_name': event_name, 'event_place': event_place, 'holding_date': holding_date,
                               'total_capacity': total_capacity, 'start_date': start_date, 'end_date': end_date,
                               'event_type': event_type, 'remaining_capacity': remaining_capacity}
        print("This event was successfully registered ✔ Thanks. ")
        log.logger.info(f'The {event_name} event was recorded on the {holding_date} !', exc_info=True)
        return event_name, event_place, holding_date, total_capacity, start_date, end_date, event_type

    @classmethod
    def edit_event_information(cls):
        Select = ['event_name', 'event_place', 'holding_date', 'total_capacity', 'event_type']
        while True:
            try:
                key1 = int(input("""
                Which of the following do you want to change? Select !
                1.Event name  2.Event place  3.Holding date  4.Total capacity  5.Event type  6.Exit
                """))
                for i, item in enumerate(Select):
                    if key1 - 1 == i:
                        change = cls.Recorded_events
                        while True:
                            try:
                                if item == 'event_name':
                                    new_name = input("Event name : ")
                                    change['event_name'] = new_name
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'event_place':
                                    new_event_place = input("Event place : ")
                                    change['event_place'] = new_event_place
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'holding_date':
                                    while True:
                                        try:
                                            year = int(input("Year (i.e ---> 2020 ):"))
                                        except Exception as E:
                                            print(E)
                                        else:
                                            break
                                    while True:
                                        try:
                                            month = int(input("Month :"))
                                        except Exception as E:
                                            print(E)
                                        else:
                                            break
                                    while month > 12:
                                        month = int(input("month must be in 1..12"))
                                    while True:
                                        try:
                                            day = int(input("d:"))
                                        except Exception as E:
                                            print(E)
                                        else:
                                            break
                                    while day > 31:
                                        day = int(input("day must be in 1..31"))
                                    while True:
                                        try:
                                            hour = int(input("Hour :"))
                                        except Exception as E:
                                            print(E)
                                        else:
                                            break
                                    while hour > 24:
                                        hour = int(input("hour must be in 1..24"))
                                    while True:
                                        try:
                                            minute = int(input("Minute :"))
                                        except Exception as E:
                                            print(E)
                                        else:
                                            break
                                    while minute > 59:
                                        minute = int(input("minute must be in 1..59"))
                                    new_holding_date = datetime(year, month, day, hour=hour, minute=minute, second=0)
                                    while True:
                                        try:
                                            new_registration_deadline = int(
                                                input("registration deadline ? "))  # r_d ---> registration deadline
                                        except Exception as E:
                                            print(E)
                                        else:
                                            break
                                    new_start_date = new_holding_date - timedelta(days=new_registration_deadline)
                                    new_end_date = new_holding_date - timedelta(days=1)
                                    change['holding_date'] = new_holding_date
                                    change['start_date'] = new_start_date
                                    change['end_date'] = new_end_date
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'total_capacity':
                                    new_total_capacity = input("Event total capacity : ")
                                    change['total_capacity'] = new_total_capacity
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'event_type':
                                    event_type = input("1.Security  2.public :")
                                    if event_type == '1':
                                        event_type = 'Security'
                                    elif event_type == '2':
                                        event_type = 'public'
                                    else:
                                        log.logger.warning('The entered phrase is incorrect', exc_info=True)
                                    change['event_type'] = event_type
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                if key1 == 6:
                    break
                else:
                    log.logger.warning('The entered phrase is incorrect', exc_info=True)
            except Exception as E:
                print(E)

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
