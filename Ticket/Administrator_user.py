import logging
import re
from File_Handler import FileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create handlers and set level
file_handler = logging.FileHandler('Administrator_user')
file_handler.setLevel(level=logging.INFO)
# create formatters and add it to handlers
file_format = logging.Formatter('%(asctime)s ::%(levelname)s - %(filename)s - %(message)s')
file_handler.setFormatter(file_format)
# add handlers to the logger
logger.addHandler(file_handler)


class Administrator_user:
    special_code = 'SniMda1309'
    list_Administrator_user = []  # for all Administrator user

    def __init__(self, user_name, password, name, l_name, national_code, phone_number, email_address):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.l_name = l_name
        self.national_code = national_code
        self.phone_number = phone_number
        self.email_address = email_address

    @staticmethod
    def generate_id(*args):
        args = list(args)
        new_args = [str(i).lower() for i in args]
        uniqe_id = '_'.join(new_args)
        return uniqe_id

    @classmethod
    def add_admin(cls):  # add new account for administrator_user
        name = input("please enter your First name :")
        l_name = input("please enter your Last name :")
        phone_number = int(input("please enter your phone_number :"))
        while not cls.check_phone_number(phone_number):
            phone_number = int(input("The phone_number is incorrect. please enter again :"))
        national_code = int(input("please enter your national_code :"))
        while not cls.check_national_code(national_code):
            national_code = int(input("The national_Code is incorrect, Must be 10 digits. please enter again :"))
        email_address = input("please enter your email_address :")
        while not cls.check_email(email_address):
            email_address = input("The address email is incorrect, put '@' in the email. Please enter again :")
        user_name = input("please enter your user_name :")
        password = input("please enter your password :")
        while not Administrator_user.pass_validity(password):
            print("""password must contain 1 number (0-9)\npassword must contain 1 uppercase letters
            password must contain 1 lowercase letters\npassword must contain 1 non-alpha numeric number
            password is 8-16 characters with no space\n for example ---> #m_4xF%t"Bu5jeb$""")

        re_pass = input("please Re-enter your password :")
        while not Administrator_user.check_pass(password, re_pass):
            print("❌ The two passwords entered do not match, please enter again ❌")
            password = input("password :")
            while not Administrator_user.pass_validity(password):
                print("""password must contain 1 number (0-9)\npassword must contain 1 uppercase letters
                password must contain 1 lowercase letters\npassword must contain 1 non-alpha numeric number
                password is 8-16 characters with no space\n for example ---> #m_4xF%t"Bu5jeb$""")
            re_pass = input("Re_password :")
        id = cls.generate_id(user_name, password)
        cls.list_Administrator_user.append(id)
        print(f"Your registration was completed successfully. Special code for admin is {cls.special_code} "
              f"Please remember .")
        return name, l_name, user_name, password, re_pass, phone_number, national_code, email_address

    @staticmethod
    def pass_validity(password):
        pass_pattern = r"(/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$/gm)"
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
        n_c_pattern = r"(/^[0-9]{10}$/g)"
        matches3 = re.search(n_c_pattern, national_code)
        if matches3:
            return True
        else:
            return False

    @staticmethod
    def check_phone_number(phone_number):
        p_n_pattern = r"(/^(0|84)(2(0[3-9]|1[0-6|8|9]|2[0-2|5-9]|3[2-9]|4[0-9]|5[1|2|4-9]|6[0-3|9]|7[0-7]" \
                 r"|8[0-9]|9[0-4|6|7|9])|3[2-9]|5[5|6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])([0-9]{8})$/mg)"
        matches4 = re.search(p_n_pattern, phone_number)
        if matches4:
            return True
        else:
            return False

    @classmethod
    def log_in(cls):
        """
        This method takes the username and password and checks if it is correct or not
        """
        for i in range(1, 4):
            user_name = input("please enter your user_name :")
            password = input("please enter your password :")
            id = Administrator_user.generate_id(user_name, password)
            if id in Administrator_user.list_Administrator_user:
                print("welcome ✔")
                logger.info(f"Login by admin with username {Administrator_user.add_admin()[2]} !", exc_info=True)
                break
            else:
                if i == 3:
                    print("Your account has been locked 🔒")
                    logger.warning(f"Account locking !", exc_info=True)
                else:
                    print(f"The user_name or password is incorrect ❌ You have {3 - i} more chances")

    def file_admin(self):
        """
        for submit and edit file
        :return:
        """
        print("for submit names Administrator_user ")

