import peakutils


def get_peaks(column):
    peaks_array  = peakutils.indexes(column, thres=0.55, min_dist=3)
    peaks = {
        "times": peaks_array,
        "number" : len(peaks_array)
        }
    
    return peaks