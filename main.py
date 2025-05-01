from Simulation import run_simulation
import openpyxl
# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    wb = openpyxl.load_workbook("simulation_resultues.xlsx")
    sheet = wb.active
    sum=0
    number_of_runs=10000
    for x in range(number_of_runs):
        turns = run_simulation(N=56, P=56, num_cats=3, num_mice=3, num_obstacles=155, wait_time=0)
        sum+=turns
        sheet["A"+str((x+2))]=3
        sheet["B"+str((x+2))]=3
        sheet["C"+str((x+2))]=turns
        print(f"{x}: Game finished in {turns} turns!")
    print(f"Avrage time {sum/number_of_runs} turns!")
    wb.save("simulation_resultues.xlsx")
