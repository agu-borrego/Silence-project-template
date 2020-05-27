from silence.decorators import endpoint

@endpoint(
    route="/departments",
    method="GET",
    sql="SELECT * FROM Departments",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/departments/$departmentId",
    method="GET",
    sql="SELECT * FROM Departments WHERE departmentId = $departmentId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/departments",
    method="POST",
    sql="INSERT INTO Departments (name, city) VALUES ($name, $city)"
)
def add(name, city):
    pass

###############################################################################

@endpoint(
    route="/departments/$departmentId",
    method="PUT",
    sql="UPDATE Departments SET name = $name, city = $city WHERE departmentId = $departmentId"
)
def update(name, city):
    pass

###############################################################################

@endpoint(
    route="/departments/$departmentId",
    method="DELETE",
    sql="DELETE FROM Departments WHERE departmentId = $departmentId"
)
def delete():
    pass
