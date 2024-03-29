Future improvements
===================

For simplicity, the following features where not added to the service:

- The route for creating new users does not required authentication. In a production version of the service, only high level users should be able to create new users.
- There is no ``PATCH`` route to updating a existing customer.
- There is no ``DELETE`` route to delete a existing customer.
- There are no filters when listing the events.
- when receiving a lot of simultaneous data through the endpoints, store them and only do 1 commit instead of several.
- Add monitoring service to check API health.
