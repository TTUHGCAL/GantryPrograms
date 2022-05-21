# Python program to demonstrate
# command line arguments


import argparse
import numpy as np
import matplotlib.pyplot as plt
import csv
import codecs




def plotterXY(inFileName, outFileName):
  # inFileName, outFileName = initFunc()
  x1 = []
  y1 = []
  point1 = 1
  with open(inFileName,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    for row in plots:
      x1.append(float(row[0]))
      y1.append(float(row[1]))

    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.plot(x1,y1, label='X vs Y', marker=".", color='red',linestyle = 'None')
    #plt.xlabel('Position')
    #plt.ylabel(r'Variation wrt point 0 ($\mu$m), Z=%f' %round(refPoint,3))
    plt.grid()
  
##    for index in range(len(x1)):
##      ax.text(x1[index], y1[index], round(y1[index],2))


    plt.savefig(outFileName)

def plotterPvsVal(inFileName, outFileName):
  # inFileName, outFileName = initFunc()
  x1 = []
  y1 = []
  point1 = 1
  with open(inFileName,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    for row in plots:
      x1.append(point1)
      y1.append(float(row[0]))
      point1 = point1+1
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.plot(x1,y1, label='X vs Y', marker=".", color='red',linestyle = 'None')
    #plt.xlabel('Position')
    #plt.ylabel(r'Variation wrt point 0 ($\mu$m), Z=%f' %round(refPoint,3))
    plt.grid()
  
##    for index in range(len(x1)):
##      ax.text(x1[index], y1[index], round(y1[index],2))


    plt.savefig(outFileName)
    # plt.show()

