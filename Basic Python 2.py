import numpy as np

def get_data():
    df=np.loadtxt('houseelf_earlength_dna_data.csv', dtype=str, delimiter=',')
    return df

def count_GC(s,b,sGC,bGC,data):
    
    for i in range(1,11):
        if float(data[i][1]) < 10.0:
            b.append(float(data[i][1]))
            bGC.append(data[i][2].count('C')+data[i][2].count('G'))
        elif float(data[i][1]) >= 10.0:
            s.append(float(data[i][1]))
            sGC.append(data[i][2].count('C')+data[i][2].count('G'))
    return bGC, sGC

def count_avg_GC(sGC,bGC):
    ave1 = sum(bGC)/len(bGC)
    ave2 = sum(sGC)/len(sGC)
    return ave1, ave2

def write_GC(b,bGC,s,sGC):
    s_ear = np.array(s)
    b_ear = np.array(b)
    bGC_arr = np.array(bGC)
    sGC_arr = np.array(sGC)
    output = np.column_stack((s_ear,sGC_arr,b_ear,bGC_arr))
    np.savetxt('grangers_analysis.csv', output, fmt='%2.1f', delimiter=';')

def main():
    data = get_data()
    big = []
    small = []
    big_GC_number = []
    small_GC_number = []
     
    count_GC(small,big,small_GC_number,big_GC_number,data)
    
    print(count_avg_GC(small_GC_number,big_GC_number))
    write_GC(big, big_GC_number, small, small_GC_number)
    

    
    
main()
data = get_data()
for i in range(1,len(data)):
    print(data[i][1])