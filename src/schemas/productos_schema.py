from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.productos import Productos

class ProductoSchema(SQLAlchemyAutoSchema):
        class Meta:
            model = Productos
            load_instance = True

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)