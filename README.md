This repository includes the data and code which was used for the research described in the paper below:
Kasapis, S., Kitiashvili, I.N., Kosovich, P., Kosovichev, A.G., Sadykov, V.M., O'Keefe, P., and Wang, V. Forecasting SEP Events During Solar Cycles 23 and 24 Using Interpretable Machine Learning. The Astrophysical Journal, (2024, forthcoming). 

Prediction of the Solar Energetic Particle (SEP) events garner increasing interest as space missions extend beyond Earth’s protective magnetosphere. 
These events, which are, in most cases, products of magnetic reconnection-driven processes during solar flares or fast coronal-mass-ejection-driven shock waves, pose significant radiation hazards to aviation, space-based electronics, and particularly, space exploration. 
In this work, we utilize the recently developed dataset that combines the Solar Dynamics Observatory/Helioseismic and Magnetic Imager’s (SDO/HMI) Space weather HMI Active Region Patches (SHARP) and the Solar and Heliospheric Observatory/Michelson Doppler Imager’s (SoHO/MDI) Space Weather MDI Active Region Patches (SMARP). 
We employ a suite of machine learning strategies, including Support Vector Machines (SVM) and regression models, to evaluate the predictive potential of this new data product for a forecast of post-solar flare SEP events. 
Our study indicates that despite the augmented volume of data, the prediction accuracy reaches 0.7 ± 0.1, which aligns with but does not exceed these published benchmarks. 
A linear SVM model with training and testing configurations that mimic an operational setting (positive-negative imbalance) reveals a slight increase (+0.04 ± 0.05) in the accuracy of a 14-hour SEP forecast compared to previous studies. 
This outcome emphasizes the imperative for more sophisticated, physics-informed models to better understand the underlying processes leading to SEP events.

The folder includes the content necessary to reproduce the results of the aforementioned paper. The folder includes:

a) Seven jupyter notebook files (.ipynb) which correspond to different models and experimental setups.
b) The dataset our team developed in a file named "flares_matched_manual.dat"
c) A .py file that contains all necessary functions used within the .ipynb files.
d) The .csv file which contains the SHARP-SMARP dataset values for observations up to 2023 can be downloaded from here:
https://drive.google.com/file/d/1-bCMlPbFzoCjBhGwfPHJXAUC_Cc5OmQI/view?usp=sharing

The solar flare data file (flares_matched_manual.dat) noted in (b) contains several key headers that describe various attributes of each recorded solar flare event. 
The t_start, t_max, and t_end columns represent the start time, peak time, and end time of the solar flare, respectively. The class column denotes the classification of the flare (e.g., C, M, X), indicating its magnitude. 
The location column provides the heliographic coordinates of the flare on the solar disk, specified in terms of latitude (N/S) and longitude (E/W). The AR column identifies the active region number associated with the flare. 
The SEP_Match column indicates whether the flare was associated with a Solar Energetic Particle (SEP) event (True/False). The intensity column gives the flare's intensity, converted to a numeric value based on its class. 
The coords column lists the numerical coordinates derived from the location field, while the ang_dist column calculates the angular distance between an active solar region and the Earth's magnetic footpoint.

The python script (functions.py) noted in (c) contains a variety of functions that perform different tasks related to data processing, conversion, and evaluation metrics. 
The round_to_n function rounds a number to a specified number of significant digits. The convert_class_to_intensity function converts solar flare classifications (e.g., C, M, X) into their corresponding intensity values. 
The coordinate_transformation function converts geographic coordinates from the NSEW format to positive or negative numeric values. 
The angular_distance function calculates the angular distance between an active solar region and the Earth's magnetic footpoint. 
The get_data_points_before_start function retrieves SHMARP (Space Weather HMI Active Region Patch) data points that occur just before the start of a solar flare. 
The calculate_tss, calculate_hss, calculate_far, and calculate_f1 functions compute various evaluation metrics (True Skill Statistic, Heidke Skill Score, False Alarm Ratio, and F1 Score, respectively) used in assessing the performance of predictive models. 
Each of these functions contributes to different aspects of data analysis and model evaluation in the context of solar physics and space weather forecasting.


All jupyter notebooks in (a) are contain code for training and validating different ML models on the SMARP-ShARP dataset except for "match_SHMARPs_time.ipynb" which creates the dataset files (using the (b) and (d) files) necessary to run the ML examples in the rest .ipynb files. 
The SMARP-SHARP dataset file in (d) includes a continuous set of 21 keywords (Table 1 in Kasapis et al.), representing homogeneous observations of active region patches from SoHO/MDI and SDO/HMI for the period between April 4, 1996, and May 9, 2023. 
To obtain the results discussed in the aforementioned publication one would have to: 
a) Create his dataset by running match_SHMARPs_time.ipynb (requires the "flares_matched_manual.dat" and the SHARP-SMARP .csv dataset file)
b) Run any of the other .ipynb files based on which ML model he wants to train and validate (requires produced .dat file from (a) and the functions.py file). 
