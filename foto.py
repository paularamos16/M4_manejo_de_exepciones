class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho > self.MAX or ancho <1:
            raise DimensionError('Error en ancho', ancho,self.Max)
            self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto > self.MAX or alto < 1:
            raise DimencionError('error en ancho', alto, self.max)
            self.__alto = alto


if __name__ =='_main_':
    # se ingresan los datos de la foto que se creara
    ancho = 1000   
    alto = 1000 
    ruta = 'www.mifoto.com/mifoto' 

    # se crea una instancia de foto
    foto_pedro =foto(ancho,alto,ruta)

    # evaluamos si hay error

    try:    
       # asignamos nuevos valores
        foto_pedro.ancho =2000
        foto_pedro.alto = 2000
    except DimensionError as e:
     print('Error en la modificacion de datos:')    
     print(e)  
    else:
        print('se modificaron las dimensiones de la foto')
    finally:
        print('>>>programa terminado.fin<<<<')