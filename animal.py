
from mammals import Mammals
from zooTable import Zoo
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine('postgresql://postgres:yossef7875@localhost:5432/myzoo',  echo=False)
Session = Session(bind=engine)



class Animal(Mammals):

    def __init__(self,  name_of_zoo,name_of_animal, family, hungry, age):

        super().__init__(name_of_zoo, family)

        self.name_of_animal = name_of_animal
        self.hungry = hungry
        self.age = age

    def add_animal(self):

        # Session = engenes()

        animal_obj = Zoo(
            name_of_zoo= self.name_of_zoo,
            name_of_animal= self.name_of_animal,
            family= self.family,
            hungry= self.hungry,
            age= self.age
            )
        try:
         # a(True)
         Session.add(animal_obj)
         Session.commit()
         return "Animal added successfully"
        except:
         return  "Animal ""not"" added successfully"

    def delete_animal(self):
        # Session = engenes()
        x = Session.query(Zoo).filter(Zoo.name_of_animal == self.name_of_animal).delete()
        Session.commit()
        if x:
            return True
        return "animal not exist"

    
    def all_animal(self):

        all_anima = dict()
        len_animal = Session.query(Zoo).all()
        for j in range(0, len(len_animal)):
            for i in len_animal:
              z = dict({
                    "id": i.id,
                    "name_of_zoo": i.name_of_zoo,
                    "name_of_animal": i.name_of_animal,
                    "family": i.family,
                    "hungry": i.hungry,
                    "age": i.age
                })

              all_anima[j] = f'{j} {z}'

        return  len_animal

    def all_name_animal(self):

        len_animal = Session.query(Zoo.name_of_animal).all()
    
        return  len_animal

    

    def pull_animal(self):

        try:
            animal = Session.query(Zoo).filter(Zoo.name_of_animal == self.name_of_animal).one()
            Session.commit()

            animal_send = Animal(
                name_of_zoo=animal.name_of_zoo,
                name_of_animal=animal.name_of_animal,
                family=animal.family,
                hungry=animal.hungry,
                age=animal.age
                

            )
            
            
            return animal_send
        except:
            return "animal not exist"

    def animal_group(self):
        # Session = engenes()
        try:
            x = Session.query(
                Zoo.id,
                Zoo.name_of_zoo,
                Zoo.name_of_animal,
                Zoo.family,
                Zoo.hungry,
                Zoo.age
            ).filter(Zoo.name_of_animal == self.name_of_animal
                     ).group_by(
                Zoo.id,
                Zoo.name_of_zoo,
                Zoo.name_of_animal,
                Zoo.family,
                Zoo.hungry,
                Zoo.age).all()
            Session.commit()
            return str(x)
        except:
            return False

    
    def the_feed_animal(self):
      

        print(self.name_of_animal)
        test = self.name_of_animal
        
        change_animal = Session.query(Zoo).filter_by(name_of_animal= test).first()
        change_animal.hungry = True
        Session.commit()
        
        return "sdfs"
        
            


        

    def the_feed_all_animals(self):
      # Session = engenes()
      try:
        Session.query(Zoo).filter(Zoo.hungry).update({"hungry": False})
        Session.commit()
        return "all animals ate"

      except:
        return "noooo"
      