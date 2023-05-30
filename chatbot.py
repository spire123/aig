import re as regx

responses = {
    r"hi|hello|hey": ["Welcome to our restaurant! How can I assist you?"],
    r"menu": ["Our menu includes a variety of dishes, such as burgers, pizzas, and salads. Would you like me to recommend anything?"],
    r"recommendation": ["Based on your preferences, I would recommend our special burger with fries and a drink."],
    r"reservation": ["Sure, let me check availability. How many people will be dining and what time would you like to make a reservation for?"],
    r"hours": ["We're open from 11am to 10pm every day."],
    r"location|directions": ["We're located at 123 Main Street in Nashik. Can I help with directions?"],
    r"thanks|thank you": ["You're welcome! Enjoy your meal."],
    r"food|dishes": ["We use fresh ingredients in all of our dishes to ensure the best quality and taste."],
    r"drinks": ["We offer a variety of non-alcoholic and alcoholic drinks, including beer, wine, and cocktails."],
    r"dessert|sweets": ["Don't forget to save room for dessert! Our most popular desserts are the chocolate cake and the cheesecake."],
    r"vegetarian|veggie": ["We have several vegetarian options on our menu, including a veggie burger and a garden salad."],
    r"gluten-free": ["We also have gluten-free options available, such as a gluten-free pizza crust and a quinoa salad."],
    r"burgers": ["Classic Burger - $10.99", "Cheeseburger - $11.99", "Bacon Burger - $12.99", "Mushroom Swiss Burger - $13.99"],
    r"pizza": ["Pepperoni Pizza - $14.99, Margherita Pizza - $15.99, Hawaiian Pizza - $16.99, BBQ Chicken Pizza - $17.99"],
    r"salads": ["Caesar Salad - $8.99", "Greek Salad - $9.99", "Cobb Salad - $10.99", "Spinach Salad - $11.99"],
    r"desserts": ["Chocolate Cake - $6.99", "Cheesecake - $7.99", "Ice Cream Sundae - $5.99", "Fruit Tart - $8.99"],
    r"drinks": ["Soda - $2.99", "Iced Tea - $3.99", "Lemonade - $4.99", "Coffee - $2.99", "Beer - $5.99", "Wine - $8.99", "Cocktails - $9.99"]
}

def match_response(user_input):
    for pattern, response in responses.items():
        if regx.search(pattern, user_input, regx.IGNORECASE):
            return response
    return ["I'm sorry, I didn't understand your request. Please try again."]


print("Wrlcome to our restaurant. How can I assist you?")
while True: 
    user_input = input("You: ")
    response = match_response(user_input)
    print("Bot: ", response[0])