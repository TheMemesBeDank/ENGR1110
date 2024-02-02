import pandas as pd
import matplotlib.pyplot as plt 

#Sophie and Braeden:
def computeAvgTempChange(temps_list):
  sumTempChange = 0
  avgTempChangeUnrounded = 0
  for i in range(len(temps_list)):
    sumTempChange += temps_list[i]
  avgTempChangeUnrounded = sumTempChange/len(temps_list)
  return round(avgTempChangeUnrounded, 3)

def compute_average(Temperature):
  return sum(Temperature)/len(Temperature)

#Zack:
while(True): # ensures program can run indefinitely -Z
  
  should_loop = True     # using to make sure we get a valid choice -Z
  while(should_loop):
    should_loop = False   # if this remains False, we can exit safely -Z
    
    # add countries to this list below for user to select from -Z
    #Sophie, Christian, and Jackson:
    print('Type the number of the desired country:')
    print("1. China")
    print("2. United Kingdom")
    print("3. India")
    print("4. Nigeria")
    print("5. Iraq")
    print("6. Cuba")
    print("7. United States")
    print("8. Australia")
    # etc, etc, etc... as much as we need. -Z

    
    #Zack and Christian:
    choice = input("> ")
    if choice == "1":
      country_name_temps = "China, P.R.: Mainland"
      country_name_co2 = "CHINA (MAINLAND)"
    elif choice == "2":
      country_name_temps = "United Kingdom"
      country_name_co2 = "UNITED KINGDOM"
    elif choice == "3":
      country_name_temps = "India"
      country_name_co2 = "INDIA"
    elif choice == "4":
      country_name_temps = "Nigeria"
      country_name_co2 = "NIGERIA"
    elif choice == "5":
      country_name_temps = "Iraq"
      country_name_co2 = "IRAQ"
    elif choice == "6":
      country_name_temps = "Cuba"
      country_name_co2 = "CUBA"
    elif choice == "7":
      country_name_temps = "United States"
      country_name_co2 = "UNITED STATES OF AMERICA"
    elif choice == "8":
      country_name_temps = "Australia"
      country_name_co2 = "AUSTRALIA"
    else:
      print("ERROR: Invalid choice selected.")
      should_loop = True

  print(f"Getting data for {country_name_co2}. See Output tab for graphs, this may take a moment.")
  print(f"When ready to view another country, close the graph shown.")
  
  countries_dataset_temps = pd.read_csv("datasets/Global_Warming_Trends_1961_2022/long_format_annual_surface_temp.csv")

  #Sophie, Zack, Christian:
  country_data_temps = countries_dataset_temps[countries_dataset_temps['Country'] == country_name_temps]
  country_temps = country_data_temps["Temperature"]
  country_year = country_data_temps["Year"]
  years_list = country_year.values.tolist()
  temps_list = country_temps.values.tolist()

  #Zack, Christian, Jackson:
  for i, year in enumerate(years_list):
    years_list[i] = int(year.replace("F", ""))
  
  filtered_years_list = [year for year in years_list if year <= 2014] # for use in 2nd graph later -Z
  
  #print(years_list)
  
  # #print average temperature change
  #print("Average Yearly Temperature Change: ", computeAvgTempChange(temps_list))
  
  emission_data = pd.read_csv("datasets/CO2 Emissions from Fossil Fuels/fossil-fuel-co2-emissions-by-nation.csv")
  country_emission = emission_data[emission_data['Country'] == country_name_co2]
  #print(china_emission)
  
  emission_year = country_emission[(country_emission["Year"] >= 1961) & (country_emission["Year"] <= 2014)]
  #print(emission_year)
  emissions_solid= emission_year["Solid Fuel"]
  emissions_liquid= emission_year["Liquid Fuel"]
  emissions_gas= emission_year["Gas Fuel"]
  emissions_total = emission_year["Total"]
  total_emissions_list = emissions_total.values.tolist()

  #Sophie and Braeden:
  #get average emissions
  yearlyChange = 0 
  sumEmissionsChange = 0
  avgEmissionsChangeUnrounded = 0
  co2_change_yearly = []
  
  for i in range(len(total_emissions_list)-1):
    yearlyChange = total_emissions_list[i+1] - total_emissions_list[i]
    co2_change_yearly.append(yearlyChange)
    sumEmissionsChange += yearlyChange
  
  avgEmissionsChangeUnrounded = sumEmissionsChange/len(total_emissions_list)
  avgEmissionsChange = round(avgEmissionsChangeUnrounded, 3)
  print("Average Yearly Change in Total CO2 Emissions: ", avgEmissionsChange)
  
  
  #Stack plot
  #plt.figure(figsize=(10, 6))
  #plt.stackplot(filtered_years_list, emissions_solid, emissions_liquid, emissions_gas, labels=['Solid Fuel', 'Liquid Fuel', 'Gas Fuel'],)
  #plt.title("CO2 Emissions from Fossil Fuels (1961-2014) - China", fontsize=20)
  #plt.xlabel("Year", fontsize=15)
  #plt.ylabel("CO2 Emissions", fontsize=15)
  #plt.legend(loc='upper left')
  #plt.show()
  
  #Christian and Jackson:
  fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10, 12))
  
  ax1.plot(years_list, country_temps, color='blue', linewidth=3)
  ax1.set_title(f"Surface Temperature Change in {country_name_temps} (1961-2022)")
  ax1.set_ylabel("Temperature (C)")
  
  ax2.stackplot(filtered_years_list, emissions_solid, emissions_liquid, emissions_gas, labels=['Solid Fuel', 'Liquid Fuel', 'Gas Fuel'], baseline='zero')
  ax2.set_title(f"CO2 Emissions from Fossil Fuels (1961-2014) - {country_name_co2}")
  ax2.set_xlabel("Year")
  ax2.set_ylabel("CO2 Emissions (Metric Tons(Mg))")
  ax2.legend(loc='upper left')
  
  ax3.stackplot(filtered_years_list[1:], co2_change_yearly, labels=['Change in Average CO2 Emissions'], color='green', baseline='zero')
  ax3.set_title(f"Change in Average CO2 Emissions from Fossil Fuels (1962-2014) - {country_name_co2}")
  ax3.set_xlabel("Year")
  ax3.set_ylabel("CO2 Emissions (Metric Tons(Mg))")
  ax3.legend(loc='upper left')
  
  plt.show()