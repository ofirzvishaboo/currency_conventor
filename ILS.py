import API


Current_ils = API.get_data()[2]

class ILS:
    def get_value(self):
        return Current_ils
        # return 0.28

    def calculate(self, user_input):
        return user_input * self.get_value()
