# What is Statistics?
methodological subject encompassing all aspects of learning from data

* Statistics as the art of summarizing data
* Statistics as the science of uncertainty
* as the science of decisions
* as the science of variation
* as the art of forecasting
* as the Science of measurement
* as the basis for principled data collection

# Allied Fields
* CS
* Mathematics
* Probability theory
* Data Science

# Perspectives on Statistics in Real Life
* take advantage of the datasets, practice makes perfect
* never afraid of making mistakes, many free resources available

# This is Statistics website http://thisisstatistics.org/

# Cool stuff in Data
* Data can be Numbers
* Data can be Images -> Quick Draw with Google
* Data can be Words
* Data can be Audio

# Let's Play with Data
* https://flowingdata.com/2015/12/15/a-day-in-the-life-of-americans/

# Where do Data Come From?
* Different Types of Data
	* Organic -> Netfilx, Point-of-Sales, Browsing Data
		- Big Data
		- Procesing required
	* Designed -> Individual sampled from a population, typically smaller 
* Are the Data i.i.d? (Independent and Id = Identically Distributed
	- no correlation of other observation
	- Final Exam Scores
	* not i.i.d :
		- students sitting next to each other
		- Makes and females might have different means
		- students from same discussion session may have similar scores
		* Need different analytic procedures
* CAN WE ASSUME I.I.D DATA? WHERE DO THE DATA COME FROM?

# Variable Types
* Quantitative
	* Continuous 
	* Discreet
* Qualitative
	* Ordinal -> ranking
	* Nominal

# Study Design
* Types :
	* Exploratory vs Confirmatory
		- Confirmatory : specify falsifiable hypothesis -> test
		- Exploratory : collect and analyze data withour first pre-specifying question
	* Comparative vs Non-Comparative
		- Comparative : 
		- Non-Comparative : estimating or predicting
	* Observational vs Experiments
		- Observational : naturally
		- Experiments : Manipulation or assignment
* Power -> asses wether study design likely yield findings
* Bias -> Measurements systematically off target (Observational vulnerable)

# Data Management and manipulation
* Typical Rectangular Data Set -> Column as Variable, Row as Data
* Best Practices for Data Management
	- Never modify the source data files
	- Write a script
	- Name variables with brief interpretable names
	- Variable names consisting only letters, numbers, and underscore char (no whitespaces)
	- Most statistical software will treat blank, "NA", or "." as missing value
	- Text/CSV is a better choice than spreadsheet formats
	- Database software and tools can be very useful for large-scale data management
	- HDF5, Apache Parquet and Apache Arrow -> open source standards dor large binary datasets
	- Hadoop, Sparks -> large datasets manipulation
	- Large datasets can be compressed (gzip)
* Repeated Measures Data : Wide and Long
	- Wide format : one row / subject -> good for data entry where each subjects is assesed the same number of times
	- Long format : one row / measurement -> more flexible, more natural
* Other data formats -> graphs, images, geospatial data, text data
