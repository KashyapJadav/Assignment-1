"""Problem statement: File Monitoring system
The goal of this task is to design and develop a file monitoring system.
Generate a random writer that writes pseudo strings
(with at least 50% probability of generating the “MARUTI” keyword. Note that we are strictly looking at the "MARUTI" keyword only as a
single value not the MARUTI keyword inside a random string)
into two separate files at regular interval of time.
It should have the capability to monitor both the files and count the total number of occurrences
for the “MARUTI” keyword by each file and write output to the "counts.log" file.
"""

import random
import asyncio
import aiofiles
import logging
import string

logging.basicConfig(filename="newfile.log", format='%(asctime)s - %(message)s',
                    filemode='a', level=logging.DEBUG)
logger = logging.getLogger(__name__)


#Made class for FileMonitoringSystem
class FileMonitoringSystem:
    def __init__(self,filename):
        self.filename = filename

    #Random String Generator function
    async def string_generator(self):
        k = random.randint(10,20)
        ran_str = ''.join(random.choices(string.ascii_letters, k=k))
        lst = [ran_str,"MARUTI"]
        return random.choice(lst)

    #Generated string write into a files
    async def file_writer(self):
        while True:
            try:
                s = await self.string_generator()
                async with aiofiles.open(self.filename,'a') as file:
                    await file.write(s)
            except KeyboardInterrupt as e:
                logger.error(f"Error in file {self.filename}:{e}")
                break

#Word count function from files
async def word_counter(files):
    while True:
        for file in files:
            try:
                async with aiofiles.open(file,'r') as f:
                    c = await f.read()
                    count = c.count("MARUTI")
                    logger.info(f"Total count in file {file}:{count}")
            except Exception as e:
                logger.error(f"Error in file {file}:{e}")

#Call a main Drivercode function
async def DriverCode():
    d = FileMonitoringSystem("file1.txt")
    d1 = FileMonitoringSystem("file2.txt")
    await asyncio.gather(d.file_writer(),d1.file_writer(),word_counter(['file1.txt','file2.txt']))

try:
    asyncio.run(DriverCode())
except Exception as e:
    logger.error(f"Error in Drivercode {e}")