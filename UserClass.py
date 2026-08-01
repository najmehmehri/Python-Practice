"""
User Login System with Active Users Counter
Problem: Create a User class that:
1. Only allows specific users to log in
2. Tracks the number of active users
3. Handles user logout
"""

class User:
    
    ActiveUsers = 0               
    AllowedUsers = ["ali", "najme", "arshia"]
    
    def __init__(self, name, family):
        if name not in User.AllowedUsers:
            raise ValueError(f"'{name}' is not allowed to log in")
        
        self.name = name                 # Instance variables
        self.family = family
        User.ActiveUsers += 1
        print(f"✓ {self.name} has logged in")
    
    def logout(self):
        print(f"✓ {self.name} has logged out")
        User.ActiveUsers -= 1
    
    def get_full_name(self):
        return f"{self.name} {self.family}"
    
    @classmethod
    def get_active_users(cls):
        return cls.ActiveUsers



# Test


if __name__ == "__main__":
    print(f"Active users: {User.get_active_users()}")
    
    # Create allowed users
    najme = User("najme", "mehr")
    ali = User("ali", "rezai")
    
    print(f"Active users: {User.get_active_users()}")
    
    # Logout
    najme.logout()
    print(f"Active users: {User.get_active_users()}")
    
    # Access instance methods
    print(f"Full name: {ali.get_full_name()}")