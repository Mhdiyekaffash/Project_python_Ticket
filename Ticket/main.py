#    In the name of God ❤❤❤❤

# import Administrator_user
# import Event

special_code = 'SniMda1309'  # Special code for admins
introduction = input("who are you ? 1.Admin user or 2.client ! ")
if introduction == '1':
    login_admin = input("\n1.Register\n2.login ?")
    if login_admin == '1':
        """
        ----> Call method add_administrator_user of module Administrator
        """
    if login_admin == '2':
        for i in range(1, 4):
            Admin_password = input("please Enter the admin password : ")
            if Admin_password == special_code:
                print("The password is correct ✔ welcome.")
                """
                ---> Call method log_in of module Administrator 
                *** The event definition operation is written in this section
                """
                break
            else:
                if i == 3:
                    print("sorry ! Your access to the site has been blocked")
                else:
                    print(f"The password is incorrect ❌ You have {3-i} more chances")

