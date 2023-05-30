import unittest
from main import * #asterix importa tudo
from unittest.mock import patch

class Test_help(unittest.TestCase): #criando_uma_classe_pra_testar nome_classe( Herança do teste )
    @patch('builtins.input', lambda _: 'Yasmin')
    def test_ler_nome(self):
        esperado = "Yasmin"
        resultado = ler_nome()
        self.assertEqual(resultado, esperado) #ve se ta o nome certo

    @patch('builtins.input', lambda _: '2911')
    def test_ler_senha(self):
        esperado = "2911"
        resultado = ler_senha()
        self.assertEqual(resultado, esperado)

    def test_listar(self):
        self.assertEqual(type(listar()), str)

    def test_login_eu_amo_ela(self):
        user = "Yasmin"
        senha = "16"
        self.assertTrue(login(user, senha)) #esta vendo se ta tudo re4almenrte sdendo feito da forma necessaria
        
        user = "gorda"
        senha = "login"
        self.assertFalse(login(user, senha)) #esta vendo se ta tudo re4almenrte sdendo feito da forma necessaria
        

    # def teste_cadatro(self): #def = funçao/ self= ele mesmo/ ele testa o cadastro
    #     cadastrar()
    
        