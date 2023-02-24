# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# accounts:
# User Model
# 	Phone_number:unique
# 	Email:EF
# 	is_customer:BF
# 	is_admin:BF
# userProfileModel:
# 	owner:OTO(User)
# 	Name:
# 	Date_of_birth:
# 	Gender:choices(MALE,FEMALE,OTHERS)
# 	Image:
# userloginotpModel:
# 	owner:FK(User)
# 	Otp:IF
# 	active:BF
# UserCartProductModel:
# 	owner:FK(User)
# 	product:FK(productMainModel)
# 	status:Choices(pending,completed)
#
# UserCartModel:
# 	owner:OTO(User)
# 	products:MTM(UserCartProductModel)
# 	price:

# Product:
# productMainModel:
# Title:
# Description:
# Unique_id: unique
# Price:
#
# productImageModel:
# product: FK(productMainModel)
# image: IF
