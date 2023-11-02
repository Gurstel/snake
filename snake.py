from cmu_112_graphics import*
import random, time

def appStarted(app):
    app.margin = 5
    app.topMargin = 30
    app.gridWidth = app.width - app.margin*2
    app.gridHeight = app.height - app.margin - app.topMargin
    app.row = 10
    app.col = 10
    app.cellWidth = app.gridWidth/app.col
    app.cellHeight = app.gridHeight/app.row
    app.snake = [(1,2), (2,2), (3,2), (4,2)]
    app.score = 0
    app.topScore = 0
    app.direction = (1,0)
    app.timerDelay = 100
    app.apple = (3,1)
    app.startTime = 0
    app.timeElapsed = 0
    app.gameOver = False
    app.pause = True
    app.directionChosen = True
    app.start = True

def restart(app):
    app.snake = [(1,2), (2, 2), (3,2), (4,2)]
    app.apple = app.apple = (3,1)
    app.score = 0
    app.direction = (1,0)
    app.timerDelay = 100
    app.startTime = time.time()
    app.timeElapsed = 0
    app.gameOver = False
    app.pause = True
    app.directionChosen = True
    app.start = True

def cellBounds(app, row, col):
    x0 = app.margin + app.cellWidth * col
    x1 = app.margin + app.cellWidth * (col+1)
    y0 = app.topMargin + app.cellHeight * row
    y1 = app.topMargin + app.cellHeight * (row+1)
    return x0, x1, y0, y1

def keyPressed(app, event):
    if event.key == event.key and app.start:
         app.startTime = time.time()
         app.start = False
         app.pause = False
    if event.key.isdigit():
        if int(event.key) < 7:
            app.row = 10 + int(event.key)
            app.col = 10 + int(event.key)
        else:
            app.row = int(event.key)
            app.col = int(event.key)
        restart(app)
        app.topScore = 0
    elif event.key == "Up" and not (app.direction == (0, 1) or app.direction == (0, -1))  and app.directionChosen:
        app.direction = (0, -1)
        app.directionChosen = False
    elif event.key == "Down" and not (app.direction == (0, 1) or app.direction == (0, -1)) and app.directionChosen:
        app.direction = (0, 1)
        app.directionChosen = False
    elif event.key == "Left" and not (app.direction == (1, 0) or app.direction == (-1, 0)) and app.directionChosen:
        app.direction = (-1, 0)
        app.directionChosen = False
    elif event.key == "Right" and not (app.direction == (1, 0) or app.direction == (-1, 0)) and app.directionChosen:
        app.direction = (1, 0)
        app.directionChosen = False
    elif event.key == 'p':
        app.pause = not app.pause
    elif event.key == 'r' and app.gameOver:
        restart(app)
    elif event.key == 'Space':
        doStep(app)
    app.cellWidth = app.gridWidth/app.col
    app.cellHeight = app.gridHeight/app.row

def convertTime(time):
    minute = int(time//60)
    second = int(time%60)
    millisecond = int(round(time%1, 3) * 1000)
    return f"{minute}:{second}:{millisecond}"

def timerFired(app):
    if app.pause or app.start:
        return
    app.timeElapsed = time.time() - app.startTime
    doStep(app)

def doStep(app):
    oldHead = app.snake[-1]
    newHead = oldHead[0] + app.direction[0], oldHead[1] + app.direction[1]
    if ((newHead[0] < 0 or newHead[0] == app.col)
        or (newHead[1] < 0 or newHead[1] == app.row) or newHead in app.snake):
        restart(app)
        app.pause = True
        app.gameOver = True
    else:
        app.snake.append(newHead)
    if app.apple in app.snake:
        createApple(app)
        app.score += 1
        if app.score > app.topScore:
            app.topScore += 1
    else:
        app.snake.pop(0)
    app.directionChosen = True

def createApple(app):
    if len(app.snake) == app.col * app.row:
        return
    while True:
        app.apple = (random.randrange(app.col),random.randrange(app.row))
        if not app.apple in app.snake:
            break

def redrawAll(app, canvas):
    if app.gameOver:
        drawGameOver(app, canvas)
    else:
        drawTitleAndScoresAndTimer(app, canvas)
        drawGrid(app, canvas)
        drawSnake(app, canvas)
        drawApple(app, canvas)

def drawGameOver(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text = "Game Over!\nPress r to restart", 
                        font = "Times 24 bold", justify = "center")

def drawGrid(app, canvas):
    for row in range(app.row):
        for col in range(app.col):
            x0, x1, y0, y1 = cellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)

def drawTitleAndScoresAndTimer(app, canvas):
    #Title
    canvas.create_text(app.width/2, 0, text = "Snake!", font = "Times 24 bold", anchor = 'n')
    #Score
    canvas.create_text(app.width - 5, 0, text = f"Score: {app.score}", font = "Times 24 bold", anchor = 'ne')
    #Top Score
    canvas.create_text(5, 0, text = f"Top Score: {app.topScore}", font = "Times 24 bold", anchor = 'nw')
    #Timer
    canvas.create_text(175, 0, text = f"Time: {convertTime(app.timeElapsed)}", font = "Times 24 bold", anchor = 'nw')

def drawSnake(app, canvas):
    scalingFactor = app.cellWidth/30
    for (col, row) in app.snake:
        x0, x1, y0, y1 = cellBounds(app, row, col)
        x0 += scalingFactor
        x1 -= scalingFactor
        y0 += scalingFactor
        y1 -= scalingFactor
        canvas.create_oval(x0, y0, x1, y1, fill = 'green')
        if (col, row) == app.snake[-1] and app.direction[1] != 0:
            canvas.create_text((x0+x1)/2, (y0+y1)/2, text = ". .", font = "Times 55")
        elif (col, row) == app.snake[-1] and app.direction[0] != 0:
            canvas.create_text((x0+x1)/2, (y0+y1)/2, text = ":", font = "Times 55")

def drawApple(app, canvas):
    x0, x1, y0, y1 = cellBounds(app, app.apple[1], app.apple[0])
    canvas.create_rectangle(x0, y0, x1, y1, fill = 'red')

def main():
    runApp(width=750, height=750)

if __name__ == '__main__':
    main()