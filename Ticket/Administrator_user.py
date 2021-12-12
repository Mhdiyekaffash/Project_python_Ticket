import logging
from File_Handler import FileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create handlers and set level
stream_handler = logging.StreamHandler()
stream_handler.setLevel(level=logging.INFO)
file_handler = logging.FileHandler('Administrator_user')
file_handler.setLevel(level=logging.WARNING)
# create formatters and add it to handlers
stream_format = logging.Formatter('%(asctime)s ::%(levelname)s - %(name)s - %(filename)s - %(message)s')
file_format = logging.Formatter('%(asctime)s ::%(levelname)s - %(filename)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)
# add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.debug('this is a debug message')
logger.info('this is an info message')
logger.warning('this is an warning message')
logger.error('this is an error message')
logger.critical('this is an critical message')


class Administrator_user:
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
    def add_administrator_user(cls):  # add new account for administrator_user
        name = input("please enter your First name :")
        l_name = input("please enter your Last name :")
        user_name = input("please enter your user_name :")
        password = input("please enter your password :")
        re_pass = input("please Re-enter your password :")
        # چک شود حتما دو پسورد یکی باشن
        phone_number = int(input("please enter your phone_number :"))
        national_code = int(input("please enter your national_code :"))
        email_address = input("please enter your email_address :")
        id = cls.generate_id(user_name, password)
        cls.list_Administrator_user.append(id)

        return name, l_name, user_name, password, re_pass, phone_number, national_code, email_address

    def check_email(self, email_address):
        print("To check the correctness of the email")

    def check_national_code(self, national_code):
        print("To check the correctness of the national_code")

    @classmethod
    def log_in(cls):
        """
        این متد نام کاربری و پسورد رو میگیره و چک میکنه که ایا صحیح است یا خیر
        """
        user_name = input("please enter your user_name :")
        password = input("please enter your password :")

        id = Administrator_user.generate_id(user_name, password)  # braye inke check konim ghablan sabtnam shode ya na
        try:
            if id in Administrator_user.list_Administrator_user:
                print("میتونید وارد بشید")
            else:
                raise Exception
        except Exception as E:
            logger.error("expection occured here !", exc_info=True)
            print("There is no user by this name, please try again")
            # if bishtar az 3 bar eshtebah vared kard ---> logger.critical("expection occured here !", exc_info=True)

    def file_admin(self):  # for submit names Administrator_user
        print("for submit names Administrator_user ")


