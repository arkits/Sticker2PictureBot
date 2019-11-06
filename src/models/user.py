# Encapsulate data representing a User
class User:
    def __init__(self, tg_id):
        self.id = tg_id
        self.delivery_perference = None