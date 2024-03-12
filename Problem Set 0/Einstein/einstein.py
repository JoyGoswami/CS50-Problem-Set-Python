def main():
    get_mass = int(input("m: "))
    speed_of_light = pow(300000000, 2)
    
    energy = get_mass * speed_of_light

    print(energy)

main()