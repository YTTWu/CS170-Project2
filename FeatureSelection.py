import csv

class NearestNeighbor:
    def __init__(self, data):
        self.data = data

    def getAccuracy(self, featureList):
        result = []
        curMinDis = []
        minDis = [999,0]
        count = 0
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                temp = []
                temp2 = []
                total = []
                for feature in featureList:
                    if self.data[i][feature] != self.data[j][feature]:
                        temp.append(self.data[i][feature])
                        temp2.append(self.data[j][feature])
                if temp and temp2:
                    total = [temp,temp2]
                    curMinDis = [self.getDistance(total),j]
                    if(float(minDis[0]) > float(curMinDis[0])):
                        minDis = curMinDis
            if minDis != 0:
                if self.data[i][0] == self.data[minDis[1]][0]:
                    count += 1
            minDis = [999,0]
        print("Accuracy: ", count/len(self.data))
        return count / len(self.data)

    
    def getDistance(self, set):
        distance = 0
        for i in range(len(set[0])):
            distance += abs(float(set[0][i]) - float(set[1][i])) ** 2
        return distance ** 0.5
            

def main():
    data = []
    with open("P2_datasets/CS170_Large_Data__21.txt", "r") as file:
        data = [[x for x in line.split()] for line in file]
    print(data)
    temp = NearestNeighbor(data)
    temp.getAccuracy([37])
    

main()