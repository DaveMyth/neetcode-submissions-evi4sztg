class Solution:

    def encode(self, strs: List[str]) -> str:
        return '['+"|".join(strs)+']' if len(strs)>0 else '[*]'

    def decode(self, s: str) -> List[str]:
        return s[1:-1].split('|') if s != '[*]' else []