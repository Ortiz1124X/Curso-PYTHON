from time import localtime, time, mktime

class JornadaTrabajo:
    def __int__(self, hora_inicio, hora_fin):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def eshorariojornada(self):
        result = localtime()
        eshorario = 0
        if self.hora_inicio > result.tm_hour:
            eshorario = -1

        if self.hora_fin <= result.tm_hour:
            eshorario = 1
        return eshorario

    def finjornada(self):

        segundos = time()
        result = time()
        horariofin = mktime((result.tm_year, result.tm_mon, result.tm_mday, self.hora_fin, 0, 0, 0, 0, 0))
        return horariofin-segundos