#Preemptive Priority Scheduling

def waitingTime(pid, n, wt, bt, priority):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if priority[j] > priority[j + 1]:
                temp = priority[j]
                priority[j] = priority[j + 1]
                priority[j + 1] = temp

                temp = bt[j]
                bt[j] = bt[j + 1]
                bt[j + 1] = temp

                swap = pid[j]
                pid[j] = pid[j + 1]
                pid[j + 1] = swap

    wt[0] = 0
    for i in range(1, n):
        wt[i] += wt[i - 1] + bt[i - 1]


def turnAroundTime(n, wt, bt, tat):
    tat[0] = bt[0]
    for i in range(1, n):
        tat[i] += wt[i] + bt[i]


def averageTime(pid, n, bt, priority):
    wtTotal = 0
    tatTotal = 0
    wt = [0] * n
    tat = [0] * n

    waitingTime(pid, n, wt, bt, priority)
    turnAroundTime(n, wt, bt, tat)

    print("Process ID \t Burst Time \t Priority \t Waiting Time \t Turn Around Time")
    for i in range(n):
        wtTotal += wt[i]
        tatTotal += tat[i]
        print("\t", pid[i], " \t\t ", bt[i], " \t\t ", priority[i], " \t\t\t ", wt[i], " \t\t\t ", tat[i])

    print("Average Waiting Time: ", wtTotal / n)
    print("Average Turn Around Time: ", tatTotal / n)


if __name__ == "__main__":
    pid = [1, 2, 3, 4, 5]
    n = len(pid)

    bt = [3, 5, 1, 7, 4]
    priority = [6, 4, 1, 7, 8]

    averageTime(pid, n, bt, priority)