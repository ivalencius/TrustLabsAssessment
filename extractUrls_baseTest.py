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
    
def main() :
    # Change source of json file here
    with open('example2.json') as infile :
        data = json.load(infile)
    # Alter searchParam to filter results
    searchParam = 'http'
    search_list = siftDict(data, [], searchParam)
    print('\n=== Found Based On : ' + searchParam + " ===\n")
    for search in search_list :
        print(search)

main()