# collecting arguments

def artistNames (*artists):
    """
    Our Documentation about function can be written in this way...
    When we aren't clear about the no. of parameters being passed, we use * as above.
    """
    for artist in artists:
        print (artist)

artistNames('Sushant KC', 'Swopna Suman', 'Rajesh Hamal')