import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from datetime import datetime
import sqlalchemy as sql
from time import sleep

kivy.require("1.11.1")

class MyGrid(Widget):

    dre = ObjectProperty(None)
    nome = ObjectProperty(None)
    curso = ObjectProperty(None)
    genero = ObjectProperty(None)
    nascimento = ObjectProperty(None)
    altura = ObjectProperty(None)
    peso = ObjectProperty(None)
    cra = ObjectProperty(None)
    creditos = ObjectProperty(None)
    renda = ObjectProperty(None)
    submit = ObjectProperty(None)
    status = ObjectProperty(None)
    count = ObjectProperty(None)
    cra_medio = ObjectProperty(None)
    renda_media = ObjectProperty(None)
    imc_medio = ObjectProperty(None)

    engine = sql.create_engine('sqlite:///data/database.db', echo=False)

    def update(self):

        inputs = [self.dre, self.nome,self.curso,self.genero,self.nascimento,self.altura,self.peso,self.cra,self.creditos,self.renda]
        for element in inputs:
            if element.text == '':
                self.status.text = 'Status: Update failed, complete all fields before submiting.'
                return

        try:
            if len(self.dre.text) != 9:
                raise Exception
            int(self.dre.text)
        except:
            self.status.text = 'Status: Update failed, DRE must be a 9 digit number.'
            return
        
        try:
            float(self.altura.text)
            float(self.peso.text)
            float(self.cra.text)
            float(self.creditos.text)
            float(self.renda.text)
        except:
            self.status.text = 'Status: Update failed, altura, peso, cra, creditos and renda must be numbers.'
            return

        try:
            bool(datetime.strptime(self.nascimento.text, "%d-%m-%Y"))
        except ValueError:
            self.status.text = 'Status: Update failed, data de nascimento must be in the correct format.'
            return

        

        dre = self.dre.text
        curso = self.curso.text
        nome = self.nome.text
        genero = self.genero.text
        nascimento = self.nascimento.text
        altura = self.altura.text
        peso = self.altura.text
        cra = self.cra.text
        creditos = self.creditos.text
        renda = self.renda.text

        
        query = f"""
        insert into students
        values ({dre},'{curso}','{nome}','{genero}',{nascimento},{altura},{peso},{cra},{creditos},{renda})
        """

        with self.engine.connect() as connection:
            connection.execute(query)

        self.status.text = 'Status: Update successfull'
        self.refresh_stats()

    def refresh_stats(self):
        
        query = "select count(*) from students"
        with self.engine.connect() as connection:
            result = connection.execute(query)

            count = result.first()[0]
            self.count.text = 'Número de alunos: '+ str(count)

            query = "select avg(CRA) from students"
            result = connection.execute(query)
            
            self.cra_medio.text = "CRA médio: "+ str(result.first()[0])

            query = "select avg(Renda) from students"
            result = connection.execute(query)
            
            self.renda_media.text = "Renda média: "+  str(result.first()[0])
            
            query = "select avg(Peso/(Altura*Altura))  from students"
            result = connection.execute(query)

            self.imc_medio.text = "Índice de massa corporal médio: "+ str(result.first()[0]/count)




    
    

class MyApp(App):
    def build(self):
        return MyGrid()

    

Builder.load_file('MyGrid.kv')
app = MyApp()
app.run()