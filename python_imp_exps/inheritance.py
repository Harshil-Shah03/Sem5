'''Write python code to implement the following inheritance example:
Classes: Employee, Developer, Tester,
ManagerDeveloper, tester, Manager inherit EmployeeManager handles Developer,
 testerManager class : implement
functions to add Developer/Tester and Remove Developer/ TesterDisplay ..
 to see the list of employees he manages

'''


class Employee:
    def __init__(self, _id, desig, name):
        self._id = _id
        self.desig = desig
        self.name = name


class Developer(Employee):
    def __init__(self, _id, name):
        super().__init__(_id, "Developer", name)


class Tester(Employee):
    def __init__(self, _id, name):
        super().__init__(_id, "Tester", name)


class Manager(Employee):
    def __init__(self, _id, name):
        super().__init__(_id, "Manager", name)
        self.devel_l = []

    def add_dev(self, developer: Developer):
        self.devel_l.append(developer)
        print(f"You hired a developer {self.devel_l[-1].name}")

    def rem_dev(self, _id):
        for i in self.devel_l:
            if i._id == _id:
                self.devel_l.remove(i)
                print(f"You fired {i.name}")

    def myDevs(self):
        print(f"My devs are {[i.name for i in self.devel_l]}")

def main():
    manager=Manager(1,'Virat')
    developer1=Developer(2,'Rohit')
    developer2=Developer(3,'Rohit')
    developer3=Developer(4,'Rohit')
    tester=Tester(3,'Dhoni')
    manager.add_dev(developer=developer1)
    manager.add_dev(developer=developer2)
    manager.add_dev(developer=developer3)
    manager.myDevs()
    manager.rem_dev(2)
    manager.myDevs()
main()

# class Employee:
#     _id:int
#     name:str
#     desig:str
#     def __init__(self,_id,name,desig):
#         self._id=_id
#         self.name=name
#         self.desig=desig
# class Developer(Employee):
#     def __init__(self,_id,name):
#         super().__init__(_id,name,desig="Developer")
# class Tester(Employee):
#     def __init__(self,_id,name):
#         super().__init__(_id,name,desig="Tester")
# class Manager(Employee):
#     def __init__(self,_id,name):
#         super().__init__(_id,name,desig="Manager")
#     _developers=[]
#     def add_dev(self,developer:Developer):
#         self._developers.append(developer)
#     def rem_dev(self,_id):
#         for dev in self._developers:
#             if _id==dev._id:
#                 self._developers.remove(dev)
#                 return True
#         return False
#     def myDevs(self):
#         print("Devs under me")
#         for dev in self._developers:
#             print(dev.name)
#         return
# def main():
#     manager=Manager(1,'Virat')
#     developer1=Developer(2,'Rohit')
#     developer2=Developer(3,'Rohit')
#     developer3=Developer(4,'Rohit')
#     tester=Tester(3,'Dhoni')
#     manager.add_dev(developer=developer1)
#     manager.add_dev(developer=developer2)
#     manager.add_dev(developer=developer3)
#     manager.myDevs()
#     manager.rem_dev(2)
#     manager.myDevs()
# main()
