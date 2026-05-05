import turtle as t

t.bgcolor('black')
t.speed(0)
colors = ['red', 'yellow', 'blue', 'purple', 'cyan', 'green']

for i in range(360):
    t.color(colors[i % 6])
    t.fd(i * 2)
    t.right(61)

t.done()