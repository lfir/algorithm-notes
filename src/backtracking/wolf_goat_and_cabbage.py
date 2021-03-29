def solve(currentstate, prevstates):
    """Problem: Take the Wolf, Goat and Cabbage to the other side of the river (one at a time)
    without leaving the Wolf with the Goat or the Goat with the Cabbage alone (without the Farmer).
    https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem

    currentstate -- List with the current position of the farmer and each purchase.
    prevstates -- List of lists with the valid states explored so far.
    return -- Whether a valid end state was reached and the list of valid states explored.
    
    Example:
    Being on one of the sides of the river is represented by True
    and on the other one using False.
           Farmer, Wolf, Goat, Cabbage
    arr = [True, True, True, False]
    res = solve(arr, [])
    """
    end = False
    if currentstate == [True, True, True, True]:
        end = True
        return end, prevstates

    for i in range(4):
        newstate = next_state(currentstate, i)
        valid = is_valid(newstate)
        new = is_new(newstate, prevstates)
        if valid and new:
            prevstates.append(newstate)
            end, prevstates = solve(newstate, prevstates)
            # If the call above did not reach a valid end state, backtrack
            # and try another option.
            if end:
                break

    return end, prevstates

def is_valid(arr):
    if arr[1] == arr[2]:
        # If the Wolf and the Goat are on the same side it is valid
        # only if the Farmer is also on that side.
        return arr[0] == arr[2]
    elif arr[2] == arr[3]:
        # If the Goat and the Cabbage are on the same side it is valid
        # only if the Farmer is also on that side.
        return arr[0] == arr[2]
    else:
        return True

def is_new(newstate, statelist):
    for state in statelist:
        if state == newstate:
            return False
    return True

def next_state(state, index):
    newstate = [boolean for boolean in state]
    if newstate[0]:
        newstate[0] = False
        newstate[index] = False
    else:
        newstate[0] = True
        newstate[index] = True

    return newstate
