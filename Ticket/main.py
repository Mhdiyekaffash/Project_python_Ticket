#    In the name of God ❤❤❤❤

from datetime import datetime
from File_Handler import FileHandler
from Administrator_user import Administrator_user
from Event import Event
from Ticket_types import Specify_ticket, special_days
from Customer import type_event, date_registration, num_ticket, type_ticket, list_n_c_p, list_num_ticket
import hashlib
import log


special_code = 'SniMda1309'  # Special code for admins
introduction = input("Login as --->  1.Admin user  2.client ! ")
if introduction == '1':
    admin_login = input("\n1.Register\n2.login \nWhich ?  ")
    if admin_login == '1':

        Administrator_user.add_admin()
        path_file_info_admin = 'Registration_admin_account_information.csv'
        my_file = FileHandler(path_file_info_admin)
        my_file.write_file(Administrator_user.Register_admin_information)
        log.logger.info(f"Registration of admin account information whit National_code  "
                        f"{Administrator_user.Register_admin_information['National_code']} !", exc_info=True)

        while True:
            try:
                edit = input("Do you want to edit your information? 1.Yes  2.No ")
                if edit == '1':
                    Administrator_user.edit_admin_information()
                    my_file.edit_row(Administrator_user.Register_admin_information)
                    log.logger.info(f"Edit of admin account information whit National_code "
                                    f"{Administrator_user.Register_admin_information['National_code']} !",
                                    exc_info=True)
                elif edit == '2':
                    break
                else:
                    log.logger.warning('The entered phrase is incorrect', exc_info=True)
            except Exception:
                log.logger.error(f"Error in input data type !", exc_info=True)

        # *-*  Event definition section

        print("Welcome to the event page, dear admin .\n  You can now register your event 📝  ")
        Event.add_event()
        while True:
            try:
                edit_event = input("Do you want to edit your information? 1.Yes  2.No ")
                if edit_event == '1':
                    Event.edit_event_information()
                    print(Event.Recorded_events)
                elif edit_event == '2':
                    break
                else:
                    log.logger.warning('The entered phrase is incorrect', exc_info=True)
            except Exception:
                log.logger.error(f"Error in input data type !", exc_info=True)

        # *-* Ticket section for the event

        Specify_ticket()
        special_days()
        path_file_info_Event = 'Event_information_registration.csv'
        my_file01 = FileHandler(path_file_info_Event)
        my_file01.write_file(Event.Recorded_events)
        log.logger.info(f"Registration {Event.Recorded_events['event_name']} event !", exc_info=True)

    if admin_login == '2':
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
                if my_file.read_file() is False:
                    print("path is incorrect")
                else:
                    b = my_file.read_file()
                    List_of_all_ideas = []
                    for c in b:
                        List_of_all_ideas.append(c['id'])
                    for d in range(1, 4):
                        user_name = input("please enter your user_name :")
                        password = input("please enter your password :")
                        Password_hash = password.encode()
                        Password_hash_01 = hashlib.sha256(Password_hash).hexdigest()
                        user_name_hash = user_name.encode()
                        user_name_hash_01 = hashlib.sha256(user_name_hash).hexdigest()
                        id = Administrator_user.generate_id(user_name_hash_01, Password_hash_01)
                        if id in List_of_all_ideas:
                            print(" ✔")
                            log.logger.info(f"Login by admin with id {id} !", exc_info=True)

                            # *-*  Event definition section

                            Admin_activity = input("1.Add event   2.View ticket status :")
                            if Admin_activity == '1':
                                print("\nWelcome to the event page, dear admin .\n  You can now register your event 📝")
                                Event.add_event()
                                print(Event.Recorded_events)
                                while True:
                                    try:
                                        edit_event = int(input("Do you want to edit your information? 1.Yes  2.No "))
                                        if edit_event == 1:
                                            Event.edit_event_information()
                                            print(Event.Recorded_events)
                                        elif edit_event == 2:
                                            break
                                        else:
                                            log.logger.warning('The entered phrase is incorrect', exc_info=True)
                                    except Exception:
                                        log.logger.error(f"Error in input data type !", exc_info=True)

                                # *-* Ticket section for the event

                                Specify_ticket()
                                special_days()
                                path_file_info_Event = 'Event_information_registration.csv'
                                my_file01 = FileHandler(path_file_info_Event)
                                my_file01.write_file(Event.Recorded_events)
                                log.logger.info(f"Registration {Event.Recorded_events['event_name']} event !",
                                                exc_info=True)
                            elif Admin_activity == '2':
                                path_file_info_Event = 'Event_information_registration.csv'
                                my_file01 = FileHandler(path_file_info_Event)
                                if my_file01.read_file() is False:
                                    print("path is incorrect")
                                else:
                                    f = my_file01.read_file()
                                    List_of_names_of_all_events = []
                                    List_of_capacity_of_all_events = []
                                    for cc in f:
                                        List_of_names_of_all_events.append(cc['event_name'])
                                        List_of_capacity_of_all_events.append(cc['remaining_capacity'])
                                    res = dict(zip(List_of_names_of_all_events, List_of_capacity_of_all_events))
                                    for iii in res:
                                        print(f'Remaining capacity of the event {iii} ---> {res[iii]}')
                            else:
                                log.logger.warning('The entered phrase is incorrect', exc_info=True)

                            break
                        else:
                            if d == 3:
                                print("Your account has been locked 🔒")
                                log.logger.warning(f"Account locking !", exc_info=True)
                                break
                            else:
                                print(f"The user_name or password is incorrect ❌ You have {3 - d} more chances")
                break
            else:
                if i == 3:
                    print("sorry ! Your access to the site has been blocked")
                else:
                    print(f"The password is incorrect ❌ You have {3 - i} more chances")
    else:
        log.logger.warning('The entered phrase is incorrect', exc_info=True)
