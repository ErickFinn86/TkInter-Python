from Tkinter import *
import ttk
import MySQLdb
import os
import tkMessageBox
import csv





#ventana

ventana = Tk()




def insertar():
      Id = int()
      d1 = fecha_text.get()
      d2 = usuario_text.get() 
      d3 = aplicacion_text.get() 
      d4 = folio_text.get() 
      d5 = status_text.get() 
      d6 = inputway_text.get()

      conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "efrias002")
      cursor = conn.cursor()

      sql ='INSERT INTO base17 VALUES("%s","%s", "%s", "%s", "%s", "%s","%s")'%(Id, d1, d2, d3, d4, d5, d6)

      try:
          cursor.execute(sql)
          conn.commit()
          conn.close()
          tkMessageBox.showinfo("Info","Registro Agregado Correctamente")
          
      except:
          conn.rollback()
          conn.close()


def mostrar():
    conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "efrias002")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM base17")
    data = cursor.fetchall()
    for item in data:
        list1.insert(END,item)
    cursor.execute("SELECT COUNT(*) FROM base17")
    for item in cursor:
        tkMessageBox.showinfo("Registros Totales", item)
    conn.close()
    

def buscar():
    res = busqueda_text.get()
    conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "efrias002")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM base17 WHERE usuario = %s",[res])
    for item in cursor:
        list1.insert(END,item)
    conn.close()

def buscar2():
    res2 = busqueda2_text.get()
    conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "efrias002")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM base17 WHERE fecha = %s",[res2])
    for item in cursor:
        list1.insert(END,item)
    cursor.execute("SELECT COUNT(*) FROM base17 WHERE fecha = %s",[res2])
    for item in cursor:
        list2.insert(END,item)
    conn.close()

def buscar3():
    res3 = busqueda3_text.get()
    conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "efrias002")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM base17 WHERE aplicacion = %s",[res3])
    for item in cursor:
        list1.insert(END,item)
    conn.close()

    
def generar():
      conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "efrias002")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM base17")
      rows = cursor.fetchall()
      fp = open('file.csv', 'w')
      myFile = csv.writer(fp)
      myFile.writerows(rows)
      fp.close()
      conn.close()

def win2 ():
      t1 = Toplevel(bg="Brown")
      t1.title("Modificar Datos")
      t1.geometry('580x400')
      t1.focus_set()
      t1.grab_set()
      t1.transient(master=ventana)
      t1.resizable(width = FALSE, height = FALSE)
             
      
      lb1 = Label(t1,text='ID del Registro',bg="Cyan2")
      lb1.grid(row=5, column=1,padx=70,pady=10)
            
      inf2=StringVar()
      t2=Entry(t1,textvariable=inf2)
      t2.grid(row=6,column=1,pady=15)

      lb2 = Label(t1,text='Campo del Dato a Modificar',bg="Cyan2")
      lb2.grid(row=5, column=3,padx=25,pady=5)

      inf3=StringVar()
      t3=Entry(t1,textvariable=inf3)
      t3.grid(row=6,column=3,pady=15)

      lb3 = Label(t1,text='Dato a Modificar',bg="Cyan2")
      lb3.grid(row=11, column=2,padx=10,pady=10)

      inf4=StringVar()
      t4=Entry(t1,textvariable=inf4)
      t4.grid(row=12,column=2,pady=10)
      
      def cambiar():
             d1= inf2.get()
             d2= inf3.get()
             d3= inf4.get()
             conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "efrias002")
             cursor = conn.cursor()
             cursor.execute("UPDATE base17 SET %s='%s' WHERE ID='%s'" % (d2,d3,d1))
             conn.close()
           

      wb = Frame(t1, width = 15, height = 10)
      b1 = Button(wb, text = "Cerrar(X)", bg = "SkyBlue", command = t1.destroy)
      b1.pack()
      wb.grid(column = 1, row = 13, pady=85)

      wc = Frame(t1, width = 15, height = 10)
      b2 = Button(wc, text = "Enviar", bg = "Orange", command = cambiar)
      b2.pack()
      wc.grid(column = 2, row = 13, pady=35)

      





                  
      #def opt():
            #var1 = StringVar()
            #var1.set('Fecha')

            #opt1 = OptionMenu(t1, var1, 'Fecha', 'Usuario','Aplicacion','Folio Ticket','Status','Inputway').pack(fill=X)

      #wc = Frame(t1)
      #b2 = Button(wc, text = "Opciones", bg = "Light Gray", command = opt)
      #b2.pack()
      #wc.grid(column = 2, row = 4, pady=5)

      

            
      



      

    
         #menu desplegable


      top = t1.winfo_toplevel()
      t1.menuBar = Menu(top)
      top['menu'] = t1.menuBar

      t1.subMenu = Menu(t1.menuBar)
      t1.menuBar.add_cascade(label='File', menu=t1.subMenu)

      t1.subMenu2 = Menu(t1.menuBar)
      t1.menuBar.add_cascade(label='Edit', menu=t1.subMenu2)

      t1.subMenu2.add_command(label = "Delete")
      
      t1.subMenu.add_command(label = "New")
      t1.subMenu.add_command(label = "Close(X)", command = t1.destroy)

     

