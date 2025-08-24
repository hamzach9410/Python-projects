import random
import os

#100 amazing facts
facts = [
    "Honey never spoils. Archaeologists found 3000-year-old honey still edible!",
    "Bananas are berries, but strawberries aren't!",
    "Sharks existed before trees.",
    "Your stomach gets a new lining every 3–4 days.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can grow up to 6 inches during summer.",
    "A day on Venus is longer than a year on Venus.",
    "Sloths can hold their breath longer than dolphins.",
    "Hot water freezes faster than cold water – this is called the Mpemba effect.",
    "Wombat poop is cube-shaped.",
    "There are more stars in the universe than grains of sand on all the Earth's beaches.",
    "A group of flamingos is called a 'flamboyance'.",
    "Your body has more bacterial cells than human cells.",
    "Butterflies can taste with their feet.",
    "Water can boil and freeze at the same time.",
    "Cows have best friends.",
    "Sea otters hold hands while sleeping to avoid drifting apart.",
    "There is a species of jellyfish that is biologically immortal.",
    "Some cats are allergic to humans.",
    "It rains diamonds on Jupiter and Saturn.",
    "A cloud can weigh over a million pounds.",
    "Pineapples take about two years to grow.",
    "Mosquitoes are attracted to people who have recently eaten bananas.",
    "There’s enough DNA in your body to stretch from the sun to Pluto and back.",
    "Kangaroos can’t walk backwards.",
    "The inventor of the Pringles can is buried in one.",
    "Shakespeare invented more than 1,700 words.",
    "Banging your head against a wall burns 150 calories an hour.",
    "Avocados are poisonous to birds.",
    "The shortest war in history lasted 38 minutes.",
    "The first oranges weren’t orange.",
    "Peanuts are not nuts; they are legumes.",
    "Snails can sleep for up to three years.",
    "The heart of a blue whale is the size of a small car.",
    "An ostrich’s eye is bigger than its brain.",
    "Humans share 60% of their DNA with bananas.",
    "Polar bear skin is black.",
    "The dot over the letter 'i' is called a tittle.",
    "A jiffy is an actual unit of time: 1/100th of a second.",
    "Bees sometimes sting other bees.",
    "Some fish can recognize human faces.",
    "Coca-Cola was the first soft drink in space.",
    "The first computer virus was created in 1986.",
    "An apple, potato, and onion all taste the same if you eat them with your nose plugged.",
    "There’s a basketball court in the U.S. Supreme Court building.",
    "The longest English word is 189,819 letters long.",
    "Pigeons can recognize themselves in a mirror.",
    "There’s a species of ant that can explode.",
    "Horses can’t vomit.",
    "Elephants can “hear” with their feet.",
    "A cockroach can live for weeks without its head.",
    "Your tongue print is unique, just like fingerprints.",
    "A bolt of lightning is five times hotter than the sun.",
    "Cows produce more milk when they listen to music.",
    "Sea cucumbers can eject their internal organs as a defense mechanism.",
    "A day on Mercury lasts 1,408 hours.",
    "Some turtles can breathe through their butts.",
    "A single strand of spider silk is five times stronger than steel of the same diameter.",
    "A group of porcupines is called a prickle.",
    "Blue whales are the loudest animals on Earth.",
    "The human nose can detect over 1 trillion different scents.",
    "The fingerprints of a koala are almost identical to humans.",
    "Giraffes have no vocal cords.",
    "Otters have a pocket in their skin to store food.",
    "Sharks don’t have bones.",
    "Butter doesn’t actually need to be refrigerated.",
    "A hummingbird’s heart beats up to 1,260 times per minute.",
    "Mice sing to each other.",
    "The moon has moonquakes.",
    "A “moment” technically means 90 seconds.",
    "Tigers have striped skin, not just striped fur.",
    "Bananas glow blue under black light.",
    "Dragonflies have six legs but can’t walk.",
    "There’s a lake in Australia that’s bright pink.",
    "Rainbows can appear at night; they’re called moonbows.",
    "Some frogs can freeze solid and come back to life.",
    "There are more public libraries than McDonald’s in the U.S.",
    "Antarctica is the largest desert in the world.",
    "The smell of freshly cut grass is actually a plant distress signal.",
    "Dolphins have names for each other.",
    "Some metals are so reactive that they explode on contact with water.",
    "A group of crows is called a murder.",
    "There’s a basketball court on the top floor of the U.S. Supreme Court building.",
    "A human can survive longer without food than without sleep.",
    "You can’t burp in space.",
    "There are over 200 dead bodies on Mount Everest.",
    "The average cumulus cloud weighs over a million pounds.",
    "Bamboo can grow up to 35 inches in a single day.",
    "Dogs’ sense of smell is 40 times better than humans.",
    "An octopus has nine brains.",
    "The longest hiccuping spree lasted 68 years.",
    "Birds are the closest living relatives of dinosaurs.",
    "The inventor of the microwave received only $2 for his discovery.",
    "A group of jellyfish is called a smack.",
    "Some worms can jump.",
    "A sneeze can travel up to 100 mph.",
    "There’s enough iron in your blood to make a small nail.",
    "You are taller in the morning than at night."
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print(" Random Fun Fact Generator – Project 16\n")
    print("Type 'next' for another fact or 'q' to quit.\n")

    while True:
        fact = random.choice(facts)
        print(f" {fact}")
        
        user_input = input("\n Your choice (next/q): ").strip().lower()
        clear_screen()
        
        if user_input == 'q':
            print("Thanks for learning something new today! ")
            break

if __name__ == "__main__":
    main()
