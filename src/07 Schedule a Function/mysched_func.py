import time


def schedule_function(duration, func, *args, **kwargs):

    time.sleep(duration)

    func(*args, **kwargs)


if __name__ == '__main__':
    #                      time,       func,  args...
    # schedule_function(time.time()+1, print, "Howdy")
    foo = 'we are'
    schedule_function(1, print, "Hey dummy", foo, "DONE!", sep=', ')
