from ddd import DDD
from repository_ddd import RepositoryDDD
from user_interface import UserInterface

reposiutory_ddd = RepositoryDDD()
ui = UserInterface(reposiutory_ddd)

reposiutory_ddd.add(DDD(61, "Brasília"))
reposiutory_ddd.add(DDD(71, "Salvador"))
reposiutory_ddd.add(DDD(11, "São Paulo"))
reposiutory_ddd.add(DDD(21, "Rio de Janeiro"))
reposiutory_ddd.add(DDD(32, "Juiz de Fora"))
reposiutory_ddd.add(DDD(19, "Campinas"))
reposiutory_ddd.add(DDD(27, "Vitória"))
reposiutory_ddd.add(DDD(31, "Belo Horizonte"))

print(reposiutory_ddd)

while True:
    result = ui.input_()
    if(result == None):
        break
    else:
        print(f" ({result.ddd}) -> {result.estado} \n")

