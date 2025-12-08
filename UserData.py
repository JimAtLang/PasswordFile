class UserData:
    def __init__(self, first, last, email):
        """
        Args:
            first (str): First name
            last (str): Last name
            email (str): Email
        """
        self.first = first
        self.last = last
        self.email = email
    def __str__(self):
        return f"{self.first} {self.last} {self.email}"