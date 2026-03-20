import pizza_small
import pizza_large
import pepperoni
import mushrooms
def main():
    p = pizza_small.PizzaSmall()
    p = mushrooms.Mushrooms(p)
    p = pepperoni.Pepperoni(p)

    l = pizza_large.PizzaLarge()
    l = mushrooms.Mushrooms(l)
    print(p.get_description()) # Small Pizza +Mushrooms +Pepperoni
    print(p.get_price())       # 8.5
    
    print(l.get_description()) # Small Pizza +Mushrooms +Pepperoni
    print(l.get_price())   
main() 