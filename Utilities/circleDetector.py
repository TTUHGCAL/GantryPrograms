import sys
import cv2 as cv
import numpy as np

def circleDetectorPCB(filename, outFileName):
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    ## [load]

    ## [convert_to_gray]
    # Convert it to gray
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ## [convert_to_gray]

    ## [reduce_noise]
    # Reduce the noise to avoid false circle detection
    gray = cv.medianBlur(gray, 5)
    ## [reduce_noise]

    ## [houghcircles]
    rows = gray.shape[0]
    
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 4, rows ,
                              param1=100, param2=30,
                              minRadius=725, maxRadius=750) # PCB new cam
    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 800 ,
    #                           param1=100, param2=60,
    #                           minRadius=30, maxRadius=70) # Si old cam
    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 350 ,
    #                           param1=30, param2=25,
    #                           minRadius=50, maxRadius=70) # Si old cam trials
    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 800 ,
    #                           param1=100, param2=60,
    #                           minRadius=900, maxRadius=1300) # Syringe new cam

    ## [houghcircles]

    ## [draw]
    centRadius = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
            print(i[0],i[1],i[2])
            centRadius = i
    ## [draw]

    ## [display]
    # cv.imshow("detected circles", src)
    # cv.waitKey(0)
    cv.imwrite(outFileName, src)
    ## [display]
    return centRadius

def circleDetectorSi(filename, outFileName):
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    # Convert it to gray
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ## [reduce_noise]
    gray = cv.medianBlur(gray, 5)
    ## [houghcircles]
    rows = gray.shape[0]
    
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 2, rows ,
                              param1=200, param2=80,
                              minRadius=150, maxRadius=200) # Si new cam, new fiducials
    ##    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 4, rows ,
    ##                              param1=100, param2=30,
    ##                              minRadius=500, maxRadius=900) # PCB new cam
    ##    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 800 ,
    #                           param1=100, param2=60,
    #                           minRadius=30, maxRadius=70) # Si old cam
    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 350 ,
    #                           param1=30, param2=25,
    #                           minRadius=50, maxRadius=70) # Si old cam trials
    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 800 ,
    #                           param1=100, param2=60,
    #                           minRadius=900, maxRadius=1300) # Syringe new cam

    ## [houghcircles]

    ## [draw]
    centRadius = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (0, 0, 255), 3)
            print(i[0],i[1],i[2])
            centRadius = i
    ## [draw]

    ## [display]
    # cv.imshow("detected circles", src)
    # cv.waitKey(0)
    cv.imwrite(outFileName, src)
    ## [display]
    return centRadius

#circleDetectorPCB('C:\\Users\\TTUHEP\\Pictures\\imageCam.png', 'C:\\Users\\TTUHEP\\Documents\\LabVIEW\\GantryPrograms\\Utilities\\detectedCircles.png')
