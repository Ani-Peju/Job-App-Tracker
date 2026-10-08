applications = []


def user_options():
    print("1. Add Application")
    print("2. View Applications")
    print("3. Update Application")
    print("4. Exit")


def add_application():
    application_id = len(applications) + 1
    company = input("Company: ")
    position = input("Position: ")
    status = input("Status: ")
    date_applied = input("Date Applied (MM/DD/YYYY): ")

    application = {
        "application_id": application_id,
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
            f"{application['application_id']} - "
            f"{application['company']} - "
            f"{application['position']} - "
            f"{application['status']} - "
            f"{application['date_applied']} "
        )


def update_application():
    application_id = int(input("\nEnter application ID: "))
    found = False

    for application in applications:
        if application["application_id"] == application_id:
            application["status"] = input("Update your status: ")
            found = True

    if found:
        print("Update Complete")
    else:
        print("Application not found")


while True:
    print("\nJob Application Tracker")
    print("=======================")
    user_options()

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_application()
    elif choice == "2":
        view_applications()
    elif choice == "3":
        view_applications()
        update_application()
    elif choice == "4":
        print("Thank you! Bye for now.")
        break
    else:
        print("Error! You've entered an invalid option")
