import turtle
import pandas

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"Guess the state?({len(guessed_state)}/50)", prompt="What's the another "
                                                                               "state's ?").capitalize()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        missing_data = pandas.DataFrame(missing_state)
        missing_data.to_csv('learn_missing_state.csv')
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

