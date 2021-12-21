import logging
import re
import hashlib
from File_Handler import FileHandler
import log


class Administrator_user:
    counter = 0
    special_code = 'SniMda1309'
    list_Administrator_user = []  # for all Administrator user
    Register_admin_information = {}

    def __init__(self, user_name, password, name, l_name, national_code, phone_number, email_address):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.l_name = l_name
        self.national_code = national_code
        self.phone_number = phone_number
        self.email_address = email_address
        self.id_01 = Administrator_user.counter + 1
        Administrator_user.counter += 1

    @staticmethod
    def generate_id(*args):
        args = list(args)
        new_args = [str(i).lower() for i in args]
        uniqe_id = '_'.join(new_args)
        return uniqe_id

    @classmethod
    def add_admin(cls):  # add new account for administrator_user
        id_01 = cls.counter + 1
        cls.counter += 1
        name = input("please enter your First name :")
        l_name = input("please enter your Last name :")
        phone_number = input("please enter your phone_number :")
        while not cls.check_phone_number(phone_number):
            phone_number = input("The phone_number is incorrect. please enter again :")
        national_code = input("please enter your national_code :")
        while not cls.check_national_code(national_code):
            national_code = input("The national_Code is incorrect, Must be 10 digits. please enter again :")
        email_address = input("please enter your email_address :")
        while not cls.check_email(email_address):
            email_address = input("The address email is incorrect, put '@' in the email. Please enter again :")
        user_name = input("please enter your user_name :")
        password = input("please enter your password :")
        while not cls.pass_validity(password):
            print("""
password must contain 1 number (0-9)
password must contain 1 uppercase letters
password must contain 1 lowercase letters
password must contain 1 non-alpha numeric number
password is 8-16 characters with no space
for example ---> #m_4xF%t"Bu5jeb$""")
            password = input("please enter your password :")
        re_pass = input("please Re-enter your password :")
        while not cls.check_pass(password, re_pass):
            print("❌ The two passwords entered do not match, please enter again ❌")
            password = input("password :")
            while not cls.pass_validity(password):
                print("""
password must contain 1 number (0-9)
password must contain 1 uppercase letters
password must contain 1 lowercase letters
password must contain 1 non-alpha numeric number
password is 8-16 characters with no space
for example ---> #m_4xF%t"Bu5jeb$""")
                password = input("please enter your password :")
            re_pass = input("Re_password :")
        Password_hash = password.encode()
        Password_hash_01 = hashlib.sha256(Password_hash).hexdigest()
        user_name_hash = user_name.encode()
        user_name_hash_01 = hashlib.sha256(user_name_hash).hexdigest()
        # print(user_name_hash_01)
        id = cls.generate_id(user_name_hash_01, Password_hash_01)
        # print(id)
        cls.list_Administrator_user.append(id)
        print(f"Your registration was completed successfully. Special code for admin is [ {cls.special_code} ] "
              f"Please remember .")
        cls.Register_admin_information = {'id_01': id_01, 'id': id, 'First Name': name, 'Last Name': l_name,
                                          'User_name': user_name_hash_01, 'Password': Password_hash_01,
                                          'Phone_number': phone_number, 'National_code': national_code,
                                          'Email_address': email_address}
        return name, l_name, user_name, password, re_pass, phone_number, national_code, email_address

    @classmethod
    def edit_admin_information(cls):
        Select = ['name', 'last_name', 'user_name', 'password', 'phone_number', 'national_code', 'email_address']
        while True:
            try:
                key = int(input("""
                Which of the following do you want to change? Select !
                1.First name  2.Last name  3.User_name  4.Password  5.Phone number  6.National_code  7.Email_address  8.Exit
                """))
                for i, item in enumerate(Select):
                    if key - 1 == i:
                        change = cls.Register_admin_information
                        while True:
                            try:
                                if item == 'name':
                                    new_name = input("please enter your First name :")
                                    change['First Name'] = new_name
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'last_name':
                                    new_l_name = input("please enter your Last name :")
                                    change['Last Name'] = new_l_name
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'user_name':
                                    new_user_name = input("please enter your user_name :")
                                    new_user_name_hash = new_user_name.encode()
                                    user_name_hash_01 = hashlib.sha256(new_user_name_hash).hexdigest()
                                    # print(user_name_hash_01)
                                    Password_hash_01 = change['Password']
                                    new_id = cls.generate_id(user_name_hash_01, Password_hash_01)
                                    change['User_name'] = user_name_hash_01
                                    change['id'] = new_id
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'password':
                                    new_password = input("please enter your password :")
                                    while not cls.pass_validity(new_password):
                                        print("""
password must contain 1 number (0-9)
password must contain 1 uppercase letters
password must contain 1 lowercase letters
password must contain 1 non-alpha numeric number
password is 8-16 characters with no space
for example ---> #m_4xF%t"Bu5jeb$""")
                                        new_password = input("please enter your password :")
                                    re_pass = input("please Re-enter your password :")
                                    while not cls.check_pass(new_password, re_pass):
                                        print("❌ The two passwords entered do not match, please enter again ❌")
                                        new_password = input("password :")
                                        while not cls.pass_validity(new_password):
                                            print("""
password must contain 1 number (0-9)
password must contain 1 uppercase letters
password must contain 1 lowercase letters
password must contain 1 non-alpha numeric number
password is 8-16 characters with no space
for example ---> #m_4xF%t"Bu5jeb$""")
                                            new_password = input("please enter your password :")
                                        re_pass = input("Re_password :")
                                    new_password_hash = new_password.encode()
                                    new_password_hash_01 = hashlib.sha256(new_password_hash).hexdigest()
                                    # print(user_name_hash_01)
                                    user_name_hash_01 = change['User_name']
                                    new_id = cls.generate_id(user_name_hash_01, new_password_hash_01)
                                    change['Password'] = new_password_hash_01
                                    change['id'] = new_id
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'phone_number':
                                    new_phone_number = input("please enter your phone_number :")
                                    while not cls.check_phone_number(new_phone_number):
                                        new_phone_number = input("The phone_number is incorrect. please enter again :")
                                    change['Phone_number'] = new_phone_number
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'national_code':
                                    new_national_code = input("please enter your national_code :")
                                    while not cls.check_national_code(new_national_code):
                                        new_national_code = input("The national_Code is incorrect, Must be 10 digits. "
                                                                  "please enter again :")
                                    change['National_code'] = new_national_code
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                        while True:
                            try:
                                if item == 'email_address':
                                    new_email_address = input("please enter your email_address :")
                                    while not cls.check_email(new_email_address):
                                        new_email_address = input(
                                            "The address email is incorrect, put '@' in the email. Please enter again :")
                                    change['Email_address'] = new_email_address
                            except Exception:
                                log.logger.error(f"Error in input data type !", exc_info=True)
                            else:
                                break
                if key == 8:
                    break
                else:
                    log.logger.warning('The entered phrase is incorrect', exc_info=True)
            except Exception as E:
                print(E)

    @staticmethod
    def pass_validity(password):
        pass_pattern = r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$"
        matches1 = re.search(pass_pattern, password, re.MULTILINE)
        if matches1:
            return True
        else:
            return False

    @staticmethod
    def check_pass(password, re_pass):
        if password != re_pass:
            return False
        else:
            return True

    @staticmethod
    def check_email(email_address):
        email_pattern = r"(.+\@.+\.[c][o][m])"
        matches2 = re.search(email_pattern, email_address)
        if matches2:
            return True
        else:
            return False

    @staticmethod
    def check_national_code(national_code):
        n_c_pattern = r"^[0-9]{10}$"
        matches3 = re.search(n_c_pattern, national_code)
        if matches3:
            return True
        else:
            return False

    @staticmethod
    def check_phone_number(phone_number):
        p_n_pattern = r"^(0|84)(2(0[3-9]|1[0-6|8|9]|2[0-2|5-9]|3[2-9]|4[0-9]|5[1|2|4-9]|6[0-3|9]|7[0-7]|8[0-9]|" \
                      r"9[0-4|6|7|9])|3[2-9]|5[5|6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])([0-9]{8})$"
        matches4 = re.search(p_n_pattern, phone_number)
        if matches4:
            return True
        else:
            return False
