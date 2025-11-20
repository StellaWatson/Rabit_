# begin
def sayingHello(name):
    print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
    print("""                                                               """)
    print(f"""  😀HEY, {name.upper()}, WELCOME TO GreenBit HABIT TRACKER    """)
    print("""                                                               """)
    print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
def choosePet(pets):
    for pet in pets:
        print(pet,end=", ")

    while True:
        choosenPet = input("\nChoose Your pet : ")
        if choosenPet in pets:
            break
        else:
            print("❗ Please choose a pet from the list ")
    return choosenPet
def showstatuOfAnimal(animal):
    print("Your Pet's status ")
    print("_________________")
    for k,v in animal.items():

        print(f"{k} - > {v}")
def addHabit():
    habits = [
        "Regular exercise",
        "Healthy diet",
        "Hydration",
        "Hygiene",
        "Healthy sleep time"
    ]

    print("Recommended tasks:")
    for habit in habits:
        print(f"- {habit}")

    while True:
        task = input("Add a habit (write 'done' to finish): ")
        if task.lower() == 'done':
            break
        userSelectedHabits[task] = False   # store habit with uncompleted status

def viewHabits():
    print("Your Habits:")
    if len(userSelectedHabits)==0:
        print("No Habits")
    for habit, done in userSelectedHabits.items():
        status = "✓ done" if done else "✗ not done"
        print(f"- {habit} : {status}")

def askHabitIsDone(habits):
    for habit in habits:
        answer=input(f"Did you completed the {habit} : (y/n)").lower()
        if answer=='y':
            return True
    return False
def trackProgress(status):
    print("Let's check today's progress!")

    for habit in userSelectedHabits.keys():
        answer = input(f"Did you complete '{habit}' today? (y/n): ").lower()

        if answer == 'y':
            userSelectedHabits[habit] = True

            # effects of habits on the pet:
            if "sleep" in habit.lower():
                status["Energy"] += 10
            elif "exercise" in habit.lower() or "running" in habit.lower():
                status["Energy"] += 5
            elif "diet" in habit.lower() or "food" in habit.lower():
                status["Hunger"] = str(int(status["Hunger"]) - 10)
            elif "hydration" in habit.lower() or "water" in habit.lower():
                status["Energy"] += 3
            elif "play" in habit.lower():
                status["Energy"]-=5
                status["Happiness"]+=10
            else:
                status["Energy"] += 1   # default effect
        else:
            userSelectedHabits[habit] = False
            status["Energy"] -= 5   # pet gets sad if user skips habits

    # Limit values
    if status["Energy"] > 100: status["Energy"] = 100
    if status["Energy"] < 0: status["Energy"] = 0
    print("____________________")
    print("Updated pet status:")
    showstatuOfAnimal(status)

if __name__=='__main__':
    name=input("Enter your name: ")
    sayingHello(name)
    userSelectedHabits = {}
    pets=["Cat","Dog","Rabbit",]
    statusOfPet={"Energy":5,"Hunger":5,"Happiness":5}
    userPet = choosePet(pets)


    print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
    print(f"Your Pet is {userPet}, Take Care of it ! ")
    print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
    while True:

        print("Menu:")
        print("1. View habits")
        print("2. Add habits")
        print("3. Show status of my Pet")
        print("4. Track  progress")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice=='1':
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            viewHabits()
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
        elif choice=='2':
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            addHabit()
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
        elif choice=='3':
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            showstatuOfAnimal(statusOfPet)
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")

        elif choice=='4':
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            trackProgress(statusOfPet)
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
        elif choice=='5':
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            print(" 😃 Thank you for Using Rabit Habit Tracker! ")

        if statusOfPet["Energy"]<=0:
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            print(f"😯 Unfortunately, Your {userPet}  is Died ! You are a stupid, Procrastinator! 😡")
            print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            break

