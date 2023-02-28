import turtle


def get_x_y_coordinates_from_map(x, y):
    """Helper function to get coordinates of US States."""
    print(x, y)


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

# screen.onscreenclick(get_x_y_coordinates_from_map)

player_answer = screen.textinput(title="Guess the State.", prompt="What's another states name?")
print(player_answer)


screen.mainloop()


