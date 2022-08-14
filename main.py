

from flask import Flask ,redirect ,url_for ,render_template , request ,flash


from validation import validation
from animal import Animal


app = Flask(__name__)
app.secret_key = "hello"

def get_file(the_animal):
    animal_obj = Animal(
        name_of_zoo=the_animal["name_of_zoo"],
        name_of_animal=the_animal["name_of_animal"],
        family=the_animal["family"],
        hungry=the_animal["hungry"],
        age=the_animal["age"])
    return animal_obj


def pull_file(the_pull_animal):
    animal_obj = Animal(
        name_of_zoo="",
        name_of_animal=the_pull_animal["name_of_animal"],
        family="",
        hungry="",
        age=""
    )
    return animal_obj


@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for("the_feed_animal",))
    return render_template("welcom.html")


@app.route("/the_feed_animal", methods=['POST','GET'])
def the_feed_animal():
    
    if request.method == 'POST':

        animal_test =Animal(
        name_of_zoo="",
        name_of_animal=request.form["animal"],
        family="",
        hungry="",
        age="")
        
        animal_test = animal_test.pull_animal()
        if type(animal_test) == str:
            flash("animal not exist")
            return redirect(url_for("the_feed_animal"))
        else:
            if animal_test.hungry == True:
               flash(f"animal alredy ate :{animal_test.hungry}")
               return redirect(url_for("the_feed_animal"))
            else:
                feed = request.form["ate"]                                                                                                                                  
                if feed == 'True':
                    animal =Animal(
                    name_of_zoo="",
                    name_of_animal=request.form["animal"],
                    family="",
                    hungry="",
                    age="")
                    animal.the_feed_animal()
                    flash(f"will done you feed the animal: {animal_test.name_of_animal} ")
                    return redirect(url_for("the_feed_animal"))
                else:
                    flash(f"animal hungry pleas fedd the: {animal_test.name_of_animal} ")
                    return redirect(url_for("the_feed_animal"))    

    all_name_animal = Animal(
    name_of_zoo="",
    name_of_animal="",
    family="",
    hungry="",
    age="")    
    return render_template("index.html",values=all_name_animal.all_name_animal())


  



@app.route("/add_animal" , methods=['POST','GET'])
def add_animal():


    if request.method == 'POST':
        test = request.form["hungry"]
        if test == 'True':
            test2 = True
        else:
            test2 = False    
        animal_obj = Animal(
        name_of_zoo=request.form["name_of_zoo"],
        name_of_animal=request.form["name_of_animal"],
        family=request.form["family"],
        hungry=test2,
        age=request.form["age"])
    
        animal_obj.add_animal()
        flash("animal add succesfuly")
        return redirect(url_for("add_animal" ))
  
  
    return render_template("add_animal.html")


@app.route("/all_animal")
def all_animal():
    a = Animal(
        name_of_zoo="",
        name_of_animal="",
        family="",
        hungry="",
        age="")
    return render_template("all_animal.html",values=a.all_animal())



@app.route("/delete_animal", methods=['POST', 'GET'])
def delete_animal():

    if request.method == 'POST':
           
            delete_animal =Animal(
            name_of_zoo="",
            name_of_animal=request.form["animal"],
            family="",
            hungry="",                  
            age="")
            if type(delete_animal.delete_animal()) == str:
                flash("animal not exist")
                return redirect(url_for("delete_animal"))
            else:    
                delete_animal.delete_animal()    
                flash("animal delete successfuly")
                return redirect(url_for("delete_animal"))   
                
    all_name_animal = Animal(
    name_of_zoo="",
    name_of_animal="",
    family="",
    hungry="",
    age="")    
    return render_template("delete_animal.html",values=all_name_animal.all_name_animal())
        



@app.route('/allAnimal', methods=['POST', 'GET'])
def pull_all_animal():
    a = Animal(
        name_of_zoo="",
        name_of_animal="",
        family="",
        hungry="",
        age="")

    return f"<h6>{a.all_animal()}</h6>"


@app.route('/pullAnimal', methods=['POST', 'GET'])
def pull_animal():
    if validation(request.is_json, request.json) == True:
        json_animal = pull_file(request.json)
        animal = json_animal.pull_animal()
        if animal == False:
          return  "the animal was not found"
        return animal
    


@app.route('/pullGroup', methods=['POST', 'GET'])
def pull_group():
    if validation(request.is_json, request.json) == True:
        the_group = pull_file(request.json)
        the_group = the_group.animal_group()
        if the_group == False:
            return "the animal was not found"
        return the_group
    else:
        return validation(request.is_json, request.json)

  


@app.route('/the_feed_all_animals', methods=['POST', 'GET'])
def the_feed_all_animals():
    if request.method == 'POST':
        animal = Animal(
            name_of_zoo="",
            name_of_animal="",
            family="",
            hungry="",
            age="")

        animal.the_feed_all_animals()
        flash("all animal ate!!")
        return redirect(url_for("the_feed_all_animals"))
    return render_template("feed_all_animal.html")


if __name__ == '__main__':
    app.run()
