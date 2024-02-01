from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def root_route():
    return render_template("home.html")

@app.route("/anotherRoute")
def another_route():
    return "This is a new Route!"

@app.route("/greet/<string:name>")
def greet(name):

    pet_list = ["Dog" , "Cat" , "Fish" , "Dragon" , "Butterfly"]

    return render_template("greet.html" , name_to_greet = name , pets = pet_list)



if __name__ == "__main__":
    app.run()


