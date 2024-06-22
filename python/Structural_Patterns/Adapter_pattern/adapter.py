from TypeC import  TypeC
class Adapter(TypeC):
    def charger(self):
        return f"Adapter: {self.charge()}"