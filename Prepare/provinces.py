
def main():
    with open("provinces.txt", "r") as file:
        provinces = file.readlines()
        provinces.pop(0)
        provinces.pop()
        for i in range(len(provinces)):
            if provinces[i] == "AB":
                provinces[i] = "Alberta"
        print(provinces)
        count = provinces.count("Alberta")
        print()
        print(f"Alberta ocurs {count} times in the modified list.")

def read_provinces():
    provinces = []
    with open("provinces.txt", "r") as file:
        for line in file:
            clean_line = line.strip()
            provinces.append(clean_line)
    return provinces

if __name__ == "__main__":
    main()