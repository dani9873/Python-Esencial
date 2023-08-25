""" respository json"""
import json

class JsonRepository:
    """ JsonRepository """
    def __init__(self):
        self.filename = "data.json"
    
    def write(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file)

    def read(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
        return data
    
    def add(self, data):
        data_list = self.read()
        data_list.append(data)
        return self.write(data_list)
        
    def delete(self, data):
        data_list = self.read()
        data_list.remove(data)
        self.write(data_list)