
n = int(input('enter number of disks:\n'))

sourceRod = []
AuxiliaryRod = []
destinationRod = []

for i in range(1, n + 1):
    sourceRod.append(i)

sourceRod.reverse()


def hanoi(numOfDisks, source, destination, auxiliary):
    if numOfDisks > 0:
        # bordane n-1 disk az mabda be komaki
        move(numOfDisks - 1, source, auxiliary, destination)

        # bordane akharin disk az mabda be maqsad
        destination.append(source.pop())

        print(sourceRod, AuxiliaryRod, destinationRod, '----next Level------', sep='\n')

        # bordane n-1 disk az komaki be maqsad
        move(numOfDisks - 1, auxiliary, destination, source)


hanoi(n, sourceRod, destinationRod, AuxiliaryRod)
