class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_a = 0
        count_b = 0
        store_a = {}
        store_b = []
        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                count_a += 1
            else:
                store_b.append(guess[i])
                if secret[i] not in store_a:
                    store_a[secret[i]] = 1
                else:
                    store_a[secret[i]] += 1
​
        for j in store_b:
            if j in store_a and store_a[j] > 0:
                count_b += 1
                store_a[j] -= 1
​
        return str(count_a) + "A" + str(count_b) + "B"
