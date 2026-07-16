class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0  # modèle 010101...
        count2 = 0  # modèle 101010...

        for i in range(len(s)):
            if i % 2 == 0:
                expected1 = "0"
                expected2 = "1"
            else:
                expected1 = "1"
                expected2 = "0"

            if s[i] != expected1:
                count1 += 1

            if s[i] != expected2:
                count2 += 1

        return min(count1, count2)