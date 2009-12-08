from src.shinymud.models.world import *
from src.shinymud.models.user import *
from src.shinymud.commands import *
import unittest

class TestGeneralCommands(unittest.TestCase):
    
    def setUp(self):
        self.world = World()
        self.user = User(world=self.world)
    
# Now we just need to test some commands!

suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneralCommands)
unittest.TextTestRunner(verbosity=2).run(suite)