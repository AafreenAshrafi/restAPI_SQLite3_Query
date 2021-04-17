# restAPI_SQLite3_Query

itilite is my Project name and app is myapiapp
DB in use : SQLite3

methods restframework::
get,put,delete,post API supported at url:

1) event -
	a)get,post - http://127.0.0.1:8000/myapiapp/event
	b)edit- put,delete -http://127.0.0.1:8000/myapiapp/editevent/1/
2) category-
	a)get,post - http://127.0.0.1:8000/myapiapp/category
	b)edit- put,delete - http://127.0.0.1:8000/myapiapp/editcategory/1/
	
3) Show list of events by each category specific: URL - http://127.0.0.1:8000/myapiapp/showeventoncategory/1/
4) Show Top 3 Category based on no of events which associated with that category :URL - http://127.0.0.1:8000/myapiapp/TopEventOnCategoryDetails/
Note:
	1) I have attached the screenshot of all 6 restframework pages with the mail
	2) secret key has been changed 
	3) categoryMaster -id column is foreign key for eventMaster so if category id 5 is deleted all events belonging to that will get deleted
	4) to simplify the get method id is key we are searching with as mentioned in urls above
	5) Delete api on category should delete all events associated with that category.
		
---------------
sample eventMaster request body:

{
"id":"1",
"eventName":"birthday",
"place":"gaya",
"time":"1pm",
"duration":"20 min",
"cast":"early",
"categoryName":"1"
}
--------------
sample categoryMaster request body:

{
"id":6,
"categoryName":"oneday",
"parentName":"one"
}
--------------
