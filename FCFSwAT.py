#First Come First Serve with Arrival Time

def waitingTime (n, bt, wt, at, ct):
    wt[0] = 0
    for i in range(1, n, 1):
        wt[i] = ct[i] - bt[i] - at[i]


def turnAroundTime (n, bt, wt, tat, at, ct):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def averageTime(pid, n, bt, at):
    wtTotal = 0
    tatTotal = 0
    wt = [0] * n
    tat = [0] * n

    ct = [0] * n
    ct[0] = bt[0]

    for i in range(1, n, 1):
        ct[i] = bt[i] + ct[i-1]

    waitingTime(n, bt, wt, at, ct)
    turnAroundTime(n, bt, wt, tat, at,  ct)

    print("Process ID \t Arrival Time \t Burst Time \t Waiting Time \t Turn Around Time")
    for i in range(n):
        wtTotal += wt[i]
        tatTotal += tat[i]
        print("\t", pid[i], " \t\t ", at[i], " \t\t ", bt[i], " \t\t\t ", wt[i], " \t\t\t ", tat[i])

    print("Average Waiting Time: ", wtTotal / n)
    print("Average Turn Around Time: ", tatTotal / n)


if __name__ == "__main__":
    pid = [1, 2, 3, 4, 5]
    n = len(pid)

    at = [0, 1, 2, 3, 4]
    bt = [5, 10, 15, 20, 25]

    averageTime(pid, n, bt, at)