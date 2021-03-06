import numpy as np
import matplotlib
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False})
import matplotlib.pylab as plt
plt.close('all')



showHD10700 = True
showHD26965 = True
showHD33411 = True
showHD101501 = True



if showHD10700:
    data = np.loadtxt("10700_activity.csv",delimiter=',', 
                      skiprows=1, usecols=(1,4,5))
    time1 = data[:,0].T #in MJD
    val1RV, val1RVerr = data[:,1].T, data[:,2].T
    
    plt.figure()
    plt.title('HD 10700 observations')
    plt.errorbar(time1, val1RV, val1RVerr, fmt='.')
    
    #Lowell Observatory is on Flagstaff, Arizona, United States.
    # UTC Offset: UTC -7; 8 hours behind Porto
    import datetime as dt
    from tedi import time
    
    jdTime = time.mjd_to_jd(time1)
    
    normalTime = []
    for i, j in enumerate(jdTime):
        normalTime.append(time.jd_to_datetime(j))
    normalTime = np.array(normalTime) #Greenwich time
    
    delta = dt.timedelta(hours=7)
    expresTime = []
    for i, j in enumerate(normalTime):
        expresTime.append(np.array([i, j - delta]))
    expresTime = np.array(expresTime) # Arizona Time
    
    #variations
    variations1 = [val1RV[0: 2+1].ptp(), val1RV[3: 4+1].ptp(), val1RV[5: 7+1].ptp(),
                  val1RV[8: 10+1].ptp(), val1RV[11: 15+1].ptp(), val1RV[16: 19+1].ptp(),
                  val1RV[20: 25+1].ptp(),val1RV[26: 45+1].ptp(),val1RV[46: 50+1].ptp(),
                  val1RV[51: 74+1].ptp(),val1RV[75: 79+1].ptp(),val1RV[80: 84+1].ptp(),
                  val1RV[85: 89+1].ptp(),val1RV[90: 94+1].ptp(),val1RV[95: 99+1].ptp(),
                  val1RV[100: 104+1].ptp(),val1RV[105: 109+1].ptp(),val1RV[110: 113+1].ptp(),
                  val1RV[114: 117+1].ptp(),val1RV[118: 120+1].ptp(),val1RV[121: 123+1].ptp(),
                  val1RV[124: 126+1].ptp(),val1RV[127: 129+1].ptp(),val1RV[130: 132+1].ptp(),
                  val1RV[133: 135+1].ptp(),val1RV[136: 140+1].ptp(),val1RV[141: 145+1].ptp(),
                  val1RV[146].ptp(),val1RV[147: 150+1].ptp(),val1RV[151: 155+1].ptp(),
                  val1RV[156: 160+1].ptp(),val1RV[161: 163+1].ptp(),val1RV[164: 168+1].ptp(),
                  val1RV[169: 173+1].ptp()]
    variations1 = np.array(variations1)
    plt.figure()
    plt.title('HD 10700 RV variation per observation (average = {0}m/s)'.format(np.round(variations1.mean(),3)))
    plt.plot(variations1, '.k')
    
    
