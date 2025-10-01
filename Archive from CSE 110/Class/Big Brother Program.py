


with open("hr_system.txt") as file:
    for line in file:
        name, eid, position, salary = line.strip().split(" ")
        salary = float(salary)
        week_payment = salary / 24
        if position == "Engineer":
            week_payment += 1000
        print(f"{name} (ID: {eid}), {position} - ${week_payment:.2f}")

    


