import dataConstants as dc

def data_analysis_usingDICT():
    #printing numnber of rows in both the datasets
    for key,value in dc.dataset.items():
        print(f"Number of rows in {key} dataset is {len(value['data'])}")
    
    #combining respective rows with columns
    for key,val in dc.dataset.items():
        val["data_as_dicts"] = []
        for row in val["data"]:
            data_row_dict = dict(zip(val["columns"],row))
            val["data_as_dicts"].append(data_row_dict)
    #creating country with athelete code dict ??
    country_atheleteCode_pair = [
    (row["country"],row["code"]) for row in dc.dataset["atheletes"]["data_as_dicts"]]

    #creating list of countries of atheletes
    countries_of_atheletes = [row["country"] for row in dc.dataset["atheletes"]["data_as_dicts"]]
    #number of atheles by country
    numberOfAtheletesByCountry = dc.collections.Counter(countries_of_atheletes)
    
    maxAtheletesByCountry,maxvalue = dc.maximaAndMinima(numberOfAtheletesByCountry)
    dc.resultLST.append((maxAtheletesByCountry,maxvalue))

    #medal winners by countries
    countries_medalWinners = [row["country"] for row in dc.dataset["medals"]["data_as_dicts"]]
    numberOfMedalsByCountry = dc.collections.Counter(countries_medalWinners)

    maxMedalsByCountry,maxvalue = dc.maximaAndMinima(numberOfMedalsByCountry)
    dc.resultLST.append((maxMedalsByCountry,maxvalue))

    #Finding out percentage of medal winners by country
    percentageOfMedalWinners = {}
    for tcountry, tvalue in numberOfAtheletesByCountry.items():
        for mcountry, mvalue in numberOfMedalsByCountry.items():
            if tcountry == mcountry:
                percentageOfMedalWinners[mcountry] = (mvalue/tvalue*100)
        if tcountry not in numberOfMedalsByCountry.keys():
            percentageOfMedalWinners[tcountry] = 0
    #not required but doing for fun
    sortedDict = {}
    for key in sorted(percentageOfMedalWinners, key=percentageOfMedalWinners.get):
        sortedDict[key] = percentageOfMedalWinners[key]
    
    maxMedalWinnerPercentage,maxvalue = dc.maximaAndMinima(sortedDict)
    dc.resultLST.append((maxMedalWinnerPercentage,maxvalue))

    return(dc.resultLST)


    
    