################################################################################
if showHD26965:
    data = np.loadtxt("26965_activity.csv",delimiter=',', 
                      skiprows=1, usecols=(1,4,5))
    time2 = data[:,0].T
    val2RV, val2RVerr = data[:,1].T, data[:,2].T
    
    plt.figure()
    plt.title('HD 26965 observations')
    plt.errorbar(time2, val2RV, val2RVerr, fmt='.')
    
    #Lowell Observatory is on Flagstaff, Arizona, United States.
    # UTC Offset: UTC -7; 8 hours behind Porto
    import datetime as dt
    from tedi import time
    
    jdTime = time.mjd_to_jd(time2)
    
    normalTime = []
    for i, j in enumerate(jdTime):
        normalTime.append(time.jd_to_datetime(j))
    normalTime = np.array(normalTime) #Greenwich time
    
    delta = dt.timedelta(hours=7)
    expresTime = []
    for i, j in enumerate(normalTime):
        expresTime.append(np.array([i, j - delta]))
    expresTime = np.array(expresTime) # Arizona Time

    #variations
    variations2 = [val2RV[0].ptp(), val2RV[1: 2+1].ptp(), val2RV[3].ptp(),
                  val2RV[4: 6+1].ptp(), val2RV[7: 9+1].ptp(), val2RV[10: 12+1].ptp(),
                  val2RV[13: 15+1].ptp(), val2RV[16: 18+1].ptp(), val2RV[19: 22+1].ptp(),
                  val2RV[23: 26+1].ptp(), val2RV[27: 30+1].ptp(), val2RV[31: 34+1].ptp(),
                  val2RV[35: 38+1].ptp(), val2RV[39: 42+1].ptp(), val2RV[43: 46+1].ptp(),
                  val2RV[47: 50+1].ptp(), val2RV[51: 54+1].ptp(), val2RV[55: 58+1].ptp(),
                  val2RV[59: 60+1].ptp(), val2RV[61].ptp(), val2RV[62: 63+1].ptp(),
                  val2RV[64: 66+1].ptp(), val2RV[67: 69+1].ptp(), val2RV[70: 72+1].ptp(),
                  val2RV[73: 75+1].ptp(), val2RV[76: 78+1].ptp(), val2RV[79: 81+1].ptp(),
                  val2RV[82: 87+1].ptp(), val2RV[88: 90+1].ptp(), val2RV[91: 94+1].ptp(),
                  val2RV[95: 97+1].ptp(), val2RV[98: 102+1].ptp(), val2RV[103: 106+1].ptp(),
                  val2RV[107].ptp(), val2RV[108: 110+1].ptp(), val2RV[111: 113+1].ptp()]
    
    variations2 = np.array(variations2)
    plt.figure()
    plt.title('HD 26965 RV variation per day (average = {0}m/s)'.format(np.round(variations2.mean(),3)))
    plt.plot(variations2, '.k')
    
    
################################################################################
if showHD33411:
    data = np.loadtxt("34411_activity.csv",delimiter=',', skiprows=1, usecols=(1,4,5))
    time3 = data[:,0].T
    val3RV, val3RVerr = data[:,1].T, data[:,2].T
    
    plt.figure()
    plt.title('HD 34411 observations')
    plt.errorbar(time3, val3RV, val3RVerr, fmt='.')
    
    #Lowell Observatory is on Flagstaff, Arizona, United States.
    # UTC Offset: UTC -7; 8 hours behind Porto
    import datetime as dt
    from tedi import time
    
    jdTime = time.mjd_to_jd(time3)
    
    normalTime = []
    for i, j in enumerate(jdTime):
        normalTime.append(time.jd_to_datetime(j))
    normalTime = np.array(normalTime) #Greenwich time
    
    delta = dt.timedelta(hours=7)
    expresTime = []
    for i, j in enumerate(normalTime):
        expresTime.append(np.array([i, j - delta]))
    expresTime = np.array(expresTime) # Arizona Time
    
    #variations
    variations3 = [val3RV[0: 2+1].ptp(), val3RV[3: 5+1].ptp(), val3RV[6: 8+1].ptp(),
                    val3RV[9: 11+1].ptp(), val3RV[12: 14+1].ptp(), val3RV[15: 17+1].ptp(),
                    val3RV[18: 20+1].ptp(), val3RV[21: 25+1].ptp(), val3RV[26: 29+1].ptp(),
                    val3RV[30: 33+1].ptp(), val3RV[34: 37+1].ptp(), val3RV[38: 41+1].ptp(),
                    val3RV[42: 45+1].ptp(), val3RV[46: 49+1].ptp(), val3RV[50: 53+1].ptp(),
                    val3RV[54: 56+1].ptp(), val3RV[57: 60+1].ptp(), val3RV[61: 64+1].ptp(),
                    val3RV[65: 68+1].ptp(), val3RV[69: 72+1].ptp(), val3RV[73: 76+1].ptp(),
                    val3RV[77: 79+1].ptp(), val3RV[80: 84+1].ptp(), val3RV[85: 88+1].ptp(),
                    val3RV[89: 93+1].ptp(), val3RV[94: 97+1].ptp(), val3RV[98: 99+1].ptp(),
                    val3RV[100: 102+1].ptp(), val3RV[103: 105+1].ptp(), val3RV[106: 107+1].ptp(),
                    val3RV[108: 109+1].ptp(), val3RV[110: 111+1].ptp(), val3RV[112: 114+1].ptp(),
                    val3RV[115: 117+1].ptp(), val3RV[118: 120+1].ptp(), val3RV[121: 122+1].ptp(),
                    val3RV[123: 125+1].ptp(), val3RV[126: 128+1].ptp(), val3RV[129: 130+1].ptp(),
                    val3RV[131].ptp(), val3RV[132: 134+1].ptp(), val3RV[135: 137+1].ptp(),
                    val3RV[138: 140+1].ptp(), val3RV[141: 143+1].ptp(), val3RV[144: 146+1].ptp(),
                    val3RV[147: 149+1].ptp(), val3RV[150: 152+1].ptp(), val3RV[153: 155+1].ptp(),
                    val3RV[156: 158+1].ptp(), val3RV[159: 161+1].ptp(), val3RV[162: 166+1].ptp(),
                    val3RV[167: 169+1].ptp(), val3RV[170: 172+1].ptp(), val3RV[173: 175+1].ptp(),
                    val3RV[176: 179+1].ptp(), val3RV[180: 181+1].ptp(), val3RV[182: 184+1].ptp(),
                    val3RV[185: 187+1].ptp()]
    
    variations3 = np.array(variations3)
    plt.figure()
    plt.title('HD 34411 RV variation per day (average = {0}m/s)'.format(np.round(variations3.mean(),3)))
    plt.plot(variations3, '.k')
    
    
