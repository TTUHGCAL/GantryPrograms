# Python program to demonstrate
# command line arguments


import argparse
import numpy as np
import matplotlib.pyplot as plt
import csv
import codecs




def plotter(inFileName, outFileName):
  # inFileName, outFileName = initFunc()
  x1 = []
  y1 = []
  point1 = 0
  with open(inFileName,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    for row in plots:
      # x1.append(float(row[0]))
      # y1.append(float(row[1]))
      x1.append(point1)
      y1.append(float(row[0]))
      point1 = point1+1

    refPoint = y1[0]
    for i in range(len(y1)):
      y1[i] = 1000*(refPoint - y1[i])
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.plot(x1,y1, label='Height', marker=".", color='red',linestyle = 'None')
    plt.xlabel('Position')
    plt.ylabel(r'Variation wrt point 0 ($\mu$m), Z=%f' %round(refPoint,2))
    plt.grid()
    
    # ax.set_ylim(0,10)
    # plt.plot(x1,y1)
    # for i,j in zip(x1,y1):
      # ax.annotate(str(j), xy=(i,j), xytext=(10,10), textcoords='offset points')
      # ax.annotate(str(j),xy=(i,j))

    for index in range(len(x1)):
      ax.text(x1[index], y1[index], round(y1[index],2))


    plt.savefig(outFileName)
    # plt.show()



def initFunc():
  print("Checking the arguments....")

  # Initialize
  inFileName = "C:\\Users\\TTUHEP\\Documents\\LabVIEW\\GantryPrograms\\Configs\\temp.txt"
  outFileName = "C:\\Users\\TTUHEP\\Documents\\LabVIEW\\GantryPrograms\\LogFiles\\plot.png"
  
  parser = argparse.ArgumentParser()

  # Adding optional argument
  parser.add_argument("-i", "--inFile", help = "Input text file with data points")
  parser.add_argument("-o", "--outFile", help = "Output file name for the plot, including .png/.jpg extension")
  
  # Read arguments from command line
  args = parser.parse_args()
  
  if args.inFile:
    print("Using data from : % s" % args.inFile)
    inFileName = args.inFile
  else:
    print("Using data from default file : %s" %inFileName)

  if args.outFile:
    print("Saving plot as : % s" % args.outFile)
    outFileName = args.outFile
  else:
    print("Saving plot using default name : %s" %outFileName)

  plotter(inFileName, outFileName)

  return inFileName, outFileName

#initFunc()
