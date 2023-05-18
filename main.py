import turtle


def get_x_y_coordinates_from_map(x, y):
    """Helper function to get coordinates of US States."""
    print(x, y)


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("Guess the States Game by Mateusz Hyla")
user_choice = screen.textinput(title=f"Country Choice", prompt="Choose: USA / Italy / Poland?").lower()
countries_shorts = {
    "usa": "usa",
    "poland": "pl",
    "italy": "it"
}
country_short = countries_shorts[user_choice]
image = f"./img/blank-states-img-{country_short}.gif"
csv_cords_file = f"states-{country_short}-cords.csv"

screen.addshape(image)

turtle.shape(image)

game_is_on = True
while game_is_on:
    player_answer = screen.textinput(title="Guess the State.", prompt="What's another states name?")
    if player_answer:
        print(player_answer)
        break

# Testing Purposes.
# screen.onscreenclick(get_x_y_coordinates_from_map)

screen.mainloop()
