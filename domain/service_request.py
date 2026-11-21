from domain.exceptions import InvalidPriorityError

class ServiceRequest:
    VALID_PRIORITIES = ["LOW", "MEDIUM", "HIGH"]

    def __init__(self, request_id, employee_name, issue, priority):
        if priority.upper() not in self.VALID_PRIORITIES:
            raise InvalidPriorityError(
                "Priority must be LOW, MEDIUM or HIGH"
            )

        self.request_id = request_id
        self.employee_name = employee_name
        self.issue = issue
        self.priority = priority.upper()
        self.status = "OPEN"

    def resolve(self):
        self.status = "RESOLVED"

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "issue": self.issue,
            "priority": self.priority,
            "status": self.status
        }