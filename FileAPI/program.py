#!/usr/local/bin/python3
import json
import xml.etree.ElementTree as xmltree
import os
from FileAPI.logger import Logger


class Program:
    def __init__(self):
        this_folder = os.path.dirname(__file__)
        data_folder = this_folder + '/data'
        self.data_folder = os.path.abspath(data_folder)
        self.logger = Logger(os.path.join(self.data_folder, "log.txt"))

    def run(self):
        try:
            self.log_startup()
            self.load_xml()
            self.load_json()
            self.load_csv()
        except Exception as e:
            print(e.__repr__())

    def log_startup(self):
        self.logger.log("Application starting up...")
        self.logger.log("Data folder: {0}".format(self.data_folder))

    def load_xml(self):
        filename = os.path.join(self.data_folder, "michael-kennedy-blog.xml")
        # TODO: log which xml file is being opened
        self.logger.log("Loading XML file: {0}".format(filename))
        # TODO: Create new ElementTree and parse file
        dom = xmltree.ElementTree()
        dom.parse(filename)
        print()
        print("Titles of recent posts:")
        # TODO: use the xpath expression channel/item to find all blog posts
        items = list(dom.findall("channel/item"))
        self.logger.log("Found {0} titles in RSS feed.".format(len(items)))
        # TODO: loop over and find title and link
        for item in items:
            print("{0} [{1}]".format(
                item.find("title").text,
                item.find("link").text
            ))
        print()

    def load_json(self):
        filename = os.path.join(self.data_folder, "python-course.json")
        # TODO: log which json file is being opened
        self.logger.log("Loading JSON file: {0}".format(filename))
        # TODO: open a file as a standard text file
        # TODO: read the contents into a string
        # TODO: load the string with json module
        # TODO: locate the course Name property, show and log it.
        # TODO: find the course engagements via the Engagements property, print the City of each
        with open(filename, "r") as file_input:
            data = json.loads(file_input.read())
            print("Course title: {0}".format(data["Name"]))
            self.logger.log("Found course title to be: {0}".format(data["Name"]))
            engagements = data["Engagements"]
            print("Number of engagements: {0}".format(len(engagements)))
            print("Locations:")
            for e in engagements:
                print("\t" + e["City"] + " on " + e["StartDate"] + " [active? " + str(e["ActiveEngagement"]) + "]")
        print()

    def load_csv(self):
        filename = os.path.join(self.data_folder, "fx-seven-day.csv")
        # TODO: log which csv file is being opened
        self.logger.log("Loading CSV file: {0}".format(filename))

        # TODO: Answer what is the 7 day average for RUPEEs to USD?
        # (need to go from rupees -> canadian dollars -> usd)
        # hint: build a lookup of each row by ID (e.g. CZK),
        #       store the seven day values as a list of floats.

        lookup = self.build_currency_lookup(filename)
        rupee = lookup["INR"]
        usd = lookup["USD"]
        rupees_per_canadian_dollar = self.average(rupee["values"])
        usa_per_canadian_dollar = self.average(usd["values"])
        rupee_per_usd = usa_per_canadian_dollar / rupees_per_canadian_dollar

        # TODO: show and log the answer 1 USD is worth X Rupees
        # note: this value should be around 60.
        # we have provided an average method below for you to use
        print("1 USD is worth {0} Rupees.".format(rupee_per_usd))
        self.logger.log("1 USD is worth {0} Rupees.".format(rupee_per_usd))

    @staticmethod
    def build_currency_lookup(filename):
        lookup = dict()
        with open(filename, "r") as file_input:
            for line in file_input:
                if line is None:
                    continue
                if line.strip().startswith("#"):
                    continue
                if line.strip().startswith("Date"):
                    continue
                parts = line.split(sep=',')
                entry = {
                    "name": parts[0].strip(),
                    "key": parts[1].strip(),
                    "values": [
                        float(parts[2]),
                        float(parts[3]),
                        float(parts[4]),
                        float(parts[5]),
                        float(parts[6]),
                        float(parts[7]),
                        float(parts[8]),
                    ]
                }

                lookup[entry["key"]] = entry
        return lookup

    @staticmethod
    def average(numbers):
        if len(numbers) <= 0:
            return float('nan')

        return sum(numbers) / float(len(numbers))


if __name__ == "__main__":
    p = Program()
    p.run()
