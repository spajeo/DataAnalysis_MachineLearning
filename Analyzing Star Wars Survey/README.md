While waiting for [Star Wars: The Force Awakens](https://en.wikipedia.org/wiki/Star_Wars:_The_Force_Awakens) to come out, the team at [FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey) became interested in answering some questions about Star Wars fans. 
In particular, they wondered: **does the rest of America realize that “The Empire Strikes Back” is clearly the best of the bunch?**

The team needed to collect data addressing this question. To do this, they surveyed Star Wars fans using the online tool SurveyMonkey. They received 835 total responses, which you download from their [GitHub repository](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey).

## Features

The data has several columns, including:

`RespondentID` - An anonymized ID for the respondent (person taking the survey)    
`Gender` - The respondent's gender   
`Age` - The respondent's age   
`Household Income` - The respondent's income     
`Education` - The respondent's education level    
`Location (Census Region)` - The respondent's location    
`Have you seen any of the 6 films in the Star Wars franchise?` - Has a Yes or No response    
`Do you consider yourself to be a fan of the Star Wars film franchise?` - Has a Yes or No response    
`Have you seen any of the 6 films in the Star Wars franchise?`    
`Do you consider yourself to be a fan of the Star Wars film franchise?`    

* The next six columns represent a single checkbox question. The respondent checked off a series of boxes in response to the question, `Which of the following Star Wars films have you seen? Please select all that apply`. 

The columns for this question are:

  * `Which of the following Star Wars films have you seen? Please select all that apply. - Whether or not the respondent saw Star Wars:  Episode I The Phantom Menace.`    
  *   `Unnamed: 4` - Whether or not the respondent saw Star Wars: Episode II Attack of the Clones.    
  * `Unnamed: 5` - Whether or not the respondent saw Star Wars: Episode III Revenge of the Sith.    
  * `Unnamed: 6` - Whether or not the respondent saw Star Wars: Episode IV A New Hope.    
  * `Unnamed: 7` - Whether or not the respondent saw Star Wars: Episode V The Empire Strikes Back.     
  * `Unnamed: 8` - Whether or not the respondent saw Star Wars: Episode VI Return of the Jedi.    

* The next six columns represent a single checkbox question. The respondent checked off a series of boxes in response to the question, `Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film`. 

The columns for this question are:

  *  `Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film. - How much the respondent    
             liked Star Wars: Episode I The Phantom Menace`    
  * `Unnamed: 10` - How much the respondent liked Star Wars: Episode II Attack of the Clones    
  * `Unnamed: 11` - How much the respondent liked Star Wars: Episode III Revenge of the Sith   
  * `Unnamed: 12` - How much the respondent liked Star Wars: Episode IV A New Hope   
  * `Unnamed: 13` - How much the respondent liked Star Wars: Episode V The Empire Strikes Back    
  * `Unnamed: 14` - How much the respondent liked Star Wars: Episode VI Return of the Jedi  

`Do you consider yourself to be a fan of the Star Wars film franchise?` - True or False  
`Do you consider yourself to be a fan of the Star Trek franchise?` - Yes or No   
`Gender` - Male or Female    




## Here are some potential next steps:

* Try to segment the data based on columns like Education, Location (Census Region), and Which character shot first?, which aren't binary. Are they any interesting patterns?
* Clean up columns 15 to 29, which contain data on the characters respondents view favorably and unfavorably.
* Which character do respondents like the most?
* Which character do respondents dislike the most?
* Which character is the most controversial (split between likes and dislikes)?
