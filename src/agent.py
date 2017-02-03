from predictors import *
import random as rnd

class Agent:
    def __init__(self,crowded):
        self.__crowded = crowded
        self.__predictors = []
        #The first predictor is the active one
        self.__activePredIndex = 0

    #Determine if agent should attend
    def isGoing(self,attendances):
        prediction = self.__predictors[self.__activePredIndex](attendances)
        #If agent predicts it won't be crowded,then it will attend
        if prediction >= self.__crowded:
            return 0
        else:
            return 1

    #Add a new predictor
    def addPredictor(self,pred):
        self.__predictors.append(pred)
        
    #Find the most accurate predictor and active it
    def updatePredictors(self,attendances,newatt):
        distances = []
        #Calculate the distance of each prediction to the actual value
        for i in range(len(self.__predictors)):
            prediction = self.__predictors[i](attendances)
            distances.append(abs(prediction-newatt))
        #Pick the predictor with the least error
        self.__activePredIndex = distances.index(min(distances))