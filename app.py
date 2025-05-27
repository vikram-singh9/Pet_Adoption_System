import streamlit as st
from pet import Pet
from pet_manager import PetManager

manager  = PetManager()

st.title("🐶 Pet Adoption System")
menu = st.sidebar.selectbox('Menu', ["Add Pet", "View Pets", "Adopt Pet", "View Adopted Pets", "Remove Pet"])

# adding a pet 

if menu == "Add Pet":
    st.subheader(" Add a New Pet")
    name = st.text_input("Pet Name")
    species = st.selectbox("Species", ["Dog🐕", "Cat😾", "Rabbit🐰", "Bird 🕊"])
    age = st.number_input("Age",min_value=0)
    breed = st.text_input("Breed")

    if st.button("Add Pet"):
        new_pet = Pet(name, age, species, breed)
        manager.add_pet(new_pet)
        st.success(f"✅ Pet {name} added successfully!")

# viewing all pets
elif menu == "View Pets":
    st.subheader("Available Pets")
    pets = manager.get_available_pets()

    if pets:
        for pet in pets:
            st.write(f"**{pet.name}** - {pet.species}, {pet.age}, {pet.breed}")
    else:
        st.warning("No pets available for adoption at the moment.")

# adopting a pet
elif menu == "Adopt Pet":
    pets = manager.get_available_pets()
    pet_options = {f"{pet.name} - {pet.species}": pet.id for pet in pets}
    if pet_options:
        choice = st.selectbox('choose a pet ', list(pet_options.keys()))
        if st.button("Adopt"):
            manager.adopt_pet(pet_options[choice])
            st.success("🎉 Congratulations! Pet adopted.")

elif menu == "View Adopted Pets":
    adopted = manager.get_adopted_pets()
    if adopted:
        for pet in adopted:
            st.write(f"**{pet.name}** - {pet.species}, {pet.age} years, {pet.breed}")


elif menu == "Remove Pet":
    all_pets = manager.pets
    pet_options = {f'{pet.name} - {pet.species}': pet.id for pet in all_pets}
    if pet_options:
        choice = st.selectbox('Select a Pet to remove', list(pet_options.keys()))
        if st.button("Remove"):
            manager.remove_pet(pet_options[choice])
            st.success('Pet removed successfully')
