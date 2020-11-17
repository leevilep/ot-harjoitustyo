from timer import Timer
import random


def main():
    print("Tämä on Brain Test -sovelluksen prototyyppi.")
    while True:
        print()
        print("Mitataan vastaajan reaktionopeuskykyä. Paina ENTER-näppäintä...")
        reaction = Timer()
        wait = random.randrange(3.0, 10.0)
        waiter = Timer()
        waiter.start()
        while waiter.get_s() < wait:
            pass
        print("NYT!")
        reaction.start()
        input("")
        reaction.stop()
        print("Reaktionopeutesi:", round(reaction.get_ms()), "ms")
        c = "a"
        while c!="e" and c!="k":
            c = input("Uudelleen? [k/e]: ")
        if c=="e":
            break
main()
