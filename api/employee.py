from silence.decorators import endpoint
from silence.exceptions import HTTPError

@endpoint(
    route="/employees",
    method="GET",
    sql="SELECT * FROM Employees",
)
def get_all():
    pass

###############################################################################

@endpoint(
    route="/employees/$employeeId",
    method="GET",
    sql="SELECT * FROM Employees WHERE employeeId = $employeeId",
)
def get_by_id():
    pass

###############################################################################

@endpoint(
    route="/employees",
    method="POST",
    sql="INSERT INTO Employees \
         (departmentId, bossId, firstName, lastName, salary, contractStart, contractEnd, fee) \
         VALUES \
         ($departmentId, $bossId, $firstName, $lastName, $salary, $contractStart, $contractEnd, $fee)"
)
def add(departmentId, bossId, firstName, lastName, salary, contractStart, contractEnd, fee):
    if not firstName or not lastName:
        raise HTTPError(400, "The first and last name are required.")

###############################################################################

@endpoint(
    route="/employees/$employeeId",
    method="PUT",
    sql="UPDATE Employees SET departmentId = $departmentId, bossId = $bossId, \
         firstName = $firstName, lastName = $lastName, salary = $salary, \
         contractStart = $contractStart, contractEnd = $contractEnd, fee = $fee \
         WHERE employeeId = $employeeId"
)
def update(departmentId, bossId, firstName, lastName, salary, contractStart, contractEnd, fee):
    pass

###############################################################################

@endpoint(
    route="/employees/$employeeId",
    method="DELETE",
    sql="DELETE FROM Employees WHERE employeeId = $employeeId"
)
def delete():
    pass
