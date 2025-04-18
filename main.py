from pet import Pet

def main():
    my_pet = Pet("Buddy")

    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.get_status()

    # 🎯 Bonus
    my_pet.train("roll over")
    my_pet.train("play dead")
    my_pet.show_tricks()

    my_pet.get_status()

if __name__ == "__main__":
    main()
