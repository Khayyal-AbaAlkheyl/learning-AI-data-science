class Vechile:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def moves(self):
        print("moves along..")
    def get_make_model(self):
        print(f"I'am a {self.make} {self.model} owner")

my_car=Vechile('Tesla','m3')

print(my_car.model)
print(my_car.make)
my_car.moves()


my_car.get_make_model()
my_car.moves()

your_car=Vechile("sonata","smart")
your_car.get_make_model()
your_car.moves()

############

class Airplan(Vechile):
   def __init__(self,make,model,faa_id):
    super().__init__(make,model)
    self.faa_id=faa_id
   def moves(self):
       print("flying away")

class Truck(Vechile):
    def moves(self):
        print("shvling away")

class golfcart(Vechile):
    pass

cessna=Airplan("Cessna","Skymark",'N1---222')
mack=Truck("Mack","Pinnacle")
golfwagon=golfcart("golfwagon","GC100")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print("\n\n\n")

for v in (my_car,your_car,cessna,mack,golfwagon):
    v.get_make_model()
    v.moves()