def win3():
        t1 = Toplevel(bg="Brown")
        t1.title("Busqueda por Usuario")
        t1.geometry('500x300')
        t1.focus_set()
        t1.grab_set()
        t1.transient(master=ventana)

      

        inf3=StringVar()
        t2=Entry(t1,textvariable=inf3)
        t2.grid(row=5,column=1,pady=10)

        t2l = Label(t1,text='Ingrese el dato que desea buscar',bg="Cyan2")
        t2l.grid(row=4, column=1,padx=10,pady=10, sticky = N)

        wb = Frame(t1, width = 15, height = 10)
        b1 = Button(wb, text = "Cerrar", bg = "SkyBlue", command = t1.destroy)
        b1.pack()
        wb.grid(column = 1, row = 8, pady = 10)

        wc = Frame(t1, width = 15, height = 10)
        b2 = Button(wc, text = "Buscar", bg = "Green", font="helvetica")
        b2.pack()
        wc.grid(column = 2, row = 5, pady = 40)

def win4():
        t1 = Toplevel(bg="Brown")
        t1.title("Informacion de Usuario")
        t1.geometry('800x450')
        t1.focus_set()
        t1.grab_set()
        t1.transient(master=ventana)

        def buscar4():
              res4 = inf4.get()
              conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "users")
              cursor = conn.cursor()
              cursor.execute("SELECT * FROM usuarios WHERE usuario = %s",[res4])
              for item in cursor:
                    lst.insert(END,item)
              conn.close()

        def mostrar3():
              conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "users")
              cursor = conn.cursor()
              cursor.execute("SELECT * FROM usuarios")
              data = cursor.fetchall()
              for item in data:
                    lst.insert(END,item)
              conn.close()
              
         
        def borrar2():
              lst.delete(0,END)

        inf4=StringVar()
        t2=Entry(t1,textvariable=inf4)
        t2.grid(row=1,column=1,pady=5)

        t2l = Label(t1,text='Ingrese el GUID del usuario',bg="Cyan2")
        t2l.grid(row=0, column=1,padx=10,pady=10, sticky = N)

        t3l = Label(t1,text='Informacion Encontrada',bg="Cyan2")
        t3l.grid(row=2, column=5,padx=10,pady=5, sticky = N)

        wb = Frame(t1, width = 15, height = 10)
        b1 = Button(wb, text = "Cerrar(X)", bg = "SkyBlue", command = t1.destroy)
        b1.pack()
        wb.grid(column = 1, row = 4)

        wc = Frame(t1, width = 20, height = 20)
        b2 = Button(wc, text = "Buscar", bg = "Green", font="helvetica", command = buscar4)
        b2.pack()
        wc.grid(column = 2, row = 1)

        wd = Frame(t1, width = 1, height = 1)
        b3 = Button(wd, text = "Limpiar Lista", bg = "Light Blue", font="helvetica", command = borrar2)
        b3.pack()
        wd.grid(column = 3, row = 2)

        we = Frame(t1)
        b4 = Button(we, text = "Mostrar Todo", bg = "Yellow", font="helvetica", command = mostrar3)
        b4.pack()
        we.grid(column = 3, row = 1)


        lst = Listbox(t1, width =55, height = 20)
        lst.grid(column = 5, row = 3,rowspan = 2, pady = 10, padx = 45)

        
