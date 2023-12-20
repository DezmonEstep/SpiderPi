import Hexapod
import time

def main():
   # Initialize the hexapod
   Hexapod.load()

   # Move each leg forward
   for leg in range(6):
       Hexapod.forward_step(leg)

   # Wait for a while
   time.sleep(2)

   # Move each leg backward
   for leg in range(6):
       Hexapod.backward_step(leg)

   # Unload the hexapod
   Hexapod.unload()

if __name__ == "__main__":
   main()
