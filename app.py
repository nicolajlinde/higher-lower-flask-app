from flask import Flask
from random import randint, choice

app = Flask(__name__)

random_num = randint(0, 9)
random_color = ['orange', 'purple', 'blue', 'red', 'green', 'yellow']


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<p>Enter the value in the URL after</p> /' \
           '<img src="https://media1.giphy.com/media/glJdAXojfP3wPEg84a/giphy.gif?cid=ecf05e47dz3yfmugazkrmvx3vw05z797w05z83h0oemkhrix&rid=giphy.gif&ct=g" alt="number">'


@app.route('/<int:num>')
def guess_num(num):
    if num == random_num:
        return f'<h1 style="color: {choice(random_color)}">You guessed correct! You won!</h1>' \
               f'<img src="https://media3.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif?cid=ecf05e473mat7lvbipt3m196yd71uxblz1bseam20nc8sfsc&rid=giphy.gif&ct=g">'
    elif num > random_num:
        return f'<h1 style="color: {choice(random_color)}">Too high! Guess again!</h1>' \
               f'<img src="https://media0.giphy.com/media/ICOgUNjpvO0PC/giphy.gif?cid=ecf05e473mat7lvbipt3m196yd71uxblz1bseam20nc8sfsc&rid=giphy.gif&ct=g">'
    else:
        return f'<h1 style="color: {choice(random_color)}">Too low! Guess again!</h1>' \
               f'<img src="https://media1.giphy.com/media/ND6xkVPaj8tHO/giphy.gif?cid=ecf05e47mt481ydgx1c8rxhgephx5xmoxkcg1so5z869tv88&rid=giphy.gif&ct=g">'


if __name__ == '__main__':
    app.run()
