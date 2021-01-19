# INPUTS --> JSON file, list of search parameters (strs)
# USE --> Filters a JSON file, returning a combined list of any urls that match the search criteria
import json

# Works on dictionaries
def siftDict(dictionary, searchList, searchParam) :
    for key, value in dictionary.items() :
        # Check Key
        if ((searchParam in key) and ("http" in key)) :
            searchList.append(key)
        # Need another recursive call
        if isinstance(value, list) :
            searchList + siftList(value, searchList, searchParam)
        elif isinstance(value, dict) :
            searchList + siftDict(value, searchList, searchParam)
        # Single item check value
        if ((searchParam in value) and ("http" in value)) :
            searchList.append(value)
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
        if ((searchParam in item) and ("http" in item)) :
            searchList.append(item)
    return searchList                              
    
def extract_urls(source, searchParamList) :
    search_list = []
    for searchParam in searchParamList:
        search_list + siftDict(source, [], searchParam)
        print(search_list)
    # Returns searchParam1 OR searchParam2 OR ... 
    # Filter for just URLS : FIXED DO COMPARISON WHILE SEARCHING
    #for result in search_list :
    #    if 'http' not in result :
    #        search_list.remove(result)
    # Eliminate duplicates
    return search_list