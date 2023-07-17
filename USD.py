import API


Current_usd = API.get_data()[0]

class USD:
    def get_value(self):
        return Current_usd
        # return 3.52

    def calculate(self, user_input):
        return user_input * self.get_value()
