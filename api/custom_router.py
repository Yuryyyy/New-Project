from .use_cases import GetUser, PostUser, PutUser, DeleteUser

GET_ROUTES = {
    "user": GetUser,
}

POST_ROUTES = {
    "user": PostUser,
}

PUT_ROUTES = {
    "user": PutUser,
}

DELETE_ROUTES = {
    "user": DeleteUser,
}

ROUTES = {
    "GET": GET_ROUTES,
    "POST": POST_ROUTES,
    "PUT": PUT_ROUTES,
    "DELETE": DELETE_ROUTES,
}
