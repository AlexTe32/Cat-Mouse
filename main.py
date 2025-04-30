from Simulation import run_simulation

# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    # Example: 3 cats, 5 mice, and some obstacles
    obstacles = {(3, 4), (5, 6), (2, 7)}

    # Run the simulation and get the number of turns it took
    turns_taken = run_simulation(num_cats=3, num_mice=5, obstacles=obstacles)
    print(f"The simulation took {turns_taken} turns to win.")

