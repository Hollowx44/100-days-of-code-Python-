import art
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 170,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
  
def report():
    for details in resources:
        print(details.title(),":",resources[details])
    print(f"Money : ₹{profit["profit"]}")
def order(prompt):
    items=MENU[prompt]["ingredients"]
    for qty in items:
        if items[qty] > resources[qty]:
            print(f"Sorry there is not enough {qty}")
            return
    payment()

def payment():
    price=MENU[prompt]["cost"]
    money=float(input("Insert cash :"))
    if money >= price:
        print(f"Payment successful ---> Enojoy your {prompt.title()}")
        items=MENU[prompt]["ingredients"]
        for qty in items:
            resources[qty] -= items[qty]
        profit["profit"] += price
        if money > price:
           print(f"Here's your change {money - price}")
    elif money < price:
        print("Not enough money....MONEY REFUNDED")
profit={"profit":0}
while True:        
    print(art.logo)
    prompt=input("What would you like? (espresso/latte/cappuccino) :").lower()
    if prompt == "off":
        break
    elif prompt == "report":
        report()
    elif prompt in ("espresso","latte","cappuccino"):
        order(prompt)
    else:
        print("No such item!")
