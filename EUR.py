import API


Current_eur = API.get_data()[1]
class EUR:
    def get_value(self):
        # return 4.27
        return Current_eur

    def calculate(self, user_input):
        return user_input / self.get_value()
