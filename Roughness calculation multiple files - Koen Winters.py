
#Author: K.Winters

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

file = pd.read_csv('/Users/Koen/Documents/Roughness measurements/375/mp-375-300x-data-all.csv', encoding = 'unicode_escape')
input_data1 = pd.DataFrame(file, columns=['Sample 1'])
input_data2 = pd.DataFrame(file, columns=['Sample 2'])
input_data3 = pd.DataFrame(file, columns=['Sample 3'])
input_data4 = pd.DataFrame(file, columns=['Sample 4'])
input_data5 = pd.DataFrame(file, columns=['Sample 5'])
input_data6 = pd.DataFrame(file, columns=['Sample 6'])
input_data7 = pd.DataFrame(file, columns=['Sample 7'])
input_data8 = pd.DataFrame(file, columns=['Sample 8'])
input_data9 = pd.DataFrame(file, columns=['Sample 9'])
input_data10 = pd.DataFrame(file, columns=['Sample 10'])


sampling_length = 1000 #choose the sampling length
start_point = 0 # start point in data
end_point = start_point + sampling_length #end point

input_data1 = input_data1[start_point:end_point]
input_data2 = input_data2[start_point:end_point]
input_data3 = input_data3[start_point:end_point]
input_data4 = input_data4[start_point:end_point]
input_data5 = input_data5[start_point:end_point]
input_data6 = input_data6[start_point:end_point]
input_data7 = input_data7[start_point:end_point]
input_data8 = input_data8[start_point:end_point]
input_data9 = input_data9[start_point:end_point]
input_data10 = input_data10[start_point:end_point]







data = np.array([input_data1,input_data2,input_data3,input_data4,input_data5,input_data6,input_data7,input_data8,input_data9,input_data10])

for i in range(len(data)):
    data[i] = (data[i] - np.mean(data[i]))

linesegment = int(sampling_length/5) #makes 5 equal linesegments from data set length

def inputdata(reshape): ##Divide input data in 5 equal segments
    segmented_data = reshape.reshape(5,linesegment)
    Rz_med = np.zeros(len(segmented_data))  # initializing Rz_med
    Rzi = np.zeros(len(segmented_data))  # initializing Rzi
    return segmented_data, Rz_med, Rzi


def roughness(segmented_data):
    for i in range(len(segmented_data)):
        Rz_med[i] = np.mean(segmented_data[i,:])
        Rzimax = max(segmented_data[i,:]) #- Rz_med[i]
        Rzimin = min(segmented_data[i,:]) #- Rz_med[i]
        Rzi[i] = Rzimax + abs(Rzimin)
    Rz = np.mean(Rzi)
    # print('The Rzi =',Rzi)

    return Rz_med,Rz

Rt = np.zeros(len(data))
Rz_result = np.zeros(len(data))

for k in range(len(data)):
    segmented_data, Rz_med, Rzi = inputdata(data[k])
    Rz_med,Rz = roughness(segmented_data)
    Rz_result[k] = Rz
    Rt[k] = max(data[k])-min(data[k])


print(f"Rz = {Rz_result} \nRt = {Rt}")

for l in range(len(data)):
    ra_data = abs(data[l])
    Ra = np.mean(ra_data)
    print("Ra:",Ra)




# Set the font family to Georgia
# font_family = 'Georgia'
# plt.rcParams['font.family'] = font_family
#
# plt.figure()
# plt.axhline(0, color='black')
# plt.title("Surface roughness")
# plt.xlabel("Distance along the Surface (μm)")
# plt.ylabel("Surface Roughness (μm)")
# legend_text = f"Rz: {Rz}, Ra: {Ra}, Rt {Rt}"
#
# # Set the font properties for the text
# font_properties = fm.FontProperties(style='normal', size=8)


# # plt.text(900, 50, legend_text, fontproperties=font_properties)
# plt.text(0.7, 0.85, legend_text, transform=plt.gca().transAxes, fontproperties=font_properties)
# tu_delft_color = (0/255, 166/255, 214/255)
# plt.xlim(0, 1000)
#
# plt.plot(data[0], color=tu_delft_color)
# plt.show()




