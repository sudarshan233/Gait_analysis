# Importing Pandas and Numpy for data analysis and data loading
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Loading dataset using Pandas
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Function for Sensor Analysis
def Sensor_Analysis():
    count_Acc=0
    count_Gyro=0
    for i in train_data.columns:
        if 'Acc' in i:
            count_Acc+=1
        elif 'Gyro' in i:
            count_Gyro+=1
        else:
            pass
    plt.figure(figsize=(5,6))
    plt.bar(x=['Accelerometer', 'Gyroscope'], height=[count_Acc, count_Gyro],color=['tab:red', 'tab:blue'])
    plt.title("SENSOR ANALYSIS", fontsize=20)
    plt.xlabel("Sensor")
    plt.ylabel("Utilization time")
    plt.show()

Sensor_Analysis()

Sampling_rate=50
test_activities=test_data["Activity"].value_counts().index
print(test_activities)


def test_plot_activity(activity,test_data):
    fig, (ax0,ax1,ax2) = plt.subplots(nrows=3,figsize=(15,5), sharex=True)
    test_plot_axis(ax0,test_data['angle(X,gravityMean)'],'X-Axis')
    test_plot_axis(ax1,test_data['angle(Y,gravityMean)'],'Y-Axis')
    test_plot_axis(ax2,test_data['angle(Z,gravityMean)'], 'Z-Axis')
    plt.subplots_adjust(hspace=0.2)
    fig.suptitle(activity)
    plt.subplots_adjust(top=0.90)
    plt.show()
def test_plot_axis(ax,y,title):
    ax.plot(y,'g')
    ax.set_title(title)
    ax.xaxis.set_visible(False)
    ax.set_ylim([min(y)-np.std(y),max(y)+np.std(y)])
    ax.grid(True)

for activity in test_activities:
    data_for_plot=test_data[(test_data['Activity']==activity)][:Sampling_rate*10]
    test_plot_activity(activity,data_for_plot)



