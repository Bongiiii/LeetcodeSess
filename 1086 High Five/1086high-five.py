class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scoreDict = {}

        for key, value in items:
            if key not in scoreDict:
                scoreDict[key] = [value]
            else:
                scoreDict[key].append(value)

        output = []
       # Process each student's scores
        for id, score in scoreDict.items():
            score.sort(reverse=True)  # Sort scores in descending order
            avg = sum(score[:5]) // 5  # Take the average of the top 5 scores
            output.append([id, avg])

        # Sort the output based on student ID
        output.sort(key=lambda x: x[0])

        return output