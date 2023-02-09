import random
import asyncio
import logging
import string

logging.basicConfig(filename="newfile.log", format='%(asctime)s - %(message)s',
                    filemode='a', level=logging.DEBUG)
logger = logging.getLogger()


# Define Function using asyncio
async def main(str1):
    c1 = 0
    while True:
        for i in range(10):
            ran_ascii_letter = ''.join(random.choices(string.ascii_letters, k=4))
            res1 = random.choice([str1, ran_ascii_letter])
            res2 = random.choice([str1, ran_ascii_letter])
            print("Generated string:" + str(res1))
            print("Generated string:" + str(res2))

            if res1 == 'MARUTI':
                c1 += 1
            with open("file1.txt", "a") as file1:
                file1.write(res1 + " ")
            # await asyncio.sleep(1)
            if res2 == 'MARUTI':
                c1 += 1
            with open("file2.txt", "a") as file2:
                file2.write(res2 + " ")

            with open("file1.txt", "r") as newfile:
                temp1 = newfile.read()
                temp3 = temp1.count('MARUTI')
            with open("file2.txt", "r") as newfile1:
                temp2 = newfile1.read()
                temp4 = temp2.count("MARUTI")
                await asyncio.sleep(1)
                logger.info(f"Total count in file1 {temp3}")
                logger.info(f"Total count in file2 {temp4}")


# SaveCount()
asyncio.run(main('MARUTI'))
