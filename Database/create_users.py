from Database.tables import User


for i in range(1, 11):
    user = User.create_user(username=f"{i}username", email=f"email{i}@gmail.com")