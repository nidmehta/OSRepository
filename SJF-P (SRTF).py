# Shortest Job First- Preemptive
# Shortest Remaining Time First
import sys


def waitingTime(n, at, bt, wt):
    # Remaining Time
    rt = [0] * n
    for i in range(n):
        rt[i] = bt[i]

    complete = 0
    check = False
    currentt = 0
    minrt = sys.maxsize
    sidx = 0

    # Till all processes are completed
    while (complete != n):

        # To find the process with minimum remaining time among the arrived processes
        for j in range(n):
            if (at[j] <= currentt) and (rt[j] < minrt) and rt[j] > 0:
                minrt = rt[j]
                sidx = j
                check = True

        # Check for IDLE time
        if not check:
            currentt += 1
            continue

        # Remaining time after 1 unit processing
        rt[sidx] -= 1
        minrt = rt[sidx]

        # If process gets completed
        if (rt[sidx] == 0):
            minrt = sys.maxsize
            complete += 1
            check = False

            # Completion Time
            ct = currentt + 1

            # Waiting Time
            wt[sidx] = ct - bt[sidx] - at[sidx]

            if wt[sidx] < 0:
                wt[sidx] = 0

        currentt += 1


def turnAroundTime(n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def averageTime(pid, n, at, bt):
    wtTotal = 0
    tatTotal = 0
    wt = [0] * n
    tat = [0] * n

    waitingTime(n, at, bt, wt)
    turnAroundTime(n, bt, wt, tat)

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
    bt = [5, 10,  15, 20, 25]

    averageTime(pid, n, at, bt)
