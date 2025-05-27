import json
import os 
from pet import Pet


DATA_FILE = "data/pets.json"
class PetManager:
    def __init__(self):
        self.pets = self.load_pets()

    def load_pets(self):
        if not os.path.exists(DATA_FILE):
            return []
        else:
            with open(DATA_FILE, "r")  as file:
                return [Pet.from_dict(p) for p in json.load(file)]
            
    def save_pets(self):
        with open(DATA_FILE, "w") as file:
            json.dump([p.to_dict() for p in self.pets], file, indent=2)

    def add_pet(self, pets):
        self.pets.append(pets)
        self.save_pets()

    def get_available_pets(self):
        return [pet for pet in self.pets if not pet.adopted]
    
    def get_adopted_pets(self):
        return [ pet for pet in self.pets if pet.adopted]
    
    def adopt_pet(self, pet_id):
        for pet in self.pets:
            if pet.id == pet_id:
                pet.adopted = True
                self.save_pets()
                return True
        return False
    
    def remove_pet(self, pet_id):
        self.pets =  [pet for pet in self.pets if pet.id != pet_id]
        self.save_pets()


