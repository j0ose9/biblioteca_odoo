from odoo import fields, models

class BibliotecaCategorias(models.Model):

  _name="biblioteca.categorias"
  _description="Categorias"

  nombre=fields.Char(string="Categoria", required=True)
  libro_ids=fields.Many2many(comodel_name="biblioteca.libros")