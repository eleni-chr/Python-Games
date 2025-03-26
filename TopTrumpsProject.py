# Code written by Eleni Christoforidou, 2023

# This program is an extended version of a Pokémon-based Top Trumps game. Players are given the choice to select a
# Pokémon from multiple random options. The game supports multiple rounds, and the player with the most rounds won is
# declared the winner. In each round, both the player and the computer (opponent) choose a stat (ID, height, weight, or
# base_experience) to compare. The Pokémon with the higher chosen stat wins the round. If both Pokémon have the same
# chosen stat, the round is considered a draw.


import requests
import random


# Get Pokémon data by ID from the API and return a dictionary with required stats
def get_pokemon_by_id(pokemon_id):
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_id)
    response = requests.get(url)
    pokemon_data = response.json()

    pokemon = {
        "name": pokemon_data["name"],
        "id": pokemon_data["id"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"],
        "base_experience": pokemon_data["base_experience"],
    }

    return pokemon


# Generate a random Pokémon by picking a random ID
def random_pokemon():
    random_id = random.randint(1, 151)
    return get_pokemon_by_id(random_id)


# Compare the chosen stats of the player's and opponent's Pokémon and return the winner
def compare_stats(player, opponent, stat):
    if player[stat] > opponent[stat]:
        return "player"
    elif player[stat] < opponent[stat]:
        return "opponent"
    else:
        return "draw"


# Print the stats of a given Pokémon
def print_pokemon_stats(pokemon):
    print("Name: {}".format(pokemon['name'].capitalize()))
    print("ID: {}".format(pokemon['id']))
    print("Height: {}".format(pokemon['height']))
    print("Weight: {}".format(pokemon['weight']))
    print("Base Experience: {}".format(pokemon['base_experience']))


# Choose a Pokémon from the given list
def choose_pokemon(pokemon_list):
    for index, pokemon in enumerate(pokemon_list):
        print("{}:".format(index + 1))
        print_pokemon_stats(pokemon)
        print()

    chosen_index = int(input("Choose a Pokémon by entering its number: ")) - 1
    while chosen_index not in range(len(pokemon_list)):
        chosen_index = int(input("Invalid input. Please choose a valid number: ")) - 1

    return pokemon_list[chosen_index]


# Run the game
rounds = int(input("Enter the number of rounds you want to play: "))
player_score = 0
opponent_score = 0

for i in range(rounds):
    print("Round {}:".format(i + 1))
    print("Select your Pokémon:")

    pokemon_options = [random_pokemon() for _ in range(3)]
    player_pokemon = choose_pokemon(pokemon_options)
    opponent_pokemon = random_pokemon()

    print("\nYour Pokémon stats:")
    print_pokemon_stats(player_pokemon)

    chosen_stat = input("\nWhich stat do you want to use? (id, height, weight, base_experience): ").lower()
    while chosen_stat not in ["id", "height", "weight", "base_experience"]:
        chosen_stat = input("Invalid input. Please choose id, height, weight, or base_experience: ").lower()

    result = compare_stats(player_pokemon, opponent_pokemon, chosen_stat)

    print("\nYour opponent's Pokémon is {}.".format(opponent_pokemon['name'].capitalize()))
    print("\nOpponent's Pokémon stats:")
    print_pokemon_stats(opponent_pokemon)

    if result == "player":
        print("You win this round! Your {} has a higher {} than your opponent's {}.".format(player_pokemon['name'].capitalize(), chosen_stat, opponent_pokemon['name'].capitalize()))
        player_score += 1
    elif result == "opponent":
        print("You lose this round! Your {} has a lower {} than your opponent's {}.".format(player_pokemon['name'].capitalize(), chosen_stat, opponent_pokemon['name'].capitalize()))
        opponent_score += 1
    else:
        print("It's a draw! Both your {} and your opponent's {} have the same {}.".format(player_pokemon['name'].capitalize(), opponent_pokemon['name'].capitalize(), chosen_stat))
    print("\n")

print("Game Over!")
print("Player Score: {}".format(player_score))
print("Opponent Score: {}".format(opponent_score))

if player_score > opponent_score:
    print("Congratulations! You won the game!")
elif player_score < opponent_score:
    print("You lost the game. Better luck next time!")
else:
    print("It's a tie! No one wins this time.")
