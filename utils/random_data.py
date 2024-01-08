from faker import Faker

fake = Faker()

def username():
    username = fake.user_name()
    return username

def password():
    password = fake.password(length=15)
    return password

def email():
    email = fake.email()
    return email


# email_user = email()
# password_user = password()
# username = username()
#
# print(type(email_user))
# print(password_user)
# print(type(username))