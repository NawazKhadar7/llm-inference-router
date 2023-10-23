import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
import asyncio
from syslab.core import Router
from syslab.providers import Provider
class RouterTests(unittest.TestCase):
    def test_single_flight_cache(self):
        async def work():
            r=Router();return await asyncio.gather(*(r.route('t','hello') for _ in range(5)))
        results=asyncio.run(work());self.assertEqual(sum(x['status']=='ok' for x in results),1)
    def test_all_unavailable(self):
        r=Router([Provider('broken',100,1,True)])
        self.assertEqual(asyncio.run(r.route('t','hello'))['status'],'unavailable')
