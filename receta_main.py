from Recetas_wx import MyFrame1, Crear_Receta, MateriasPrimas, Precio_de_Materia_Prima, Informe
import wx
import wx.xrc
import wx.grid
import archivo 
import operaciones_auxiliares

###########################################################################
# Programa para calcular precio de recetas por porciones
#
#
#
#
#
###########################################################################


class Planilla(MyFrame1):

    def __init__(self, *args, **kwargs):
        super(Planilla, self).__init__(*args, **kwargs)
        self.panel1 = CrearReceta(self)
        self.panel2 = PrecioMateriaPrima(self)
        self.panel3 = Inform(self)
        self.panel4 = Materias_Prima(self)
        self.panel2.Hide()
        self.panel3.Hide()
        self.panel1.Hide()

        self.bSizer27 = wx.BoxSizer(wx.VERTICAL)
        self.bSizer27.Add(self.panel1, 1, wx.EXPAND)
        self.bSizer27.Add(self.panel2, 1, wx.EXPAND)
        self.bSizer27.Add(self.panel3, 1, wx.EXPAND)
        self.bSizer27.Add(self.panel4, 1, wx.EXPAND)
        self.SetSizer(self.bSizer27)

    def m_menuItem1_Ingreso_mat_primasOnMenuSelection(self, event):

        self.panel1.Hide()
        self.panel2.Hide()
        self.panel3.Hide()
        self.panel4.Show()
        self.Layout()

    def m_menuItem2_Modificacion_mat_primasOnMenuSelection(self, event):
        event.Skip()

    def m_menuItem3_Baja_mat_primasOnMenuSelection(self, event):
        event.Skip()

    def m_menuItem10_precio_ingredienteOnMenuSelection(self, event):
        self.panel1.Hide()
        self.panel2.Show()
        self.panel3.Hide()
        self.panel4.Hide()
        self.panel2.carga_combo()
        self.Layout()

    def m_menuItem4_Crear_recetaOnMenuSelection(self, event):
        self.panel1.Show()
        self.panel2.Hide()
        self.panel3.Hide()
        self.panel4.Hide()
        self.Layout()

    def m_menuItem5_Modificar_recetaOnMenuSelection(self, event):
        event.Skip()

    def m_menuItem6_Eliminar_recetaOnMenuSelection(self, event):
        event.Skip()

    def m_menuItem7_informeOnMenuSelection(self, event):
        self.panel1.Hide()
        self.panel2.Hide()
        self.panel3.Show()
        self.panel4.Hide()
        self.Layout()
        self.panel3.combo()

    def m_menuItem8_AyudaOnMenuSelection(self, event):
        event.Skip()

    def m_menuItem9_acercaOnMenuSelection(self, event):
        event.Skip()

#######################################################################################
#
# Carga de Materia prima y tipo de cantidad
#
#######################################################################################


class Materias_Prima(MateriasPrimas):

    def __init__(self, *args, **kwargs):
        mat = "materia_prima"
        try:
            self.dicc_ingrediente = archivo.recuperar_datos(mat)
        except:
            self.dicc_ingrediente = {}
        self.ingrediente = ""
        self.cantidad = ""
        super(Materias_Prima, self).__init__(*args, **kwargs)

    def m_textCtrl15_ingredienteOnText(self, event):
        self.ingrediente = self.m_textCtrl15_ingrediente.GetValue().upper()

    def Gramos_radio_botonOnRadioButton(self, event):
        self.cantidad =  "gramos"

    def cm3_radio_botonOnRadioButton(self, event):
        self.cantidad = "cm3"

    def Unidad_radio_botonOnRadioButton(self, event):
        self.cantidad = "unidad"

    def m_button7_guadarOnButtonClick(self, event):
        if self.ingrediente in self.dicc_ingrediente:
            wx.MessageBox("Existe el ingrediente en la base de datos",
                          "Ya existe el ingrediente", wx.OK | wx.ICON_EXCLAMATION)

        else:
            self.dicc_ingrediente[self.ingrediente] = self.cantidad
            mat = "materia_prima"
            guardado = archivo.guardar_datos(self.dicc_ingrediente, mat)
            if guardado:
                self.limpiar()
                wx.MessageBox("Se guardaron los datos", "Datos guardados", wx.OK | wx.ICON_EXCLAMATION)

            else:
                wx.MessageBox("Error al guardar los datos", "Cierre y vuelva a abrir el programa para"
                                                            " volver a cargar los datos", wx.OK | wx.ICON_EXCLAMATION)
    def limpiar(self):
        self.m_textCtrl15_ingrediente.Clear()


