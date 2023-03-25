//  Define a function to forever loop sad and happy faces
//  Start of the main program (Show a happy face, then start the forever loop)
basic.showIcon(IconNames.Happy)
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Sad)
    basic.pause(500)
    basic.showIcon(IconNames.Happy)
    basic.pause(500)
})
