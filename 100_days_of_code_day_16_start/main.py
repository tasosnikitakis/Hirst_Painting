from turtle import Turtle, Screen
from prettytable import PrettyTable

#timmy = Turtle()
#timmy.color("green4")
#print(timmy)
#timmy.shape("turtle")
#timmy.forward(100)
#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)