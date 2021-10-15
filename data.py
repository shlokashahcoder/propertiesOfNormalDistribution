import pandas as pd
import statistics
 
df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

range1_min,range1_max = mean-std, mean+std
range2_min,range2_max = mean-(2*std), mean+(2*std)
range3_min,range3_max = mean-(3*std), mean+(3*std)

range1_array = [i for i in  data if i > range1_min and i < range1_max]
range2_array = [i for i in  data if i > range2_min and i < range2_max]
range3_array = [i for i in  data if i > range3_min and i < range3_max]


totalData= len(data)
range1_data = len(range1_array)
range2_data = len(range2_array)
range3_data = len(range3_array)

percentange1 = (range1_data/totalData)*100
percentange2 = (range2_data/totalData)*100
percentange3 = (range3_data/totalData)*100
print(percentange1,percentange2,percentange3)