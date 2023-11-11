import re
PATTERNS=[re.compile(p,re.I) for p in (r'ignore\s+(all\s+)?previous\s+instructions',r'reveal\s+(the\s+)?system\s+prompt',r'jailbreak')]
def blocked(prompt):
    if not isinstance(prompt,str) or len(prompt)>32768: raise ValueError('prompt must be text <=32768 characters')
    return any(p.search(prompt) for p in PATTERNS)
def approximate_tokens(prompt): return max(1,(len(prompt)+3)//4)
