class Cargo:
    def __init__(self, description, destination_name):
        self.description = description
        self.destination_name = destination_name

    def get_description(self):

        return self.description

    def get_destination(self):

        return self.destination_name
