"""
Create a very simple inheritance hierarchy of three classes that write to text files.  

LogFile(WriteFile):  its instance writes a date and message to a log file:  
2015-01-21 18:35   this is a log message

DelimFile (WriteFile):  its instance writes values separated by a delimeter:
a,b,c,d

WriteFile(object):  the parent class to both LogFile and DelimFile, does work that is common between them.   Not intended to be instantiated.

This is a relatively uncomplicated assignment, but the basic challenge in designing your three classes will be in avoiding duplication of code, and in producing a solution in as few lines as possible.  Obviously there are some tasks that are common between the two classes, and some that are specific.  Your assignment is to create a parent class, WriteFile, that holds the common functionality, which may include part of the constructor tasks, and have LogFile and DelimFile inherit from WriteFile, drawing upon its methods as necessary.  The key then would be to figure out the shortest possible solution using inheritance.

For extra credit (or just a little more challenge), solve the same assignment using composition instead of inheritance.  
"""

from datetime import datetime as dt
import abc


class WriteFile:
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self):
        return

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()


class LogFile(WriteFile):
    def write(self, msg):
        dt_str = dt.now().strftime('%Y-%m-%d %H:%M')
        self.write_line(f'{dt_str}    {msg}')


class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, items):
        for i in range(len(items)):
            if self.delim in items[i]:
                items[i] = f'\"{items[i]}\"'
        self.write_line(self.delim.join(items))


# test it:
log = LogFile('log.txt')                  # passes the filename to write to
mydelim = DelimFile('data.csv', ',')      # passes the filename to write to
                                          # and a delimeter

log.write('this is a log message')        # writes a message to the file
log.write('this is another log message')  # same

mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
mydelim.write(['a', 'b,2', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same


# Here's what the two files look like when we're done:
# text of log.txt
# 2015-01-21 18:35   this is a log message
# 2015-01-21 18:35   this is another log message

# text of data.csv
# a,b,c,d
# a,"b,2",c,d
# 1,2,3,4