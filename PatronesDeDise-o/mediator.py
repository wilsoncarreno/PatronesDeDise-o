class ChatRoom:
    def show_message(self, user, message):
        print(f"{user}: {message}")

class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom
    def send(self, message):
        self.chatroom.show_message(self.name, message)

# Uso
room = ChatRoom()
u1 = User("Juan", room)
u2 = User("Ana", room)
u1.send("Hola")
u2.send("Hola Juan")
