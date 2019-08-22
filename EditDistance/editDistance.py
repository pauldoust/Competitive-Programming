# https://leetcode.com/problems/edit-distance/submissions/
# Runtime: 192 ms, faster than 47.88% of Python3 online submissions for Edit Distance.
class Solution:
    infInt = 2**32-1

    def minDistance(self, word1: str, word2: str) -> int:

        # distanceArray = [[0]* (len(word2)+1)] * (len(word1)+1)
        distanceArray = [0]* (len(word1)+1)
        for ind in range(len(word1)+1):
            distanceArray[ind] = [0] * (len(word2)+1)

        for zeroRows in range (0, len(word1)+1):
            distanceArray[zeroRows][0] = zeroRows

        for zeroCols in range (0, len(word2)+1):
            distanceArray[0][zeroCols] = zeroCols



        for i in range (0, len(word1)):
            for j in range(0, len(word2)):
                print("first: ", word1[:i+1])
                print("second: ", word2[:j+1])

                replaceCost = 0 if word1[i] == word2[j] else  1
                replaceCost += distanceArray[i] [j]
                addCost = distanceArray[i+1][j]
                # addCost = distanceArray[i+1][j] if i <= j else self.infInt
                removeCost = distanceArray[i][j+1]
                # removeCost = distanceArray[i][j+1]  if i > j else self.infInt 
                # removeCost = distanceArray[i][j+1]  if i > j else self.infInt 
                print("replaceCost: ", replaceCost)
                print("addCost: ", addCost +1)
                print("removeCost: ", removeCost + 1)
                distanceArray[i+1][j+1] = min(replaceCost, addCost + 1, removeCost + 1)


        print(distanceArray)
        return distanceArray[len(word1)][len(word2)]


# b
# a b

# a
# a b
word1 = "horse"
word2 = "ros"

word1 = "intention"
word2 = "execution"


# word1 = "biting"
# word2 = "sitting"

# word1 = "bt"
# word2 = "btt"
# word1 = "b"
# word2 = "bt"

# word1 = "sea"
# word2 = "eat"



# word1 = "plasma"
# word2 = "altruism"

word1 = "teacher"
word2 = "acheer"


print (Solution().minDistance(word1, word2))