def who_you_know():
    people = input("Enter the people you know with commo separated: ")
    people_list = people.split(",")
    people_list_normal = [pple.strip() for pple in people_list]
    return people_list_normal
def ask_user():
    pple = input("Enter the person you know: ")
    if pple in who_you_know():
        print("You know {}!".format(pple))
ask_user()