if introduction == '2':
    Customer_login = input("Dear customer, welcome. \n Press the * button to view the list of events . ")

    if Customer_login == '*':
        path_file_info_Event = 'Event_information_registration.csv'
        my_file01 = FileHandler(path_file_info_Event)
        if my_file01.read_file() is False:
            print("path is incorrect")
        else:
            f = my_file01.read_file()
            List_of_names_of_all_events = []
            for cc in f:
                List_of_names_of_all_events.append(cc['event_name'])
            for count, value in enumerate(List_of_names_of_all_events, start=1):
                print(f'{count}. {value}')
            Customer_selection = input("Enter the name of the event you want : ")
            while True:
                if Customer_selection in List_of_names_of_all_events:
                    d = my_file01.read_file()
                    for x in d:
                        cc = [[k, x[k]] for k in x]
                        if cc[0][1] == Customer_selection:
                            if cc[6][1] == 'Security':
                                print("The event of your choice is security ⚠")
                                type_event()
                                dic_nationa_code = {'national_code': list_n_c_p[-1], 'event_name': cc[0][1]}
                                path_file_Security_Event = 'National_Code_of_Security_Event_Participants.csv'
                                my_file02 = FileHandler(path_file_Security_Event)
                                list_national_code = []
                                try:
                                    for b in my_file02.read_file():
                                        if b['event_name'] == cc[0][1]:
                                            list_national_code.append(b['national_code'])
                                except Exception as E:
                                    print(E)
                                if list_n_c_p[-1] in list_national_code:
                                    print("A user has already registered with this national code")
                                else:
                                    my_file02.write_file(dic_nationa_code)
                                    dic = {'end_date': cc[5][1], 'start_date': cc[4][1]}
                                    date_end = datetime.strptime(dic['end_date'], '%Y-%m-%d %H:%M:%S')
                                    date_s = datetime.strptime(dic['start_date'], '%Y-%m-%d %H:%M:%S')
                                    if date_registration(date_end, date_s):
                                        num_ticket(cc[6][1], int(cc[7][1]))
                                        cc[7][1] = int(cc[7][1]) - 1
                                        x['remaining_capacity'] = int(x['remaining_capacity']) - 1
                                        path_file_info_Event = 'Event_information_registration.csv'
                                        my_file01 = FileHandler(path_file_info_Event)
                                        my_file01.edit_row2(x)
                                        type_ticket(x)
                                        log.logger.info(f"{x['event_name']} event tickets are purchased by a person "
                                                        f"with "
                                                        f"a national code {list_n_c_p[-1]}!", exc_info=True)
                                        print(list_n_c_p)
                                    else:
                                        print("Sorry! Registration deadline has expired .")
                            else:
                                dic = {'end_date': cc[5][1], 'start_date': cc[4][1]}
                                date_end = datetime.strptime(dic['end_date'], '%Y-%m-%d %H:%M:%S')
                                date_s = datetime.strptime(dic['start_date'], '%Y-%m-%d %H:%M:%S')
                                if date_registration(date_end, date_s):
                                    xx = num_ticket(cc[6][1], int(cc[7][1]))
                                    cc[7][1] = int(cc[7][1]) - xx
                                    if type_ticket(x):
                                        x['remaining_capacity'] = int(x['remaining_capacity']) - xx
                                        path_file_info_Event = 'Event_information_registration.csv'
                                        my_file01 = FileHandler(path_file_info_Event)
                                        my_file01.edit_row2(x)
                                    log.logger.info(f"{list_num_ticket[0]} tickets were purchased for the "
                                                    f"{x['event_name']} event", exc_info=True)
                                else:
                                    print("Sorry! Registration deadline has expired .")
                    break
                else:
                    Customer_selection = input("This event is not available! Please re-enter the name of your desired "
                                               "event : ")

    else:
        log.logger.warning('The entered phrase is incorrect', exc_info=True)
else:
    log.logger.warning('The entered phrase is incorrect', exc_info=True)
