import requests

base_url = "https://vpic.nhtsa.dot.gov/api/"

def decode_vin(vin):
    url = f"{base_url}/vehicles/DecodeVinValuesExtended/{vin}"
    params = {"format": "json"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Decode VIN: Data retrieved!")

        vin_data = response.json()

        return vin_data["Results"]
    else:
        print(f"Failed to retrieve data \nResponse Code: {response.status_code}")

def get_vehicle_info(vin):
    vin_data = decode_vin(vin)

    relevant_data = {}

    for i in vin_data:
        relevant_data["Make"] = i["Make"]
        relevant_data["Model"] = i["Model"]
        relevant_data["Year"] = i["ModelYear"]
        relevant_data["Trim"] = i["Trim"]
        relevant_data["FuelTypePrimary"] = i["FuelTypePrimary"]
        relevant_data["FuelTypeSecondary"] = i["FuelTypeSecondary"]
        relevant_data["DriveTrain"] = i["DriveType"]
        relevant_data["Transmission"] = i["TransmissionStyle"]
        relevant_data["Engine"] = { "cylinders": i["EngineCylinders"], "hp": i["EngineHP"], "kw": i["EngineKW"], "displacement": i["DisplacementL"]}

    drive = relevant_data["DriveTrain"]
    if "4WD" in drive or "4-Wheel Drive" in drive or "4x4" in drive:
        relevant_data["DriveTrain"] = "4WD"
    if "FWD" in drive or "Front-Wheel Drive" in drive:
        relevant_data["DriveTrain"] = "FWD"
    if "AWD" in drive or "All-Wheel Drive" in drive:
        relevant_data["DriveTrain"] = "AWD"
    if "6x4" in drive or "6x2" in drive or "4x2" in drive or "Other" in drive or "Glider" in drive:
        relevant_data["DriveTrain"] = "Other"

    transmission = relevant_data["Transmission"]

    if "Manual" in transmission or "Standard" in transmission:
        relevant_data["Transmission"] = "Man"
    elif "Continuously Variable Transmission (CVT)" in transmission:
        relevant_data["Transmission"] = "CVT"
    else:
        relevant_data["Transmission"] = "Auto"

    return relevant_data

def beautify_info(info):
    vehicleString = f"{info["Year"]} {info["Make"]} {info["Model"]}"

    return vehicleString
