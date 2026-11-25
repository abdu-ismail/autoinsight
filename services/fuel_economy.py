import requests
import math
base_url = f"https://fueleconomy.gov/ws/rest"

def get_vehicle_models(info):
    headers = {"Accept": "application/json"}
    params = {"year": info["Year"], "make": info["Make"]}

    url = f"{base_url}/vehicle/menu/model"
    response = requests.get(url, params=params, headers=headers)

    data = response.json()["menuItem"]

    vehicle_model = ""

    for i in data:

        if str.lower(info["Model"]) in str.lower(i["value"]):
            vehicle_model = i
            if str.lower(info["DriveTrain"]) in str.lower(i["value"]):
                vehicle_model = i


    return vehicle_model

def get_vehicle_identifier(info):
    model = get_vehicle_models(info)
    headers = {"Accept": "application/json"}
    params = {"year": info["Year"], "make": info["Make"], "model": model["value"]}

    url = f"{base_url}/vehicle/menu/options"
    response = requests.get(url, params=params, headers=headers)

    data = response.json()["menuItem"]
    identifier = ""

    for k in data:

        if str(math.ceil(float(info["Engine"]["displacement"]))) in k["text"]:
            identifier = k["value"]

            if info["Engine"]["cylinders"] in k["text"]:
                identifier = k["value"]
                if info["Transmission"] in k["text"]:
                    identifier = k["value"]
                    break

    return identifier
        

def get_fuel_economy(id):
    headers = {"Accept": "application/json"}

    url = f"{base_url}/vehicle/{id}"
    response = requests.get(url, headers=headers)
    data = response.json()

    formatted_data = {"cityMPG": data["city08"], "highwayMPG": data["highway08"], "combMPG": data["comb08"]}

    return formatted_data