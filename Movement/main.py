from Movement.Hexapod import Hexapod
import time

# Create a new Hexapod object
hexapod = Hexapod()

# Move the hexapod forward
hexapod.walk('forward')

# Wait for a while
time.sleep(5)

# Move the hexapod backward
hexapod.walk('backward')

