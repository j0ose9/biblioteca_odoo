from odoo import fields, models

class Biblioteca(models.Model):
  _name="biblioteca"
  _description="biblioteca"

  nombre= fields.Char()