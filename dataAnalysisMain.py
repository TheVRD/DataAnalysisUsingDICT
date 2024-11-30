import lib_data_analysis_usingDICT as dct

def main():
    dct.outresultLST = dct.data_analysis_usingDICT()

    print(f"{dct.outresultLST[0][0]} send most number of atheletes, and that number was {dct.outresultLST[0][1]} ")
    print(f"{dct.outresultLST[1][0]} won most number of medals, and that number was {dct.outresultLST[1][1]} ")
    print(f"{dct.outresultLST[2][0]} has the highest winning percentage, and that value was {dct.outresultLST[2][1]} ")

main()

