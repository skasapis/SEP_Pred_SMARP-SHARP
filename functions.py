# functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def round_to_n(x,n):
    if np.isnan(x) or x == 0: return x
    else: return round(x, -int(np.floor(np.log10(abs(x)))) + (n - 1))

def convert_class_to_intensity(flare_class):
    # Define the conversion factors
    conversion_factors = {'C': 1.0e-6, 'M': 1.0e-5, 'X': 1.0e-4}
    # Extract the letter and the number from the flare class
    letter = flare_class[0]
    number = float(flare_class[1:])
    print(number)
    # Apply the appropriate conversion factor
    intensity = number * conversion_factors[letter]
    return intensity

# Coordinate transformation
def coordinate_transformation(nsew_coords):
    if len(nsew_coords) < 6:
        pos_neg_coords = (0, 0)
    elif (nsew_coords[0] == 'N' or nsew_coords[0] == 'S') and (nsew_coords[3] == 'E' or nsew_coords[3] == 'W'):
        # Latitude Coordinate Sign
        if nsew_coords[0] == 'N': lat_sign = 1
        else: lat_sign = -1
        # Londitude Coordinate Sign
        if nsew_coords[3] == 'W': lon_sign = 1
        else: lon_sign = -1
        # Transform
        pos_neg_coords = (lat_sign*int(nsew_coords[1:3]),lon_sign*int(nsew_coords[4:6]))
        #pos_neg_coords = str(pos_neg_coords)
    else:
        pos_neg_coords = (0, 0)
    return pos_neg_coords

# Function to calculate the angular distance between the active region and the magnetic footpoint of earth
def angular_distance(coords): #(LAT_FTW,LON_FTW)
    # Convert in radiants before I use in sin and cosine (1 Degree = 0.01745329 Radian)
    theta1 = coords[0]*0.01745329 # theta_1, phi_1 is the latitude and longitude of the active region
    phi1 = coords[1]*0.01745329
    theta2 = 0*0.01745329 # theta_2, phi_2 is the latitude and longitude of the magnetic foot point of earth (for now constant)
    phi2 = 45*0.01745329
    # angular distance
    dist = np.arccos(np.sin(theta1)*np.sin(theta2) + np.cos(theta1)*np.cos(theta2)*np.cos(phi1-phi2)) #distance is in radiants - I can convert back to degrees
    # Add sign if east or west of W45
    add_sign = True
    if add_sign:
        if coords[1] < 45: dist = -dist
    return dist

# Get the SHMARP points righte before the beginning of the flare (for a variable number of points before)
def get_data_points_before_start(flare, matching_rows, before_start_num):
    if matching_rows.shape[0] == 0:
        shmarp_parameters = pd.DataFrame([0]*len(matching_rows.columns), index=matching_rows.columns).transpose()
        print('SHMARPs:',shmarp_parameters)
    else:
        t_start = pd.to_datetime(flare['t_start'])
        shmarp_parameters = matching_rows[pd.to_datetime(matching_rows['T_OBS']) < t_start].iloc[-before_start_num:]
    return shmarp_parameters

def calculate_tss(tp, tn, fp, fn):
    tss = (tp/(tp+fn)) - (fp/(fp+tn))
    return tss

def calculate_hss(tp, tn, fp, fn):
    hss = 2*(tp*tn - fp*fn) / ((tp+fn)*(fn+tn) + (tp+fp)*(fp+tn))
    return hss

def calculate_far(tp, tn, fp, fn):
    far = fp/(fp+tn)
    return far

def calculate_f1(tp, tn, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1