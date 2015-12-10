App Engine application for the Udacity training course.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080][5].)
1. (Optional) Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.

## Task 1 - Design Choices
1. Sessions can be created as entities within datastore by making use of the Session Class in models.py
2. Speakers are simply a Stringfield attribute to the Session object

## Task 3 - Additonal Queries
1. Query for all sessions accross all conferences, this query is designed for potential delegates to view the actual content available in existing conferences and make their decisions on which conferences to attend thereon.
2. An additional wishlist query was implemented allowing users to view all the sessions in their wishlist accross all conferences, and not only within a specific conference.

## Task 3 - Query Problem
1. The problem with this query is that it would need to filter the query using more than one inequality filter which is not allowed in Google Datastore.
2. The Solution to this problem implemented in this application was to do the first filter for 'typeOfSession' using the datastore query, and then the additional filtering implemented through the actual code of the application by iterating over the query result and storing all items within the query object that match the target criteria in a new object to be returned by the endpoints method.
3. The endpoints method implemented to demonstrate this functionality is the 'getSpecialSessions' method in the conference API class.



[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
