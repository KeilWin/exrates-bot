import os
import pprint

from dotenv import load_dotenv


load_dotenv('.env')


if __name__ == '__main__':
    print(os.environ['OS'])
