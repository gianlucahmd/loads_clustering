#from scipy.interpolate import interp1d
#from sklearn.linear_model import Ridge
#from sklearn.preprocessing import PolynomialFeatures
#from sklearn.pipeline import make_pipeline
#from statsmodels.nonparametric.kernel_regression import KernelReg
#clf = Ridge()

import peakutils

def get_peaks(column):
    #interpol = interp1d(column.index.values[1::2], column.values[1::2], kind = "cubic")
    #n_datapoints = 24
    #x = column.index.values[1:]
    #y = interpol(x)
    #y = signal.savgol_filter(column.values, 5,2)
    #clf.fit(column.index.values.reshape(24,1), column.values)
    #y = clf.predict(column.index.values.reshape(24,1))
    #x = column.index.values
    #y, y_std = kr.fit(x)

#    model = make_pipeline(PolynomialFeatures(5), Ridge())
#    model.fit(column.index.values.reshape(24,1), column.values)
#    
#    y = model.predict(column.index.values.reshape(24,1))

    #plt.subplot(121)
    plt.plot(column)
    #plt.subplot(122)
    #plt.plot(x, y)
    plt.show()
    #peakutils.indexes(column, thres=0.6, min_dist=3)
    #signal.argrelmax(y, order = 2)
    peaks = peakutils.indexes(column, thres=0.35, min_dist=3)
    return peaks

for file in files:
    column = make_building_model(folder, file)["Electricity:Facility [kW](Hourly)"]
    peaks = get_peaks(column) 
    print(peaks)
    #print("n peaks = ", len(maxs[0]))
    print("n peaks = ", len(peaks))
    threshold = 0.3
    print("--------------------------------------------------------------")