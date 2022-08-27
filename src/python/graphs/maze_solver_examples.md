#### Examples:

    from graphs.maze_solver import solve
    
    m0 = [
        ["S"],
        ["E"]
    ]
    print(solve(m0))

    m1 = [["S", "E"]]
    print(solve(m1))

    m2 = [["S", "P", "E"]]
    print(solve(m2))

    m3 = [
        ["S"],
        ["P"],
        ["E"]
    ]
    print(solve(m3))

    m4 = [
        ["S", "P", "W"],
        ["W", "E", "W"]
    ]
    print(solve(m4))

    m5 = [
        ["W", "P", "S"],
        ["W", "P", "W"],
        ["P", "P", "P"],
        ["P", "P", "E"]
    ]
    print(solve(m5))
