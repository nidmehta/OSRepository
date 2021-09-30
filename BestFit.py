# Best Fit Allocation
def bestFit(blockNo, processNo, blockSize, processSize):
    # Stores block no of the block allocated to a process
    allocation = [-1] * processNo

    temp = blockSize.copy()

    for i in range(processNo):
        bestBlock = -1
        for j in range(blockNo):
            if temp[j] >= processSize[i]:
                if bestBlock == -1:
                    bestBlock = j
                elif temp[bestBlock] > temp[j]:
                    bestBlock = j

        if bestBlock != -1:
            allocation[i] = bestBlock

            # Remaining memory in the block
            temp[bestBlock] -= processSize[i]

    print("Process No. \t Process Size \t Block No. \t\t\t Block Size \t Internal Fragmentation")
    for i in range(processNo):
        print("\t", i, "\t\t\t\t", processSize[i], end="\t\t\t")
        if allocation[i] != -1:
            print(allocation[i], "\t\t\t\t\t", blockSize[allocation[i]], "\t\t\t",
                  blockSize[allocation[i]] - processSize[i])
        else:
            print("Not Allocated")


if __name__ == '__main__':
    blockNo = int(input("Enter total number of blocks: "))
    blockSize = [0] * blockNo
    print("Enter size of each block: ")
    for i in range(blockNo):
        blockSize[i] = int(input())

    processNo = int(input("Enter total number of processes: "))
    processSize = [0] * processNo
    print("Enter size of each process: ")
    for i in range(processNo):
        processSize[i] = int(input())

    bestFit(blockNo, processNo, blockSize, processSize)
