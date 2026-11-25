import requests

base_url = "https://vpic.nhtsa.dot.gov/api/"

def decode_vin(vin):
    url = f"{base_url}/vehicles/DecodeVinValuesExtended/{vin}"

    response = requests.get(url, params={"format": "json"})

    if response.status_code == 200:
        print("Data retrieved!")

        vin_data = response.json()

        return vin_data["Results"]
    else:
        print(f"Failed to retrieve data \nResponse Code: {response.status_code}")

placeholder_vin = "1FMHK8D86BGA47454" # 2011 Ford Explorer XLT

def get_vehicle_info(vin):
    vin_data = decode_vin(vin)

    relevant_data = {}

    # print(vin_data)
    for i in vin_data:
        relevant_data["Make"] = i["Make"]
        relevant_data["Model"] = i["Model"]
        relevant_data["Year"] = i["ModelYear"]
        relevant_data["Trim"] = i["Trim"]
        relevant_data["FuelTypePrimary"] = i["FuelTypePrimary"]
        relevant_data["FuelTypeSecondary"] = i["FuelTypeSecondary"]
        relevant_data["Engine"] = { "cylinders": i["EngineCylinders"], "hp": i["EngineHP"], "kw": i["EngineKW"], "displacement": i["DisplacementL"]}
        
    return relevant_data

def beautify_info(info):
    vehicleString = f"{info["Year"]} {info["Make"]} {info["Model"]}"
    
    return vehicleString
print(beautify_info(get_vehicle_info(placeholder_vin)))