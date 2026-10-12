#Q1
altitude = [56.4, 23.2, 19,20,23,34,7,33,56]
battery_voltage = [19, 5, 4, 2, 34, 23]
temperature = [12, 13, 43, 42, 86]
a_limit = 100
b_limit = 20
t_limit = 40
above = 0
below = 0
dic = {"altitude": altitude,
    "voltage": battery_voltage,
    "temperature": temperature}
x = input("Enter the sensor for which you want to do the analysis:\n").strip().lower()
if x in dic:
    readings = dic[x]
    print(readings)
    print("Number of elements =", len(readings))
    print("Minimum =", min(readings))
    print("Maximum =", max(readings))
    print("Average =", sum(readings)/len(readings))
if(x=="altitude"):
    limit = a_limit
elif(x=="voltage"):
    limit = b_limit
else :
    limit = t_limit
for i in readings:
    if(int(i)>limit):
        print("Warning")
        break
y = int(input("Enter a threshold:\n"))
for i in readings:
    if(y<i):
        above +=1
    else:
        below +=1
print("Number of values above threshold = ",above)
print("Number of values below threshold = ",below)

#Q2
drone_fleet = [
    {
        "drone id": "DRN-90210",
        "model name": "SkyRider Pro 4K",
        "current altitude": 45.5,
        "battery percentage": 88,
        "flight mode": "GPS Stabilized"
    },
    {
        "drone id": "DRN-90211",
        "model name": "SkyRider Mini",
        "current altitude": 12.0,
        "batterypercentage": 64,
        "flightmode": "Manual"
    }
]

#Q3
filename = "drone_flights.txt"
try:
    print("Existing Drone Flight Records")
    with open(filename, "r") as file:
        print(file.read())
    new_record = "F191,Charlie,2026-5-10,23:00,8:00\n"
    with open(filename, "a") as file:
        file.write(new_record)
    print("Updated Drone Flight Records")
    with open(filename, "r") as file:
        print(file.read())
except Exception as error:
    print(str(error))