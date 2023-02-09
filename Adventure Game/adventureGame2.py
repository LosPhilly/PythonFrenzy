# World Map
world_map = {
    'outside': {
        'description': 'You are outside of a castle.',
        'exits': {'west': 'castle'}
    },
    'castle': {
        'description': 'You are inside of a castle.',
        'exits': {'east': 'outside'},
        'objects': {'sword': 'a shiny sword'}
    }
}

# Player
player = {
    'location': 'outside',
    'inventory': []
}

# Game Loop
while True:
    # Print the player's location
    current_location = world_map[player['location']]
    print(current_location['description'])

    # Print the exits from the current location
    exits = current_location['exits']
    print(f"Exits: {', '.join(exits)}")

    # Print the objects in the current location
    objects = current_location.get('objects', {})
    if objects:
        print("You see the following objects:")
        for object_name, object_description in objects.items():
            print(f" - {object_name}: {object_description}")

    # Get player input
    command = input("What do you want to do? ")

    # Handle player movement
    if command in exits:
        player['location'] = exits[command]
    elif command == 'take sword':
        if 'sword' in objects:
            sword = objects.pop('sword')
            player['inventory'].append(sword)
            print(f"You take the sword.")
        else:
            print("There is no sword here.")
    else:
        print("I don't understand that command.")
