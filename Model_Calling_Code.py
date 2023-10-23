# -*- coding: utf-8 -*-




'''
Please reda the following:

    
This code is a companion to the World Earthquake Engineering paper, and is used 
to call the XGBoost-SC of the ground shaking prediction model.
If you have any difficulties, please leave a comment on the github repository.


= between is the user to modify the parameters.
* between is the code execution calculation, try not to do change.
'''





from matplotlib import pyplot as plt
import pickle
import numpy as np
import os

plt.rc('font', family='Times New Roman', size=20)



# 1 Set the model path here.
#==============================================================================
# Set the model path here Change the path of the model file here, if you download
# it from github normally, the file name should be: XGBoost-SC.pickle.



modelFilePath = r'C:/Users/DangHotil/Desktop/BSSA-大修/XGBoost-SC.pickle'
#==============================================================================

# 2 Change ground vibration input parameters here.
#==============================================================================
M = 4.6 # Magnitude, in MJMA.
Rhypo = 18.66 # hypo-central distance, in km.
Depth = 17 # depth of earthquake source, in km.
Vs30 = 449 # Vs30, in m/s.
mechName = 'R' # focal mechanism of earthquake, R for Reverse, S for Strike Strip, N for Normal
H = 79 # site altitude, in m.
#==============================================================================


if mechName == 'R':
    mech = 1
    
elif mechName == 'S':
    mech = 2
    
elif mechName == 'N':
    mech = 3    
    
X = [Depth, M, Rhypo, Vs30, mech, H]
#==============================================================================


# 3 Set the path of the model prediction data output file (TXT format), if it is 
# empty then do not set, the output file name is SA-output.txt.
# For example: r'C:\Users\DangHotil\Desktop'
txtFilePath = r'C:\Users\DangHotil\Desktop'

# 4 Set the path of the model predicted decay curve image (PNG format), if it is
# empty then it is not set, and the output file name is SA-figure.png.
# For example: r'C:\Users\DangHotil\Desktop'
curveFilePath = r'C:\Users\DangHotil\Desktop'
#==============================================================================






# The following calculations were performed.
#******************************************************************************
with open(modelFilePath, 'rb') as file:
    model = pickle.load(file)
    
# Call the model to compute the outputs of the input ground vibration parameters.
modelPre = model.predict(np.array([X]))[0]

# The model output is in logarithmic form, so it is converted to gal.
modelpre2Exp = np.exp(modelPre)

# Output is: PGA with SA.

XName = ['PGA', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', 
         '0.07', '0.08', '0.09', '0.1', '0.12', '0.14', '0.15',
         '0.16', '0.18', '0.2', '0.25', '0.3', '0.35', '0.4', '0.45',
         '0.5', '0.6', '0.7', '0.8', '0.9', '1', '1.5', '2', 
         '2.5', '3', '3.5', '4','5']

# Printed display of model predictions
print("{:^10} {:^15}".format("T(s)", "gal"))
print("="*25)
for period, SA in zip(XName, modelpre2Exp):
    if period == 'PGA':
        print("{:^10} {:^15.3f}".format(period, SA))
    else:
        print("{:^10.2f} {:^15.3f}".format(float(period), SA))
#******************************************************************************



#******************************************************************************
if os.path.exists(txtFilePath):
    with open(os.path.join(txtFilePath, 'SA-output.txt'), 'w') as output:
        output.writelines('depth of earthquake source(km)    magnitude(MJMA)    hypo-central distance(km)    Vs30(m/s)    mechanism    station altitude(m)\n')
        output.writelines('          {:.3f}                        {:.2f}                  {:.3f}               {:.3f}         {}              {:.3f}\n\n'.\
                          format(X[0], X[1], X[2], X[3], mechName, X[5]))
        output.writelines("{:^10} {:^15}\n".format("T(s)", "gal"))
        output.writelines('{}\n'.format("="*25))
        
        for period, SA in zip(XName, modelpre2Exp):
            if period == 'PGA':
                output.writelines("{:^10} {:^15.3f}\n".format(period, SA))
            else:
                output.writelines("{:^10.2f} {:^15.3f}\n".format(float(period), SA))
    print('The output file has been saved to {}'.format(os.path.join(txtFilePath, 'SA-output.txt')))
else:
    print('\033[1;31;40mTip: The path {}, does not exist on your computer.\033[0m'.format(txtFilePath))
    print("Ignore this message if you don't need to output a file.")
#******************************************************************************




#******************************************************************************

SAListNum = [float(I) for I in XName if I != 'PGA']

plt.figure(figsize=(10, 8), dpi=100)
plt.plot(SAListNum, modelpre2Exp[1:],color='red', marker='*')
plt.yscale('log')
plt.xscale('log')
plt.yticks([0.01,0.1,1,10,100,1000])
plt.tick_params(which='major',length=5,width=2)
plt.tick_params(which='minor',length=5,width=2)
plt.ylabel('SA (gal)')
plt.text(0.012, 0.01, '$M_{JMA}$ = ' + str(X[1]) +'\n$R_{hypo}$ = ' + \
         str(round(X[2],2)) +'km\nD = ' + str(X[0]) +'km\n$V_{s30}$ = '\
         + str(round(X[3],3)) + 'm/s\n'+ 'H = ' + str(round(X[5],3)) + 'm\n'\
         + 'mechanism = '+ mechName + '\n')
plt.xlabel('T(s)')
plt.ylabel('SA(gal)')

if os.path.exists(curveFilePath):
    plt.savefig(os.path.join(curveFilePath, 'SA-figure.png'))
    print('The decay curve has been saved to {}'.format(os.path.join(txtFilePath, 'SA-figure.png')))

else:
    print('\033[1;31;40mTip: The path {}, does not exist on your computer.\033[0m'.format(curveFilePath))
    print("Ignore this message if you don't need to output a file.")
plt.show()
#******************************************************************************





        
        
        
        
    