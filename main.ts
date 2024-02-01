input.onButtonPressed(Button.A, function () {
    bird.change(LedSpriteProperty.Y, -1)
    control.waitMicros(6000)
})
let score = 0
let bad_guy: game.LedSprite = null
let bird: game.LedSprite = null
bird = game.createSprite(1, 2)
basic.forever(function () {
    bad_guy = game.createSprite(5, randint(0, 5))
    control.waitMicros(3000000)
})
basic.forever(function () {
    if (bird.get(LedSpriteProperty.Y) != 5) {
        control.waitMicros(200000)
        bird.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    bad_guy.move(-1)
    control.waitMicros(100000)
    if (bad_guy.isTouchingEdge()) {
        bad_guy.delete()
        score += 1
    }
    if (true) {
    	
    }
})