def win5():
      eb = Toplevel(bg="brown")
      eb.geometry("500x350")
      eb.title("Nuevo Registro de Usuario")

      def insertar2():
            Id = int()
            e1 = es1.get()
            e2 = es2.get() 
            e3 = es3.get() 
            e4 = es4.get() 
            e5 = es5.get() 
      

            conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "users")
            cursor = conn.cursor()

            sql ='INSERT INTO usuarios VALUES("%s","%s", "%s", "%s", "%s", "%s")'%(Id, e1, e2, e3, e4, e5)

            try:
                cursor.execute(sql)
                conn.commit()
                conn.close()
                tkMessageBox.showinfo("Info","Usuario Agregado Correctamente")
          
            except:
                   conn.rollback()
                   conn.close()

      lb1 = Label(eb, text = "Usuario", bg = "cyan")
      lb1.pack
      lb1.grid(column = 1, row = 1, pady = 10)

      es1 = StringVar()
      esub = Entry(eb,textvariable = es1)
      esub.grid(column = 1, row = 2, padx = 5)

      lb2 = Label(eb, text = "Apellido Paterno", bg = "cyan")
      lb2.pack
      lb2.grid(column = 2, row = 1, pady = 10)

      es2 = StringVar()
      esub2 = Entry(eb,textvariable = es2)
      esub2.grid(column = 2, row = 2, padx = 5)

      lb3 = Label(eb, text = "Apellido Materno", bg = "cyan")
      lb3.pack
      lb3.grid(column = 3, row = 1, pady = 10)

      es3 = StringVar()
      esub3 = Entry(eb,textvariable = es3)
      esub3.grid(column = 3, row = 2, padx = 5)

      lb4 = Label(eb, text = "Nombre(s)", bg = "cyan")
      lb4.pack
      lb4.grid(column = 2, row = 3, pady = 10)

      es4 = StringVar()
      esub4 = Entry(eb,textvariable = es4)
      esub4.grid(column = 2, row = 4, padx = 5)

      lb5 = Label(eb, text = "Oficina", bg = "cyan")
      lb5.pack
      lb5.grid(column = 3, row = 3, pady = 10)

      es5 = StringVar()
      esub5 = Entry(eb,textvariable = es5)
      esub5.grid(column = 3, row = 4, padx = 5)

      bwin52 = Button(eb, text = "Guardar", bg = "SkyBlue", command = insertar2)
      bwin52.pack
      bwin52.grid(column = 2, row = 5, pady = 30 )
      
      bwin53 = Button(eb, text = "Cerrar(X)", bg = "Light Gray", command = eb.destroy)
      bwin53.pack
      bwin53.grid(column = 1, row = 6, pady = 30 )
      
      
        
def about():
     
      ab = Toplevel(bg="brown")
      ab.geometry("300x250")
      ab.title("Acerca de")

      pic = PhotoImage(file = "finn3.gif")
      wid = Label(ab,image = pic)
      wid.pack()
      wid.grid(row=1, column=2,rowspan=3)

def borrar():
    list1.delete(0,END)
    list2.delete(0,END)

def salir():
    ventana.destroy()


pic = PhotoImage(file = "pwc2.gif")
wid = Label(ventana,image = pic)
wid.pack()
wid.grid(row=1, column=11,rowspan=3)

#Menus

win = Menu(ventana)

menubar = Menu(win)
win.add_cascade(label = "Archivo", menu = menubar)
menubar.add_command(label = "Nueva Consulta")
menubar.add_command(label = "Exportar a CSV", command=salir)
menubar.add_command(label = "Agregar nuevo usuario", command = win5)
menubar.add_command(label = "Cerrar(x)", command=salir)


menubar2 = Menu(win)
win.add_cascade(label = "Edit", menu = menubar2)
menubar2.add_command(label="Modificar Registro", command=win2)
menubar2.add_command(label="Copiar")
menubar2.add_command(label="Seleccionar todo")

menubar3 = Menu(win)
win.add_cascade(label = "Buscar", menu = menubar3)
menubar3.add_command(label="Buscar Informacion de Usuario",command= win4)
menubar3.add_command(label="Buscar Registro por Usuario",command=win3)
menubar3.add_command(label="Buscar Registro por Fecha")
menubar3.add_command(label="Buscar Registro por Aplicacion")

menubar4 = Menu(win)
win.add_cascade(label = "Informacion", menu = menubar4)
menubar4.add_command(label="Acerca de", command=about)

ventana.title("Erick Finn's Reporter - GTS Soporte")
ventana.configure(background = "brown",menu=win)


#Etiquetas

l1=Label(ventana, fg= "Blue",bg="Orange",borderwidth = 5, relief = "ridge",text = "Fecha")
l1.grid(row=0,column=2, pady=10)

l2=Label(ventana,fg= "Blue",bg="Orange",borderwidth = 5,relief = "ridge",text = "Usuario")
l2.grid(row=0,column=3)

