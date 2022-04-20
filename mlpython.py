import requests
import pandas as pd
from pytube import YouTube


def say_hello():
    """
  print "hello world""
  :return: None
  """
    print('Hello World!')


def get_first_name(name: str):
    """
    This function gets the first name and prints it
  """
    # Different ways to print
    print("First Name: ", name)
    print("First name: %s" % name)
    print(f'First name: {name}')


# Function with default value
def get_first_name2(name: str = 'Ana'):
    """
  print 3 time the name
  :param name: a string
  :return: None
  """
    print("First Name: ", name)
    print("First name: %s" % name)
    print(f'First name: {name}')


def download(url: str):
    """
  download a file from an URL
  :param url: the url of the needed file
  :return: None
  """
    req = requests.get(url)
    url_content = req.content
    csv_file = open('iris.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()


def get_data_url(url: str):
    """
  download a file from an URL
  :param url: the url of the needed file
  :return: a pandas file
  """
    res = pd.read_csv(url, header=None)
    return res


def download_yt_video(save_path: str, link_video: str):
    """
  download a youtube video
  :param save_path: directory path to save the video
  :param link_video: url of a youtube video
  :return: None
  """

    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(link_video)
    except:
        print("Connection Error")  # to handle exception

    # get the video with the extension and
    # resolution passed in the get() function
    # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
    # try:
    yt.streams.filter(progressive=True,
                      file_extension="mp4").first().download(output_path=save_path,
                                                             filename="Video_Test")
    # downloading the video
    # d_video.download(save_path)
    # except:
    # print("Some Error!")
    print('Task Completed!')


# Count the number of words in a sentence
def count_words(sentence: str) -> int:
    """
  Count the number of word (define base on the space) in string
  :param sentence: a string
  :return: the count as integer
  """
    counter = 0
    if type(sentence) == type(str):
        words = sentence.split()  # default split by space

        for i in words:
            counter += 1
    else:
        raise Exception

    return counter


# Count the number of words in a sentence whose length is greater than k
def count_words_k(sentence: str, k: int) -> int:
    """
  This function returns the number of words in a sentence whose length is
  greater than a given parameter 'k'
  """
    # declare the return variable and initialize it to 0
    counter = 0

    # Check the type of the param 'sentence' is of type 'string'
    if type(sentence) == str:
        words = sentence.split()  # default split by space

        # Iterate throw the list of words
        for word in words:
            # Check the length of each word
            if len(word) > k:  # if the length is greater than 'k', count 1
                counter += 1

    # if 'sentence' is not a string raise a ValueError Exception
    else:
        raise ValueError

    # return the final counter of words whose length is greater than k
    return counter


# Rewrite function with try except clause
def get_data_url(url: str):
    """
  get data from an url using try except
  :param url:  the url of the data as CSV
  :return: a pandas dataframe
  """
    res = None
    flag = False
    try:
        res = pd.read_csv(url, header=None)
    except Exception as e:
        flag = True
        print(e)

    if flag:  # Check if 'res' has not value None
        raise Exception  # Block the code
    else:
        return res