################################################################################
if showHD101501:
    data = np.loadtxt("101501_activity.csv",delimiter=',', 
                      skiprows=1, usecols=(1,4,5))
    time4 = data[:,0].T
    val4RV, val4RVerr = data[:,1].T, data[:,2].T
    
    plt.figure()
    plt.title('HD 10700 observations')
    plt.errorbar(time4, val4RV, val4RVerr, fmt='.')
    
    #Lowell Observatory is on Flagstaff, Arizona, United States.
    # UTC Offset: UTC -7; 8 hours behind Porto
    import datetime as dt
    from tedi import time
    
    jdTime = time.mjd_to_jd(time4)
    
    normalTime = []
    for i, j in enumerate(jdTime):
        normalTime.append(time.jd_to_datetime(j))
    normalTime = np.array(normalTime) #Greenwich time
    
    delta = dt.timedelta(hours=7)
    expresTime = []
    for i, j in enumerate(normalTime):
        expresTime.append(np.array([i, j - delta]))
    expresTime = np.array(expresTime) # Arizona Time
    
    #variations
    variations4 = [val4RV[0: 3+1].ptp(), val4RV[4: 6+1].ptp(), val4RV[7].ptp(),
                    val4RV[8].ptp(), val4RV[9].ptp(), val4RV[10].ptp(),
                    val4RV[11].ptp(), val4RV[12].ptp(), val4RV[13].ptp(),
                    val4RV[14: 15+1].ptp(), val4RV[16].ptp(), val4RV[17].ptp(),
                    val4RV[18: 19+1].ptp(), val4RV[20: 21+1].ptp(), val4RV[22: 25+1].ptp(),
                    val4RV[26: 27+1].ptp(), val4RV[28: 30+1].ptp(), val4RV[31 : 33+1].ptp(),
                    val4RV[34: 36+1].ptp(), val4RV[37: 39+1].ptp(), val4RV[40 : 42+1].ptp(),
                    val4RV[43: 44+1].ptp()]
    
    variations4 = np.array(variations4)
    plt.figure()
    plt.title('HD 101501 RV variation per day (average = {0}m/s)'.format(np.round(variations4.mean(),3)))
    plt.plot(variations4, '.k')