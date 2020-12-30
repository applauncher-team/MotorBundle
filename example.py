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