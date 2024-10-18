import sys
import numpy as np
from collections import defaultdict

def mid_point(start, stop):
    mid = (start + stop) / 2
    return int(mid)

matrix_dict = defaultdict(lambda:defaultdict(int))

for line in sys.stdin:
        line = line.strip()

        new_list = line.split("\t")

        ctcf_start = int(new_list[2])

        ctcf_stop = int(new_list[3])

        fragment_start = int(new_list[8])

        fragment_stop = int(new_list[9])

        len_fragment = int(new_list[11])

        ctcf_mid = mid_point(ctcf_start, ctcf_stop)

        fragment_mid = mid_point(fragment_start, fragment_stop)

        relative_distance = round(fragment_mid - ctcf_mid)

        matrix_dict[len_fragment][relative_distance] +=1 


with open("final_matrix_wide_new.txt","a") as file:
	relative_positions = range(-509,510)
	file.write("\t"+"\t".join(map(str,relative_positions))+"\n")
	for keys in matrix_dict.keys():
		new_array = np.zeros(1019,dtype = int)
		for values in matrix_dict[keys].items():
			pos = int(values[0])+509
			new_array[pos] = values[1]
		file.write(f"{keys}\t " + "\t".join(map(str, new_array)) + "\n")   
        
