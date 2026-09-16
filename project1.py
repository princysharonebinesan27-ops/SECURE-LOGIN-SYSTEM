print("\n==========SECURE LOGIN SYSTEM==========\n")#displaying the title "secure login system"
user=input("\nEnter Username:")#to get  username from user 
pw=int(input("\nenter password:"))#to get password from user
password=123#assinging the password
if pw == password:#assinging the password to the variable name "pw"
    print("\nLogin Credentials Verified!")#displaying login credentials verified
else:#using else part to declare the alternate output
    print("\ninvalid password")#displaying invalid password when wrong password is given by the user
otp=583214#assinging the otp number
attempts=3#assinging the number of attempts
for i in range(attempts):#using for loop to use the 3 attempts
    user_otp=int(input("\nenter the otp:"))#to get user_otp from user
    if user_otp==otp:#using if statement to check the correct otp
        print("\nOTP verification successful!")#displaying otp verification successful when the otp is correct
        break
    else:#using else part to declare the alternate output
        print("\ninvalid otp")#displaying that the otp is wrong
        if i < attempts -1:#assigning the condition for continuos loop
            print("\ntry again")#displaying try again for wrong otp    
        else:#using else part to declare the alternate output
            print("access denied")#displaying that the entered otp is wrong
            print("\n=================================")
            print("\nLOGIN SUCCESSFUL")#displaying login successful
            print("\n=================================")
