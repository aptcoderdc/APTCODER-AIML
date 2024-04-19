class Sandwich:
    def __init__(self, bread=2, cheese=1, lettuce=1, tomatoes=2):
        self.bread = bread
        self.cheese = cheese
        self.lettuce = lettuce
        self.tomatoes = tomatoes


    def make(self):
        print("Making a sandwich with the following ingredients:")
        print(f"- Bread slices: {self.bread}")
        print(f"- Cheese slices: {self.cheese}")
        print(f"- Lettuce leaves: {self.lettuce}")
        print(f"- Tomato slices: {self.tomatoes}")


    def rate(self):
        print("\nPlease rate the sandwich based on taste, texture, and overall satisfaction (1 to 5):")
        taste = int(input("Taste: "))
        texture = int(input("Texture: "))
        satisfaction = int(input("Overall satisfaction: "))
        return taste, texture, satisfaction




def main():
    print("Welcome to the Sandwich Making Activity!")
    print("Let's start by making a baseline sandwich...")
    
    # Create a baseline sandwich with default quantities
    baseline_sandwich = Sandwich()
    baseline_sandwich.make()
    
    # Evaluate baseline sandwich
    print("\nEvaluation of Baseline Sandwich:")
    baseline_ratings = baseline_sandwich.rate()
    
    print("\nNow, let's experiment with tuning the sandwich!")
    print("Adjust the quantities of ingredients to create your own sandwich.")


    # Allow kids to tune their sandwiches
    print("\nSandwich Tuning:")
    bread = int(input("Enter the number of bread slices: "))
    cheese = int(input("Enter the number of cheese slices: "))
    lettuce = int(input("Enter the number of lettuce leaves: "))
    tomatoes = int(input("Enter the number of tomato slices: "))


    # Create the tuned sandwich
    tuned_sandwich = Sandwich(bread=bread, cheese=cheese, lettuce=lettuce, tomatoes=tomatoes)
    tuned_sandwich.make()


    # Evaluate tuned sandwich
    print("\nEvaluation of Tuned Sandwich:")
    tuned_ratings = tuned_sandwich.rate()


    # Compare ratings
    print("\nComparison of Ratings:")
    print("Baseline Sandwich Ratings:", baseline_ratings)
    print("Tuned Sandwich Ratings:", tuned_ratings)




if __name__ == "__main__":
    main()
