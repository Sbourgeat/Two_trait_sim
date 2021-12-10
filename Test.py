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
data_path = os.path.join(home_data_path, 'Documents', 'DGRP_simulation', 'New_simulation', 'two_traits',
                         'sync_files copy')
path_with_all_files = os.path.join(data_path, '*')
output_dir = os.path.join(data_path, "/unzip")

all_files = sorted(glob.glob(path_with_all_files))

T1_files = [f for f in all_files if "T1" in f]
T2_files = [f for f in all_files if "T2" in f]

all_the_files = [T2_files]
G = [i for i in range(1,99)]
R = [i for i in range(99)]

ONE = [i for i in T1_files if str(0) + "_" + '0.sync' in i]
# print(G)


# print(all_files)


T2 = []

Stop = 4

total_line = range(740947)
rep_count = 0

for Line_to_process in total_line:
    # print(f'LINE={LINE}')
    T2 = []
    #if Line_to_process == 2:
    #    break
    for Trait in all_the_files:
        for rep in R:
            #print(f'Rep={rep}')
            #if rep == 4:
            #    break
            for gen in G:

                #print(f'gen={gen}')

                #if gen == Stop:
                    #break

                file = [f for f in Trait if 'selection_T2_r_' + str(rep) + '_' + str(gen) + '.sync' in f]
                #os.system(f"echo '{file}'")
                #print(rep, gen, file)
                file = file[0]
                # print(file)

                with gzip.open(file, "rt") as ff:
                    list_pos_count = 0
                    # print('FFF',ff)
                    # break
                    line_pos_count = 0
                    for line in ff:
                        #print(T2)
                        if rep == 0:
                            if line_pos_count == Line_to_process:
                                #print(T2)
                                k = line.split()
                                #T2.append([k])
                                # print(k)
                                if gen == 1:
                                    T2 = [i for i in k]
                                    line_pos_count += 1
                                    #print(T2)
                                    # print(T1)
                                else:
                                    T2.append(k[4])
                                    line_pos_count += 1
                                    #print(T2)
                            else:
                                line_pos_count += 1
                        else:
                            if line_pos_count == Line_to_process:
                                k = line.split()
                                #T2.append(T2[3])
                                # print(k)
                                if gen == 1:
                                    T2.append(T2[3])
                                    #T2[Line_to_process].append(k[3])
                                    T2.append(k[4])
                                    line_pos_count += 1
                                    #print(T2)
                                    # print(T1)
                                else:
                                    T2.append(k[4])
                                    line_pos_count += 1
                                    #print(T2)
                            else:
                                line_pos_count += 1
            # break

        # break
        # I+=1

    for i in T2:
        print(i, end="\t")
    print('')


