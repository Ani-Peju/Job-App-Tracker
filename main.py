applications = []

def user_options():
    print("1. Add Application")
    print("2. View Application")
    print("3. Exit")


def add_application():
    company = input("Company:")
    position = input("Position: ")
    status = input("Status: ")
    date_applied = input("Date Applied (MM/DD/YYYY): ")

    application = {
        "company": company,
        "position": position,
        "status": status,
        "date_applied": date_applied
    }
    applications.append(application)

    print("\nApplication added!")


def view_applications():
    print("\nAPPLICATIONS")
    print("-----------------------------------")

    if len(applications) == 0:
        print("No application found.")
        return
    for application in applications:
        print(
            f"{application['company']} - "
            f"{application['position']} - "
            f"{application['status']} - "
            f"{application['date_applied']} "
        )


while True:
    print("\nJOB Application Tracker")
    print("=======================")
    user_options()

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_application()
    elif choice == "2":
        view_applications()
    elif choice == "3":
        print("Thank you! Bye for now.")
        break
    else:
        print("Error! You've entered an invalid option")
