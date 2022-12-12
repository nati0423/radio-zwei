def on_button_pressed_a():
    music.play_melody("B C5 E D C F - A ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
