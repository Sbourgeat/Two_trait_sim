######################################################################################
# Code created by Samuel Bourgeat, PhD candidate at EPFL                             #
# Date: 09/12/2021                                                                   #
# This script reformat all the sync files created during the two traits simulation.  #
#                                                                                    #
######################################################################################

import os
import glob
import gzip


home_data_path = os.path.expanduser('~')
data_path = os.path.join(home_data_path, 'Documents', 'DGRP_simulation', 'New_simulation', 'two_traits', 'sync_files copy')
path_with_all_files = os.path.join(data_path, '*')
output_dir = os.path.join(data_path, "/unzip")

all_files = sorted(glob.glob(path_with_all_files))

T1_files = [f for f in all_files if "T1" in f]
T2_files = [f for f in all_files if "T2" in f]


L = [T1_files]
G = [i for i in range(100)]
R = [i for i in range(100)]

ONE = [i for i in T1_files if str(0)+"_"+'0.sync' in i]
#print(G)


#print(all_files)



T1 = []
T2 = []

Stop = 3

for Trait in L:
    for rep in R:
        for gen in G:

            file = [f for f in Trait if 'selection_T1_r_' + str(rep) + '_' + str(gen) + '.sync' in f]
            #(rep, gen, file)
            file = file[0]
            # print(file)
            with gzip.open(file, "rt") as ff:
                I = 0
                # print('FFF',ff)
                # break
                for line in ff:
                    # print(gen)
                    k = line.split()
                    T1.append(k)
                    #print(k)
                    if gen == 1:
                        T1.append(k)
                        # print(T1)
                    else:
                        T1[I].append(k[4])
                        I += 1
        #bre

        # ak

    #break
    # I+=1

S=0
for i in T1:
    for ii in i:
        if ii == '2R' and S == 0:
            print(ii, end="\t")
            S = 1
        elif ii == '2R' and S ==1:
            print('')
            print(ii, end="\t")
        else:
            print(ii, end="\t")