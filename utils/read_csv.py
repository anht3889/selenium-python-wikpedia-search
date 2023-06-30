import csv

class ReadCSV:
    @staticmethod
    def read_data_from_csv( filename):
        data = []
        csvdata = open(filename, "r")
        reader = csv.reader(csvdata)
        # skip header
        next(reader)
        for rows in reader:
            data.append(rows)
        return data

    @staticmethod
    def get_match_data():
        return ReadCSV.read_data_from_csv(f"./data/match_data.csv")
