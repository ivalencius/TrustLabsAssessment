# INPUTS --> JSON file, list of search parameters (strs)
# USE --> Filters a JSON file, returning a combined list of any urls that match the search criteria
import json

# Works on dictionaries
def siftDict(dictionary, searchList, searchParam) :
    for key, value in dictionary.items() :
        # Check for null types
        if isinstance(key, (bool,int,float,complex,bytes,bytearray)) :
            continue
        # Check Key
        elif ((searchParam in key) and ("http" in key)) and len(key) <150: # Length requirement prevents copying paragraphs
            searchList.append(key)
        # Check for Null types
        if isinstance(value, (bool,int,float,complex,bytes,bytearray)) :
            continue
        # Check key
        if isinstance(value, list) :
            searchList + siftList(value, searchList, searchParam)
        elif isinstance(value, dict) :
            searchList + siftDict(value, searchList, searchParam)
        # Single item check --> endcases
        elif (searchParam in value) and ("http" in value) and len(value) <150:
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
        # Single item found --> endcases
        elif isinstance(item, (bool,int,float,complex,bytes,bytearray)) :
            continue
        elif ((searchParam in item) and ("http" in item)) and len(item) <150:
            searchList.append(item)
    return searchList                              
    
def extract_urls(json_dict, searchParamList) :
    search_list = []
    for searchParam in searchParamList:
        search_list + siftDict(json_dict, search_list, searchParam)
    # Returns searchParam1 OR searchParam2 OR ... 
    # Filter for just URLS : FIXED DO COMPARISON WHILE SEARCHING
    #for result in search_list :
        #if 'http' not in result :
            #search_list.remove(result)
    return search_list

#def main() :
#     search_list = []
#     searchParam = "http"
#     with open('test.json') as infile :
#        json_dict = json.load(infile)
#        search_list = siftDict(json_dict, [], searchParam)
#        print('\n=== Found Based On : ' + searchParam + " ===\n")
#        for search in search_list :
#            print(search)
            
#main() 