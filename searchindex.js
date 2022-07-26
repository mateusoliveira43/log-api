Search.setIndex({"docnames": ["architecture", "future_improvements", "index", "modules/modules", "modules/source", "modules/source.database", "modules/source.database.functions", "modules/source.dependencies", "modules/source.routes", "modules/source.schemas"], "filenames": ["architecture.rst", "future_improvements.rst", "index.rst", "modules/modules.rst", "modules/source.rst", "modules/source.database.rst", "modules/source.database.functions.rst", "modules/source.dependencies.rst", "modules/source.routes.rst", "modules/source.schemas.rst"], "titles": ["Architecture", "Future improvements", "Welcome to Log API\u2019s documentation!", "source", "source package", "source.database package", "source.database.functions package", "source.dependencies package", "source.routes package", "source.schemas package"], "terms": {"overview": 0, "project": [0, 4], "s": [0, 6, 7, 8], "The": [0, 1, 8], "must": 0, "fulfil": 0, "thi": 0, "list": [0, 1, 6, 8], "an": 0, "http": 0, "server": 0, "have": 0, "authent": [0, 1, 3, 4, 6, 8], "method": 0, "receiv": [0, 1], "store": [0, 1, 6, 7, 8], "retriev": 0, "open": 0, "end": 0, "event": [0, 1, 3, 4, 5], "type": [0, 4, 6, 7, 8, 9], "all": [0, 6], "should": [0, 1], "contain": 0, "common": 0, "set": [0, 3], "field": 0, "specif": [0, 4], "us": 0, "why": 0, "thei": 0, "where": [0, 1, 4], "chosen": 0, "fastapi": [0, 6, 7, 8], "improv": 0, "my": 0, "product": [0, 1], "write": 0, "code": [0, 4, 5], "provid": 0, "document": 0, "endpoint": [0, 1, 8, 9], "free": 0, "sqlalchemi": [0, 4, 5, 6, 7, 8], "To": 0, "scale": 0, "allow": 0, "easili": 0, "test": 0, "function": [0, 4, 5, 7], "access": 0, "without": 0, "mock": 0, "postgresql": 0, "relat": [0, 5, 7, 8], "i": 0, "most": 0, "experi": 0, "docker": 0, "compos": 0, "environ": 0, "reproduc": 0, "differ": 0, "oper": 0, "system": 0, "due": 0, "given": 0, "exampl": 0, "usag": 0, "decid": 0, "3": 0, "tabl": [0, 5], "user": [0, 1, 3, 4, 5, 7], "inform": 0, "custom": [0, 1, 3, 4, 5], "object": [0, 5, 9], "present": 0, "each": 0, "For": 1, "simplic": 1, "follow": 1, "featur": 1, "ad": 1, "servic": [1, 4, 6, 7, 8, 9], "rout": [1, 3, 4], "creat": [1, 7, 8], "new": [1, 6], "doe": 1, "requir": 1, "In": 1, "version": 1, "onli": 1, "high": 1, "level": 1, "abl": 1, "There": 1, "patch": 1, "updat": 1, "exist": 1, "delet": 1, "ar": [1, 6], "filter": 1, "when": 1, "lot": 1, "simultan": 1, "data": 1, "through": 1, "them": 1, "do": 1, "1": 1, "commit": 1, "instead": 1, "sever": 1, "technic": 2, "challeng": 2, "select": 2, "process": 2, "packag": 3, "subpackag": 3, "databas": [3, 4, 8], "submodul": 3, "model": [3, 4], "modul": 3, "depend": [3, 4, 8], "schema": [3, 4], "messag": [3, 4, 6, 8], "__main__": 3, "log": 4, "api": [4, 7], "get_database_set": 4, "str": [4, 6, 7, 9], "get": [4, 6, 7], "instanti": 4, "engin": 4, "format": 4, "dialect": 4, "driver": 4, "usernam": [4, 6, 7, 8], "password": [4, 6, 7, 8, 9], "host": 4, "port": 4, "database_nam": 4, "lowercas": 4, "python": 4, "dbapi": 4, "name": [4, 5, 6, 9], "return": [4, 6, 7, 8, 9], "map": 5, "orm": [5, 6, 7, 8], "class": [5, 9], "kwarg": 5, "base": [5, 9], "_sa_class_manag": 5, "email": [5, 6, 7, 8, 9], "attribut": 5, "instrumentedattribut": 5, "id_": 5, "is_act": [5, 6], "customer_id": 5, "registered_at": [5, 9], "type_": [5, 6, 9], "hashed_password": [5, 7], "manipul": 6, "check_email_avail": 6, "database_sess": [6, 8], "session": [6, 7, 8], "none": [6, 7], "check": [6, 7], "avail": 6, "paramet": [6, 7, 8, 9], "rais": [6, 7, 8], "httpexcept": [6, 7, 8], "If": [6, 7, 8], "alreadi": [6, 8], "regist": [6, 8], "get_customer_avail": 6, "bool": [6, 7], "statu": 6, "true": [6, 7], "activ": [6, 8], "fals": [6, 7], "otherwis": [6, 7], "pass": 6, "associ": [6, 9], "get_customer_by_email": 6, "add_creation_ev": 6, "add": 6, "registr": 6, "add_custom_ev": 6, "add_status_ev": 6, "get_event_list": 6, "option": [6, 8], "eventmodel": [6, 8, 9], "authenticate_us": 6, "form_data": 6, "oauth2passwordrequestform": [6, 8], "incorrect": 6, "check_authent": 7, "token": [7, 8, 9], "oauth2passwordbear": 7, "ha": 7, "valid": 7, "author": 7, "header": 7, "default": [7, 8, 9], "tokenurl": 7, "f": 7, "user_url": 7, "token_url": 7, "invalid": 7, "expir": [7, 9], "check_password": 7, "correct": 7, "plain": 7, "hash": 7, "could": 7, "create_authentication_token": 7, "create_hashed_password": 7, "get_database_sess": [7, 8], "gener": [7, 9], "yield": 7, "async": 8, "activate_custom": 8, "emailstr": [8, 9], "form": [8, 9], "ellipsi": [8, 9], "pydant": [8, 9], "network": [8, 9], "success": 8, "create_custom": 8, "customerform": [8, 9], "deactivate_custom": 8, "deactiv": 8, "create_ev": 8, "eventform": [8, 9], "list_ev": 8, "create_us": 8, "userform": [8, 9], "create_user_token": 8, "nonetyp": 8, "constrainedstrvalu": 9, "basemodel": 9, "_abc_impl": 9, "_abc": 9, "_abc_data": 9, "classmethod": 9, "constr": 9, "datetim": 9, "detail": 9, "jwttoken": 9, "iat": 9, "float": 9, "exp": 9, "sub": 9, "jwt": 9, "With": 9, "issu": 9, "time": 9, "subject": 9, "access_cod": 9, "bearer": 9}, "objects": {"": [[4, 0, 0, "-", "source"]], "source": [[4, 0, 0, "-", "__main__"], [5, 0, 0, "-", "database"], [7, 0, 0, "-", "dependencies"], [8, 0, 0, "-", "routes"], [9, 0, 0, "-", "schemas"], [4, 0, 0, "-", "settings"]], "source.database": [[6, 0, 0, "-", "functions"], [5, 0, 0, "-", "models"]], "source.database.functions": [[6, 0, 0, "-", "customer"], [6, 0, 0, "-", "event"], [6, 0, 0, "-", "user"]], "source.database.functions.customer": [[6, 1, 1, "", "check_email_availability"], [6, 1, 1, "", "get_customer_available"], [6, 1, 1, "", "get_customer_by_email"]], "source.database.functions.event": [[6, 1, 1, "", "add_creation_event"], [6, 1, 1, "", "add_custom_event"], [6, 1, 1, "", "add_status_event"], [6, 1, 1, "", "get_event_list"]], "source.database.functions.user": [[6, 1, 1, "", "authenticate_user"]], "source.database.models": [[5, 2, 1, "", "Customer"], [5, 2, 1, "", "Event"], [5, 2, 1, "", "User"]], "source.database.models.Customer": [[5, 3, 1, "", "_sa_class_manager"], [5, 3, 1, "", "email"], [5, 3, 1, "", "events"], [5, 3, 1, "", "id_"], [5, 3, 1, "", "is_active"], [5, 3, 1, "", "name"]], "source.database.models.Event": [[5, 3, 1, "", "_sa_class_manager"], [5, 3, 1, "", "customer_id"], [5, 3, 1, "", "id_"], [5, 3, 1, "", "registered_at"], [5, 3, 1, "", "type_"]], "source.database.models.User": [[5, 3, 1, "", "_sa_class_manager"], [5, 3, 1, "", "email"], [5, 3, 1, "", "hashed_password"], [5, 3, 1, "", "id_"]], "source.dependencies": [[7, 0, 0, "-", "authentication"], [7, 0, 0, "-", "database"]], "source.dependencies.authentication": [[7, 1, 1, "", "check_authentication"], [7, 1, 1, "", "check_password"], [7, 1, 1, "", "create_authentication_token"], [7, 1, 1, "", "create_hashed_password"]], "source.dependencies.database": [[7, 1, 1, "", "get_database_session"]], "source.routes": [[8, 0, 0, "-", "customer"], [8, 0, 0, "-", "event"], [8, 0, 0, "-", "user"]], "source.routes.customer": [[8, 1, 1, "", "activate_customer"], [8, 1, 1, "", "create_customer"], [8, 1, 1, "", "deactivate_customer"]], "source.routes.event": [[8, 1, 1, "", "create_event"], [8, 1, 1, "", "list_event"]], "source.routes.user": [[8, 1, 1, "", "create_user"], [8, 1, 1, "", "create_user_token"]], "source.schemas": [[9, 0, 0, "-", "customer"], [9, 0, 0, "-", "event"], [9, 0, 0, "-", "message"], [9, 0, 0, "-", "user"]], "source.schemas.customer": [[9, 2, 1, "", "CustomerForm"]], "source.schemas.customer.CustomerForm": [[9, 3, 1, "", "_abc_impl"], [9, 3, 1, "", "email"], [9, 4, 1, "", "form"], [9, 3, 1, "", "name"]], "source.schemas.event": [[9, 2, 1, "", "EventForm"], [9, 2, 1, "", "EventModel"]], "source.schemas.event.EventForm": [[9, 3, 1, "", "_abc_impl"], [9, 3, 1, "", "email"], [9, 4, 1, "", "form"], [9, 3, 1, "", "type_"]], "source.schemas.event.EventModel": [[9, 3, 1, "", "_abc_impl"], [9, 3, 1, "", "customer"], [9, 3, 1, "", "registered_at"], [9, 3, 1, "", "type_"]], "source.schemas.message": [[9, 2, 1, "", "Message"]], "source.schemas.message.Message": [[9, 3, 1, "", "_abc_impl"], [9, 3, 1, "", "detail"]], "source.schemas.user": [[9, 2, 1, "", "JWTToken"], [9, 2, 1, "", "Token"], [9, 2, 1, "", "UserForm"]], "source.schemas.user.JWTToken": [[9, 3, 1, "", "_abc_impl"], [9, 3, 1, "", "exp"], [9, 3, 1, "", "iat"], [9, 3, 1, "", "sub"]], "source.schemas.user.Token": [[9, 3, 1, "", "_abc_impl"], [9, 3, 1, "", "access_code"], [9, 3, 1, "", "type_"]], "source.schemas.user.UserForm": [[9, 3, 1, "", "_abc_impl"], [9, 3, 1, "", "email"], [9, 4, 1, "", "form"], [9, 3, 1, "", "password"]], "source.settings": [[4, 1, 1, "", "get_database_settings"]]}, "objtypes": {"0": "py:module", "1": "py:function", "2": "py:class", "3": "py:attribute", "4": "py:method"}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "function", "Python function"], "2": ["py", "class", "Python class"], "3": ["py", "attribute", "Python attribute"], "4": ["py", "method", "Python method"]}, "titleterms": {"architectur": 0, "servic": 0, "requir": 0, "technolog": 0, "databas": [0, 5, 6, 7], "futur": 1, "improv": 1, "welcom": 2, "log": 2, "api": 2, "s": 2, "document": 2, "sourc": [3, 4, 5, 6, 7, 8, 9], "packag": [4, 5, 6, 7, 8, 9], "subpackag": [4, 5], "submodul": [4, 5, 6, 7, 8, 9], "__main__": 4, "modul": [4, 5, 6, 7, 8, 9], "set": 4, "model": 5, "function": 6, "custom": [6, 8, 9], "event": [6, 8, 9], "user": [6, 8, 9], "depend": 7, "authent": 7, "rout": 8, "schema": 9, "messag": 9}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 6, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx": 56}})