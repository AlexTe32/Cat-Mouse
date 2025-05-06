from Simulation import run_simulation
import openpyxl
# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    wb = openpyxl.Workbook()
    sheet = wb.active
    sum=0
    number_of_runs=100
    for y in range (100):
        sum=0
        for x in range(number_of_runs):
            turns = run_simulation(N=56, P=56, num_cats=3, num_mice=y+1, num_obstacles=155, wait_time=0)
            sum+=turns
            print(f"{x}: Game finished in {turns} turns!")
        sheet["A"+str((y+2))]=3
        sheet["B"+str((y+2))]=y+1
        sheet["C"+str((y+2))]=sum/number_of_runs
        print(f"Avrage time {sum/number_of_runs} turns!")
    wb.save("simulation_resultues3.xlsx")
