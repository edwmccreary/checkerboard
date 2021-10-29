from flask import Flask, render_template

app = Flask(__name__) # Create a new instance of the Flask class called "app"

@app.route('/')
def default():
    return render_template("index.html",rows = 8,cols = 8,color1 = 'red',color2 = 'black')

@app.route('/<int:rows>')
def custom_rows(rows):
    return render_template("index.html",rows = rows,cols = 8,color1 = 'red',color2 = 'black')

@app.route('/<int:rows>/<int:cols>')
def custom(rows,cols):
    return render_template("index.html",rows = rows,cols = cols,color1 = 'red',color2 = 'black')

@app.route('/<int:rows>/<int:cols>/<string:color1>/<string:color2>')
def custom_colors(rows,cols,color1,color2):
    return render_template("index.html",rows = rows,cols = cols,color1 = color1,color2 = color2)

if __name__=="__main__":
    app.run(debug=True)