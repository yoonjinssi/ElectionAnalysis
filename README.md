# ElectionAnalysis

## Project Overview
  An audit of a local congressional election for Colorado Election Board.
  In this project, we will find out which are the counties who have participated in the voting and which county has most voting turnout.
  We'll also find out who are the candidates, how many votes they won and who was the winner of the election.
  
### 1. Calculate the total number of cast votes.
###### To calculate the total number of cast votes, we first initialized a variable 'total_votes' and set it equal to zero.
###### And then we put ```total_votes = total_votes + 1``` inside the for loop to increase it by 1 whenever the csv file is read by the row.
###### ![Screen Shot 2021-05-17 at 2 17 45 PM](https://user-images.githubusercontent.com/81896860/118557869-a928fb00-b71a-11eb-8171-e4d40a293a65.png)

    
### 2. Name of candidates who received votes.
###### To retrieve the name of candidates who received votes, we used an idex 2 which is the last item from every row of csv file. When the name is something new,
###### we added this name to the the candidate_options which was initiated as an empty list in the beginning. 
###### ```if candidate_name not in candidate_options:```
######    ``` candidate_options.append(candidate_name)```


### 3. Calcuate the total number of votes each candidate received.
###### To count the votes each candidate received, candidate_name was increased by 1 everytime a row was read.
###### ```for row in reader:```
###### ```candidate_votes[candidate_name] += 1```

### 4. Calculate the % of votes each candidate received.
###### To calculate the % of votes each candidate received, each candidate's votes were divided by the total votes and multiplied by 100.
###### ```for candidate_name in candidate_votes:```
###### ```    votes = candidate_votes.get(candidate_name)```
###### ```    vote_percentage = float(votes) / float(total_votes) * 100```
###### ![Screen Shot 2021-05-17 at 5 17 28 PM](https://user-images.githubusercontent.com/81896860/118571814-c3bb9e00-b733-11eb-8153-b0853373f830.png)


###  5. Determine the winner of the election based on popular votes.
###### Winner of the election was Diana DeGette who won 73.8% of popular votes. She earned 306,055 out of 369,711 total votes, which I think is significant win.

## Election Audit Summary
###### Election Commision can use this script to figure future elections on what county or candidate has won the election.

## Resources
- Data Source: election_results.csv
- Software - Python 3.7


