# Recruitment Analytics

Basically, the idea is to make sure that our PV assessment system is fair and accurate at delivering the best candidates to the bootcamp stage.

Our primary way of doing so is by assessing our assessors itself, as we currently lack the ability to sufficiently assess candidates' answers using machine learning or other tools.

## Assessing Assessors' Leniency

We want to assess applicant's strength through testing our assessors' leniency. By knowing if an assessor is lenient or not, we can derive accurate gradings for each candidate. 

Through our key assumption, we constructed a linear regression model of each question's scores for each assessor, against the word count for the applicant assessed, under this equation:

The current equation works as follows:

𝑠𝑐𝑜𝑟𝑒 = 𝛽0 + 𝛽𝑗 𝑤𝑜𝑟𝑑𝑐𝑜𝑢𝑛𝑡𝑗 + ε

Currently the understanding for the linear regression is that:

𝑠𝑐𝑜𝑟𝑒^ = 𝛽̂0 + 𝛽̂𝑗 𝑙𝑜𝑔(𝑤𝑜𝑟𝑑𝑐𝑜𝑢𝑛𝑡𝑗)

Of course, there is the case whereby we fail to account for a variable (omitted variable bias) of experience, as well as language ability.

A proxy for experience would be question one itself, asking about experience, for the next questions. As established earlier, to combat this omitted variable bias, we should use average score itself as a proxy variable.

𝑠𝑐𝑜𝑟𝑒^ = 𝛽̂0 + 𝛽̂𝑗 𝑙𝑜𝑔(𝑤𝑜𝑟𝑑𝑐𝑜𝑢𝑛𝑡𝑗) + 𝛽̂𝑘 𝑝𝑟𝑜𝑥𝑦𝑘

## Making Sense of Data

After running a linear regression of each question, we find the standard deviation of each assessor's score from the predicted score which would be given for the word count, and we add a weight based on the average score of the word count.

Why do we add a weight based on the average score? This is so that we penalise less harshly good answers that were rated by both assessors highly, but had a relatively smaller word count. Maybe some people are better at explaining their thoughts concisely. We shouldn't penalise people for writing more concisely, and hence we multiply a weight based on average scores to discount word counts from weighing too heavily.

After we have obtained the standard deviation of each assessor on each question, we put them into a table, and find the mean standard deviation of the assessor on the entire application.

We find some interesting results which for privacy reasons will not be shared here.

## Recommendations

1. In the next round of assessments, we should assign the most lenient assessor to the least lenient assessor, and continue this sequence, like a gauss summation.

   Gauss Summation: For a row of 1 to 100, the sum of this row is adding 1 + 100, 2 + 99, 3 + 98, etc

   Likewise, we can match the most lenient with the least lenient, and follow on as such.

   I have already done a sample matchup.

2. You can take note of the lenient scores when assigning assessors to zoom rooms for the interviews, to make sure a room is not too strict with the judging process.

3. For future assessments in later years, we can let assessors grade a bunch of past year applications, and determine their leniency as compared to previous years' assessments, plus the existing linear model, and match assessors up accordingly to ensure a balance between lenient and strict assessor for each applicant.