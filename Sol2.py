# Input number of participants (not necessary for the logic)
n = int(input())

# Input the scores and store them as a list of integers
scores = list(map(int, input().split()))

# Convert the list to a set to remove duplicates and then sort it
unique_scores = list(set(scores))

# Sort the unique scores in descending order
unique_scores.sort(reverse=True)

# The runner-up score will be the second highest in the sorted list
runner_up_score = unique_scores[1]

# Print the runner-up score
print(runner_up_score)
