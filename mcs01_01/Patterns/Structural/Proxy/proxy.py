class Document:
    def __init__(self, content):
        self.content = content

    def display(self):
        print(f"Displaying Document: {self.content}")

class ProtectedDocumentProxy:
    """Proxy Class для контролю доступу до документа."""
    def __init__(self, document, user_role):
        self.document = document
        self.user_role = user_role

    def display(self):
        if self.user_role == "authorized":
            self.document.display()
        else:
            print("Access Denied: You are not authorized to view the document.")

# Клієнтський код
if __name__ == "__main__":
    confidential_document = Document("This is a very confidential document.")
    proxy = ProtectedDocumentProxy(confidential_document, "unauthorized")
    proxy.display()  # Повинен вивести "Access Denied: You are not authorized to view the document."

    proxy = ProtectedDocumentProxy(confidential_document, "authorized")
    proxy.display()  # Повинен вивести "Displaying Document: This is a very confidential document."
