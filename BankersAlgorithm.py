#Banker's Algorithm for Deadlock Avoidance
if __name__ == "__main__":

    processes = 5
    resources = 3

    allocationMatrix = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]

    availResources = [3, 3, 2]

    f = [0] * processes
    ans = [0] * processes
    ind = 0
    for k in range(processes):
        f[k] = 0

    need = [[0 for i in range(resources)] for i in range(processes)]
    for i in range(processes):
        for j in range(resources):
            need[i][j] = max[i][j] - allocationMatrix[i][j]
    y = 0
    for k in range(5):
        for i in range(processes):
            if f[i] == 0:
                flag = 0
                for j in range(resources):
                    if need[i][j] > availResources[j]:
                        flag = 1
                        break

                if flag == 0:
                    ans[ind] = i
                    ind += 1
                    for y in range(resources):
                        availResources[y] += allocationMatrix[i][y]
                    f[i] = 1

    print("Safe Sequence:", end = ' ')
    for i in range(processes - 1):
        print(ans[i], "-> ", end="")
    print(ans[processes - 1])