l3=Label(ventana, fg="Blue",bg="Orange",borderwidth = 5, relief = "ridge", text = "Aplicacion")
l3.grid(row=2,column=2)

l4=Label(ventana,fg = "Blue",bg="Orange",borderwidth = 5, relief = "ridge",text = "Folio Ticket")
l4.grid(row=2,column=3)

l5=Label(ventana,fg="Blue", bg="Orange",borderwidth = 5, relief = "ridge",text = "Status")
l5.grid(row=4,column=2)

l6=Label(ventana,fg = "Blue",bg="Orange",borderwidth = 5, relief = "ridge", text = "Input Way")
l6.grid(row=4,column=3)

l7=Label(ventana,font = "Comic",bg="DeepSkyBlue",borderwidth = 10, relief = "raised" ,text = "Resultados")
l7.grid(row=29,column=2,columnspan=3,pady=5)

l8=Label(ventana,fg = "Blue",bg="Orange",borderwidth = 5, relief = "ridge",text = "Busqueda por usuario")
l8.grid(row=0,column=4)

l9=Label(ventana,fg = "Blue",bg="Orange",borderwidth = 5,relief = "ridge", text = "Busqueda por fecha")
l9.grid(row=2,column=4)

l10=Label(ventana,fg = "Blue",bg="Orange",borderwidth = 5,relief = "ridge", text = "Busqueda por aplicacion")
l10.grid(row=4,column=4,pady=15)




#campos de entrada

fecha_text=StringVar()
e1=Entry(ventana,textvariable=fecha_text)
e1.grid(row=1,column=2)

usuario_text=StringVar()
e2=Entry(ventana,textvariable=usuario_text)
e2.grid(row=1,column=3)

aplicacion_text=StringVar()
e3=Entry(ventana,textvariable=aplicacion_text)
e3.grid(row=3,column=2)

folio_text=StringVar()
e4=Entry(ventana,textvariable=folio_text)
e4.grid(row=3,column=3)

status_text=StringVar()
e5=Entry(ventana,textvariable=status_text)
e5.grid(row=5,column=2)

inputway_text=StringVar()
e6=Entry(ventana,textvariable=inputway_text)
e6.grid(row=5,column=3)

busqueda_text=StringVar()
e7=Entry(ventana,textvariable=busqueda_text)
e7.grid(row=1,column=4)

busqueda2_text=StringVar()
e8=Entry(ventana,textvariable=busqueda2_text)
e8.grid(row=3,column=4)

busqueda3_text=StringVar()
e9=Entry(ventana,textvariable=busqueda3_text)
e9.grid(row=5,column=4)


#definir listbox

list1 = Listbox(ventana,bg = "white",height=10, width=90)
list1.grid(row=30, column=2, columnspan=4)

list2 = Listbox(ventana,bg="white",height=1,width=3)
list2.grid(row=29,column=4)


#crear scroll

sb1=Scrollbar(ventana)
sb1.grid(row=30,column=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


#crear botones

b1=Button(ventana, text="Crear nuevo registro",relief = "raised",borderwidth = 5,bg = "Light Green", command=insertar)
b1.pack()
b1.grid(row=24 ,column=11)

b2 = Button(ventana, text="Mostrar Registros",relief = "raised",borderwidth = 5,bg = "Orange", command=mostrar)
b2.pack()
b2.grid(row=25, column=11)

b3 = Button(ventana, text="Buscar por Usuario",relief = "raised",borderwidth = 5,bg = "Yellow", command=buscar)
b3.pack()
b3.grid(row=27, column=11)

b4 = Button(ventana, text="Limpiar Consulta",relief = "raised",borderwidth = 5,bg = "Light Blue", command=borrar)
b4.pack()
b4.grid(row=29, column=11)

b5 = Button(ventana, text="Salir de la App",relief = "raised",borderwidth = 5,bg = "Red",fg="Yellow", command=salir)
b5.pack()
b5.grid(row=31, column=0)

b6 = Button(ventana, text="Crear CSV",relief = "raised",borderwidth = 5,bg = "Light Gray", command=generar)
b6.pack()
b6.grid(row=30, column=11)

b7 = Button(ventana, text="Buscar por Fecha",relief = "raised",borderwidth = 5,bg = "SeaGreen1", command=buscar2)
b7.pack()
b7.grid(row=28, column=11)

b8 = Button(ventana,text="Buscar por App",relief = "raised",borderwidth = 5,bg="Cyan2", command=buscar3)
b8.pack()
b8.grid(row=26,column=11)






ventana.mainloop()
