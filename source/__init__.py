"""Source code of the project."""

__version__ = "0.1.0"  # major.minor.patch

# - user
#     - email email
#     - password str

# - customer
#     - name str
#     - email email
#     - is_active bool

# - event
#     - event_type str
#     - customer FK [ID]
#     - registration_time timedate [GENERATED]

# POST /user/create/
# GET /user/login/

# *special events*

# [AUTH] POST /customer/create/
# [AUTH] GET /customer/deactivate/id -> error if already deactivated
# [AUTH] GET /customer/activate/id -> error if already activated

# *common events*

# [AUTH] POST /event/
# [AUTH] GET /event/list/{id}

# *common errors*

# access routes without [AUTH]
# wrong name endpoints
# POST without/wrong data
