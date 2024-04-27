import random

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
]

def generate_quote():
    # Select a random quote from the list
    quote = random.choice(quotes)
    return quote

if __name__ == "__main__":
    print("Welcome to the Inspirational Quote Generator!")
    input("Press Enter to generate an inspirational quote...")
    
    # Generate and print a random quote
    quote = generate_quote()
    print("\nHere's your inspirational quote:")
    print(quote)
