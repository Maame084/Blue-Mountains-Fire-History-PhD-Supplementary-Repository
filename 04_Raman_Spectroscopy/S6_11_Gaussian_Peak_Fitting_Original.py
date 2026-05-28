from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
#import console


# Gaussian class builds a set of gaussians, storing each gaussian
class gaussian:
    def __init__(self, x=[],height=[],position=[],width=[],slope=0,int=0):
        self.height = np.array(height)
        self.position = np.array(position)
        self.width = np.array(width) # note width is the FWHM
        self.area = np.array(height)
        self.slope = slope
        self.intercept = int
        self.x = np.array(x)
        self.y = np.zeros(len(x)) # for total envelope
        self.peak = np.zeros((len(position),len(x)),dtype=float) # peaks
        
    def build(self,noise=0.0):
        y_value = np.zeros(len(self.x))
        self.y = self.slope*self.x + self.intercept
        for j in range(len(self.position)):
            y_value = self.height[j] * np.exp(-((self.x-self.position[j])**2)/(2*(self.width[j]/2.35482)**2)) # convert FWHM to c
            self.peak[j,:] = y_value
            self.area[j] = self.height[j]*(self.width[j]/2.35482)*(2*np.pi)**0.5
            self.y += y_value
        if noise > 0:
            self.y += np.random.random_sample(len(self.x))*noise-(noise/2)

    def build2D(self,noise=0.0):
        self.X = np.arange(-5, 5, 0.25)
        self.Y = np.arange(-5, 5, 0.25)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        self.R = np.sqrt(self.X**2 + self.Y**2)
        self.Z = np.sin(self.R)

    def build_asym(self,noise=0.0):
        # build an asymmetric peak (eg. MS or XPS) 
        a = 0.1
        b = 0.0001
        y_value = np.zeros(len(self.x))
        self.y = self.slope*self.x + self.intercept
        for j in range(len(self.position)):
            w = 2.0*self.position[j]/(1.0+np.exp(-a*(self.x-b)))
            y_value = self.height[j] * np.exp(-((self.x-self.position[j])**2)/(2*w**2))
            self.peak[j,:] = y_value
            self.y += y_value
        if noise > 0:
            self.y += np.random.random_sample(len(self.x))*noise-(noise/2)

    def build_lorentzian(self,noise=0.0):
        # work still needed on this
        y_value = np.zeros(len(self.x))
        self.y = self.slope*self.x + self.intercept
        for j in range(len(self.position)):
            y_value = (0.25*self.width[j]) / (np.pi*(self.x-self.position[j])**2 + (0.5*self.width[j])**2)
            self.peak[j,:] = y_value
            self.area[j] = self.height[j]*self.width[j]*(2*np.pi)**0.5 #check this!
            self.y += y_value
        if noise > 0:
            self.y += np.random.random_sample(len(self.x))*noise-(noise/2)
            
    def peak_report(self):
        print('height\t\tposition\tFWHM\t\tarea')
        for i in range(self.peak.shape[0]):
            print('{:.1f}\t\t{:.1f}\t\t{:.1f}\t\t{:.1f}\t\t\t'.format(self.height[i],self.position[i],self.width[i],self.area[i]))
            
    def normalise(self):
        self.y = self.y/(max(self.y)-min(self.y))

    def scale(self,factor):
        result = gaussian()
        result.x = self.x
        result.y = self.y * factor
        return result

    def __add__(self, g):
        # return the sum of this gaussian and g
        # note: assumes same x-range, and new object is missing
        # position, width and height data
        result = gaussian()
        result.x = self.x
        result.y = self.y+g.y
        return result

    def save(self, filename):
        # save xy of total and individual peaks as csv text
        file_data = ''
        line = ''
        for i in range(len(self.x)):
            line = '{:f},{:f},'.format(self.x[i],self.y[i])
            for j in range(self.peak.shape[0]):
                line = line + '{:f},'.format(self.peak[j,i])
            # remove last comma
            line = line[0:len(line)-1]
            file_data = file_data + line + '\n'

        f = open(filename, 'w')
        f.write(file_data)
        f.close()

    def load(self, filename):
        csvReader = csv.reader(open(filename), delimiter=',', quotechar='|')
        print('content of file:')
        for row in csvReader:
            print(', '.join(row))

    def random_set(self,x,h_max,p_max,w_max,m,b,n=6):
        # build a random set of n peaks with baseline mx+b...then use build
        self.height = np.random.random_sample(n)*h_max
        self.position = np.random.random_sample(n)*p_max
        self.width = np.random.random_sample(n)*w_max
        self.slope = m
        self.intercept = b
        self.x = np.array(x)
        self.y = np.zeros(self.x.shape[0])
        self.peak = np.zeros((n,len(x)),dtype=float)
        #print(self.peak)

option = -1
#console.clear()
if option == 0:
    # test gaussian peaks
    g = gaussian(np.arange(100),[10.0,20.0],[30.0,70.0],[5.0,7.0],0.0,0.0)
    g.build()
    plt.clf()
    plt.plot(g.x,g.y+20)
    for i in range(g.peak.shape[0]):
        plt.plot(g.x,g.peak[i,:])
    plt.show()
    
    # test area calculation
    g.peak_report()
    print('peak0',np.sum(g.peak[0]))
    print('peak1',np.sum(g.peak[1]))
    g.save('test.txt')
    
if option == 1:
    # test random gaussian peaks
    g = gaussian(np.arange(300),[0,0,0],[0,0,0],[0,0,0],0.0,0.0)
    g.random_set(np.arange(300),100.0,300.0,10.0,0.0,0.0,3)
    g.build(1)
    plt.clf()
    plt.plot(g.x,g.y+50)
    for i in range(g.peak.shape[0]):
        plt.plot(g.x,g.peak[i,:])
    plt.show()
    
if option == 2:
    # test asymmetric peaks
    g = gaussian(np.arange(-1000,1000),[10.0],[10.0],[0.1],0.0,0.0)
    g.build_asym(0.1)
    plt.clf()
    plt.plot(g.x,g.y+2)
    for i in range(g.peak.shape[0]):
        plt.plot(g.x,g.peak[i,:])
    plt.show()
    
if option == 3:
    # test lorentzian peaks
    g = gaussian(np.arange(100),[25.0,60.0],[25.0,60.0],[1.0,3.0],0.0,0.0)

    plt.clf()
    g.build_lorentzian()
    g.peak_report()
    for i in range(g.peak.shape[0]):
        plt.plot(g.x,g.peak[i,:])

    g.build()
    g.peak_report()
    for i in range(g.peak.shape[0]):
        plt.plot(g.x,g.peak[i,:])
                
    plt.show()
    
if option == 4:
    # test 2D gaussian peaks
    g = gaussian(np.arange(100),[10.0,20.0],[30.0,70.0],[5.0,7.0],0.0,0.0)
    g.build2D(1.0)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    surf = ax.plot_surface(g.X, g.Y, g.Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
