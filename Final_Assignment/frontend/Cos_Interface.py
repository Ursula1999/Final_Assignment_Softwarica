from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from backend.dbconnection import *
from model.get_set import *

dbconnect = Curd()


class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Login Form')
        self.geometry('1500x800+200+100')
        self.configure(bg='white')

        self._frame = None
        self.switch_frame(Login)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
        # for frame1


class Login(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        self.window = window
        self.window.title('Login')
        self.background_1 = ImageTk.PhotoImage(file="Images/cover2.jpg")
        Label(self.window, image=self.background_1).grid()

        # for database
        self.dbconnect = Curd()
        # ===================== All login Images ===================#
        self.user_icon = PhotoImage(file="Images/user1.png")
        self.pass_icon = ImageTk.PhotoImage(file="Images/password1.png")
        # --------------------------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # frame for title
        self.rtx_frame = Frame(self.window, bg='light pink')
        self.rtx_frame.place(x=0, y=0, width=1510, height=130)

        Label(self.rtx_frame, text='BEAUTY', fg='#32405b', bd=1, relief=GROOVE, font=('Bell MT', 35, 'bold'),
              bg='light pink').place(x=650, y=15)
        Label(self.rtx_frame, text='Makeup     S T O R E', fg='#32405b', bd=1, relief=GROOVE,
              font=('Bell MT', 20, 'bold'),
              bg='light pink').place(x=625, y=80)

        # frame for lining
        self.lining_frame = Frame(self.window, width=10, height=600, bg='black')
        self.lining_frame.place(x=745, y=100)

        # frame for login
        self.login_frame = Frame(self.window, bg='light pink', bd=4, relief=GROOVE)
        self.login_frame.place(x=200, y=250)
        label_login = Label(self.login_frame, text='Log In', fg='grey', font=('Bell MT', 30, 'bold'),
                            bg='light pink').grid(
            row=1, column=0, padx=20, pady=20)

        label_user = Label(self.login_frame, text='Username', image=self.user_icon, bg='light pink',
                           font=('Arial', 15, 'bold'),
                           compound=LEFT).grid(row=3, column=0, padx=20, pady=10)

        label_pass = Label(self.login_frame, text='Password', image=self.pass_icon, bg='light pink',
                           font=('Arial', 15, 'bold'), compound=LEFT
                           ).grid(row=4, column=0, padx=20, pady=10)

        # -----------------------------------ENTRY--------------------------------------------------------------------------
        self.entry_username = Entry(self.login_frame, font=('Arial', 15), relief=GROOVE)
        self.entry_username.grid(row=3, column=1, padx=20)

        self.entry_password = Entry(self.login_frame, show='*', relief=GROOVE, font=('Arial', 15),
                                    )
        self.entry_password.grid(row=4, column=1, padx=20)

        # =====login & signup button=====#
        loginBtn = Button(self.login_frame, text='Log In', command=self.login, bg='pink', cursor="hand2",
                          font=('Arial', 10, 'bold'),
                          bd=1, padx=16).grid(row=5, column=1)
        SignupBtn = Button(self.login_frame, text='New user,Create Account', relief="flat", bg='light pink',
                           fg='royal blue',
                           cursor="hand2", font=('Arial', 10, 'bold', 'underline', 'italic'),
                           command=self.switch_registration,
                           bd=1, padx=16).grid(
            row=6, column=1, pady=8)

    def login(self):
        query = 'select *from tbl_registration'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        a = 0
        for i in range(len(data)):
            if self.entry_username.get() == data[i][0] and self.entry_password.get() == data[i][1]:
                a = 1
        if a == 1:
            messagebox.showinfo('congratulation', 'Successfully Logged In !')
            self.login_frame.destroy()
            self.window.switch_frame(Dashboard)
        elif self.entry_username.get().upper() == 'ADMIN' and self.entry_username.get() == 'admin':
            messagebox.showinfo('congratulation', 'Successfully Logged In !')
            self.lining_frame.destroy()
            self.login_frame.destroy()
            self.window.switch_frame(Dashboard)

        else:
            messagebox.showwarning('sorry', 'Wrong Username or Password !')
        # if a == 1:
        #     messagebox.showwarning('sorry', 'Wrong Username or Password !')

    def switch_registration(self):
        # self.login_frame.destroy()
        self.window.switch_frame(Registration)


class Registration(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.title('Registration')
        self.login_frame = Frame(self.window, bg='light pink')
        self.login_frame.place(x=200, y=200)

        self.dbcoonect = Curd()

        # ------------------------------------------label side----------------------------------------------------------
        label_login = Label(self.login_frame, text='Registration', fg='grey', bd=1, relief=GROOVE,
                            font=('Bell MT', 30, 'bold'),
                            bg='light pink').grid(
            row=0, columnspan=3, padx=20, pady=20)

        Label(self.login_frame, text="Username", bg='light pink', font=('arial', 15, 'bold')).grid(row=3, padx=30,
                                                                                                   pady=10,
                                                                                                   sticky=W)
        Label(self.login_frame, text="Email", bg='light pink', font=('arial', 15, 'bold')).grid(row=4, padx=30, pady=10,
                                                                                                sticky=W)
        Label(self.login_frame, text="Password", bg='light pink', font=('arial', 15, 'bold')).grid(row=5, padx=30,
                                                                                                   pady=10,
                                                                                                   sticky=W)
        Label(self.login_frame, text="Confirm Password", bg='light pink', font=('arial', 15, 'bold')).grid(row=6,
                                                                                                           padx=(20, 0),
                                                                                                           sticky=W,
                                                                                                           pady=10)
        # ------------------------------------------Entry side----------------------------------------------------------

        self.entry_username = Entry(self.login_frame, font=('arial', 15))
        self.entry_username.grid(row=3, column=1, padx=(20, 40))

        self.entryEmail = Entry(self.login_frame, font=('arial', 15))
        self.entryEmail.grid(row=4, column=1, padx=(20, 40))

        self.entryPassword = Entry(self.login_frame, show='*', font=('arial', 15))
        self.entryPassword.grid(row=5, column=1, padx=(20, 40))

        self.entryConfirm = Entry(self.login_frame, show='*', font=('arial', 15))
        self.entryConfirm.grid(row=6, column=1, padx=(0, 20))

        # ---------------------------------------BUTTON-----------------------------------------------------------------
        self.SignupBtn = Button(self.login_frame, text='Register',
                                cursor="hand2", font=('Arial', 10, 'bold'),
                                command=self.saveRegistration,
                                bd=1, padx=16, pady=10).grid(
            row=8, column=1, pady=16)
        self.loginBtn = Button(self.login_frame, text='Log In', command=self.switch_login, cursor="hand2",
                               font=('Arial', 10, 'bold'),
                               bd=1, padx=16, pady=10).grid(row=8, column=0, pady=16)

    def saveRegistration(self):
        if len(self.entry_username.get()) == 0 or len(self.entryPassword.get()) == 0 or len(
                self.entryConfirm.get()) == 0 or len(self.entryEmail.get()) == 0:
            messagebox.showerror('warning', 'Please complete the registration form')

        elif self.entryConfirm.get() != self.entryPassword.get():
            messagebox.showinfo('unequal', 'Password and confirm password did not matched')

        else:
            account_ref = SaveRegistration(self.entry_username.get(), self.entryEmail.get())
            query = 'insert into tbl_registration (username,email, u_password) values(%s,%s,%s)'
            values = (account_ref.get_username(), account_ref.get_email(), account_ref.get_password())
            self.dbcoonect.add_data(query, values)
            messagebox.showinfo('Success', 'Account Created!')
            messagebox.showinfo('congratulation', 'Successfully Logged In !')
            self.login_frame.destroy()
            self.window.switch_frame(Login)

    def switch_login(self):
        self.login_frame.destroy()
        self.window.switch_frame(Login)


class Dashboard(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen
        self.screen.configure(bg='white')
        self.dbconnect = Curd()
        self.setup_frame = Frame(self.screen, bg='white')
        self.setup_frame.place(x=0, y=0, width=1500, height=800)
        # -------------------photos-------------------
        self.photo1 = ImageTk.PhotoImage(file='Images/men/1.jpg')
        self.photo2 = ImageTk.PhotoImage(file="Images/men/2.jpg")
        self.photo3 = ImageTk.PhotoImage(file="Images/men/3.JPG")
        self.photo4 = ImageTk.PhotoImage(file="Images/women/1.JPG")
        self.photo5 = ImageTk.PhotoImage(file="Images/women/2.JPG")
        self.photo6 = ImageTk.PhotoImage(file="Images/women/3.JPG")
        self.photo7 = ImageTk.PhotoImage(file="Images/brand.png")
        # --------------------------------------------

        self.header_frame = Frame(self.screen, bg='light pink', width=1500, height=35)
        self.header_frame.place(x=0, y=0)
        Label(self.header_frame, text='Welcome', fg='white', font=('Bell MT', 15, 'bold'), bg='light pink').place(x=100,
                                                                                                                  y=2)
        Label(self.header_frame, text='BEAUTY     MAKEUP STORE', fg='white', font=('Bell MT', 15, 'bold'),
              bg='light pink').place(x=300, y=2)
        Label(self.header_frame, text='Contact No.: 0908765', fg='white', font=('Bell MT', 15, 'bold'),
              bg='light pink').place(x=1300, y=2)

        self.searching_frame = Frame(self.screen, width=1500, height=80, bg='white')
        self.searching_frame.place(x=0, y=35)

        # searching
        def click_event_username(event):  # function for click event to remove the default value on clicking
            self.search_entry.delete(0, END)
            self.search_entry.config(fg='Black')

        self.search_entry = Entry(self.searching_frame, width=30, bg='white', font=('arial', 20), fg='light grey')
        self.search_entry.insert(0, '@Product name....')
        self.search_entry.place(x=150, y=18)
        self.search_entry.bind('<Button-1>', click_event_username)

        self.btn_search = Button(self.searching_frame, text='Search', command=self.search_data, width=10, bg='black',
                                 fg='white',
                                 font=('arial', 15), height=1).place(x=600, y=15)

        self.cart_img = ImageTk.PhotoImage(file='Images/mycart.jpg')
        Label(self.searching_frame, image=self.cart_img).place(x=1200, y=12)

        self.btn_mycard = Button(self.searching_frame, command=self.order, text='MY CART', bg='black', fg='white',
                                 font=('Bell MT', 20, 'bold')).place(x=1250, y=12)
        # ---------------------------------------------------------------------------------------------------------------------
        self.menu_frame = Frame(self.screen, width=1500, height=40, bg='#bf663a')
        self.menu_frame.place(x=0, y=115, width=1500)
        Label(self.menu_frame).grid(padx=15, pady=2)
        Button(self.menu_frame, text='Women', relief='flat', command=self.women, cursor='hand2', fg='white',
               font=('Bell MT', 15, 'bold'),
               bg='#bf663a').grid(row=0, column=1, padx=5)
        Button(self.menu_frame, text='Men', relief='flat', command=self.men, cursor='hand2', fg='white',
               font=('Bell MT', 15, 'bold'),
               bg='#bf663a').grid(row=0, column=2, padx=5)
        Button(self.menu_frame, text='Brands', relief='flat', command=self.brand, cursor='hand2', fg='white',
               font=('Bell MT', 15, 'bold'),
               bg='#bf663a').grid(row=0, column=3, padx=5)
        # Button(self.menu_frame, text='Customer Service', relief='flat', cursor='hand2',fg='#6f7b76', font=('Bell MT', 15, 'bold'),
        #        bg='#f4f4f4').grid(row=0, column=4,padx=5)
        Button(self.menu_frame, text='LogOut', relief='flat', command=self.logout, cursor='hand2', fg='white',
               font=('Bell MT', 15, 'bold'),
               bg='#bf663a').grid(row=0, column=5, padx=5)
        # -----------------------------------------------------------------------------------------------------
        self.hoz_frame = Frame(self.setup_frame, bg='white')
        self.hoz_frame.place(x=20, y=200)

        self.mens_size = ImageTk.PhotoImage(file='Images/side1.JPG')
        self.womens_size = ImageTk.PhotoImage(file='Images/side2.JPG')

        Label(self.hoz_frame, image=self.womens_size).grid(row=0, column=0)
        Label(self.hoz_frame, image=self.mens_size).grid(row=1, column=0, pady=15)

        self.border_frame = Frame(self.setup_frame, bg='#6f7b76', width=10, height=500)
        self.border_frame.place(x=250, y=200)

        #    -----------------------------------------
        self.product_frame = Frame(self.setup_frame, bd=0, relief=RIDGE, bg='white')
        self.product_frame.place(x=270, y=220, width=1200, height=570)
        # --------------------------------------------------------------------------------------------------------------------
        self.shoes1 = Button(self.product_frame, image=self.photo1, compound=BOTTOM, width=200, height=250,

                             command=self.product1)
        self.shoes1.grid(row=1, column=0, padx=70)
        query = 'select *from product where product_id =' + str(1)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows[0][1])
        Label(self.product_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
        Label(self.product_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
        Label(self.product_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        # -------------------------------------------------------------------------------------------------------------------
        self.shoes2 = Button(self.product_frame, image=self.photo4, compound=BOTTOM, width=200, height=250,

                             command=self.product2)
        self.shoes2.grid(row=1, column=1, pady=4, padx=70)
        query = 'select *from product where product_id =' + str(4)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows[0][1])
        Label(self.product_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=2, column=1, pady=4)
        Label(self.product_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=3, column=1, pady=4)
        Label(self.product_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=4, column=1, pady=4)
        # ----------------------------------------------------------------------------------------------------------------------
        self.shoes3 = Button(self.product_frame, image=self.photo7, compound=BOTTOM, width=200, height=250,

                             command=self.product3)
        self.shoes3.grid(row=1, column=2, padx=70)

        query = 'select * from product where product_id =' + str(5)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows[0][1])
        Label(self.product_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=2, column=2, pady=4)
        Label(self.product_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=3, column=2, pady=4)
        Label(self.product_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=4, column=2, pady=4)

    # ------------------------------------------------
    def search_data(self):
        query = 'select *from product;'
        rows = self.dbconnect.fetch_data(query)
        data = self.search_method_function(rows, self.search_entry.get())
        self.product_frame = Frame(self.screen, bd=0, relief=RIDGE, bg='white')
        self.product_frame.place(x=270, y=270, width=1000, height=570)
        # --------------------------------------------------------------------------------------------------------------------
        self.photo()
        print(rows)

    def order(self):
        self.product_frame.destroy()
        self.screen.switch_frame(OrderDetails)

    def men(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Dashboard)
        self.screen.switch_frame(Men)

    def women(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Women)

    def logout(self):
        self.product_frame.destroy()
        self.screen.quit()

    def photo(self):
        query = 'select *from product'
        row = self.dbconnect.fetch_data(query)
        a = self.search_entry.get()
        print(row)
        data = self.search_method_function(row, a)
        print(data)
        print(a)
        if int(data[0][0]) == int(1):
            self.shoes = Button(self.product_frame, image=self.photo1, compound=BOTTOM, width=200, height=250,

                                command=self.shoes1)
            self.shoes.grid(row=1, column=0, padx=30)
            Label(self.product_frame, text=data[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
            Label(self.product_frame, text=data[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
            Label(self.product_frame, text=data[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        elif str(data[0][0]) == str(2):
            self.shoes = Button(self.product_frame, image=self.photo2, compound=BOTTOM, width=200, height=250,

                                command=self.shoes2)
            self.shoes.grid(row=1, column=0, padx=30)
            Label(self.product_frame, text=data[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
            Label(self.product_frame, text=data[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
            Label(self.product_frame, text=data[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        elif str(data[0][0]) == str(3):
            self.shoes = Button(self.product_frame, image=self.photo3, compound=BOTTOM, width=200, height=250,

                                command=self.shoes3)
            self.shoes.grid(row=1, column=0, padx=30)
            Label(self.product_frame, text=data[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
            Label(self.product_frame, text=data[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
            Label(self.product_frame, text=data[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        elif str(data[0][0]) == str(4):
            self.shoes = Button(self.product_frame, image=self.photo4, compound=BOTTOM, width=200, height=250,

                                command=self.product4)
            self.shoes.grid(row=1, column=0, padx=30)
            Label(self.product_frame, text=data[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
            Label(self.product_frame, text=data[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
            Label(self.product_frame, text=data[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        elif str(data[0][0]) == str(5):
            self.shoes = Button(self.product_frame, image=self.photo5, compound=BOTTOM, width=200, height=250,

                                command=self.product5)
            self.shoes.grid(row=1, column=0, padx=30)
            Label(self.product_frame, text=data[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
            Label(self.product_frame, text=data[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
            Label(self.product_frame, text=data[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        elif str(data[0][0]) == str(6):
            self.shoes = Button(self.product_frame, image=self.photo6, compound=BOTTOM, width=200, height=250,

                                command=self.product6)
            self.shoes.grid(row=1, column=0, padx=30)
            Label(self.product_frame, text=data[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
            Label(self.product_frame, text=data[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
            Label(self.product_frame, text=data[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)

    @classmethod
    def search_method_function(cls, data, b):
        rows = []
        for i in range(len(data)):
            if str(data[i][1]) == b:
                rows.append(data[i])
                return rows
        return rows

    def product1(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product1)

    def product2(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product2)

    def product3(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product3)

    def product4(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product4)

    def product5(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product5)

    def product6(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product6)

    def brand(self):
        pass


class Men(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen
        self.dbconnect = Curd()

        self.photo1 = ImageTk.PhotoImage(file='Images/men/1.jpg')
        self.photo2 = ImageTk.PhotoImage(file="Images/men/2.jpg")
        self.photo3 = ImageTk.PhotoImage(file="Images/men/3.JPG")

        self.product_frame = Frame(self.screen, bd=0, relief=RIDGE, bg='white')
        self.product_frame.place(x=270, y=270, width=1200, height=570)
        # --------------------------------------------------------------------------------------------------------------------
        self.shoes1 = Button(self.product_frame, image=self.photo1, compound=BOTTOM, width=200, height=250,

                             command=self.product1)
        self.shoes1.grid(row=1, column=0, padx=70)
        query = 'select *from product where product_id =' + str(1)
        self.rows = self.dbconnect.fetch_data(query)
        # self.data = [item for t in self.rows for item in t]
        Label(self.product_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
        Label(self.product_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
        Label(self.product_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        # -------------------------------------------------------------------------------------------------------------------
        self.shoes2 = Button(self.product_frame, image=self.photo2, compound=BOTTOM, width=200, height=250,

                             command=self.product2)
        self.shoes2.grid(row=1, column=1, pady=4, padx=70)
        query = 'select *from product where product_id =' + str(2)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows[0][1])
        Label(self.product_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=2, column=1, pady=4)
        Label(self.product_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=3, column=1, pady=4)
        Label(self.product_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=4, column=1, pady=4)
        # ----------------------------------------------------------------------------------------------------------------------
        self.shoes3 = Button(self.product_frame, image=self.photo3, compound=BOTTOM, width=200, height=250,

                             command=self.product3)
        self.shoes3.grid(row=1, column=2, padx=70)

        query = 'select *from product where product_id =' + str(3)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows[0][1])
        Label(self.product_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=2, column=2, pady=4)
        Label(self.product_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=3, column=2, pady=4)
        Label(self.product_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=4, column=2, pady=4)

    def search_data(self):
        pass

    def product1(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product1)

    def product2(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product2)

    def product3(self):
        self.product_frame.destroy()
        self.screen.switch_frame(Product3)


class Women(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen
        self.dbconnect = Curd()

        self.photo1 = ImageTk.PhotoImage(file='Images/women/1.jpg')
        self.photo2 = ImageTk.PhotoImage(file="Images/women/2.jpg")
        self.photo3 = ImageTk.PhotoImage(file="Images/women/3.JPG")

        self.shoes_frame = Frame(self.screen, bd=0, relief=RIDGE, bg='white')
        self.shoes_frame.place(x=270, y=270, width=1200, height=570)
        # --------------------------------------------------------------------------------------------------------------------
        self.shoes1 = Button(self.shoes_frame, image=self.photo1, compound=BOTTOM, width=200, height=250,

                             command=self.product1)
        self.shoes1.grid(row=1, column=0, padx=70)
        query = 'select * from product where product_id =' + str(4)
        self.rows = self.dbconnect.fetch_data(query)

        Label(self.shoes_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(row=2)
        Label(self.shoes_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(row=3)
        Label(self.shoes_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(row=4)
        # -------------------------------------------------------------------------------------------------------------------
        self.shoes2 = Button(self.shoes_frame, image=self.photo2, compound=BOTTOM, width=200, height=250,

                             command=self.product2)
        self.shoes2.grid(row=1, column=1, pady=4, padx=70)
        query = 'select * from product where product_id =' + str(5)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows[0][1])
        Label(self.shoes_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=2, column=1, pady=4)
        Label(self.shoes_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=3, column=1, pady=4)
        Label(self.shoes_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=4, column=1, pady=4)
        # ----------------------------------------------------------------------------------------------------------------------
        self.shoes3 = Button(self.shoes_frame, image=self.photo3, compound=BOTTOM, width=200, height=250,

                             command=self.product3)
        self.shoes3.grid(row=1, column=2, padx=70)

        query = 'select * from product where product_id =' + str(6)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows[0][1])
        Label(self.shoes_frame, text=self.rows[0][1], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=2, column=2, pady=4)
        Label(self.shoes_frame, text=self.rows[0][2], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=3, column=2, pady=4)
        Label(self.shoes_frame, text=self.rows[0][3], font=('Bell MT', 15, 'bold'), bg='white').grid(
            row=4, column=2, pady=4)

    def search_data(self):
        pass

    def product1(self):
        self.shoes_frame.destroy()
        self.screen.switch_frame(Product4)

    def product2(self):
        self.shoes_frame.destroy()
        self.screen.switch_frame(Product5)

    def product3(self):
        self.shoes_frame.destroy()
        self.screen.switch_frame(Product6)


class OrderDetails(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen

        # set database
        self.dbconnect = Curd()

        detail_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        detail_frame.place(x=300, y=220, width=1000, height=150)
        # ---------------------------search_methon---------------------------------
        self.search_method = Label(detail_frame, text='Search by ', font=('times new roman', 20, 'bold'),
                                   bg='white')
        self.search_method.grid(row=0, column=0, pady=10, padx=20, sticky='w')
        self.combo_search = ttk.Combobox(detail_frame, font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.combo_search['values'] = ('product_name', 'brand')
        self.combo_search.grid(row=0, column=1, sticky='w', pady=10, padx=20)

        self.entry_search = Entry(detail_frame, font=('times new roman', 15))
        self.entry_search.grid(row=0, column=2, sticky='w', pady=10, padx=20)

        sort_method = Label(detail_frame, text='Sort by ', font=('times new roman', 20, 'bold'), bg='white',
                            )
        sort_method.grid(row=1, column=0, pady=10, padx=20, sticky='w')
        self.combo_sort = ttk.Combobox(detail_frame,
                                       font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.combo_sort['values'] = ('product_name', 'brand')
        self.combo_sort.grid(row=1, column=1, sticky='w', pady=10, padx=20)
        sort_btn = Button(detail_frame, text='Sort', command=self.sorting, width=10,
                          font=('times new roman', 15, 'bold'))
        sort_btn.grid(row=1, column=2, padx=20, pady=10, sticky='w')

        show_btn = Button(detail_frame, command=self.search_data, text='Search', width=10,
                          font=('times new roman', 15, 'bold'))
        show_btn.grid(row=0, column=3, padx=20, pady=10, sticky='w')
        AllShow_btn = Button(detail_frame, text='Show All', width=15, font=('times new roman', 15, 'bold'))
        AllShow_btn.grid(row=0, column=4, padx=20, pady=10, sticky='w')

        self.table_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        self.table_frame.place(x=300, y=360, width=1000, height=300)

        scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.shoes_table = ttk.Treeview(self.table_frame, columns=(
            'product_name', 'brand', 'quantity', 'price', 'payment_method'),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.shoes_table.xview)
        scroll_y.config(command=self.shoes_table.yview)
        self.shoes_table.heading('product_name', text='Product Name')
        self.shoes_table.heading('brand', text='Brand')
        self.shoes_table.heading('quantity', text='Quantity')
        self.shoes_table.heading('price', text='Amount')
        self.shoes_table.heading('payment_method', text='Payment Method')
        self.shoes_table['show'] = 'headings'
        self.shoes_table.column('quantity', width=60)
        self.shoes_table.column('price', width=60)

        self.shoes_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        # self.movies_table.bind("<ButtonRelease-1>", self.get_cursor)

    def fetch_data(self):
        query = 'select product_name, brand, quantity, amount, payment_method from' \
                ' product as s, tbl_order as b where s.product_id = b.product_id ;'
        rows = self.dbconnect.fetch_data(query)
        if len(rows) != 0:
            self.shoes_table.delete(*self.shoes_table.get_children())
            for row in rows:
                self.shoes_table.insert('', END, values=row)
                self.dbconnect.connection.commit()

    def search_data(self):
        query = 'select product_name, brand, quantity, amount, payment_method from' \
                ' product as s, tbl_order as b where s.product_id = b.product_id ;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        a = self.combo_search.get()
        b = self.entry_search.get()

        if a == 'product_name':
            rows = Main.search_method_function(data, 0, b)
            if len(rows) != 0:
                self.shoes_table.delete(*self.shoes_table.get_children())
                for row in rows:
                    self.shoes_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()

        elif a == 'brand':
            rows = Main.search_method_function(data, 1, b)
            if len(rows) != 0:
                self.shoes_table.delete(*self.shoes_table.get_children())
                for row in rows:
                    self.shoes_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()
        else:
            rows = Main.search_method_function(data, 2, b)
            if len(rows) != 0:
                self.shoes_table.delete(*self.shoes_table.get_children())
                for row in rows:
                    self.shoes_table.insert('', END, values=row)
                    self.dbconnect.connection.commit()

    def sorting(self):
        query = 'select product_name, brand, quantity, amount, payment_method from' \
                ' tbl_shoes as s, tbl_order as b where s.shoes_id = b.shoes_id ;'
        self.dbconnect.fetch_data(query)
        data = self.dbconnect.rows
        sort_by = self.combo_sort.get()

        if sort_by == 'shoes_name':
            OrderDetails.sort_method(data, 0)
            rows = data
            if len(rows) != 0:
                self.shoes_table.delete(*self.shoes_table.get_children())
                for row in rows:
                    self.shoes_table.insert('', END, values=row)

        if sort_by == 'brand':
            OrderDetails.sort_method(data, 1)
            rows = data
            if len(rows) != 0:
                self.shoes_table.delete(*self.shoes_table.get_children())
                for row in rows:
                    self.shoes_table.insert('', END, values=row)

    @classmethod
    def sort_method(cls, data, index):
        swap = True
        while swap:
            swap = False
            for i in range(len(data) - 1):
                if data[i][index] > data[i + 1][index]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swap = True
        return data


class Product1(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen

        # set database
        self.dbconnect = Curd()
        image1 = ImageTk.PhotoImage(file='Images/men/1.jpg')
        self.order()
        # heading

    def order(self):
        # self.search_frame = Frame(self.screen, width=900, height=600).place(x=50,y=220)
        self.detail_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        self.detail_frame.place(x=250, y=220, width=1250, height=550)
        self.image_frame = Frame(self.detail_frame, width=200, height=250)
        self.image_frame.place(x=0, y=0)
        self.image1 = ImageTk.PhotoImage(file='Images/men/1.jpg')
        Label(self.image_frame, image=self.image1).place(x=0, y=0)

        self.detail_frame1 = Frame(self.detail_frame, bg='white', width=1200, height=80, bd=4, relief=GROOVE)
        self.detail_frame1.place(x=230, y=4)
        Label(self.detail_frame1, text='Shoes Name :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=0, column=1,
                                                                                                      padx=10, pady=4)
        Label(self.detail_frame1, text='Brand :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=1, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Price :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=2, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Available Size :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=3,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=4)
        Label(self.detail_frame1, text='Details :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=4, column=1,
                                                                                                   padx=10, pady=4)

        query = 'select *from product where product_id =' + str(1)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows)
        Label(self.detail_frame1, text=self.rows[0][1], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=0, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][2], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=1, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][3], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=2, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][5], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=3, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][6], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=4, column=2, padx=10, pady=4)

        # ---------------------------------------------order-----------------------------------------------------------------------------
        self.booking_frame = Frame(self.detail_frame, width=800, bd=4, relief=GROOVE, bg='white', height=350)
        self.booking_frame.place(x=50, y=250, width=800, height=250)
        self.booking_head = Label(self.booking_frame, bd=4, relief=GROOVE, text='Order Now',
                                  font=('Bell MT', 20, 'bold'), bg='white')
        self.booking_head.place(x=0, y=0, relwidth=1)

        self.lbl_qty = Label(self.booking_frame, text='Quantity', font=('Bell MT', 20, 'bold'),
                             bg='white').grid(row=0, column=0, padx=(20, 10), pady=(50, 4))
        self.entry_qty = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_qty.grid(row=0, column=1, padx=10, pady=(50, 4))

        self.lbl_price = Label(self.booking_frame, text='Price', font=('Bell MT', 20, 'bold'),
                               bg='white').grid(row=1, column=0, padx=10)
        self.entry_price = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_price.grid(row=1, column=1, padx=10)

        self.lbl_contact = Label(self.booking_frame, bg='white', text='Contact No.',
                                 font=('Bell MT', 20, 'bold'),
                                 ).grid(row=2, column=0)
        self.entry_contact = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_contact.grid(row=2, column=1)

        self.lbl_Payment = Label(self.booking_frame, text='Payment Method', bg='white',
                                 font=('Bell MT', 20, 'bold'),
                                 )
        self.lbl_Payment.grid(row=3, column=0)
        self.tbl_Payment = ttk.Combobox(self.booking_frame,
                                        font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.tbl_Payment['values'] = ('Esewa', 'Khalti', 'Phone Pay', 'Case on delivery')
        self.tbl_Payment.grid(row=3, column=1)

        # ====================btn=================================
        self.btn_bookNow = Button(self.booking_frame, command=self.order1, text='Order',
                                  font=('Bell MT', 20, 'bold'))
        self.btn_bookNow.grid(rowspan=4, column=2)

    def order1(self):
        if len(self.entry_qty.get()) != 0 and len(self.entry_price.get()) != 0 and len(
                self.entry_contact.get()) != 0 and len(self.tbl_Payment.get()) != 0:
            query = 'Insert into tbl_order (quantity, price, contact, payment_method, shoes_id) values (%s,%s,%s,%s,%s)'
            values = (
                self.entry_qty.get(), self.entry_price.get(), self.entry_contact.get(), self.tbl_Payment.get(), 1)
            self.dbconnect.add_data(query, values)
            messagebox.showinfo('Success', 'Order Registered')

        else:
            messagebox.showinfo('Incomplete', 'Complete it')


class Product2(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen

        # set database
        self.dbconnect = Curd()
        image1 = ImageTk.PhotoImage(file='Images/men/1r.jpg')
        self.order()

    def order(self):
        # self.search_frame = Frame(self.screen, width=900, height=600).place(x=50,y=220)
        self.detail_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        self.detail_frame.place(x=250, y=220, width=1250, height=550)
        self.image_frame = Frame(self.detail_frame, width=200, height=250)
        self.image_frame.place(x=0, y=0)
        self.image1 = ImageTk.PhotoImage(file='Images/men/2.jpg')
        Label(self.image_frame, image=self.image1).place(x=0, y=0)

        self.detail_frame1 = Frame(self.detail_frame, bg='white', width=1200, height=80, bd=4, relief=GROOVE)
        self.detail_frame1.place(x=230, y=4)
        Label(self.detail_frame1, text='Shoes Name :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=0, column=1,
                                                                                                      padx=10, pady=4)
        Label(self.detail_frame1, text='Brand :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=1, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Price :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=2, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Available Size :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=3,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=4)
        Label(self.detail_frame1, text='Details :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=4, column=1,
                                                                                                   padx=10, pady=4)

        query = 'select *from product where product_id =' + str(2)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows)
        Label(self.detail_frame1, text=self.rows[0][1], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=0, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][2], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=1, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][3], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=2, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][5], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=3, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][6], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=4, column=2, padx=10, pady=4)

        # ---------------------------------------------order-----------------------------------------------------------------------------
        self.booking_frame = Frame(self.detail_frame, width=800, bd=4, relief=GROOVE, bg='white', height=350)
        self.booking_frame.place(x=50, y=250, width=800, height=250)
        self.booking_head = Label(self.booking_frame, bd=4, relief=GROOVE, text='Order Now',
                                  font=('Bell MT', 20, 'bold'), bg='white')
        self.booking_head.place(x=0, y=0, relwidth=1)

        self.lbl_qty = Label(self.booking_frame, text='Quantity', font=('Bell MT', 20, 'bold'),
                             bg='white').grid(row=0, column=0, padx=(20, 10), pady=(50, 4))
        self.entry_qty = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_qty.grid(row=0, column=1, padx=10, pady=(50, 4))

        self.lbl_price = Label(self.booking_frame, text='Price', font=('Bell MT', 20, 'bold'),
                               bg='white').grid(row=1, column=0, padx=10)
        self.entry_price = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_price.grid(row=1, column=1, padx=10)

        self.lbl_contact = Label(self.booking_frame, bg='white', text='Contact No.',
                                 font=('Bell MT', 20, 'bold'),
                                 ).grid(row=2, column=0)
        self.entry_contact = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_contact.grid(row=2, column=1)

        self.lbl_Payment = Label(self.booking_frame, text='Payment Method', bg='white',
                                 font=('Bell MT', 20, 'bold'),
                                 )
        self.lbl_Payment.grid(row=3, column=0)
        self.tbl_Payment = ttk.Combobox(self.booking_frame,
                                        font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.tbl_Payment['values'] = ('Esewa', 'Khalti', 'Phone Pay', 'Case on delivery')
        self.tbl_Payment.grid(row=3, column=1)

        # ====================btn=================================
        self.btn_bookNow = Button(self.booking_frame, command=self.order1, text='Order',
                                  font=('Bell MT', 20, 'bold'))
        self.btn_bookNow.grid(rowspan=4, column=2)

    def order1(self):
        if len(self.entry_qty.get()) != 0 and len(self.entry_price.get()) != 0 and len(
                self.entry_contact.get()) != 0 and len(self.tbl_Payment.get()) != 0:
            query = 'Insert into tbl_order (quantity, amount, contact, payment_method, shoes_id) values (%s,%s,%s,%s,%s)'
            values = (
                self.entry_qty.get(), self.entry_price.get(), self.entry_contact.get(), self.tbl_Payment.get(), 2)
            self.dbconnect.add_data(query, values)
            messagebox.showinfo('Success', 'Order Registered')

        else:
            messagebox.showinfo('Incomplete', 'Complete it')


class Product3(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen

        # set database
        self.dbconnect = Curd()
        self.order()

    def order(self):

        self.detail_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        self.detail_frame.place(x=250, y=220, width=1250, height=550)
        self.image_frame = Frame(self.detail_frame, width=200, height=250)
        self.image_frame.place(x=0, y=0)
        self.image1 = ImageTk.PhotoImage(file='Images/men/3.jpg')
        Label(self.image_frame, image=self.image1).place(x=0, y=0)

        self.detail_frame1 = Frame(self.detail_frame, bg='white', width=1200, height=80, bd=4, relief=GROOVE)
        self.detail_frame1.place(x=230, y=4)
        Label(self.detail_frame1, text='Shoes Name :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=0, column=1,
                                                                                                      padx=10, pady=4)
        Label(self.detail_frame1, text='Brand :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=1, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Price :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=2, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Available Size :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=3,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=4)
        Label(self.detail_frame1, text='Details :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=4, column=1,
                                                                                                   padx=10, pady=4)

        query = 'select *from tbl_shoes where shoes_id =' + str(3)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows)
        Label(self.detail_frame1, text=self.rows[0][1], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=0, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][2], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=1, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][3], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=2, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][5], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=3, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][6], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=4, column=2, padx=10, pady=4)

        # ---------------------------------------------order-----------------------------------------------------------------------------
        self.booking_frame = Frame(self.detail_frame, width=800, bd=4, relief=GROOVE, bg='white', height=350)
        self.booking_frame.place(x=50, y=250, width=800, height=250)
        self.booking_head = Label(self.booking_frame, bd=4, relief=GROOVE, text='Order Now',
                                  font=('Bell MT', 20, 'bold'), bg='white')
        self.booking_head.place(x=0, y=0, relwidth=1)

        self.lbl_qty = Label(self.booking_frame, text='Quantity', font=('Bell MT', 20, 'bold'),
                             bg='white').grid(row=0, column=0, padx=(20, 10), pady=(50, 4))
        self.entry_qty = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_qty.grid(row=0, column=1, padx=10, pady=(50, 4))

        self.lbl_price = Label(self.booking_frame, text='Price', font=('Bell MT', 20, 'bold'),
                               bg='white').grid(row=1, column=0, padx=10)
        self.entry_price = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_price.grid(row=1, column=1, padx=10)

        self.lbl_contact = Label(self.booking_frame, bg='white', text='Contact No.',
                                 font=('Bell MT', 20, 'bold'),
                                 ).grid(row=2, column=0)
        self.entry_contact = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_contact.grid(row=2, column=1)

        self.lbl_Payment = Label(self.booking_frame, text='Payment Method', bg='white',
                                 font=('Bell MT', 20, 'bold'),
                                 )
        self.lbl_Payment.grid(row=3, column=0)
        self.tbl_Payment = ttk.Combobox(self.booking_frame,
                                        font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.tbl_Payment['values'] = ('Esewa', 'Khalti', 'Phone Pay', 'Case on delivery')
        self.tbl_Payment.grid(row=3, column=1)

        # ====================btn=================================
        self.btn_bookNow = Button(self.booking_frame, command=self.order1, text='Order',
                                  font=('Bell MT', 20, 'bold'))
        self.btn_bookNow.grid(rowspan=4, column=2)

    def order1(self):
        if len(self.entry_qty.get()) != 0 and len(self.entry_price.get()) != 0 and len(
                self.entry_contact.get()) != 0 and len(self.tbl_Payment.get()) != 0:
            query = 'Insert into tbl_order (quantity, price, contact, payment_method, shoes_id) values (%s,%s,%s,%s,%s)'
            values = (
                self.entry_qty.get(), self.entry_price.get(), self.entry_contact.get(), self.tbl_Payment.get(), 3)
            self.dbconnect.add_data(query, values)
            messagebox.showinfo('Success', 'Order Registered')

        else:
            messagebox.showinfo('Incomplete', 'Complete it')


class Product4(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen

        # set database
        self.dbconnect = Curd()
        self.order()

    def order(self):
        # self.search_frame = Frame(self.screen, width=900, height=600).place(x=50,y=220)
        self.detail_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        self.detail_frame.place(x=250, y=220, width=1250, height=550)
        self.image_frame = Frame(self.detail_frame, width=200, height=250)
        self.image_frame.place(x=0, y=0)
        self.image1 = ImageTk.PhotoImage(file='Images/women/1r.jpg')
        Label(self.image_frame, image=self.image1).place(x=0, y=0)

        self.detail_frame1 = Frame(self.detail_frame, bg='white', width=1200, height=80, bd=4, relief=GROOVE)
        self.detail_frame1.place(x=230, y=4)
        Label(self.detail_frame1, text='Shoes Name :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=0, column=1,
                                                                                                      padx=10, pady=4)
        Label(self.detail_frame1, text='Brand :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=1, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Price :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=2, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Available Size :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=3,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=4)
        Label(self.detail_frame1, text='Details :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=4, column=1,
                                                                                                   padx=10, pady=4)

        query = 'select *from product where product_id =' + str(4)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows)
        Label(self.detail_frame1, text=self.rows[0][1], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=0, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][2], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=1, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][3], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=2, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][5], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=3, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][6], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=4, column=2, padx=10, pady=4)

        # ---------------------------------------------order-----------------------------------------------------------------------------
        self.booking_frame = Frame(self.detail_frame, width=800, bd=4, relief=GROOVE, bg='white', height=350)
        self.booking_frame.place(x=50, y=250, width=800, height=250)
        self.booking_head = Label(self.booking_frame, bd=4, relief=GROOVE, text='Order Now',
                                  font=('Bell MT', 20, 'bold'), bg='white')
        self.booking_head.place(x=0, y=0, relwidth=1)

        self.lbl_qty = Label(self.booking_frame, text='Quantity', font=('Bell MT', 20, 'bold'),
                             bg='white').grid(row=0, column=0, padx=(20, 10), pady=(50, 4))
        self.entry_qty = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_qty.grid(row=0, column=1, padx=10, pady=(50, 4))

        self.lbl_price = Label(self.booking_frame, text='Price', font=('Bell MT', 20, 'bold'),
                               bg='white').grid(row=1, column=0, padx=10)
        self.entry_price = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_price.grid(row=1, column=1, padx=10)

        self.lbl_contact = Label(self.booking_frame, bg='white', text='Contact No.',
                                 font=('Bell MT', 20, 'bold'),
                                 ).grid(row=2, column=0)
        self.entry_contact = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_contact.grid(row=2, column=1)

        self.lbl_Payment = Label(self.booking_frame, text='Payment Method', bg='white',
                                 font=('Bell MT', 20, 'bold'),
                                 )
        self.lbl_Payment.grid(row=3, column=0)
        self.tbl_Payment = ttk.Combobox(self.booking_frame,
                                        font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.tbl_Payment['values'] = ('Esewa', 'Khalti', 'Phone Pay', 'Case on delivery')
        self.tbl_Payment.grid(row=3, column=1)

        # ====================btn=================================
        self.btn_bookNow = Button(self.booking_frame, command=self.order1, text='Order',
                                  font=('Bell MT', 20, 'bold'))
        self.btn_bookNow.grid(rowspan=4, column=2)

    def order1(self):
        if len(self.entry_qty.get()) != 0 and len(self.entry_price.get()) != 0 and len(
                self.entry_contact.get()) != 0 and len(self.tbl_Payment.get()) != 0:
            query = 'Insert into tbl_order (quantity, price, contact, payment_method, shoes_id) values (%s,%s,%s,%s,%s)'
            values = (
                self.entry_qty.get(), self.entry_price.get(), self.entry_contact.get(), self.tbl_Payment.get(), 4)
            self.dbconnect.add_data(query, values)
            messagebox.showinfo('Success', 'Order Registered')

        else:
            messagebox.showinfo('Incomplete', 'Complete it')


class Product5(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen

        # set database
        self.dbconnect = Curd()
        image1 = ImageTk.PhotoImage(file='Images/men/1r.jpg')
        self.order()

    def order(self):
        # self.search_frame = Frame(self.screen, width=900, height=600).place(x=50,y=220)
        self.detail_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        self.detail_frame.place(x=250, y=220, width=1250, height=550)
        self.image_frame = Frame(self.detail_frame, width=200, height=250)
        self.image_frame.place(x=0, y=0)
        self.image1 = ImageTk.PhotoImage(file='Images/women/2.JPG')
        Label(self.image_frame, image=self.image1).place(x=0, y=0)

        self.detail_frame1 = Frame(self.detail_frame, bg='white', width=1200, height=80, bd=4, relief=GROOVE)
        self.detail_frame1.place(x=230, y=4)
        Label(self.detail_frame1, text='Shoes Name :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=0, column=1,
                                                                                                      padx=10, pady=4)
        Label(self.detail_frame1, text='Brand :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=1, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Price :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=2, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Available Size :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=3,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=4)
        Label(self.detail_frame1, text='Details :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=4, column=1,
                                                                                                   padx=10, pady=4)

        query = 'select *from product where product_id =' + str(5)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows)
        Label(self.detail_frame1, text=self.rows[0][1], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=0, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][2], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=1, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][3], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=2, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][5], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=3, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][6], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=4, column=2, padx=10, pady=4)

        # ---------------------------------------------order-----------------------------------------------------------------------------
        self.booking_frame = Frame(self.detail_frame, width=800, bd=4, relief=GROOVE, bg='white', height=350)
        self.booking_frame.place(x=50, y=250, width=800, height=250)
        self.booking_head = Label(self.booking_frame, bd=4, relief=GROOVE, text='Order Now',
                                  font=('Bell MT', 20, 'bold'), bg='white')
        self.booking_head.place(x=0, y=0, relwidth=1)

        self.lbl_qty = Label(self.booking_frame, text='Quantity', font=('Bell MT', 20, 'bold'),
                             bg='white').grid(row=0, column=0, padx=(20, 10), pady=(50, 4))
        self.entry_qty = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_qty.grid(row=0, column=1, padx=10, pady=(50, 4))

        self.lbl_price = Label(self.booking_frame, text='Price', font=('Bell MT', 20, 'bold'),
                               bg='white').grid(row=1, column=0, padx=10)
        self.entry_price = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_price.grid(row=1, column=1, padx=10)

        self.lbl_contact = Label(self.booking_frame, bg='white', text='Contact No.',
                                 font=('Bell MT', 20, 'bold'),
                                 ).grid(row=2, column=0)
        self.entry_contact = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_contact.grid(row=2, column=1)

        self.lbl_Payment = Label(self.booking_frame, text='Payment Method', bg='white',
                                 font=('Bell MT', 20, 'bold'),
                                 )
        self.lbl_Payment.grid(row=3, column=0)
        self.tbl_Payment = ttk.Combobox(self.booking_frame,
                                        font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.tbl_Payment['values'] = ('Esewa', 'Khalti', 'Phone Pay', 'Case on delivery')
        self.tbl_Payment.grid(row=3, column=1)

        # ====================btn=================================
        self.btn_bookNow = Button(self.booking_frame, command=self.order1, text='Order',
                                  font=('Bell MT', 20, 'bold'))
        self.btn_bookNow.grid(rowspan=4, column=2)

    def order1(self):
        if len(self.entry_qty.get()) != 0 and len(self.entry_price.get()) != 0 and len(
                self.entry_contact.get()) != 0 and len(self.tbl_Payment.get()) != 0:
            query = 'Insert into tbl_order (quantity, price, contact, payment_method, shoes_id) values (%s,%s,%s,%s,%s)'
            values = (
                self.entry_qty.get(), self.entry_price.get(), self.entry_contact.get(), self.tbl_Payment.get(), 5)
            self.dbconnect.add_data(query, values)
            messagebox.showinfo('Success', 'Order Registered')

        else:
            messagebox.showinfo('Incomplete', 'Complete it')


class Product6(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen)
        self.screen = screen

        # set database
        self.dbconnect = Curd()
        image1 = ImageTk.PhotoImage(file='Images/men/1r.jpg')
        self.order()

    def order(self):
        # self.search_frame = Frame(self.screen, width=900, height=600).place(x=50,y=220)
        self.detail_frame = Frame(self.screen, bd=4, relief=RIDGE, bg='white')
        self.detail_frame.place(x=250, y=220, width=1250, height=550)
        self.image_frame = Frame(self.detail_frame, width=200, height=250)
        self.image_frame.place(x=0, y=0)
        self.image1 = ImageTk.PhotoImage(file='Images/women/3.jpg')
        Label(self.image_frame, image=self.image1).place(x=0, y=0)

        self.detail_frame1 = Frame(self.detail_frame, bg='white', width=1200, height=80, bd=4, relief=GROOVE)
        self.detail_frame1.place(x=230, y=4)
        Label(self.detail_frame1, text='Shoes Name :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=0, column=1,
                                                                                                      padx=10, pady=4)
        Label(self.detail_frame1, text='Brand :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=1, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Price :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=2, column=1,
                                                                                                 padx=10, pady=4)
        Label(self.detail_frame1, text='Available Size :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=3,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=4)
        Label(self.detail_frame1, text='Details :', font=('Bell MT', 20, 'bold'), bg='white').grid(row=4, column=1,
                                                                                                   padx=10, pady=4)

        query = 'select *from product where product_id =' + str(6)
        self.rows = self.dbconnect.fetch_data(query)
        print(self.rows)
        Label(self.detail_frame1, text=self.rows[0][1], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=0, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][2], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=1, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][3], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=2, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][5], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=3, column=2, padx=10, pady=4)
        Label(self.detail_frame1, text=self.rows[0][6], font=('Bell MT', 20, 'bold'),
              bg='white').grid(row=4, column=2, padx=10, pady=4)

        # ---------------------------------------------order-----------------------------------------------------------------------------
        self.booking_frame = Frame(self.detail_frame, width=800, bd=4, relief=GROOVE, bg='white', height=350)
        self.booking_frame.place(x=50, y=250, width=800, height=250)
        self.booking_head = Label(self.booking_frame, bd=4, relief=GROOVE, text='Order Now',
                                  font=('Bell MT', 20, 'bold'), bg='white')
        self.booking_head.place(x=0, y=0, relwidth=1)

        self.lbl_qty = Label(self.booking_frame, text='Quantity', font=('Bell MT', 20, 'bold'),
                             bg='white').grid(row=0, column=0, padx=(20, 10), pady=(50, 4))
        self.entry_qty = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_qty.grid(row=0, column=1, padx=10, pady=(50, 4))

        self.lbl_price = Label(self.booking_frame, text='Price', font=('Bell MT', 20, 'bold'),
                               bg='white').grid(row=1, column=0, padx=10)
        self.entry_price = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_price.grid(row=1, column=1, padx=10)

        self.lbl_contact = Label(self.booking_frame, bg='white', text='Contact No.',
                                 font=('Bell MT', 20, 'bold'),
                                 ).grid(row=2, column=0)
        self.entry_contact = Entry(self.booking_frame, font=('Bell MT', 20, 'bold'))
        self.entry_contact.grid(row=2, column=1)

        self.lbl_Payment = Label(self.booking_frame, text='Payment Method', bg='white',
                                 font=('Bell MT', 20, 'bold'),
                                 )
        self.lbl_Payment.grid(row=3, column=0)
        self.tbl_Payment = ttk.Combobox(self.booking_frame,
                                        font=('times new roman', 15, 'bold'), width=10, state='readonly')
        self.tbl_Payment['values'] = ('Esewa', 'Khalti', 'Phone Pay', 'Case on delivery')
        self.tbl_Payment.grid(row=3, column=1)

        # ====================btn=================================
        self.btn_bookNow = Button(self.booking_frame, command=self.order1, text='Order',
                                  font=('Bell MT', 20, 'bold'))
        self.btn_bookNow.grid(rowspan=4, column=2)

    def order1(self):
        if len(self.entry_qty.get()) != 0 and len(self.entry_price.get()) != 0 and len(
                self.entry_contact.get()) != 0 and len(self.tbl_Payment.get()) != 0:
            query = 'Insert into tbl_order (quantity, price, contact, payment_method, shoes_id) values (%s,%s,%s,%s,%s)'
            values = (
                self.entry_qty.get(), self.entry_price.get(), self.entry_contact.get(), self.tbl_Payment.get(), 6)
            self.dbconnect.add_data(query, values)
            messagebox.showinfo('Success', 'Order Registered')

        else:
            messagebox.showinfo('Incomplete', 'Complete it')


if __name__ == '__main__':
    a = Main()
    a.mainloop()
