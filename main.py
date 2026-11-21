from application.request_service import RequestService

def main():

    service = RequestService()

    while True:

        print("\nSMART SERVICE DESK SYSTEM")
        print("1. Create Service Request")
        print("2. View All Requests")
        print("3. Search Request")
        print("4. Resolve Request")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service.create_request()

        elif choice == "2":
            service.view_requests()

        elif choice == "3":
            service.search_request()

        elif choice == "4":
            service.resolve_request()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()