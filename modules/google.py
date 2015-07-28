__author__ = 'Vale Tolpegin & Matthew Nguyen'

"""
GoogleSearcher allows Jarvis to search the web using Google

Class Information:
- Version: 0.0.0
- Stable: No
- In-use: No

"""

import urllib
import json

class GoogleSearcher:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def search( self, search_term ):
        """ Searches Google for the search_term and returns the response """

        query = urllib.urlencode( { 'q' : search_term } )
        response = urllib.urlopen( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
        json_response = json.loads ( response )
        results = json_response[ 'responseData' ][ 'results' ]
        for result in results:
           title = result['title']
           url = result['url']   # was URL in the original and that threw a name error exception
           #print ( title + '; ' + url )
           #print ""

        return results


# Tests for if this is being run as an individual program
#if __name__ == '__main__':
#    my_searcher = GoogleSearcher()
#
#    my_searcher.search( "What time is it in San Fransisco?" )
