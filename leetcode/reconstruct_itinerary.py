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
                flights[dep] = [arr]
            else:
                flights[dep].append(arr)
                flights[dep] = sorted(flights[dep])
        
        for i in range(len(tickets)):
            start = flights[start].pop(0)
            itinerary.append(start)
        return itinerary


# test cases:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]  gives Line 19: KeyError: 'KUL'
# findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"],["SJC","JFK"],["JFK","ZBC"]])

# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] should return ["JFK","NRT","JFK","KUL"]
# JS solution: https://goo.gl/JwnyVJ  builds itinerary backwards

# [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]