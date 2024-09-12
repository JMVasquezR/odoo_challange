# -*- coding: utf-8 -*-

from datetime import date

from odoo import (api, models, fields, )
from odoo.fields import (Char, Integer, Boolean, Many2one, Many2many, Date, Float, Text, One2many)


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Asignatura'

    name = Char(string='Nombre', required=True)
    credits = Integer(string='Créditos', required=True)
    max_students = Integer(string='Máximo de Estudiantes')
    active = Boolean(string='Activo', default=True)
    student_ids = Many2many('school.student', string='Estudiantes')
    teacher_id = Many2one('school.teacher', string='Profesor')


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Estudiante'

    name = Char(string='Nombre', required=True)
    birth_date = Date(string='Fecha de Nacimiento', required=True)
    age = Integer(string='Edad', readonly=True)
    final_exam_grade = Float(string='Nota del Examen Final', required=True)
    subject_ids = Many2many('school.subject', string='Asignaturas')

    @api.model
    def create(self, vals):
        """Calcula la edad al crear un registro."""
        if vals.get('birth_date'):
            birth_date = fields.Date.from_string(vals['birth_date'])
            today = date.today()
            vals['age'] = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return super(SchoolStudent, self).create(vals)

    def write(self, vals):
        """Recalcula la edad al actualizar un registro."""
        if vals.get('birth_date') or 'birth_date' in vals:
            for record in self:
                birth_date = fields.Date.from_string(vals.get('birth_date', record.birth_date))
                today = date.today()
                vals['age'] = today.year - birth_date.year - (
                        (today.month, today.day) < (birth_date.month, birth_date.day))
        return super(SchoolStudent, self).write(vals)


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Profesor'

    name = Char(string='Nombre', required=True)
    profile = Text(string='Perfil')
    subject_ids = One2many('school.subject', 'teacher_id', string='Asignaturas')
