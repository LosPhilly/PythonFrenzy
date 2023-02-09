# Define the locations in our world map
living_room = "You are in the living room. There is a couch and a TV."
kitchen = "You are in the kitchen. There is a refrigerator and a sink."
bathroom = "You are in the bathroom. There is a toilet and a shower."
bedroom = "You are in the bedroom. There is a bed and a dresser."


# Map each location to its description
map = {
    "living room": living_room,
    "kitchen": kitchen,
    "bathroom": bathroom,
    "bedroom": bedroom
}

# Function to move the player between locations
def move(current_location, destination):
    if destination in map:
        current_location = destination
        print(map[destination])
    else:
        print(f"Sorry, there is no {destination} in our world.")
# Start the game loop
current_location = "living room"
print(map[current_location])
while True:
    destination = input("Where would you like to go? (Type 'quit' to exit.)")
    if destination.lower() == "quit":
        break
    move(current_location, destination.lower())
