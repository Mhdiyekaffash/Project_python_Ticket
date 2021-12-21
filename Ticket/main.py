#    In the name of God ❤❤❤❤
# import File_Handler
from File_Handler import FileHandler
import logging
import Administrator_user
from Administrator_user import Administrator_user
import hashlib
# import Administrator_user
# import Event


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

special_code = 'SniMda1309'  # Special code for admins
introduction = input("who are you ? 1.Admin user or 2.client ! ")
if introduction == '1':
    login_admin = input("\n1.Register\n2.login ?")
    if login_admin == '1':
        """
        ----> Call method add_admin of module Administrator
        """
        Administrator_user.add_admin()
        print(Administrator_user.Register_admin_information)
        path_file_info_admin = 'Registration_admin_account_information.csv'
        my_file = FileHandler(path_file_info_admin)
        my_file.write_file(Administrator_user.Register_admin_information)
        logger.info(f"Registration of admin account information whit National_code  "
                    f"{Administrator_user.Register_admin_information['National_code']} !", exc_info=True)
        while True:
            try:
                edit = int(input("Do you want to edit your information? 1.Yes  2.No "))
                if edit == 1:
                    Administrator_user.edit_admin_information()
                    print(Administrator_user.Register_admin_information)
                    my_file.edit_row(Administrator_user.Register_admin_information)
                    logger.info(f"Edit of admin account information whit National_code "
                                f"{Administrator_user.Register_admin_information['National_code']} !", exc_info=True)
                elif edit == 2:
                    break
            except Exception:
                logger.error(f"Error in input data type !", exc_info=True)
    if login_admin == '2':
        for i in range(1, 4):
            Admin_password = input("please Enter the admin password : ")
            if Admin_password == special_code:
                print("The password is correct ✔ welcome.")
                """
                ---> Call method log_in of module Administrator 
                *** The event definition operation is written in this section
                """

                path_file_info_admin = 'Registration_admin_account_information.csv'
                my_file = FileHandler(path_file_info_admin)
                print(my_file.read_file())
                if my_file.read_file() is False:
                    print("path is incorrect")
                else:
                    b = my_file.read_file()
                    List_of_all_ideas = []
                    for c in b:
                        List_of_all_ideas.append(c['id'])
                    print(List_of_all_ideas)
                    for d in range(1, 4):
                        user_name = input("please enter your user_name :")
                        password = input("please enter your password :")
                        Password_hash = password.encode()
                        Password_hash_01 = hashlib.sha256(Password_hash).hexdigest()
                        user_name_hash = user_name.encode()
                        user_name_hash_01 = hashlib.sha256(user_name_hash).hexdigest()
                        # print(user_name_hash_01)
                        id = Administrator_user.generate_id(user_name_hash_01, Password_hash_01)
                        if id in List_of_all_ideas:
                            print("welcome ✔")
                            logger.info(f"Login by admin with id {id} !", exc_info=True)
                            break
                        else:
                            if d == 3:
                                print("Your account has been locked 🔒")
                                logger.warning(f"Account locking !", exc_info=True)
                                break
                            else:
                                print(f"The user_name or password is incorrect ❌ You have {3 - d} more chances")
                break
            else:
                if i == 3:
                    print("sorry ! Your access to the site has been blocked")
                else:
                    print(f"The password is incorrect ❌ You have {3 - i} more chances")
