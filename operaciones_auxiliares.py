import datetime
import archivo
import wx


def fecha():
    fecha_x = datetime.now()

    m = fecha_x.strftime("%B")
    mes = dict(January="Enero", February="Febrero", March="Marzo", April="Abril", May="Mayo", June="Junio",
               July="Julio", August="Agosto", September="Septiembre", October="Octubre", November="Noviembre",
               December="Diciembre")

    me = mes[m]

    formato_fecha = "%d " + me + " %Y  -  %H:%M:%S"

    salida_fecha = fecha_x.strftime(formato_fecha)

    fechacd = str(salida_fecha)

    return fechacd


def excep_ingreso_datos_numero(dato):

    try:
        d = float(dato)
        dato = "{:.2f}".format(d)
        return True

    except:
        wx.MessageBox("Debe ingresar un número", "Falta ingresar dato", wx.OK_DEFAULT | wx.ICON_ERROR)
        return False

def numero_entero(dato):
    try:
        d = int(dato)
        return True

    except:
        return False
