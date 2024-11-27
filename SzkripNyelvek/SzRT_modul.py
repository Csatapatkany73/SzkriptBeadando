class SzRTClass:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Ez egy SzRTClass példány: {self.name}"

def szrt_function(data):
    print(f"SzRT függvény hívva, adatok: {data}")
