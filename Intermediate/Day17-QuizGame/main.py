class User:
    def __init__(self, user_id, username):
        """Constructor, to set (variables, counters, etc.) to their starting values."""
        # print("new user being created")
        self.id = user_id
        self.username = username
        self.followers = 0 # Este no hay que ponerlo como entrada porque por defecto es 0.
        self.following = 0

    def follow(self, user):
        # Usuario al que va a seguir
        user.followers += 1
        # Numero de seguidos
        self.following += 1


# Cada vez que se crea un nuevo objeto de esta clase, se llama a la función init.
User_1 = User("001", "angela")
User_2 = User("002", "jack")

User_1.follow(User_2)

print(User_1.followers)
print(User_1.following)
print(User_2.followers)
print(User_2.following)

# Add an atribute

# User_1.id = "001"
# User_1.username = "angela"

print(User_1.username)
