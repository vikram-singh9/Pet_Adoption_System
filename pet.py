import uuid

class Pet:
    def __init__(self, name, species, age, breed):
        self.id = str(uuid.uuid4())
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed
        self.adopted = False

    def to_dict(self):
        # converting an obj into dictionary in class's method
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "age":self.age,
            "breed": self.breed,
            "adopted": self.adopted
        }
    
    @staticmethod
    def from_dict(data):
        pet  = Pet(data['name'], data['species'], data['age'], data['breed'])
        pet.id = data["id"]
        pet.adopted = data["adopted"]
        return pet