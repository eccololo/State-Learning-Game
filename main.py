import turtle
from tkinter import *
from tkinter import messagebox
import pandas as pd


def get_x_y_coordinates_from_map(x, y):
    """Helper function to get coordinates of US States."""
    print(x, y)


root = Tk()
root.destroy()
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("Guess the States Game by Mateusz Hyla")
messagebox.showinfo("Special Chars Message", "In this game use only english alphabet.")
user_choice = screen.textinput(title=f"Country Choice", prompt="Choose: USA / Italy / Poland?").lower()
countries_shorts = {
    "usa": "usa",
    "poland": "pl",
    "italy": "it"
}
country_short = countries_shorts[user_choice]
image = f"./img/blank-states-img-{country_short}.gif"
csv_cords_file = f"./csv/states-{country_short}-cords.csv"

screen.addshape(image)
turtle.shape(image)

states_df = pd.read_csv(filepath_or_buffer=csv_cords_file)
all_states_num = len(states_df.count(axis="columns"))
print(all_states_num)
states_guessed = []

game_is_on = True
while game_is_on:
    player_answer = screen.textinput(title=f"Guess the state of {user_choice}.", prompt="What's another states name?")
    player_answer = player_answer.title()

    if player_answer == "Exit":
        break

    state_series = states_df[states_df["state"] == player_answer]

# Testing Purposes.
# screen.onscreenclick(get_x_y_coordinates_from_map)

screen.mainloop()
