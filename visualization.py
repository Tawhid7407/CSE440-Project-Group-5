def print_grid(grid, path):
    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0])):
            if (r, c) in path:
                row += " A "
            elif grid[r][c] == 0:
                row += " . "
            elif grid[r][c] == 1:
                row += " L "
            elif grid[r][c] == 2:
                row += " G "
            elif grid[r][c] == 3:
                row += " C "
            elif grid[r][c] == 4:
                row += " D "
            elif grid[r][c] == 5:
                row += " GO"
        print(row)