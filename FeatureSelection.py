import csv

class FeatureSelection:
    def __init__(self, data):
        self.data = data

    def getAccuracy(self, featureList):
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
        # print("Accuracy: ", count/len(self.data))
        return count / len(self.data)

    
    def getDistance(self, set):
        distance = 0
        for i in range(len(set[0])):
            distance += abs(float(set[0][i]) - float(set[1][i])) ** 2
        return distance ** 0.5

    def forwardSelection(self):
        totalBest = []
        temp_feature = []
        curBestAccuracy = []
        temp = []
        while len(totalBest) != len(self.data[0]) - 1:
            for i in range(1,len(self.data[0])):
                if i not in temp_feature:
                    temp_feature.append(i)
                    temp.append([self.getAccuracy(temp_feature),temp_feature.copy()])
                    temp_feature.pop()
            curBestAccuracy = sorted(temp, key=lambda x: x[0], reverse=True)
            f = curBestAccuracy[0][1]
            for x in f:
                if x not in temp_feature:
                    temp_feature.append(x)
            totalBest.append(curBestAccuracy[0])
            temp = []
        result = sorted(totalBest, key=lambda x: x[0], reverse=True)[0]
        return result




            

def main():
    data = []
    with open("P2_datasets/CS170_Small_Data__107.txt", "r") as file:
        data = [[x for x in line.split()] for line in file]
    print(data)
    F = FeatureSelection(data)
    print(F.forwardSelection())
    

main()