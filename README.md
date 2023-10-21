This repository provides XGBoost-SC supporting code for the ground motion prediction model, which is used to call the ground motion prediction model. This repository contains the following files: __Model_Calling_Code.py (used to call the model)__, __XGBoost-SC.pickle (model file)__.

There are four places where the user of this code can change when using it, where __1 is the path of the model file; 2 is the parameters, such as magnitude, etc.; 3 and 4 are to save the SA data as a txt file and to save the attenuation curve picture, respectively__.

This code is written in __Python__, and only supports Python editor calls. Detailed instructions for operating the code have been noted in various locations in the code file.

modelFilePath为所下载模型XGBoost-SC.pickle在用户电脑中的路径，__必填__

用户需要输入 __必填__ 参数：
震级(MJMA)、震源距(km)、震源深度(km)、场地条件Vs30(m/s)。

txtFilePath与curveFilePath分别SA输出文件与衰减曲线文件保存路径，注：用户仅需输入文件夹路径即可，且此项为 __选填__。


其余代码为计算代码，用户无须更改
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/65f3fbc6-aa00-4fc7-a12a-801845d270c3">
</div>

此为所输出PGA与SA数据。
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/ec74fca0-714c-49d7-9c2f-e8d122dec9ee">
</div>


此为衰减曲线。
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/c341bba4-7dc2-4bbe-9a82-a3a13abb413b">
</div>

模型输出文件。
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/46d219d0-8d2e-48b1-9fc0-c5acd1c91c70">
</div>
