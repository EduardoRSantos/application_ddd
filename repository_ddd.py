from ddd import DDD
class RepositoryDDD:

    def __init__(self) -> None:
        self.lista: list[DDD] = []
        
    def add(self, DDD) -> None:
        self.lista.append(DDD)

    def find(self, ddd) -> DDD:
        for x in self.lista:
            if(ddd == x.ddd):
                return x

    def checkIfExists(self, ddd: int) -> bool:
        for x in self.lista:
            if(ddd == x.ddd):
                return True
        return False
    
    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        menu = formatText.format("ddd", "Name of city")
        for city in self.lista:
            menu += formatText.format(city.ddd, city.estado)

        return menu
