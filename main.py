# DP = Array of length n + 1, initialized by infinite values
# PAR = Array of length n + 1
# DP[0] = 0              (Since we are already at point a0)
#
# For i = 1 to n:
# 	For j = 0 to i - 1:
# 		if DP[j] + abs(200 - (a[i] - a[j])) < DP[i]:
# 			DP[i] = DP[j] + abs(200 - (a[i] - a[j]))
# 			PAR[i] = j
#
# Minimum_Penalty = DP[n]
# Actual_Path = Empty List
#
# Current = n
# While Current != 0:
# 	Actual_Path.add_to_start(Current)
# 	Current = PAR[Current]


def findOptimalSequence():
    hotels = [0, 150, 175, 250, 520, 550, 620]
    n = len(hotels)
    dp = [-1] * n
    par = [-1] * n

    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if dp[i] == -1 or dp[i] > dp[j] + abs(200 - (hotels[i] - hotels[j])):
                dp[i] = dp[j] + abs(200 - (hotels[i] - hotels[j]))
                par[i] = j
    print('Cost of optimal path is {}'.format(dp[n - 1]))
    actual_path = []
    current = n - 1
    while current != -1:
        actual_path.append(current + 1)
        current = par[current]
    actual_path = list(reversed(actual_path))
    print('Actual path:', actual_path)


findOptimalSequence()
