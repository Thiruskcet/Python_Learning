class print_data:
    def __init__(self, sensor, read):
        self.input_v = sensor
        self.input_r = read
    def print_info(self):
        print(f"Test data {self.input_v} : {self.input_r}")