###########################################################################
## CREAR RECETA
###########################################################################

class CrearReceta(Crear_Receta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        receta = "receta"
        self.dicc_receta = archivo.recuperar_datos(receta)
        self.receta = ""
        self.ingrediente = ""
        self.cant_gr = ""
        self.cant_uni = ""
        self.precio = ""
        self.porciones = ""
        self.dicc_ingrediente_precio = self.ingrediente_precio()
        self.combo_ingrediente()
        self.lista_receta = []


    def ingrediente_precio(self):
        try:
            pre = "precio_materia_prima"
            dicc_ingrediente_precio = archivo.recuperar_datos(pre)
            return dicc_ingrediente_precio
        except:
            return None

    def carga_precio(self):

        self.precio = self.dicc_ingrediente_precio[self.ingrediente][3]

    def m_button6_nombre_recetaOnButtonClick(self, event):
        self.receta = self.m_textCtrl5_receta.GetValue().upper()
        self.m_staticText13_titulo_receta.SetLabel(self.receta)
        self.Layout()

    def combo_ingrediente(self):
        try:
            mat = "materia_prima"
            self.dicc_ingrediente = archivo.recuperar_datos(mat)
            datos = self.dicc_ingrediente.keys()
            self.m_comboBox3_ingredientes.SetItems(list(datos))
        except:
            self.dicc_ingrediente = {}

    def deshabilitar_text_control(self):
        if self.dicc_ingrediente.get(self.ingrediente) == "gramos":
            self.m_textCtrl3_cant_unidad.Disable()
            self.m_textCtrl2_cant_gr.Enable(True)
            return True

        elif self.dicc_ingrediente.get(self.ingrediente) == "cm3":
            self.m_textCtrl3_cant_unidad.Disable()
            self.m_textCtrl2_cant_gr.Enable(True)
            return True

        else:
            self.m_textCtrl2_cant_gr.Disable()
            self.m_textCtrl3_cant_unidad.Enable(True)
            return False

    def m_button5_agregar_mat_primaOnButtonClick(self, event):
        self.carga_precio()
        if self.deshabilitar_text_control():
            if operaciones_auxiliares.numero_entero(self.m_textCtrl2_cant_gr.GetValue()):
                self.cant_gr = self.m_textCtrl2_cant_gr.GetValue()
            else:
                wx.MessageBox("Debe ingresar un número", "Falta ingresar dato", wx.OK_DEFAULT | wx.ICON_ERROR)

        else:
            if operaciones_auxiliares.numero_entero(self.m_textCtrl3_cant_unidad.GetValue()):
                self.cant_uni = self.m_textCtrl3_cant_unidad.GetValue()
            else:
                wx.MessageBox("Debe ingresar un número", "Falta ingresar dato", wx.OK_DEFAULT | wx.ICON_ERROR)

        if self.cant_uni == "" and self.cant_gr == "":
            wx.MessageBox("Debe ingresar un número", "Falta ingresar dato", wx.OK_DEFAULT | wx.ICON_ERROR)

        else:
            self.lista_receta.append((self.ingrediente, self.cant_gr, self.cant_uni, self.precio))
            self.limpiar()
            self.cargar_grid()

    def cargar_grid(self):
        self.m_grid1.AppendRows(len(self.lista_receta))

        x = 0
        total = 0


        for ingred, cant_gr, cant_uni, precio in self.lista_receta:
            try:
                subtotal = float(precio) * float(cant_gr)
            except:
                subtotal = float(precio) * float(cant_uni)
            total = subtotal + total
            self.m_grid1.SetCellAlignment(x, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid1.SetCellAlignment(x, 2, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid1.SetCellAlignment(x, 3, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid1.SetCellAlignment(x, 4, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)

            self.m_grid1.SetCellValue(x, 0, "%s" % ingred)
            self.m_grid1.SetCellValue(x, 1, "%s" % str(cant_gr))
            self.m_grid1.SetCellValue(x, 2, "%s" % str(cant_uni))
            self.m_grid1.SetCellValue(x, 3, "%s" % str(precio))
            self.m_grid1.SetCellValue(x, 4, "%s" % str(subtotal))
            x=x+1

        self.m_textCtrl6_total.SetValue(str(total))

    def m_button1_guardarOnButtonClick(self, event):
        self.dicc_receta[self.receta] = self.lista_receta
        receta = "receta"
        archivo.guardar_datos(self.dicc_receta, receta)
        self.limpiar()


    def m_comboBox3_ingredientesOnCombobox(self, event):
        self.ingrediente = self.m_comboBox3_ingredientes.GetValue()
        self.deshabilitar_text_control()

    def limpiar(self):
        self.m_textCtrl5_receta.Clear()
        self.m_staticText13_titulo_receta.SetLabel("Nombre de la receta")
        self.m_textCtrl3_cant_unidad.Clear()
        self.m_textCtrl2_cant_gr.Clear()
        self.m_comboBox3_ingredientes.Select(0)
        self.m_grid1.ClearGrid()
        self.cant_gr = ""
        self.cant_uni = ""


###########################################################################
## Carga de PRECIO MATERIAS PRIMAS
###########################################################################

class PrecioMateriaPrima(Precio_de_Materia_Prima):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dicc_ingrediente = {}
        self.ingrediente = ""
        self.cant_gr_peso = ""
        self.cant_unidad = ""
        self.precio = 0
        self.dicc_ingrediente_precio = {}
        self.carga_grid()


    def carga_combo(self):
        try:
            pre = "precio_materia_prima"
            self.dicc_ingrediente_precio = archivo.recuperar_datos(pre)
        except:
            self.dicc_ingrediente_precio = {}

        try:
            mat = "materia_prima"
            self.dicc_ingrediente = archivo.recuperar_datos(mat)
            datos = self.dicc_ingrediente.keys()
            self.m_comboBox4_ingredientes.SetItems(list(datos))
        except:
            self.dicc_ingrediente = {}

    def carga_precio(self):
        if operaciones_auxiliares.excep_ingreso_datos_numero(self.m_textCtrl9_precio.GetValue()):
            self.precio = self.m_textCtrl9_precio.GetValue()
            return True

    def deshabilitar_text_control(self):
        if self.dicc_ingrediente.get(self.ingrediente) == "gramos":
            self.m_textCtrl8_cant_unidad.Disable()
            self.m_textCtrl10_cant_gr.Enable(True)
            return True
        elif self.dicc_ingrediente.get(self.ingrediente) == "cm3":
            self.m_textCtrl8_cant_unidad.Disable()
            self.m_textCtrl10_cant_gr.Enable(True)
            return True
        else:
            self.m_textCtrl10_cant_gr.Disable()
            self.m_textCtrl8_cant_unidad.Enable(True)
            return False

    def m_comboBox4_ingredientesOnCombobox(self, event):
        self.ingrediente = self.m_comboBox4_ingredientes.GetValue()
        self.deshabilitar_text_control()
        self.carga_grid()

    def unidad(self):
        if self.deshabilitar_text_control():
            if operaciones_auxiliares.numero_entero(self.m_textCtrl10_cant_gr.GetValue()):
                self.cant_gr_peso = self.m_textCtrl10_cant_gr.GetValue()
        else:
            if operaciones_auxiliares.numero_entero(self.m_textCtrl8_cant_unidad.GetValue()):
                self.cant_unidad = self.m_textCtrl8_cant_unidad.GetValue()

    def m_button3_guardarOnButtonClick(self, event):
        self.unidad()
        if self.carga_precio():
            try:
                self.precio_final = float(self.precio) / float(self.cant_gr_peso)

            except:
                self.precio_final = float(self.precio) / float(self.cant_unidad)

            self.dicc_ingrediente_precio[self.ingrediente] = [self.cant_gr_peso, self.cant_unidad, self.precio, str(self.precio_final)]
            pmt = "precio_materia_prima"
            guardado = archivo.guardar_datos(self.dicc_ingrediente_precio, pmt)
            if guardado:
                wx.MessageBox("Se guardaron los datos", "Datos guardados", wx.OK | wx.ICON_EXCLAMATION)
                self.limpiar_vista()
                self.carga_grid()
            else:
                wx.MessageBox("Error al guardar los datos", "Cierre y vuelva a abrir el programa para"
                                                            " volver a cargar los datos", wx.OK | wx.ICON_EXCLAMATION)
    def limpiar_vista(self):
        self.m_textCtrl9_precio.Clear()
        self.m_comboBox4_ingredientes.Select(0)
        self.m_textCtrl10_cant_gr.Clear()
        self.m_textCtrl8_cant_unidad.Clear()
        self.cant_gr_peso = None
        self.cant_unidad = None
        self.precio = 0

    def carga_grid(self):

        self.m_grid2.AppendRows(len(self.dicc_ingrediente_precio))

        x = 0

        for key, lista in self.dicc_ingrediente_precio.items():
            cant_gr, cant_uni, precio, precio_final = lista
            self.m_grid2.SetCellAlignment(x, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid2.SetCellAlignment(x, 2, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid2.SetCellAlignment(x, 3, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid2.SetCellAlignment(x, 4, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)

            self.m_grid2.SetCellValue(x, 0, "%s" % key)
            self.m_grid2.SetCellValue(x, 1, "%s" % str(cant_gr))
            self.m_grid2.SetCellValue(x, 2, "%s" % str(cant_uni))
            self.m_grid2.SetCellValue(x, 3, "%s" % str(precio))
            self.m_grid2.SetCellValue(x, 4, "%s" % str(precio_final))
            x=x+1

###########################################################################
## Informe por porciones
###########################################################################
class Inform(Informe):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total = 0
        self.dicc_receta = {}
        self.carga_dicc_receta()
        self.combo()
        self.ingrediente = ""

    def carga_dicc_receta(self):
        receta = "receta"
        try:
            self.dicc_receta = archivo.recuperar_datos(receta)
        except:
            self.dicc_receta = {}

    def combo(self):
        self.carga_dicc_receta()
        datos = self.dicc_receta.keys()
        self.m_comboBox1.SetItems(list(datos))

    def m_comboBox1OnCombobox(self, event):
        self.m_grid3.ClearGrid()
        self.ingrediente = self.m_comboBox1.GetValue()
        self.carga_grid()


    def carga_grid(self):
        self.m_grid3.AppendRows(len(self.dicc_receta[self.ingrediente]))

        x = 0

        for ingred, cant_gr, cant_uni, precio in self.dicc_receta[self.ingrediente]:
            try:
                subtotal = float(precio) * float(cant_gr)
            except:
                subtotal = float(precio) * float(cant_uni)
            self.total = subtotal + self.total
            self.m_grid3.SetCellAlignment(x, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid3.SetCellAlignment(x, 2, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid3.SetCellAlignment(x, 3, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)
            self.m_grid3.SetCellAlignment(x, 4, wx.ALIGN_RIGHT, wx.ALIGN_CENTRE_VERTICAL)

            self.m_grid3.SetCellValue(x, 0, "%s" % ingred)
            self.m_grid3.SetCellValue(x, 1, "%s" % str(cant_gr))
            self.m_grid3.SetCellValue(x, 2, "%s" % str(cant_uni))
            self.m_grid3.SetCellValue(x, 3, "%s" % str(precio))
            self.m_grid3.SetCellValue(x, 4, "%s" % str(subtotal))
            x=x+1



    def m_spinCtrl1_porcionesOnSpinCtrl(self, event):
        cant_porciones =self.m_spinCtrl1_porciones.GetValue()

        porciones = float(self.total)/int(cant_porciones)

        porciones = "{:.2f}".format(porciones)

        self.m_textCtrl13_precio_por_porcion.SetLabel(str(porciones))



if __name__ == '__main__':
    app = wx.App()
    frame = Planilla(None)
    frame.Show(True)
    app.MainLoop()



