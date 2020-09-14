import unittest
#the period before models makes it accesible
from app.models import Source, Top_Headlines, Everything


class SourceTest(unittest.TestCase) :
  '''
  Test class to test the behaviour of the ources class
  '''

  def setUp(self) :
    '''
    Set up method that will run before every test 
    '''
    self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")

  def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_source,Source))

class Top_HeadlinesTest(unittest.TestCase) :
  '''
  Test class to test the behaviour of the ources class
  '''

  def setUp(self) :
    '''
    Set up method that will run before every test 
    '''
    self.new_top = Top_Headlines("null", "YG, DJ Khaled & Marsha Ambrosius & John Legend Perform Tribute to Nipsey Hussle | BET Awards 2019 - BETNetworks", "null", "https://www.youtube.com/watch?v=ILMeLOkDxfk", "null", "2019-06-24T08:00:03Z", "[[getSimpleString(data.title)]]\r\n[[getSimpleString(data.description)]]\r\n[[getSimpleString(data.videoCountText)]]")

  def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_top,Top_Headlines))

class EverythingTest(unittest.TestCase) :
  '''
  Test class to test the behaviour of the ources class
  '''

  def setUp(self) :
    '''
    Set up method that will run before every test 
    '''
    self.new_everything = Everything("Kris Holt", "Florida city gives in to $600,000 bitcoin ransomware demand", "Riviera Beach, a city in Florida, is set to pay hackers $600,000 in bitcoin with the hope of having its systems restored. Hackers took over the systems several weeks ago, when a police department employee opened a malicious email that allowed them to inject t…", "https://www.engadget.com/2019/06/20/florida-hacker-ransom-riviera-beach/","https://o.aolcdn.com/images/dims?thumbnail=1200%2C630&quality=80&image_uri=https%3A%2F%2Fo.aolcdn.com%2Fimages%2Fdims%3Fcrop%3D5616%252C3490%252C0%252C180%26quality%3D85%26format%3Djpg%26resize%3D1600%252C994%26image_uri%3Dhttps%253A%252F%252Fs.yimg.com%252Fos%252Fcreatr-images%252F2019-06%252Fe7a36330-9367-11e9-9f77-9fe8b4d4c6fb%26client%3Da1acac3e1b3290917d92%26signature%3D4c915a40afcb463421503ea77ca8e0124a782453&client=amp-blogside-v2&signature=eb187bd7b7475f2d0532eed862383e0e7a2a73aa", "2019-06-20T14:42:00Z", "Aside from locking down the files, the attack took down the city email network, forced Riviera Beach to pay employees and contractors by check instead of direct deposit and made it so 911 dispatchers couldn't enter calls into their systems. The city says ther… [+781 chars]")

  def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_everything,Everything))



if __name__ == '__main__' :
  unittest.main()
