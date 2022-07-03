Architecture
============

Overview of the project's architecture, requirements and technologies.

Service requirements
--------------------

The service must fulfill this list of requirements:

- be an HTTP server
- have an authentication method
- receive, store and retrieve an open-ended list of event types

    -  all events should contain a common set of fields and a set of fields specific to the event type

technologies
------------

List of the technologies used by the service and why they where chosen.

- FastAPI

    Improve my productivity writing the code and provide documentation for the service endpoints for free.

- SQLAlchemy

    To scale the service, allowing to easily test functions that access the database without using mocks.

- PostgreSQL

    The relational database I have most experience with.

- Docker and Docker Compose

    To provide a environment reproducible in different operating systems.

Database
--------

Due to given examples of the service usage, I decided to have 3 tables in the system database:

- User

    Stores authentication information for usage of the service.

- Customer

    Stores the customer information, the object present in all events.

- Event

    Stores the events of each customer.
