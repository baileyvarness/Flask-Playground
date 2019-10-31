from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello New Stuff!'

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play/<times>')
def play_adding_boxes(times):
    print("Server Stuff")
    #return "Hello"
    return render_template("index.html", num_times=int(times))

@app.route('/play/<times>/<color>')
def play_adding_box_color(times,color):
    print("Server Stuff")
    #return "Hello"
    return render_template("box_color.html", num_times=int(times), box_color=(color))





if __name__=="__main__":
    app.run(debug=True)