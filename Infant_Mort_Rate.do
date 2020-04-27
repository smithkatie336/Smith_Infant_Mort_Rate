clear
use "C:\Users\smith\Documents\Syracuse University\SU Courses\Spring 2020\PAI 789\Smith_Infant_Mort_Rate\worldbank_data.dta"
reg Inf_MR __Mort_C GDP_PC Adol_FR, robust
log close
