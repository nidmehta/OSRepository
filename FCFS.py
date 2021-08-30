#First Come First Serve

def waitingTime (n, bt, wt):
    wt[0] = 0
    for i in range(1, n, 1):
        wt[i] = bt[i-1] + wt[i-1]


def turnAroundTime (n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def averageTime(pid, n, bt):
    wtTotal = 0
    tatTotal = 0
    wt = [0] * n
    tat = [0] * n

    waitingTime(n, bt, wt)
    turnAroundTime(n, bt, wt, tat)

    print("Process ID \t Burst Time \t Waiting Time \t Turn Around Time")
    for i in range(n):
        wtTotal += wt[i]
        tatTotal += tat[i]
        print("\t", pid[i], " \t\t ", bt[i], " \t\t ", wt[i], " \t\t\t ", tat[i])

    print("Average Waiting Time: ",  wtTotal / n)
    print("Average Turn Around Time: ", tatTotal / n)


if __name__ == "__main__":
    pid = [1, 2, 3, 4, 5]
    n = len(pid)

    bt = [5, 10, 15, 20, 25]

    averageTime(pid, n, bt)