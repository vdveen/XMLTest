#Goal: 
#Import XML file 
#Put info from XML in a neat class with attributes
#Create a point from the coordinates
#Calculate per station the percentage of availability

import xml.etree.ElementTree as ET
import arcpy


#The tree is the entire XML tree, and its root is the top level of the tree. In this case, 'stations'. 
tree = ET.parse('livecyclehireupdates.xml')
root = tree.getroot()


#Define station class
class Station(object):
    #Define variables: station name, coordinates, number of bikes and empty slots
    def __init__(self, name, x, y, nbBikes, nbEmpty):
        self.name = name
        self.x = x
        self.y = y
        self.nbBikes = nbBikes
        self.nbEmpty = nbEmpty

    #Create an ArcGIS point geometry 
    def pointCreation(self):
        self.point = arcpy.Point(x,y)

    #Calculate and print the nuber of bikes / total number of slots
    def percentageBikes(self):
        self.percent = float(self.nbBikes) / float(self.nbBikes + self.nbEmpty) * 100
        print self.percent, '% of the bikes are available at', self.name

#Put station info into classes
stationlist = []
for stations in root:
    name = stations[1].text
    x = float(stations[3].text)
    y = float(stations[4].text)
    nbBikes = int(stations[10].text)
    nbEmpty = int(stations[11].text)
    #Summon the class object
    station = Station(name,x,y,nbBikes,nbEmpty)
    #Generate the point geometry in the class
    station.pointCreation()
    #Calculate the bike availability percentage
    station.percentageBikes()
    #Append this newly created class object in the station list
    stationlist.append(station)

#Displays that the classes have been filled with the XML data
#for station in stationlist:
#    print station.name, station.point