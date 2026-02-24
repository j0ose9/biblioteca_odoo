from odoo import fields, models

class BibliotecaAutor(models.Model):
  _name="biblioteca.autor"
  _description="autores"

  nombre= fields.Char(string="Nombre Autor", required=True)
  autor_id=fields.One2many(comodel_name="biblioteca.libros", inverse_name="autor")