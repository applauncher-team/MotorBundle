# Motor Bundle

Motor client provider for applauncher 

Installation
------------
```bash
pip install motor_bundle  
```
Then add to your main.py
```python
import motor_bundle

bundle_list = [
    motor_bundle.MotorBundle(),
]
```

Configuration
-------------
Currently just the connection uri, for example
```yml
motor:
  uri: 'mongodb://localhost/default'
```

Usage
-----
Just inject and use it as a regular motor client. Check `example.py` for more details
```python
from applauncher import Kernel, event
from motor_bundle import MotorBundle
from motor.motor_asyncio import AsyncIOMotorClient

class ExampleBundle:
    def __init__(self):
        self.event_listeners = [
            (event.KernelReadyEvent, self.cosa),
        ]

    async def do_insert(self, db):
        document = {'key': 'value'}
        result = await db.test_collection.insert_one(document)
        print('result %s' % repr(result.inserted_id))

    def cosa(self, event):
        from applauncher.applauncher import inject
        motor = inject(AsyncIOMotorClient)
        db = motor.get_default_database()
        import asyncio
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.do_insert(db))

with Kernel(bundles=[MotorBundle(), ExampleBundle()], environment="DEV") as kernel:
    kernel.wait()
```
More information in the [motor](https://motor.readthedocs.io) documentation
