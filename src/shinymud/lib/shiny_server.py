from shinymud.lib.connection_handler import ConnectionHandler
from shinymud.lib.world import World
from shinymud.models.area import Area
from shinymud.models.schema import initialize_database
from shinymud.data.config import *

import logging
initialize_database()
format = "%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d %(message)s"
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=format)
logger = logging.getLogger('shiny_server')
world = World()

# load the entities in the world from the database
for area in world.db.select("* from area"):
    world.new_area(Area(**area))
for area in world.areas.values():
    area.load()

try:
    dloc = world.get_area(DEFAULT_LOCATION[0]).get_room(DEFAULT_LOCATION[1])
except Exception, e:
    dloc = None
    logger.debug(str(e))
finally:
    world.default_location = dloc

# Start listening for connections on a different thread
conn_handler = ConnectionHandler(PORT, HOST, world)
conn_handler.start()
logger.debug('Started the connection handler. Now listening.')

# Let there be light!
logger.info('The world is about to start turning')
world.start_turning()
logger.info('The world has stopped turning.')
conn_handler.join()