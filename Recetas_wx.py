# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculo Precio Recetas", pos = wx.DefaultPosition, size = wx.Size( 760,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1_Materias_primas = wx.Menu()
		self.m_menuItem1_Ingreso_mat_primas = wx.MenuItem( self.m_menu1_Materias_primas, wx.ID_ANY, u"Ingreso", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1_Materias_primas.Append( self.m_menuItem1_Ingreso_mat_primas )

		self.m_menuItem2_Modificacion_mat_primas = wx.MenuItem( self.m_menu1_Materias_primas, wx.ID_ANY, u"Modificacion", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1_Materias_primas.Append( self.m_menuItem2_Modificacion_mat_primas )

		self.m_menuItem3_Baja_mat_primas = wx.MenuItem( self.m_menu1_Materias_primas, wx.ID_ANY, u"Baja", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1_Materias_primas.Append( self.m_menuItem3_Baja_mat_primas )

		self.m_menubar1.Append( self.m_menu1_Materias_primas, u"Materias Primas" )

		self.precio_ingredientes = wx.Menu()
		self.m_menuItem10_precio_ingrediente = wx.MenuItem( self.precio_ingredientes, wx.ID_ANY, u"Precio Ingrediente", wx.EmptyString, wx.ITEM_NORMAL )
		self.precio_ingredientes.Append( self.m_menuItem10_precio_ingrediente )

		self.m_menubar1.Append( self.precio_ingredientes, u"Precio de Ingredientes" )

		self.m_menu2_Recetas = wx.Menu()
		self.m_menuItem4_Crear_receta = wx.MenuItem( self.m_menu2_Recetas, wx.ID_ANY, u"Crear", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2_Recetas.Append( self.m_menuItem4_Crear_receta )

		self.m_menuItem5_Modificar_receta = wx.MenuItem( self.m_menu2_Recetas, wx.ID_ANY, u"Modificar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2_Recetas.Append( self.m_menuItem5_Modificar_receta )

		self.m_menuItem6_Eliminar_receta = wx.MenuItem( self.m_menu2_Recetas, wx.ID_ANY, u"Eliminar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2_Recetas.Append( self.m_menuItem6_Eliminar_receta )

		self.m_menubar1.Append( self.m_menu2_Recetas, u"Recetas" )

		self.m_menu3 = wx.Menu()
		self.m_menuItem7_informe = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Informe ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem7_informe )

		self.m_menubar1.Append( self.m_menu3, u"Informes" )

		self.m_menu4 = wx.Menu()
		self.m_menuItem8_Ayuda = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Ayuda", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem8_Ayuda )

		self.m_menuItem9_acerca = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Acerca de ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem9_acerca )

		self.m_menubar1.Append( self.m_menu4, u"Ayuda" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuItem1_Ingreso_mat_primasOnMenuSelection, id = self.m_menuItem1_Ingreso_mat_primas.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem2_Modificacion_mat_primasOnMenuSelection, id = self.m_menuItem2_Modificacion_mat_primas.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem3_Baja_mat_primasOnMenuSelection, id = self.m_menuItem3_Baja_mat_primas.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem10_precio_ingredienteOnMenuSelection, id = self.m_menuItem10_precio_ingrediente.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem4_Crear_recetaOnMenuSelection, id = self.m_menuItem4_Crear_receta.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem5_Modificar_recetaOnMenuSelection, id = self.m_menuItem5_Modificar_receta.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem6_Eliminar_recetaOnMenuSelection, id = self.m_menuItem6_Eliminar_receta.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem7_informeOnMenuSelection, id = self.m_menuItem7_informe.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem8_AyudaOnMenuSelection, id = self.m_menuItem8_Ayuda.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem9_acercaOnMenuSelection, id = self.m_menuItem9_acerca.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_menuItem1_Ingreso_mat_primasOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem2_Modificacion_mat_primasOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem3_Baja_mat_primasOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem10_precio_ingredienteOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem4_Crear_recetaOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem5_Modificar_recetaOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem6_Eliminar_recetaOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem7_informeOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem8_AyudaOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem9_acercaOnMenuSelection( self, event ):
		event.Skip()


###########################################################################
## Class MateriasPrimas
###########################################################################

class MateriasPrimas ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 760,550 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"MATERIAS PRIMAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer26.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer26.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"INGREDIENTE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer27.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_textCtrl15_ingrediente = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer27.Add( self.m_textCtrl15_ingrediente, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer26.Add( bSizer27, 0, wx.EXPAND, 5 )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.Gramos_radio_boton = wx.RadioButton( self, wx.ID_ANY, u"Gramos", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.Gramos_radio_boton, 0, wx.ALL, 5 )

		self.cm3_radio_boton = wx.RadioButton( self, wx.ID_ANY, u"Cm3.", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.cm3_radio_boton, 0, wx.ALL, 5 )

		self.Unidad_radio_boton = wx.RadioButton( self, wx.ID_ANY, u"Unidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.Unidad_radio_boton, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer29, 0, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button7_guadar = wx.Button( self, wx.ID_ANY, u"GUARDAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button7_guadar, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		# Connect Events
		self.m_textCtrl15_ingrediente.Bind( wx.EVT_TEXT, self.m_textCtrl15_ingredienteOnText )
		self.Gramos_radio_boton.Bind( wx.EVT_RADIOBUTTON, self.Gramos_radio_botonOnRadioButton )
		self.cm3_radio_boton.Bind( wx.EVT_RADIOBUTTON, self.cm3_radio_botonOnRadioButton )
		self.Unidad_radio_boton.Bind( wx.EVT_RADIOBUTTON, self.Unidad_radio_botonOnRadioButton )
		self.m_button7_guadar.Bind( wx.EVT_BUTTON, self.m_button7_guadarOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_textCtrl15_ingredienteOnText( self, event ):
		event.Skip()

	def Gramos_radio_botonOnRadioButton( self, event ):
		event.Skip()

	def cm3_radio_botonOnRadioButton( self, event ):
		event.Skip()

	def Unidad_radio_botonOnRadioButton( self, event ):
		event.Skip()

	def m_button7_guadarOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Crear_Receta
###########################################################################

class Crear_Receta ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 760,550 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Crear Receta", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6_receta = wx.StaticText( self, wx.ID_ANY, u"RECETA", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText6_receta.Wrap( -1 )

		bSizer8.Add( self.m_staticText6_receta, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl5_receta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer8.Add( self.m_textCtrl5_receta, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button6_nombre_receta = wx.Button( self, wx.ID_ANY, u"NOMBRE RECETA", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button6_nombre_receta, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_static_Ingrediente = wx.StaticText( self, wx.ID_ANY, u"INGREDIENTE", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_static_Ingrediente.Wrap( -1 )

		bSizer4.Add( self.m_static_Ingrediente, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_comboBox3_ingredientesChoices = []
		self.m_comboBox3_ingredientes = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox3_ingredientesChoices, wx.CB_READONLY )
		bSizer4.Add( self.m_comboBox3_ingredientes, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3_PESO = wx.StaticText( self, wx.ID_ANY, u"CANTIDAD EN GRS. O EN CM3 ", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText3_PESO.Wrap( -1 )

		bSizer3.Add( self.m_staticText3_PESO, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl2_cant_gr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2_cant_gr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"CANTIDAD EN UNIDADES", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl3_cant_unidad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl3_cant_unidad, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer2.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button5_agregar_mat_prima = wx.Button( self, wx.ID_ANY, u"AGREGAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button5_agregar_mat_prima, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13_titulo_receta = wx.StaticText( self, wx.ID_ANY, u"NOMBRE DE RECETA", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText13_titulo_receta.Wrap( -1 )

		self.m_staticText13_titulo_receta.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer19.Add( self.m_staticText13_titulo_receta, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer19, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( False )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.SetColSize( 0, 278 )
		self.m_grid1.SetColSize( 1, 122 )
		self.m_grid1.SetColSize( 2, 137 )
		self.m_grid1.SetColSize( 3, 93 )
		self.m_grid1.SetColSize( 4, 80 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"INGREDIENTES" )
		self.m_grid1.SetColLabelValue( 1, u"CANT. GRS. O CM3." )
		self.m_grid1.SetColLabelValue( 2, u"CANTIDAD UNIDADES" )
		self.m_grid1.SetColLabelValue( 3, u"PRECIO" )
		self.m_grid1.SetColLabelValue( 4, u"SUBTOTAL" )
		self.m_grid1.SetColLabelValue( 5, wx.EmptyString )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 30 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"TOTAL", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText7.Wrap( -1 )

		bSizer9.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl6_total = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		bSizer9.Add( self.m_textCtrl6_total, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer2.Add( bSizer9, 0, wx.ALIGN_RIGHT, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1_guardar = wx.Button( self, wx.ID_ANY, u"GUARDAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button1_guardar, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.m_button6_nombre_receta.Bind( wx.EVT_BUTTON, self.m_button6_nombre_recetaOnButtonClick )
		self.m_comboBox3_ingredientes.Bind( wx.EVT_COMBOBOX, self.m_comboBox3_ingredientesOnCombobox )
		self.m_button5_agregar_mat_prima.Bind( wx.EVT_BUTTON, self.m_button5_agregar_mat_primaOnButtonClick )
		self.m_button1_guardar.Bind( wx.EVT_BUTTON, self.m_button1_guardarOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button6_nombre_recetaOnButtonClick( self, event ):
		event.Skip()

	def m_comboBox3_ingredientesOnCombobox( self, event ):
		event.Skip()

	def m_button5_agregar_mat_primaOnButtonClick( self, event ):
		event.Skip()

	def m_button1_guardarOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Precio_de_Materia_Prima
###########################################################################

class Precio_de_Materia_Prima ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 760,550 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"CARGA DE PRECIOS DE LAS MATERIAS PRIMAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer10.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"INGREDIENTE", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer11.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_comboBox4_ingredientesChoices = []
		self.m_comboBox4_ingredientes = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox4_ingredientesChoices, wx.CB_READONLY )
		bSizer11.Add( self.m_comboBox4_ingredientes, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"CANTIDAD POR GR. O CM3.", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer14.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl10_cant_gr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_textCtrl10_cant_gr, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"CANTIDAD EN UNIDADES", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer12.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl8_cant_unidad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl8_cant_unidad, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"PRECIO", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer13.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl9_precio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_textCtrl9_precio, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer13, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 5, 5 )
		self.m_grid2.EnableEditing( False )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.SetColSize( 0, 308 )
		self.m_grid2.SetColSize( 1, 105 )
		self.m_grid2.SetColSize( 2, 109 )
		self.m_grid2.SetColSize( 3, 88 )
		self.m_grid2.SetColSize( 4, 101 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"INGREDIENTES" )
		self.m_grid2.SetColLabelValue( 1, u"CANT. GR. O CM3." )
		self.m_grid2.SetColLabelValue( 2, u"CANT. UNIDADES" )
		self.m_grid2.SetColLabelValue( 3, u"PRECIO" )
		self.m_grid2.SetColLabelValue( 4, u"PRECIO REDUCCION" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 30 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer15.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3_guardar = wx.Button( self, wx.ID_ANY, u"GUARDAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button3_guardar, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer17, 0, 0, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		# Connect Events
		self.m_comboBox4_ingredientes.Bind( wx.EVT_COMBOBOX, self.m_comboBox4_ingredientesOnCombobox )
		self.m_button3_guardar.Bind( wx.EVT_BUTTON, self.m_button3_guardarOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_comboBox4_ingredientesOnCombobox( self, event ):
		event.Skip()

	def m_button3_guardarOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Informe
###########################################################################

class Informe ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 750,550 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"INFORME", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer21.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"RECETA", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer22.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox1Choices, wx.CB_READONLY )
		bSizer22.Add( self.m_comboBox1, 0, wx.ALL, 5 )


		bSizer21.Add( bSizer22, 0, wx.EXPAND, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"PORCIONES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer23.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl1_porciones = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 500, 1 )
		bSizer23.Add( self.m_spinCtrl1_porciones, 0, wx.ALL, 5 )


		bSizer21.Add( bSizer23, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 5, 5 )
		self.m_grid3.EnableEditing( False )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.SetColSize( 0, 297 )
		self.m_grid3.SetColSize( 1, 124 )
		self.m_grid3.SetColSize( 2, 112 )
		self.m_grid3.SetColSize( 3, 85 )
		self.m_grid3.SetColSize( 4, 80 )
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelValue( 0, u"INGREDIENTES" )
		self.m_grid3.SetColLabelValue( 1, u"CANT. GR. CM3." )
		self.m_grid3.SetColLabelValue( 2, u"CANT. UNIDAD" )
		self.m_grid3.SetColLabelValue( 3, u"PRECIO" )
		self.m_grid3.SetColLabelValue( 4, u"SUBTOTAL" )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 30 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer24.Add( self.m_grid3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer21.Add( bSizer24, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"PRECIO POR PORCION", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer25.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl13_precio_por_porcion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		bSizer25.Add( self.m_textCtrl13_precio_por_porcion, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( bSizer25, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		# Connect Events
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.m_comboBox1OnCombobox )
		self.m_spinCtrl1_porciones.Bind( wx.EVT_SPINCTRL, self.m_spinCtrl1_porcionesOnSpinCtrl )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_comboBox1OnCombobox( self, event ):
		event.Skip()

	def m_spinCtrl1_porcionesOnSpinCtrl( self, event ):
		event.Skip()


