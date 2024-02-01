def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
    control.wait_micros(6000)
input.on_button_pressed(Button.A, on_button_pressed_a)

score = 0
bad_guy: game.LedSprite = None
bird: game.LedSprite = None
bird = game.create_sprite(1, 2)

def on_forever():
    global bad_guy
    bad_guy = game.create_sprite(5, randint(0, 5))
    control.wait_micros(3000000)
basic.forever(on_forever)

def on_forever2():
    if bird.get(LedSpriteProperty.Y) != 5:
        control.wait_micros(200000)
        bird.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever2)

def on_forever3():
    global score
    bad_guy.move(-1)
    control.wait_micros(100000)
    if bad_guy.is_touching_edge():
        bad_guy.delete()
    if True:
        score += 1
basic.forever(on_forever3)
