class Auto:
    def __init__(self, sor):
        self.nev = sor[0]
        self.datum = int(sor[1])


    def __str__(self):
        return f"{self.nev}, {self.datum}"