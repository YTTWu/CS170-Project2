import time
class FeatureSelection:
    def __init__(self, data):
        self.data = data

    def getAccuracy(self, featureList):
        # array to keep track the current min distance
        curMinDis = []
        # set initial min distance to be 999
        minDis = [999,0]
        count = 0
        # nested for loop for cross comparison
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                # holds one set of features
                temp = []
                # holds another set of features
                temp2 = []
                total = []
                # for loop to compare each feature
                for feature in featureList:
                    # if the features are not the same, append to temp and temp2
                    if self.data[i][feature] != self.data[j][feature]:
                        temp.append(self.data[i][feature])
                        temp2.append(self.data[j][feature])
                if temp and temp2:
                    total = [temp,temp2]
                    # passing total to getDistance function to get the distance between two sets of features
                    curMinDis = [self.getDistance(total),j]
                    # if the current min distance is smaller than the previous min distance, replace it
                    if(float(minDis[0]) > float(curMinDis[0])):
                        minDis = curMinDis
            # check if the min distance is 0, if not, check if the class is the same
            if minDis != 0:
                if self.data[i][0] == self.data[minDis[1]][0]:
                    count += 1
            # reset min distance to 999
            minDis = [999,0]
        # return the accuracy
        return count / len(self.data)

    # calculate the distance between two sets of features, Euclidean Distance Formula
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
        # make sure we have ran all the features before ending the loop
        while len(totalBest) != len(self.data[0]) - 1:
            for i in range(1,len(self.data[0])):
                # check if the row is looked at before
                if i not in temp_feature:
                    temp_feature.append(i)
                    # get the accuracy of the current feature
                    temp.append([self.getAccuracy(temp_feature),temp_feature.copy()])
                    print("Using feature " + str(temp_feature) + " accuracy is " + str(temp[-1][0]))
                    temp_feature.pop()
            # sort the accuracy in descending order
            curBestAccuracy = sorted(temp, key=lambda x: x[0], reverse=True)
            # get the best accuracy
            f = curBestAccuracy[0][1]
            # since the best accuracy is in a nested list, break it down to a list
            for x in f:
                if x not in temp_feature:
                    temp_feature.append(x)
            # append the best accuracy to the totalBest list
            totalBest.append(curBestAccuracy[0])
            temp = []
        # sort the totalBest list in descending order and return the first element
        result = sorted(totalBest, key=lambda x: x[0], reverse=True)[0]
        return result

    def backwardElimination(self):
        totalBest = []
        temp_feature = []
        curBestAccuracy = []
        temp = []
        initial = []
        # get the initial set of features, which is all the features
        for k in range(1,len(self.data[0])):
            temp_feature.append(k)
            initial.append(k)
        # accuracy for the initial set of features
        temp.append([self.getAccuracy(temp_feature),temp_feature.copy()])
        print("Using feature " + str(initial) + " accuracy is " + str(temp[0][0]))
        totalBest.append(temp[0])
        # make sure we have ran all the features before ending the loop
        while len(temp_feature) != 0:
            for i in reversed(range(len(self.data[0]))):
                # check if the row is looked at before
                if i in temp_feature:
                    # remove for cross comparison
                    temp_feature.remove(i)
                     # get the accuracy of the current feature
                    temp.append([self.getAccuracy(temp_feature),temp_feature.copy()])                    
                    print("Using feature " + str(temp_feature) + " accuracy is " + str(temp[-1][0]))
                    # add back to the list
                    temp_feature.append(i)
            # sort the accuracy in descending order
            curBestAccuracy = sorted(temp, key=lambda x: x[0], reverse=True)
            b = curBestAccuracy[0][1]
            temp_feature = []
            # since the best accuracy is in a nested list, break it down to a list
            if len(b) == 1:
                temp_feature = []
            else:
                for x in b:
                    if x not in temp_feature:
                        temp_feature.append(x)
            totalBest.append(curBestAccuracy[0])
            temp = []
        # sort the totalBest list in descending order and return the first element
        result = sorted(totalBest, key=lambda x: x[0], reverse=True)[0]
        return result

            

def main():
    data = []
    print("Welcome to the Feature Selection Algorithm.")
        

    userInput = input("Do you want to test with Small file or Large file? (type 's' or 'l'):  ")

    if userInput == 's':
        userInput = input("Please type the number of the file you want to test with 1 - 125. (e.x. '1' or '23' or '36' or '98'):  ")
        fileName = "P2_datasets/CS170_Small_Data__" + userInput + ".txt"
        # converting .txt file to 2D array
        with open(fileName, "r") as file:
            data = [[x for x in line.split()] for line in file]
            F = FeatureSelection(data)
    elif userInput == 'l':
        userInput = input("Please type the number of the file you want to test with 1 - 125. (e.x. '1' or '23' or '36' or '98'):  ")
        fileName = "P2_datasets/CS170_Large_Data__" + userInput + ".txt"
        with open(fileName, "r") as file:
            data = [[x for x in line.split()] for line in file]
            F = FeatureSelection(data)
    else:
        print("Invalid input. Please try again.")
        return
    
    print("Please type the number of the algorithm you want to use. (1 or 2)")
    print("1. Forward Selection")
    userInput = input("2. Backward Elimination:  ")
    if userInput == '1':
        startTime = time.time()
        result = F.forwardSelection()
    elif userInput == '2':
        startTime = time.time()
        result = F.backwardElimination()
    endtime = time.time() - startTime
    # print result 
    print("SEARCH FINISHED! The best feature subset is " + str(result[1]) + ", with an accuracy of " + str(result[0]) + "%. \n\n\n")
    print("The program took " + str(endtime) + " seconds to run.")

    
    
    

main()