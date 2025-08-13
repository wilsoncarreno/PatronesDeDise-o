class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class AuthHandler(Handler):
    def handle(self, request):
        if request.get("user") == "admin":
            print("Auth OK")
            return super().handle(request)
        print("Auth Failed")

class LogHandler(Handler):
    def handle(self, request):
        print("Logging request:", request)
        return super().handle(request)

# Uso
handler_chain = AuthHandler(LogHandler())
handler_chain.handle({"user": "admin", "data": "test"})
