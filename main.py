# begin
def sayingHello(name):
    print("******************************")
    print(f" 😀 Hey,{name}. Welcome to Rabit ! ")
    print("******************************")
def choosePet(pets):
    for pet in pets:
        print(pet,end=" ")
    choosenPet=input("Choose one of them: ")
    return choosenPet
def showstatuOfAnimal(animal):
    for k,v in animal.items():
        print(f"{k} - > {v}")


animal={"energy":50,"hunger":50,"sleep":50}
showstatuOfAnimal(animal)

def askHabitIsDone(habits):
    for habit in habits:
        answer=input(f"Did you completed the {habit} : (y/n)").lower()
        if answer=='y':
            return True
    return False






