from silence.decorators import endpoint

# Los selects deberían soportar todo el rollo del filtrado por query
@endpoint(
    route="/documents",
    method="GET",
    sql="SELECT * FROM Documents",
)
def get_all_documents():
    pass

@endpoint(
    route="/users",
    method="GET",
    sql="SELECT * FROM Users",
)
def get_all_users():
    pass