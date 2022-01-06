farms = [
    {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
    {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
    {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
]

for farm in farms:
    print(farm["name"], end=" -> ")
    print("Agriculture: ", end=" ")
    for animal in farm["agriculture"]:
        print(animal, end=" ")
    print("\n")
