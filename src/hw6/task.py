def far(the, data_new):
    print("Task 2: Get Far Working: ")
    print()

    target_distance = 0.95
    current_distance = 0
    attempts = 0
    max_attempts = 100 # Prevent infinite loops
    a,b,C,_= data_new.farapart(data_new.rows)
    while current_distance < target_distance and attempts < max_attempts:
        a, b, C, _ = data_new.farapart(data_new.rows)
        current_distance = C
        attempts += 1
    
    print("far1: ", a.cells)
    print("far2: ", b.cells)
    print("distance: ", current_distance)
    print("Attempts: ", attempts)
    return current_distance, attempts