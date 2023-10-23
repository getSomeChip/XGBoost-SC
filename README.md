This repository provides XGBoost-SC supporting code for the ground motion prediction model, which is used to call the ground motion prediction model. This repository contains the following files: __Model_Calling_Code.py (used to call the model)__, __XGBoost-SC.pickle (model file)__.

There are four places where the user of this code can change when using it, where __1 is the path of the model file; 2 is the parameters, such as magnitude, etc.; 3 and 4 are to save the SA data as a txt file and to save the attenuation curve picture, respectively__.

This code is written in __Python__, and only supports Python editor calls. Detailed instructions for operating the code have been noted in various locations in the code file.

modelFilePath is the path to the downloaded model XGBoost-SC.pickle on the user's computer, __required__.

The user needs to enter the __Required__ parameters:
Magnitude (MJMA), hypo-central distance (km), focal depth (km), site condition Vs30 (m/s), focal mechanism, site altitude.

txtFilePath and curveFilePath are the paths of the output file and the attenuation curve file respectively. Note: Users only need to input the path of the folder, and this item is __optional__.



The rest of the codes are calculated codes and do not need to be changed by the user.
<div align=center>
<img src="https://github.com/getSomeChip/XGBoost-SC/assets/148534036/dd942ca2-33f5-4a49-832c-a4e44167bec3">
</div>


This is the output PGA and SA data.
<div align=center>
<img src="https://github.com/getSomeChip/XGBoost-SC/assets/148534036/f25dec5b-86bd-4a69-ac6d-599a69d11e3e">
</div>

This is the decay curve.
<div align=center>
<img src="https://github.com/getSomeChip/XGBoost-SC/assets/148534036/864c1664-f1df-44ec-9b73-20aaa36dda32">
</div>

Model output file.
<div align=center>
<img src="https://github.com/getSomeChip/XGBoost-SC/assets/148534036/6399af6d-ff66-496e-b724-3c491875c8a2">
</div>
