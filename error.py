class DimensionError(Exception):
    def _init_(self,mensaje ,dimension, maximo):
        super()._init_(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def _str_(self):
        if self.dimension < 1:
            return f'La dimension {self.dimension} no puede ser menor a 1'
        else:
            return f'La dimension {self.dimension}no puede ser mayor al maximo {self.maximo}'

