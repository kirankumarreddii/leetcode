class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        for i in range(len(guess)):
            if secret[i]==guess[i]:
                bull+=1
        secret_count=Counter(secret)
        cow=0
        for c in guess:
            if c in secret_count:
                if secret_count[c]<=0:
                    continue
                else:
                    secret_count[c]-=1
                    cow+=1
        cow-=bull
        return str(bull)+'A'+str(cow)+'B'