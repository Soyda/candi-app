from os import name
import re
import flask
import sqlite3

class Request():
    
    def get_db_connection(self):
        """[Call to get connection to the BDD]
        """
        return(sqlite3.connect('App/candidature.db'))
     
    def request_nomination_by_id(self, id):
        """[Fonction for get the nomination of the id]

        Args:
            id ([Int]): [Id to compare on the BDD]

        Returns:
            [List]: [Response of request with the id]
        """
        connection = self.get_db_connection()
        request = "SELECT C.id, E.name, E.place, C.contact, C.date, C.status FROM Candidacy as C Join Users as U ON U.id = C.user_id JOIN Enterprise as E ON E.id = C.enterprise_id WHERE U.id = "+ str(id)
        result = connection.execute(request).fetchall()
        connection.close()
        return result

    def request_nomination_by_entreprise_name(self, entreprise_name):
        """[Fonction for get the nomination of the entreprise name]

        Args:
            entreprise_name ([str]): [entreprise name to compare on the BDD]

        Returns:
            [List]: [Response of request with the entreprise name]
        """
        connection = self.get_db_connection()
        request = "SELECT U.last_name, U.first_name, E.place, C.contact, C.status FROM Candidacy as C Join Users as U ON U.id = C.user_id JOIN Enterprise as E ON E.id = C.enterprise_id WHERE E.name = '" + entreprise_name +"'"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
            
    def request_nomination_by_lastname(self, lastname):
        """[Fonction for get the nomination of the lastname]

        Args:
            lastname ([str]): [last name to compare on the BDD]

        Returns:
            [List]: [Response of request with the lastname]
        """
        connection = self.get_db_connection()
        request = "SELECT Enterprise.name, Enterprise.place, Candidacy.contact, Candidacy.status FROM Candidacy, Enterprise WHERE (SELECT id from Users WHERE LOWER(last_name) = '"+ lastname.lower() +"') = Candidacy.user_id AND Candidacy.enterprise_id = Enterprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
    
    def request_nomination_by_firstname(self, first_name):
        """[Fonction for get the nomination of the first_name]

        Args:
            first_name ([str]): [first name to compare on the BDD]

        Returns:
            [List]: [Response of request with the first_name]
        """
        connection = self.get_db_connection()
        request = "SELECT Entreprise.name, Entreprise.place, Candidacy.contact, Candidacy.status FROM Candidacy, Entreprise WHERE (SELECT id from Users WHERE LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result

    def request_nomination_by_firstname_lastname(self, first_name, lastname):
        """[Fonction for get the nomination of the first_name and lastname]

        Args:
            first_name ([str]): [first name to compare on the BDD]
            lastname ([str]): [last name to compare on the BDD]

        Returns:
            [List]: [Response of request with the first_name and lastname]
        """
        connection = self.get_db_connection()
        request = "SELECT Entreprise.name, Entreprise.place, Candidacy.contact, Candidacy.status FROM Candidacy, Entreprise WHERE (SELECT id from Users WHERE LOWER(last_name) = '"+ lastname.lower() + "' AND LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
    
    def request_all_nomination(self):
        """[Fonction for get all nomination]

        Returns:
            [List]: [Nomination in the BDD]
        """
        connection = self.get_db_connection()
        request = "SELECT Users.last_name, Users.first_name, Enterprise.name, Enterprise.place, Candidacy.contact, Candidacy.date, Candidacy.status FROM Users, Candidacy, Enterprise WHERE Users.id = Candidacy.user_id AND Candidacy.enterprise_id = Enterprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result