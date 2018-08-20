# -*- coding: utf-8 -*-

"""
{{.Title}}.models
~~~~~~~~~~
Api model mixins and definitions.

"""

from sqlalchemy.ext.hybrid import hybrid_property

from {{.Title}}.extensions import db


column = db.Column
relationship = db.relationship


class CrudMixin:
    """Mixin for convenient crud methods."""

    def to_dict(self):
        """Method to convert object to dictionary for serialization."""

        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }

    def update(self, **kwargs):
        """Update specific fields of a record."""

        for attr, value in kwargs.items():
            setattr(self, attr, value)

        db.session.commit()

        return self

    def save(self):
        """Save the record."""

        db.session.add(self)
        db.session.commit()

        return self

    def delete(self):
        """Remove the record from the database."""

        db.session.delete(self)
        db.session.commit()

        return self


# pylint: disable=C0103
class PkMixin:
    """A mixin that adds a surrogate integer 'primary key' column named ``id``
    to any declarative-mapped class.
    """

    id = column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )


class Model(CrudMixin, PkMixin, db.Model):
    """Default model including convenience mixins."""

    __abstract__ = True
