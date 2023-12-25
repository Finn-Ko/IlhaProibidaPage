from browser import document, window

# Python code to draw on the canvas
def draw_on_canvas():
    canvas = document['gameCanvas']
    ctx = canvas.getContext('2d')

    # Example: Draw a red rectangle
    ctx.fillStyle = 'green'
    ctx.fillRect(50, 50, 200, 100)

# Run the Python code on page load
draw_on_canvas()