#Round Robin with Arrival Time

def waitingTime(i, t, at, bt, wt):
    wt[i] = t - bt[i] - at[i]

def turnAroundTime(i, t, at, tat):
    tat[i] = t - at[i]


def averageTime(pid, n, at, bt, q):
    wt = [0] * n
    tat = [0] * n
    wtTotal = 0
    tatTotal = 0

    tempat = [0] * n
    tempbt = [0] * n

    for i in range(0, n, 1):
        tempat[i] = at[i]
        tempbt[i] = bt[i]

    t = 0

    while (True):
        flag = True
        for i in range (0, n, 1):
            if tempat[i] <= t:
                if tempat[i] <= n:
                    if tempbt[i] > 0:
                        flag = False
                        if tempbt[i] > n:
                            t += n
                            tempbt[i] -= n
                            tempat[i] += n
                        else:
                            t += tempbt[i]
                            turnAroundTime(i, t, at, tat)
                            waitingTime(i, t, at, bt, wt)
                            tempbt[i] = 0
                elif tempat[i] > n:
                    for j in range(0, n, 1):
                        if tempat[j] < tempat[i]:
                            if tempbt[j] > 0:
                                flag = False
                                if tempbt[j] > n:
                                    t += n
                                    tempbt[j] -= n
                                    tempat[j] += n
                                else:
                                    t += tempbt[j]
                                    turnAroundTime(j, t, at, tat)
                                    waitingTime(j, t, at, bt, wt)
                                    tempbt[j] = 0
                    if tempbt[i] > 0:
                        flag = False
                        if tempbt[i] > n:
                            t += n
                            tempbt[i] -= n
                            tempat[i] += n
                        else:
                            t += tempbt[i]
                            turnAroundTime(i, t, at, tat)
                            waitingTime(i, t, at, bt, wt)
                            tempbt[i] = 0

                elif tempat[i] > t:
                    t += 1
                    i -= 1
        if flag:
            break

    print("Process ID \t Burst Time \t Waiting Time \t Turn Around Time")
    for i in range(n):
        wtTotal += wt[i]
        tatTotal += tat[i]
        print("\t", pid[i], " \t\t ", bt[i], " \t\t ", wt[i], " \t\t\t ", tat[i])

    print("Average Waiting Time: ", wtTotal / n)
    print("Average Turn Around Time: ", tatTotal / n)


if __name__ == "__main__":
    pid = [1, 2, 3, 4, 5]
    n = len(pid)

    at = [0, 1, 2, 3, 4]
    bt = [5, 10, 15, 20, 25]
    q = 2

    averageTime(pid, n, at, bt, q)

