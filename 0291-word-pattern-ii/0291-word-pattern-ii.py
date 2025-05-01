class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def track_word(p_index,s_index):
            if p_index==len(pattern) and s_index==len(s):
                return True
            if p_index==len(pattern) or s_index==len(s):
                return False

            char=pattern[p_index]
            if char in char_dict:
                word=char_dict[char]
                if s.startswith(word,s_index):
                    return track_word(p_index+1,s_index+len(word))
                else:
                    return False
            for end in range(s_index+1,len(s)+1):
                character=s[s_index:end]
                if character in used_words:
                    continue
                char_dict[char]=character
                used_words.add(character)


                if track_word(p_index+1,end):
                    return True
                
                del char_dict[char]
                used_words.remove(character)
            return False 

        char_dict={}
        used_words = set()
        return track_word(0,0)