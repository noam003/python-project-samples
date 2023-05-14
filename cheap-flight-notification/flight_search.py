import requests

HEADER = "PhmotcgATvhCsZLkNMFm7FcbaHebv11s"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:

    def __init__(self):
        self.apikey = HEADER
        self.flight_to = None
        self.departure = "BOS"
        self.avail = "2023-06-01"
        self.busy = "2023-08-20"
        self.shortest = 2
        self.longest = 3
        self.flight_type = "round"
        self.adults = 4
        self.flight_days = "4,5"

    def day(self, code_place):
        self.flight_to = code_place
        return self.flight_to

    def correct_formatting(self, dates_string):
        new_date = dates_string.split("T")
        new_time = new_date[1][0:5]
        return new_date[0], new_time

    def search(self):
        header = {
            "apikey": self.apikey
        }
        parameters = {
            "curr": "USD",
            "fly_to": self.day(self.flight_to),
            "fly_from": self.departure,
            "date_from": self.avail,
            "date_to": self.busy,
            "nights_in_dst_from": self.shortest,
            "nights_in_dst_to": self.longest,
            "flight_type": self.flight_type,
            "adults": self.adults,
            "fly_days": self.flight_days,
            "fly_days_type": "departure"
        }



        response = requests.get(url = TEQUILA_ENDPOINT, params = parameters, headers = header)
        response.raise_for_status()
        my_dict = response.json()
        lowest_cost = my_dict["data"][0]["price"]

        link = my_dict["data"][0]["deep_link"]

        dep1 = my_dict["data"][0]["route"][0]["local_departure"]
        date1, dep1 = self.correct_formatting(dep1)
        arr1 = my_dict["data"][0]["route"][0]["local_arrival"]
        date1, arr1 = self.correct_formatting(arr1)
        dep2 = my_dict["data"][0]["route"][1]["local_departure"]
        date2, dep2 = self.correct_formatting(dep2)
        arr2 = my_dict["data"][0]["route"][1]["local_arrival"]
        date2, arr2 = self.correct_formatting(arr2)

        start = 0

        # if departure and return dates are the same
        while date1 == date2:
            start += 1

            dep1 = my_dict["data"][start]["route"][0]["local_departure"]
            date1, dep1 = self.correct_formatting(dep1)
            arr1 = my_dict["data"][start]["route"][0]["local_arrival"]
            date1, arr1 = self.correct_formatting(arr1)
            dep2 = my_dict["data"][start]["route"][1]["local_departure"]
            date2, dep2 = self.correct_formatting(dep2)
            arr2 = my_dict["data"][start]["route"][1]["local_arrival"]
            date2, arr2 = self.correct_formatting(arr2)
            lowest_cost = my_dict["data"][start]["price"]
            link = my_dict["data"][start]["deep_link"]

        return lowest_cost, date1, dep1, arr1, date2, dep2, arr2, link
