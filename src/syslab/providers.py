import asyncio
from dataclasses import dataclass
@dataclass(frozen=True)
class Provider:
    name:str
    context:int
    price:int
    fail:bool=False
    async def complete(self,prompt):
        await asyncio.sleep(0)
        if self.fail: raise ConnectionError('synthetic provider unavailable')
        return {'text':f'{self.name}: {prompt[:48]}','provider':self.name}
DEFAULTS=[Provider('economy',128,1),Provider('balanced',1024,3),Provider('large',8192,8)]
