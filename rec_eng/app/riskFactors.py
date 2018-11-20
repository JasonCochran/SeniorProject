from abc import ABC, abstractmethod
import os, sys, requests
from app import app, db, models
import numpy as np
 

class RiskMatrixFactory(object):
	def __init__(self, width, height):
		self.risks = 3
		self.width = width
		self.height = height
    	self.riskMatrix = None

    def buildMatrix():
    	aband = AbandonedBuildings("filename.csv", self.width, self.height)
    	deserts = FoodDeserts("filename.csv", self.width, self.height)
    	transport = LackOfTransportation("filename.csv", self.width, self.height)

    	self.riskMatrix = np.zeros( shape=( self.height, self.width, self.risks + 1 ) )
    	for x in np.arange(0, np.absolute(self.height)):
			for y in np.arange(0, np.absolute(self.width)):
				# Loop through the grid and at each point, run 'getRiskAtPoint' for each risk factor
				# Store the associated value in the matrix

		return self.riskMatrix

    def getMatrix():
    	return self.riskMatrix

class RiskFactorABC(ABC):
 
    def __init__(self, fileName, riskMatrix_w, riskMatrix_h):
    	self.riskMatrix = np.zeros( shape=( riskMatrix_h, riskMatrix_l) )
    	self.fileName = fileName
        super().__init__()
    
    @abstractmethod
    def calculateRisk(self):
        pass

    @abstractmethod
    def getRiskFishNet(self):
    	pass

    @abstractmethod
    def simulateRecommendation(self, recommendation):
    	pass

    @abstractmethod
    def getRiskAtPoint(self, lat, lon)
    	pass


class AbandonedBuildings(RiskFactorABC):
	def calculateRisk(self):

	def getRiskFishNet(self):

	def simulateRecommendation(self, recommendation):

	def getRiskAtPoint(self, lat, lon)


class FoodDeserts(RiskFactorABC):
	def calculateRisk(self):

	def getRiskFishNet(self):

	def simulateRecommendation(self, recommendation):

	def getRiskAtPoint(self, lat, lon)


class LackOfTransportation(RiskFactorABC):
	def calculateRisk(self):

	def getRiskFishNet(self):

	def simulateRecommendation(self, recommendation):

	def getRiskAtPoint(self, lat, lon)

