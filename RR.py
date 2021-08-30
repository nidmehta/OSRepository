#Round Robin

def waitingTime(n, bt, wt, q):
    rbt = [0] * n
    t = 0

    for i in range(n):
        rbt[i] = bt[i]

    while (1):
        complete = True
        for i in range(n):
            if rbt[i] > 0:
                complete = False
                if rbt[i] > q:
                    t += q
                    rbt[i] -= q
                else:
                    t += rbt[i]
                    wt[i] = t - bt[i]
                    rbt[i] = 0
        if complete == True:
            break

def turnAroundTime(n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def averageTime(pid, n, bt, q):
    wt = [0] * n
    tat = [0] * n
    wtTotal = 0
    tatTotal = 0

    waitingTime(n, bt, wt, q)
    turnAroundTime(n, bt,wt, tat)

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

    bt = [5, 10, 15, 20, 25]
    q = 2

    averageTime(pid, n, bt, q)

