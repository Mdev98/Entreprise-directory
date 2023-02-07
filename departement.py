from tinydb import TinyDB, table, Query
from pathlib import Path
from typing import List
import string
import logging

logging.basicConfig(level=logging.INFO,
                    filename=Path(__file__).resolve().parent / "app.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Departement:
    dir = Path(__file__).resolve().parent / 'database' 
    dir.mkdir(exist_ok=True)
    try:
        DB = TinyDB(Path(dir) / 'data.json', indent=4)
    except FileNotFoundError:
        logging.info("An error setting up the database occur")

    def __init__(self, name:str, staff: List = []):
        """ A class to represent a department in an enterprise.

        Args:
            name (str): Name of the department.
            staff (List, optional): List of staff members in the department. Defaults to [].

        """
        special_characters = string.punctuation + string.digits

        for char in name:
            if char in special_characters:
                raise ValueError("Invalid name")
        
        self.name = name
        self.staff = staff
        
    def __str__(self):
        return self.name

    def add_staff_member(self, member:dict)->int:
        """ Add a new staff member to the department.

        Args:
            member (dict): Information of the staff member.

        Returns:
            int: Number of staff members in the department after the operation.
        """        
        self.staff.append(member)
        return len(self.staff)

    def remove_staff_member(self, id:str)->bool:
        """ Remove a staff member from the departement

        Args:
            id (str): id of the staff member to remove

        Returns:
            bool: True if the staff member was removed, False otherwise.
        """    

        for member in self.staff:
            if id == member.get('id'):
                self.staff.remove(member)
                return True
        return False  

    def exist_in_db(self)->bool:
        """ Check if the instance exist in the databse

        Returns:
            bool: True if it is in the database, False otherwise
        """        
        return bool(Departement.DB.get(Query().name == self.name)) 

    def save(self)->bool:
        """ Save the instance in the database or updated if already exist

        Returns:
            bool: True if the instance was saved, False otherwise
        """   

        print(self.__dict__)     
        if not self.exist_in_db():
            try:
                res = Departement.DB.insert(self.__dict__)  
                print(f"save status {res}")
            except Exception as e:
                logging.info(f"Error while saving to the databse: {e}")
                return False
            return True
        else:
            Departement.DB.update(self.__dict__, Query().name == self.name)
            return True


    def delete(self)->bool:
        """ Delete the instance from the database

        Returns:
            bool: True if the instance was deleted, False otherwise
        """        
        if self.exist_in_db():
            try:
                res = Departement.DB.remove(Query().name == self.name)
            except Exception as e:
                logging.info(f"Error while deleting from the databse: {e}")
                return False
            
            return True
            
        return False

    @classmethod
    def get_all_departement(cls)->List:
        return [cls(**departement) for departement in cls.DB.all()]

    @classmethod
    def get_departement(cls, name)-> table.Document:
        special_characters = string.punctuation + string.digits
        for char in name:
            if char in special_characters:
                raise ValueError("Invalid name")
        return cls.DB.get(Query().name == name)

    @classmethod
    def count_departement(cls)->int:
        return len(cls.DB.all())


if __name__ == "__main__":
    departement = Departement.get_departement("IT")

    departement = Departement(**departement)

    departement.add_staff_member({"name" : "Mamour", "age" : 24})

    print(departement.__dict__)




