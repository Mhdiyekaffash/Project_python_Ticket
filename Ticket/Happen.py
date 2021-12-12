from File_Handler import FileHandler
import time


class Happen:
    def __init__(self, name, start_date, end_date, start_time, end_time, holding_time, location, total_capacity, remaining_capacity):
        """
        :param start_date: Registration start date
        :param end_date: Registration deadline
        :param start_time: Registration start time
        :param end_time: Registration end time
        :param holding_time: holding_time event

        """
        self.name_happen = name
        self.start_date = start_date
        self.holding_time = holding_time
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.Total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity

    @classmethod
    def add_happen(cls):
        print("for add happen")

    @staticmethod
    def date_registration(date_now, time_now):  # Date and time of user registration user
        date_now = date_now
        time_now = time_now
        print("display Date and time of user registration user")
        return date_now, time_now

    def file_happens(self):  # for submit Happens
        print("for submit Happens")

    def __repr__(self):
        """
        If the user wants to know the remaining capacity of the event and
         the time remaining until the end of to happen registration
        :return: string
        """
        return f"The remaining capacity of the {self.name_happen} happen is : {self.remaining_capacity} and " \
               f"time remaining until the end of to happen registration :{}-{} ,{}{} min"

    def type_ticket(self):  # display types tickets and Selected by the customer.
        print("Choose your ticket type 🙂")
        menu01 = input("""\n1.Normal\n2.Student\n3.Cultural\n4.special place\n5.Last Moment\n...? """)
        number_ticket = int(input("How many tickets do you want ? "))
        while not Happen.check_capacity(self.remaining_capacity, number_ticket):
            a = input("Are you still interested in registering for the event? yes/no")
            if a == 'yes':
                number_ticket = int(input("Re-enter the number of tickets you requested : "))
                if not Happen.check_capacity(self.remaining_capacity, number_ticket):
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

        :param num1: Number of tickets remaining from the happen
        :param num2: Number of tickets requested by the user
        :return: true or false
        """
        if num2 > num1:
            print(f"The remaining capacity of the happen is : {num1} ,"
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
