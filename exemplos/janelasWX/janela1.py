#!/usr/bin/env python
# -*- coding: latin-1 -*-
# Desenvolvimento Aberto
# MdiForms.py
  
# importa modulos
import wx
 
# Declara Classe
class MDIFormulario(wx.MDIParentFrame):
 
    # Declara Contrutor
    def __init__(self):
 
        # Cria Formulario Pai
        wx.MDIParentFrame.__init__(self, None, -1, "Python - Formulario - MDI ",size=(wx.GetDisplaySize()))
 
        # Cria Menu
        menu = wx.Menu()
        menu.Append(5000, "&Novo")
        menu.Append(5001, "&Sair")
 
        # Cria Barra de menus
        menubarra = wx.MenuBar()
        menubarra.Append(menu, "&Formulario")
        self.SetMenuBar(menubarra)
 
        # Declara Eventos dos menus
        self.Bind(wx.EVT_MENU, self.OnNovoFormulario, id=5000)
        self.Bind(wx.EVT_MENU, self.OnSair, id=5001)
 
    # Cria evento de saida
    def OnSair(self, evt):
        self.Close(True)
 
     # Cria Janela
    def OnNovoFormulario(self, evt):
        # Cria Formulario Filho
        FormularioFilho = wx.MDIChildFrame(self, -1, "Formulario Filho", size=(400, 200))
         
        # Cria componentes do formulario
        self.texto = wx.StaticText(FormularioFilho, label="Digite seu nome: ", pos=(20, 30))
        self.campo = wx.TextCtrl(FormularioFilho, size=(300, -1), pos=(20, 60))
        self.botao = wx.Button(FormularioFilho, label="Ok", pos=(20, 90))
         
        # Exibe formulario
        FormularioFilho.Show(True)
 
# Cria aplicação Wx
app = wx.PySimpleApp()
 
# Cria formulario
formulario = MDIFormulario()
formulario.Show()
 
# Loop do tcl
app.MainLoop()