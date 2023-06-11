class Car(object):
    def __init__(self, model=None):
        self.model = model
        print("init model={}".format(self.model))

    def run(self):
        print("run")


class ToyotaCar(Car):
    def run(self):
        print("fast")


class TeslaCar(Car):
    def __init__(self, model="Model S", enable_auto_run=False, password="123"):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.password = password

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        print("setter called")
        if self.password == "456":
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def auto_run(self):
        if self.__enable_auto_run:
            print("auto run")


print("##########")
tesla_car = TeslaCar("Model A", password="456")
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
tesla_car.auto_run()
print("##########")
