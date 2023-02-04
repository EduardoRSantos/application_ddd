class UserInterface:

    def __init__(self, RepositoryDDD) -> None:
        self.repository_ddd = RepositoryDDD

    def input_(self) -> int:
        ddd = int(input("type ddd and find the state: "))
        
        if(self.repository_ddd.checkIfExists(ddd) == True):
            return self.repository_ddd.find(ddd)
        else:
            print("ddd not found")