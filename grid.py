def display_grid(grid):
    """Affiche la grille du jeu."""
    print("\n")
    for i in range(0, 9, 3):
        print(f" {grid[i]} | {grid[i + 1]} | {grid[i + 2]} ")
        if i < 6:
            print("---|---|---")
    print("\n")
