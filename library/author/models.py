from django.db import models


class Author(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes last name of the author
        type surname: str max_length=20
        param patronymic: Describes middle name of the author
        type patronymic: str max_length=20
    """
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, null=True, max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """
        return f"{self.surname}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """
        return f"Author(id={self.pk})"

    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """
        try:
            return Author.objects.get(pk=author_id)
        except:
            return None

    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a author to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            author = Author.objects.get(pk=author_id)
            author.delete()
            return True
        except:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: a new author object which is also written into the DB
        """
        if name and len(name) <= 20 and surname and len(surname) <= 20:
            if patronymic and len(patronymic) > 20:
                return None 
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author
        return None


    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """
        # return self.__dict__

    def update(self,
               name=None,
               surname=None,
               patronymic=None):
        """
        Updates author in the database with the specified parameters.\n
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: None
        """

        if name and len(name) <= 20:
            self.name = name
        if surname and len(surname) <= 20:
            self.surname = surname
        if patronymic and len(patronymic) <= 20:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        return Author.objects.all()
