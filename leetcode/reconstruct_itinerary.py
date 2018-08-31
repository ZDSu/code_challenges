# https://leetcode.com/problems/reconstruct-itinerary/description/


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        itinerary = ['JFK']
        flights = {}
        start = 'JFK'
            
        for dep, arr in tickets:
            if dep not in flights:
                flights[dep] = arr
            else:
                flights[dep].extend(arr)
        
        for i in range(len(tickets)):
            if start:
                itinerary.append(flights[start])
                start = flights[start]
                # start = sorted(flights[first])[0]
        return itinerary
            
                