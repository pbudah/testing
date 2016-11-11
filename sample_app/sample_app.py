import requests

# should sort the list using any algorithm
def sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst)-n):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1

    return lst

# should return the intersection of two lists
def intersect(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        if lst1[i] in lst2:
            lst.append(lst1[i])

    return lst

# should return the list of projects
def request_get():
    headers = {
        'Content-Type': 'application/json'
    }
    auth = ('restadmin', 'restadmin')

    resp = requests.get('http://13.92.28.188:8090/rest/api/2/project', headers=headers, auth=auth)

    return resp
