'''
Created on May 31, 2017

@author: shangwei
'''
if __name__ == '__main__': 
    import numpy as np
    from matplotlib.pylab import subplots
    from sklearn.linear_model import LinearRegression
    X = np.arange(10) # create some data
    Y = X + np.random.randn(10) # linear with noise
