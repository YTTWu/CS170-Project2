import csv

class NearestNeighbor:
    def __init__(self, data):
        self.data = data

    def getAccuracy(self, featureList):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                temp = []
                temp2 = []
                total = []
                for feature in featureList:
                    temp.append(self.data[i][feature])
                    temp2.append(self.data[j][feature])
                total = [temp,temp2]
                print(total)

    
    def getDistance(self, row):
        distance = 0
        for i in range(len(row)-1):
            distance += (row[i] - row[-1])**2
        return distance**0.5
            







def main():
    data = []
    with open("P2_datasets/CS170_Small_Data__96.txt", "r") as file:
        data = [[x for x in line.split()] for line in file]
    print(data)
    temp = NearestNeighbor(data)
    temp.getAccuracy([1,3])
    

main()