import math
import random
import turtle
#Euclid
def euclid(point1,point2):
    a = 0
    for i in range(len(point1)):
        a += (point1[i]+point2[i])**2
        s = math.sqrt(a)
    return s

#Clustering 
def createCentroids(k,datadict):
    centroids = []
    centroids_count = 0
    centroid_key = []

    while centroids_count < k:
        rkey = random.randint(1,len(datadict))
        if rkey not in centroid_key:
            centroids.append(datadict[rkey])
            centroid_key.append(rkey)
            centroids_count += 1
    return centroids

def createClusters(k,centroids,datadict,repeats):
    for apass in range(repeats):
        print("****PASS",apass,"****")
        clusters = []
        for i in range(k):
            clusters.append([])
        for akey in datadict:
            distances = []
            for cluster_Index in range(k):
                dist = euclid(datadict[akey],centroids[cluster_Index])
                distances.append(dist)

            mindist = min (distances)
            index = distances.index(mindist)

            clusters[index].append(akey)
            
        dimensions = len(datadict[1])

        for clusterindex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterindex]:
                datapoint =datadict[akey]
                for ind in range(len(datapoint)):
                    sums[ind] += datapoint[ind]
            for ind in range(len(sums)):
                clusterlen = len(clusters[clusterindex])
                if clusterlen != 0:
                    sums[ind] = sums[ind] / clusterlen
            centroids[clusterindex] = sums
        for c in clusters:
            print('Cluster')
            for key in c:
                print(datadict[key],end = "")
            print()
    return clusters

# Cluster analysis

def clusterAnalysis(datafile):
    examdict = readfile(datafile)
    examcentroids = createCentroids(5,examdict)
    examclusters = createClusters(5, examcentroids , examdict ,3)
    return examclusters

#example

def readfile_earthquakes(filename):
    datafile = open(filename,'r')
    datadict = {}
    key = 0
    for aline in datafile:
        items = aline.split()
        key += 1
        lat = float(items[4])
        lon = float(items[5])
        datadict[key] = [lon,lat]
    return datadict

def visualizeQuake(datafile):
    datadict = readfile_earthquakes(datafile)
    quakeCentroids = createCentroids(6,datadict)
    clusters = createClusters(6,quakeCentroids, datadict,7)

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(609,298)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()

    colorlist = ["red",'green','blue','orange','cyan','yellow']

    for clusterIndex in range(6):
        quakeT.color(colorlist[clusterIndex])
        for key in clusters[clusterIndex]:
            lon = datadict[key][0]
            lat = datadict[key][1]
            quakeT.goto(lon*wFactor,lat*hFactor)
            quakeT.dot()
    quakeWin.exitonclick()
    return

def read(datafile):
    data = open(datafile,'r')
    for aline in data:
        print(aline)
