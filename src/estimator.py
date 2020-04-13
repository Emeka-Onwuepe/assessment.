def covid19ImpactEstimator(input):
      output= { "data": input, "impact": {}, "severeImpact": {} }
      
      output["impact"]["currentlyInfected"]= input["reportedCases"] * 10
      output["severeImpact"]["currentlyInfected"]= input["reportedCases"] * 50
      
      impact= output["impact"]["currentlyInfected"]
      severe= output["severeImpact"]["currentlyInfected"]
      temp=""
      timePeriod= input["timeToElapse"]
      
      if input["periodType"]=="days":
        for index in range(1,timePeriod+1):
            if index % 3 == 0:
                  temp= impact * 2
                  impact =temp
                  temp= severe *2
                  severe= temp
      elif input["periodType"]=="weeks":
        week=timePeriod * 7
        for index in range(1,week+1):
            if index % 3 == 0:
                temp= impact * 2
                impact =temp
                temp= severe *2
                severe= temp
      elif input["periodType"]=="months":
        month= timePeriod * 30
        for index in range(1,month+1):
              temp= impact * 2
              impact =temp
              temp= severe *2
              severe= temp
              
      output["impact"]["infectionsByRequestedTime"] = int(impact)
      output["severeImpact"]["infectionsByRequestedTime"] =int(severe)
      
      output["impact"]["severeCasesByRequestedTime"] = int(output["impact"]["infectionsByRequestedTime"] * 0.15)
      output["severeImpact"]["severeCasesByRequestedTime"] =  int(output["severeImpact"]["infectionsByRequestedTime"] * 0.15)
      
      output["impact"]["hospitalBedsByRequestedTime"] =  int(input["totalHospitalBeds"] * 0.35 -  output["impact"]["severeCasesByRequestedTime"])
      output["severeImpact"]["hospitalBedsByRequestedTime"] = int(input["totalHospitalBeds"] * 0.35 -output["severeImpact"]["severeCasesByRequestedTime"])

      output["impact"]["infectionsByRequestedTime"] = int(output["impact"]["infectionsByRequestedTime"] * 0.05)
      output["severeImpact"]["infectionsByRequestedTime"] =  int(output["severeImpact"]["infectionsByRequestedTime"] * 0.05)

      output["impact"]["casesForVentilatorsByRequestedTime"] = int(output["impact"]["infectionsByRequestedTime"] * 0.02)
      output["severeImpact"]["casesForVentilatorsByRequestedTime"] =  int(output["severeImpact"]["infectionsByRequestedTime"] * 0.02)
      
      output["impact"]["dollarsInFlight"]= int((output["impact"]["infectionsByRequestedTime"] * input["region"]['avgDailyIncomePopulation'] * input["region"]['avgDailyIncomeInUSD'])/input["timeToElapse"])
      output["severeImpact"]["dollarsInFlight"]= int((output["severeImpact"]["infectionsByRequestedTime"] * input['region']['avgDailyIncomePopulation'] *input["region"]['avgDailyIncomeInUSD'])/input["timeToElapse"])
      
      return output






