
## Objective

I'll be working with a dataset on the job outcomes of students who graduated from college between 2010 and 2012. Using visualizations, we can start to explore questions from the dataset like:

* Do students in more popular majors make more money?
* Using scatter plots
* How many majors are predominantly male? Predominantly female?
* Using histograms
* Which category of majors have the most students?
* Using bar plots
* We'll explore how to do these and more while primarily working in pandas. Before we start creating data visualizations, let's import the libraries we need and remove rows containing null values.

### Sources

The original data on job outcomes was released by [American Community Survey](https://github.com/fivethirtyeight/data/tree/master/college-majors), which conducts surveys and aggregates the data. [FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/college-majors) cleaned the dataset and released it on their Github repo.  

 
### Dataset 
Each row in the dataset represents a different major in college and contains information on gender diversity, employment rates, median salaries, and more. Here are some of the columns in the dataset:   

`Rank` - Rank by median earnings (the dataset is ordered by this column).   
`Major_code` - Major code.   
`Major` - Major description.   
`Major_category` - Category of major.   
`Total` - Total number of people with major.   
`Sample_size` - Sample size (unweighted) of full-time.   
`Men` - Male graduates.   
`Women` - Female graduates.   
`ShareWomen` - Women as share of total.   
`Employed` - Number employed.   
`Median` - Median salary of full-time, year-round workers.   
`Low_wage_jobs` - Number in low-wage service jobs.   
`Full_time` - Number employed 35 hours or more.   
`Part_time` - Number employed less than 35 hours.   




# Going further

* Use a grouped bar plot to compare the number of men with the number of women in each category of majors.
* Use a box plot to explore the distributions of median salaries and unemployment rate.
* Use a hexagonal bin plot to visualize the columns that had dense scatter plots from earlier in the project.
