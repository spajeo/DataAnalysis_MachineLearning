   
# Winning Jeopardy

Jeopardy is a popular TV show in the US where participants answer questions to win money. It's been running for a few decades, and is a major force in popular culture.

As you can see, each row in the dataset represents a single question on a single episode of Jeopardy.

Let's find out :

* How often the answer is deducible from the question.
* How often new questions are repeats of older questions.

### Dataset informations

[To dl the file.](https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/)

`Show Number` -- the Jeopardy episode number of the show this question was in.   
`Air Date` -- the date the episode aired.   
`Round` -- the round of Jeopardy that the question was asked in. Jeopardy has several rounds as each episode progresses.    
`Category` -- the category of the question.    
`Value` -- the number of dollars answering the question correctly is worth.    
`Question` -- the text of the question.    
`Answer` -- the text of the answer.    


In order to figure out whether to study past questions, study general knowledge, or not study it all, it would be helpful to figure out two things:

### potential next steps:

* Find a better way to eliminate non-informative words than just removing words that are less than 6 characters long.
* Manually create a list of words to remove, like the, than, etc.
* Find a list of stopwords to remove.
* Remove words that occur in more than a certain percentage (like 5%) of questions.
* Perform the chi-squared test across more terms to see what terms have larger differences. This is hard to do currently because the code is slow, but here are some ideas:
* Use the apply method to make the code that calculates frequencies more efficient.
* Only select terms that have high frequencies across the dataset, and ignore the others.
* Look more into the Category column and see if any interesting analysis can be done with it. Some ideas:
* See which categories appear the most often.
* Find the probability of each category appearing in each round.
* Use the whole Jeopardy dataset (available here) instead of the subset we used in this mission.
* Use phrases instead of single words when seeing if there's overlap between questions. Single words don't capture the whole context of the question well.
