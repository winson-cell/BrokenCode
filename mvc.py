# Define the Model
class Model:
    def __init__(self):
        self.data = None
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data

# Define the View
class View:
    def show_data(self, data):
        print("The data is:", data)

# Define the Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def set_data(self, data):
        self.model.set_data(data)
    
    def update_view(self):
        data = self.model.get_data()
        self.view.show_data(data)

# Example usage
model = Model()
view = View()
controller = Controller(model, view)

controller.set_data("Hello, world!")
controller.update_view()
# Output: The data is: Hello, world!