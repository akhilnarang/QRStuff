from mongoengine import StringField

from hades.models.validate import ValidateMixin


class EHJuly2019(ValidateMixin):
    """
    Database model class
    """

    meta = {'collection': 'eh_july_2019'}

    department = StringField()

    def __repr__(self):
        return '%r' % [self.id, self.name, self.email, self.phone, self.department]


class P5November2019(ValidateMixin):
    """
    Database model class
    """

    meta = {'collection': 'p5_november_2019'}

    department = StringField()
    year = StringField(max_length=3)
    level = StringField()

    def __repr__(self):
        return '%r' % [
            self.id,
            self.name,
            self.email,
            self.phone,
            self.department,
            self.year,
            self.level,
        ]
