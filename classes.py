class Employee:
    def __init__(self):
        self.car = Car()
        self.salary = 0

    def drive(self, distance):
        self.car.run(60, distance) 

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount
        if self.car.fuelRate > 100:
            self.car.fuelRate = 100

####################################################################
class Car:
    def __init__(self):
        self.velocity = 0
        self.fuelRate = 50  

    def run(self, velocity, distance):
        if velocity < 0 or velocity > 200:
            raise ValueError("Velocity must be between 0 and 200")
        if self.fuelRate == 0:
            self.stop()
            return
        self.velocity = velocity
        self.fuelRate -= velocity / 10  
        remain_distance = distance - (self.velocity * 1)  
        if remain_distance <= 0:
            self.stop()
        else:
            print(f"Remaining distance: {remain_distance} km")
            self.stop()

    def stop(self):
        self.velocity = 0
        print("Car has stopped")

#########################################################################
class Office:
    employeesNum = 0

    def __init__(self):
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.empId == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        for emp in self.employees:
            if emp.empId == empId:
                self.employees.remove(emp)
                Office.employeesNum -= 1
                break

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp is not None:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp is not None:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp is not None:
            targetHour = 9 
            distance = 10  
            velocity = 60  
            if Office.calculate_lateness(targetHour, moveHour, distance, velocity):
                emp.salary -= 10
                print("Employee is late, salary has been deducted by 10")
            else:
                emp.salary += 10
                print("Employee is not late, salary has been rewarded by 10")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        expectedArrivalTime = targetHour + (distance / velocity)
        return moveHour > expectedArrivalTime

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
##################################################################
