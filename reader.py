from abc import ABC, abstractmethod
import sys
import csv
import json
import pickle


class FileReader(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass


class FileWriter(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def write(self, data):
        pass


class CSVReader(FileReader):
    def read(self):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data


class JSONReader(FileReader):
    def read(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data


class TXTReader(FileReader):
    def read(self):
        with open(self.filename, 'r') as file:
            data = file.readlines()
        return data


class PickleReader(FileReader):
    def read(self):
        with open(self.filename, 'rb') as file:
            data = pickle.load(file)
        return data


class JSONWriter(FileWriter):

    def write(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)


class CSVWriter(FileWriter):

    def write(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


class TXTWriter(FileWriter):

    def write(self, data):
        with open(self.filename, 'w') as file:
            for line in data:
                file.write(line.rstrip() + '\n')


class PickleWriter(FileWriter):

    def write(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)


class DataTransformer:
    def __init__(self, data, changes, input_format):
        self.data = data
        self.changes = changes
        self.input_format = input_format

    def modify(self):
        for change in self.changes:
            x, y, value = map(str.strip, change.split(','))
            x, y = int(x), int(y)

            if self.input_format == 'csv':
                self.data[y][x] = value
            elif self.input_format == 'json':
                self.data[y][x] = value
            elif self.input_format == 'txt':
                row = self.data[y].split(',')
                row[x] = value
                self.data[y] = ','.join(str(item) for item in row)
            elif self.input_format == 'pkl':
                self.data[y][x] = value

    def display(self):
        for row in self.data:
            print(','.join(str(item) for item in row))
