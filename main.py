from Simulation import run_simulation
import openpyxl

if __name__ == "__main__":
    NUM_MICE = 100
    NUM_CATS = 3

    # Креираме и отвараме нов Ексел фајл
    wb = openpyxl.Workbook()
    sheet = wb.active
    sum = 0

    # Казуваме колку симулацији ни се потребни
    number_of_runs = 10

    sheet["A1"] = "Cats:"
    sheet["B1"] = "Mouse:"
    sheet["C1"] = "Time(sec):"

    # Ја извршуваме симулацијата одреден број на пати
    for x in range(number_of_runs):
        turns = run_simulation(N=56, P=56, num_cats=NUM_CATS, num_mice=NUM_MICE, num_obstacles=155, wait_time=0)
        sum += turns
        print(f"{x}: Game finished in {turns} turns!")
        # После секоја симулација ги запишуваме резултати
        sheet["A" + str((x + 2))] = NUM_CATS
        sheet["B" + str((x + 2))] = NUM_MICE
        sheet["C" + str((x + 2))] = turns
    print(f"Avrage time {sum / number_of_runs} turns!")
    # Го зачувуваме Ексел фајлот
    wb.save("primer.xlsx")
