def bead_sort(arr):
    n = len(arr)

    # Find the maximum element
    max_elem = max(arr)

    # Create beads list
    beads = [[0] for _ in range(max_elem)]

    # Fill the beads list
    for i in range(n):
        for j in range(arr[i]):
            beads[j].append(1)

    # Rearrange the array
    for i in range(max_elem):
        beads[i] = beads[i][1:]
        arr[i] = len(beads[i])

