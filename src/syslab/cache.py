import time
from collections import OrderedDict,deque
class TTLCache:
    def __init__(self,capacity=128,ttl=60,clock=time.monotonic):
        if capacity<1 or ttl<=0: raise ValueError('positive cache limits required')
        self.capacity,self.ttl,self.clock=capacity,ttl,clock;self.items=OrderedDict()
    def get(self,key):
        value=self.items.get(key)
        if value is None:return None
        deadline,data=value
        if deadline<=self.clock():del self.items[key];return None
        self.items.move_to_end(key);return data
    def put(self,key,value):
        self.items[key]=(self.clock()+self.ttl,value);self.items.move_to_end(key)
        while len(self.items)>self.capacity:self.items.popitem(last=False)
class SlidingQuota:
    def __init__(self,limit=100,window=60,clock=time.monotonic):
        if limit<1 or window<=0:raise ValueError('positive quota limits required')
        self.limit,self.window,self.clock=limit,window,clock;self.requests={}
    def allow(self,tenant):
        now=self.clock();q=self.requests.setdefault(tenant,deque())
        while q and q[0]<=now-self.window:q.popleft()
        if len(q)>=self.limit:return False
        q.append(now);return True
