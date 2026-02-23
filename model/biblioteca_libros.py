from odoo import fields, models

class BibliotecaLibros(models.Model):
  _name="biblioteca.libros"
  _description="Libros de la biblioteca"

  nombre= fields.Char(required="True")
  lanzamiento = fields.Integer(required="True")
  descripcion =fields.Char()
  active =fields.Boolean(default=True)
  state = fields.Selection ([
    ("disponible", "Disponible"),
    ("prestado","Prestado"),
    ("mantenimiento", "Mantenimiento"),
    ("vendido", "Vendido"),
  ])
  editorial = fields.Many2one(comodel_name="biblioteca.editorial", ondelete="restrict")
  autor= fields.Many2one(comodel_name="biblioteca.autor", ondelete="restrict")
  categorias= fields.Many2many(comodel_name="biblioteca.categorias")