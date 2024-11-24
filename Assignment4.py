state_capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield"
}
state = input("Enter the name of a state: ")
capital = state_capitals.get(state, "State not found")
print(f"The capital of {state} is {capital}.")