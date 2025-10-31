import os
os.system("cls")
from dataclasses import dataclass 

@dataclass 
class Autor:
    nome: str
    biografia: str

class Livro:
    titulo: str
    ano: int
    autor: Autor 


    def exibir_detalhes(self):
        print(f"Aqui o titulo do livro: {self.titulo}")


te



