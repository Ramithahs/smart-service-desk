import json
import os

class FileRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_requests(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except:
            return []

    def save_requests(self, requests):
        with open(self.file_path, "w") as file:
            json.dump(requests, file, indent=4)