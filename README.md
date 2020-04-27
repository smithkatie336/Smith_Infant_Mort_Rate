# Smith_Infant_Mort_Rate

**Summary**

Infant mortality, or the death of an infant before one year of age, provides both information about infant and maternal health as well as overall societal health ("Infant Mortality" 2019). To analyze factors that may be associated with infant mortality in South America in 2016, data for infant mortality rate, adolescent fertility rate, percent mortality by communicable disease, and GDP per capita were obtained from worldbank.org via API calls. An analysis revealed that while all three variables were correlated with infant mortality, only GDP per capita was significantly associated.

**Deliverables**

The script **collect_worldbank_data.py** will produce the csv file **worldbank_data.csv**, which will contain data obtained from www.worldbank.org. This csv will be used, along with a shapefile of South America obtained from **geo.nyu.edu** to visualize a QGIS choropleth map of infant mortality rates in the different countries. This csv will also be read into **analyze_worldbank_data.py** to produce four figures: **Infant_GDP_corr.png**, **Infant_Comm_corr.png**, **Infant_Adol-FR_corr.png**, and **Correlation_matrix**. This script will also produce the **worldbank_data.dta** file to be run in STATA using the **Infant_Mort_Rate** Do-file provided.

Instructions

**A. Collecting the data for analysis -> Run collect_worldbank_data.py script**

To construct **collect_worldbank_data.py**, the following steps were taken:

1. Import requests, pandas, and json

2. Create a list called 'SA_countries' for countries in South America using the country codes provided by worldbank.org (see "Country Codes" reference).

3. Create an empty dictionary called 'inf_mort'

4. Create a loop for 'count' in 'SA_countries' that uses reponse = requests.get() and an API call to retrieve data for infant mortality rate (indicator: SP.DYN.IMRT.IN) for 2016 from worldbank.org. The API call should appear as:

api = 'https://api.worldbank.org/v2/country/'+count+'/indicator/SP.DYN.IMRT.IN?date=2016&format=JSON'

with 'count' included to retrieve data from each country in the list 'SA_countries' during the loop.

5. Still within the loop, set json.loads(response.text) equal to 'mort'.

6. Further define 'mort' as the first element within the second element retrieved from the API call (mort = mort[1][0]).

7. From the acquired data, retrieve 'mort['country']['value']' and 'mort['value']' and name this list i_mort.

8. Add this data to the empty 'inf_mort' dictionary defined above via the code 'inf_mort.update({count: i_mort})'. (see "python loop to pull API data for iterating URLs" in references). Close the loop.

9. Outside of the loop, define 'colnames' as 'Country' and 'Inf_MR' and 'datarows' as 'inf_mort.values'.

10. Use 'colnames' and 'datarows' to create a DataFrame called 'i_m_rate'.

11. Use similar steps to retrieve data for GDP per capita (indicator NY.GDP.PCAP.PP.CD), adolescent fertility rate (indicator SP.ADO.TFRT), and percent death by communicable diseases (indicator SH.DTH.COMM.ZS) and create DataFrames for each variable.

12. Use a couple steps using pd.merge to merge the four DataFrames into one DataFrame called 'worldbank_data', merging on 'Country'.

13. Use .str.upper() to capitalize the country names in 'worldbank_data['Country']'.

14. Set the index of 'worldbank_data' to 'Country'.

15. Save DataFrame as a csv named 'worldbank_data.csv'.

**B. Visualize infant mortality rates via QGIS**
1. Retrieve the shapefile for South America from https://geo.nyu.edu/catalog/stanford-vc965bq8111 by downloading 'Original Shapefile' and save in the file for this project (will be downloaded as 'data.zip').

2. In QGIS, add layer 'data.zip' to add South America countries to the map. Export as Geopackage 'South America' with layer called 'country boundaries'. Remove previous layer.

3. Add 'worldbank_data.csv' file to map and join file to 'South America country boundaries' on 'Country' from 'worldbank_data.csv' and 'Name' for 'South America country boundaries' layer.

4. For the 'South American country boundaries' layer, set the layer as 'Graduated' for the 'worldbank_data_inf_MR' variable (Infant Mortality) with pretty breaks and 6 classes with the 'Greys' color ramp.

5. Save file as 'Infant_Mortality_SA.qgz'.

**C. Analyze infant mortality rates via correlation -> Run analyze_worldbank_data.py**

To construct **analyze_worldbank_data.py**, the following steps were taken:

1. Import pandas, seaborn, and matplotlib.pyplot.

2. Read in 'worldbank_data.csv' with its index set as 'Country' as a DataFrame called 'world_bank'.

3. Create a scatterplot of the relationship between infant mortality and GDP per capita by setting 'world_bank['GDP_PC']'' as the independent variable and 'world_bank['Inf_MR']' as the dependent variable using plt.scatter(x,y). Set the plot title as 'Infant Mortality vs GDP Per Capita' with a font size of 12. Name the x axis 'GDP Per Capita' and the y axis as 'Infant Mortality Rate', each with a font size of 8.

4. Save the figure as 'Infant_GDP_corr.png'.

5. Repeat these steps to create scatterplots of the relationship between infant mortality and adolescent fertility rates (save as 'Infant_Adol-FR_corr.png') and percent mortality from communicable diseases (save as 'Infant_Comm_corr.png').

6. Calculate the correlation between infant mortality and GDP per capita and round to 5 decimal places. Name this correlation 'corr'.

7. Print a statement with descriptive information as well as the correlation calculated in the previous step.

8. Repeat steps 6 and 7 for correlations between infant mortality and adolescent fertility rates and percent morality from communicable diseases.

9. To determine if there is a correlation among the variables besides those of interest, create a correlation matrix heatmap called sns_plot with the code sns.heatmap(world_bank.corr(), annot = True, cmap = 'coolwarm', square = True, annot_kws={'size':24}) and a font scale of 1.8 and figure size of (20,15).

10. Save the heatmap as 'Correlation_matrix.png'.

11. For further analysis in STATA, save the DataFrame as a .dta file called 'worldbank_data.dta'.

**D. Regress the variables to determine significance of association with infant mortality rate -> run 'Infant_Mort_Rate' Do-file**

To create the **Infant_Mort_Rate** Do-file, the following steps were taken:

1. Clear previous steps in STATA

2. Use 'worldbank_data.dta'

3. Run a robust linear regression to determine if adolescent fertility rate, GDP per capita, and percent mortality by communicable diseases are significantly associated with infant mortality rate.

4. Close log

5. Save Do-file as 'Infant_Mort_Rate.do'.

**References**
"Country Codes". wits.worldbank.org. Retrieved from https://wits.worldbank.org/wits/wits/witshelp/content/codes/country_codes.htm

"Detailed World Polygons (LSIB), South America, 2013". NYU Spatial Data Repository. Retrieved from https://geo.nyu.edu/catalog/stanford-vc965bq8111

"Infant Mortality" (2019). cdc.gov. Retrieved from https://www.cdc.gov/reproductivehealth/maternalinfanthealth/infantmortality.htm

"python loop to pull API data for iterating URLs" (Nov 30 2018). stackoverflow.com. Retrieved from https://stackoverflow.com/questions/53558837/python-loop-to-pull-api-data-for-iterating-urls
