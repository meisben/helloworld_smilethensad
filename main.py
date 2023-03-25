# Define a function to forever loop sad and happy faces
def on_forever():
    basic.show_icon(IconNames.SAD)
    basic.pause(500)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(500)


# Start of the main program (Show a happy face, then start the forever loop)
basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)