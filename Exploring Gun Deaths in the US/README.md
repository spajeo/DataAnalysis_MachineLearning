
### Sources

The dataset came from [**FiveThirtyEight**](http://fivethirtyeight.com/), and can be found [here](https://github.com/fivethirtyeight/guns-data). The dataset is stored in the guns.csv file. 

### Dataset

It contains information on gun deaths in the US from 2012 to 2014. Each row in the dataset represents a single fatality. The columns contain demographic and other information about the victim. Here are the first few rows of the dataset:

|   | year  |  month  | intent | police|  sex | age  | race |   hispanic |   place  | education |
|:- | :---- | :------ | -----: | :-----| :--- | ---: | :--- | ---------: |--------: |--------: |
| 1 |  2012 |   1  | Suicide  | 0   |  M   |  34.0    |  Asian/Pacific  Islander  |  100  | Home    |  4.0 | 
| 2 |  2012 |   1  |   Suicide  | 0  |   F  |   21.0   |   White   |  100  | Street  |  3.0 | 
| 3 | 2012  |  1   |  Suicide  | 0   |  M   |  60.0   |   White   |  100  | Other specified  |  4.0 | 
| 4 | 2012  |  2   |  Suicide |  0   |  M   |  64.0   |   White   |  100  | Home   |   4.0 | 
| 5 | 2012  |  2   |  Suicide  | 0  |   M   |  31.0   |   White  |   100  | Other specified  |  2.0 | 


As you can see above, the first row of the data is a header row, which tells you what kind of data is in each column of the CSV file. Each row contains information about the fatality, and the victim. Here's an explanation of each column:

` `-- this is an identifier column, which contains the row number. It's common in CSV files to include a unique identifier for each row, but we can ignore it in this analysis.
`year` -- the year in which the fatality occurred.
`month` -- the month in which the fatality occurred.
`intent` -- the intent of the perpetrator of the crime. This can be Suicide, Accidental, NA, Homicide, or Undetermined.
`police` -- whether a police officer was involved with the shooting. Either 0 (false) or 1 (true).
`sex` -- the gender of the victim. Either M or F.
`age` -- the age of the victim.
`race` -- the race of the victim. Either Asian/Pacific Islander, Native American/Native Alaskan, Black, Hispanic, or White.
`hispanic` -- a code indicating the Hispanic origin of the victim.
`place` -- where the shooting occurred. Has several categories, which you're encouraged to explore on your own.
`education` -- educational status of the victim. Can be one of the following:
1 -- Less than High School
2 -- Graduated from High School or equivalent
3 -- Some College
4 -- At least graduated from College
5 -- Not available
In this project, we'll explore the dataset, and try to find patterns in the demographics of the victims. Our first step is to read the data in and take a look at it.

### Further

Determing wheter there's a correlation between class size and SAT scores
Figuring out which neighborhoods have the best schools
If we combine this information with a dataset containing property values, we could find the least expensive neighborhoods that have good schools.
Investigating the differences between parent, teacher, and student responses to surveys.
Assigning scores to schools based on sat_score and other attributes.
