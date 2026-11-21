import json
from domain.exceptions import DuplicateRequestError


class RequestService:

    def __init__(self):

        try:
            with open("data/requests.json", "r") as file:
                self.requests = json.load(file)
        except:
            self.requests = []

    def save_requests(self):

        with open("data/requests.json", "w") as file:
            json.dump(self.requests, file, indent=4)

    def create_request(self):

        request_id = input("Enter Request ID: ")

        for request in self.requests:
            if request["request_id"] == request_id:
                print("Request ID already exists")
                return

        employee_name = input("Enter Employee Name: ")
        issue = input("Enter Issue: ")
        priority = input("Enter Priority: ")

        request = {
            "request_id": request_id,
            "employee_name": employee_name,
            "issue": issue,
            "priority": priority,
            "status": "OPEN"
        }

        self.requests.append(request)
        self.save_requests()

        print("Request Created Successfully")

    def view_requests(self):

        if not self.requests:
            print("No Requests Found")
            return

        for request in self.requests:
            print("\nRequest ID:", request["request_id"])
            print("Employee Name:", request["employee_name"])
            print("Issue:", request["issue"])
            print("Priority:", request["priority"])
            print("Status:", request["status"])

    def search_request(self):

        request_id = input("Enter Request ID: ")

        for request in self.requests:
            if request["request_id"] == request_id:

                print("\nRequest Found")
                print("Request ID:", request["request_id"])
                print("Employee Name:", request["employee_name"])
                print("Issue:", request["issue"])
                print("Priority:", request["priority"])
                print("Status:", request["status"])
                return

        print("Request Not Found")

    def resolve_request(self):

        request_id = input("Enter Request ID: ")

        for request in self.requests:
            if request["request_id"] == request_id:

                request["status"] = "RESOLVED"
                self.save_requests()

                print("Request Resolved")
                return

        print("Request Not Found")