from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", color="white")

@app.route('/', methods=["POST"])
def indexcolor():
    try:
        red = int(request.form['red'])
        green = int(request.form['green'])
        blue = int(request.form['blue'])
        print red, green, blue
    except ValueError:
        print "error"
        return redirect("/")
    if blue < 1 or blue > 255 or red < 1 or red > 255 or green < 1 or green > 255:
        return redirect("/")
    else:
        stringy = "rgb("+str(red)+", "+str(green)+", "+str(blue)+")"
        return render_template("index.html", color=stringy)


app.run(debug=True)