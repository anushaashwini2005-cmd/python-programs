class phone:
    def __init__(self,name,phoneno):
        self.name=name
        self.phoneno=phoneno
    def call_contact(self):
        print(f"Name is {self.name} phone number is {self.phoneno}")
    def take_picture(self):
        print(f"{self.name} is taking picture")
ph=phone("Ram",8752457860)
ph.call_contact()
ph.take_picture()