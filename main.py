import requests
from services import vin_decoder
from services import fuel_economy
test_vin = input("Enter VIN: ") or "1FMHK8D86BGA47454"

vehicle_info = vin_decoder.get_vehicle_info(test_vin)


id = fuel_economy.get_vehicle_identifier(vehicle_info)

print(fuel_economy.get_fuel_economy(id))