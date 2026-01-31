name=input("Enter full name:")
email=input("Enter email:")
mobile=input("Enter mobile:")
age=int(input("Enter age:"))
valid=True
if name != name.strip() or name.count(" ") < 1:
    valid = False
if email.count("@") != 1 or email.count(".") < 1 or email[0] == "@":
    valid = False
if len(mobile) != 10 or not mobile.isdigit() or mobile[0] == "0":
    valid = False
if age < 18 or age > 60:
    valid = False
if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
  
