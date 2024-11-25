class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = [word.lower() for word in re.sub(r'[^\w\s]',' ',paragraph).split()]
        print(word_list)

        dist=defaultdict(int)
        m_count=0
        m_word=''
        for word in word_list:
            if word not in banned:
                
                dist[word]+=1
                if dist[word]>m_count:
                    m_count=dist[word]
                    m_word=word
        return m_word