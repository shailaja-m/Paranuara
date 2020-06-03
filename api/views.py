from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json

people_data = json.load(open('././jsondata/people.json', 'r'))
companies_data = json.load(open('././jsondata/companies.json', 'r'))

def findAllEmployeesInCompany(request, name):
    company_index = -1
    for company in companies_data:
        if company['company'] == str(name).upper():
            company_index = company['index']
            break
    employees_list = []
    for people in people_data:
        if people["company_id"] == company_index:
            employees_list.append(people)
    return JsonResponse(employees_list, safe=False)

def findCommonFriends(request):
    guid1 = request.GET['guid1']
    guid2 = request.GET['guid2']
    result = {}
    person1 = {}
    friends1 = []
    person2 = {}
    friends2 = []
    for people in people_data:
        if people["guid"] == guid1:
            person1["name"] = people["name"]
            person1["age"] = people["age"]
            person1["address"] = people["address"]
            person1["phone"] = people["phone"]
            friends1 = people["friends"]
        if people["guid"] == guid2:
            person2["name"] = people["name"]
            person2["age"] = people["age"]
            person2["address"] = people["address"]
            person2["phone"] = people["phone"]
            friends2 = people["friends"]
    common_friends_indexes1 = set()
    for friend in friends1:
        common_friends_indexes1.add(friend["index"])
    common_friends_indexes2 = set()
    for friend in friends2:
        common_friends_indexes2.add(friend["index"])
    common_friends_indexes = common_friends_indexes1.intersection(common_friends_indexes2)

    common_friends = []
    for people in people_data:
        if people["index"] in common_friends_indexes and people["eyeColor"]=="brown" and not people["has_died"]:
            common_friends.append(people)
    result["person1"] = person1
    result["person2"] = person2
    result["common_friends"] = common_friends
    return JsonResponse(result)
def findEmployee(request,name):
    person={}
    fruitslist=[]
    vegetableslist=[]
    fruits=["orange", "apple", "banana", "strawberry"]

    for people in people_data:
        if people["name"] == name:
            person["username"] = people["name"]
            person["age"] = people["age"]

            for i in people["favouriteFood"]:
                if i in fruits:
                    fruitslist.append(i)
                else:
                    vegetableslist.append(i)
            person["fruits"]=fruitslist
            person["vegetables"]=vegetableslist

            break
    return JsonResponse(person)

