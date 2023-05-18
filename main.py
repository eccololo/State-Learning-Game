# TODO:
#  1. Create files for Italy and Poland with cordinates data to states.
#  2. Give at the beggining of the game the user a choice to pick a country.
#  3. Implement guessing states for picked country.

import turtle


def get_x_y_coordinates_from_map(x, y):
    """Helper function to get coordinates of US States."""
    print(x, y)


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "./img/blank-states-img-it.gif"

screen.addshape(image)

turtle.shape(image)

# Testing Purposes.
# screen.onscreenclick(get_x_y_coordinates_from_map)

# player_answer = screen.textinput(title="Guess the State.", prompt="What's another states name?")
# print(player_answer)


screen.mainloop()


