from odoo import fields, models

class BibliotecaEditorial(models.Model):
  _name="biblioteca.editorial"
  _description="Editoriales"


  nombre = fields.Char(string="Editorial", required=True)
  editorial_id=fields.One2many(comodel_name="biblioteca.libros", inverse_name="editorial")