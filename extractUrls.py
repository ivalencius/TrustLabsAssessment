# INPUTS --> JSON file, list of search parameters (strs)
# USE --> Filters a JSON file, returning a combined list of any urls that match the search criteria
import json

# Works on dictionaries
def siftDict(dictionary, searchList, searchParam) :
    for key, value in dictionary.items() :
        # Check Key
        if searchParam in key :
            searchList.append(key)
        # Need another recursive call
        if isinstance(value, list) :
            searchList + siftList(value, searchList, searchParam)
        elif isinstance(value, dict) :
            searchList + siftDict(value, searchList, searchParam)
        # Single item
        if searchParam in key :
            searchList.append(key)
        elif searchParam in value :
            searchList.append(value)
    searchList = list(set(searchList))
    return searchList
    
# Works on lists
def siftList(testList, searchList, searchParam) :
    for item in testList :
        # Need another recursive call
        if isinstance(item, list) :
            searchList + siftList(item, searchList, searchParam)
        elif isinstance(item, dict) :
            searchList + siftDict(item, searchList, searchParam)
        # Single item found
        if searchParam in item :
            searchList.append(item)
    return searchList                              
    
def extract(source, searchParamList) :
    search_list = []
    for searchParam in searchParamList:
        search_list + siftDict(source, [], searchParam)
    # Returns searchParam1 OR searchParam2 OR ... (NEED TO AND)
    # Achive by filtering all results which dont contain ALL search parameters
    for result in search_list :
        for param in searchParamList :
            if param not in result :
                search_list.remove(result)
    # Eliminate duplicates
    return list(set(search_list))