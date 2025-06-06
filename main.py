from pattern import BuildMashin, Mashin

def main():
    building = BuildMashin()
    car = (building.u_make('Марка - BMW').u_model('Модель - M5 f90').u_year('Год - 2017').build())
    print(car)

if __name__ == "__main__":
    main()