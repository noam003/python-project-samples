import requests
from flight_search import FlightSearch
import datetime
from twilio.rest import Client


def weekday(date):
    date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
    day_name = datetime.datetime.strftime(date_object, "%A")
    return day_name


def return_message(message):
    SID = "AC83f2e25a3142f146ca0138d79253a615"
    TOKEN = "c421ae2ec96992585b7444c7bb790ec1"

    client = Client(SID, TOKEN)

    message = client.messages.create(
        from_='+12707137585',
        body=message,
        to='+19789927814'

    )

    # print(message.sid)

class DataManager:
    sheetly_link = "https://api.sheety.co/ec31c638e139d5216f2a63c7ef1c4f4c/flightDeals/prices"
    response = requests.get(url=sheetly_link)
    response.raise_for_status()
    result = response.json()
    codes = []
    prices = []
    for key, my_list in result.items():
        for item in my_list:
            code = item.get("code")
            # prices.append(item.get("price"))
            flight = FlightSearch()
            flight.day(code)
            lowest_cost, date1, dep1, arr1, date2, dep2, arr2, link = flight.search()

            day1_name = weekday(date1)
            day2_name = weekday(date2)
            message = f"Trip to {code} for ${lowest_cost / 4} pp on \n{day1_name} {date1} at {dep1} to {arr1}\nReturn on {day2_name} {date2} at {dep2} to {arr2}\n"
            return_message(message)

            if code == "JFK":
                city = "New York"
                endpoint_row = "https://api.sheety.co/ec31c638e139d5216f2a63c7ef1c4f4c/flightDeals/prices/2"
            elif code == "AUS":
                city = "Austin"
                endpoint_row = "https://api.sheety.co/ec31c638e139d5216f2a63c7ef1c4f4c/flightDeals/prices/3"
            else:
                city = "Nashville"
                endpoint_row = "https://api.sheety.co/ec31c638e139d5216f2a63c7ef1c4f4c/flightDeals/prices/4"

            sheet_info = {
                "price": {
                    "city": city,
                    "code": code,
                    "cost": lowest_cost / 4,
                    "message": message,
                    "link": link
                }
            }

            update_response = requests.put(url=endpoint_row, json=sheet_info)

