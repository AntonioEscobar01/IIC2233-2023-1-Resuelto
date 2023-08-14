import unittest
from encriptar import serializar_diccionario, verificar_secuencia, \
    codificar_secuencia, codificar_largo, separar_msg, encriptar
from desencriptar import deserializar_diccionario, decodificar_largo, \
    separar_msg_encriptado, decodificar_secuencia, desencriptar
from errors import JsonError, SequenceError
from io import StringIO
from unittest.mock import patch


class TestEncriptar(unittest.TestCase):

    def test_serializar_diccionario(self):
        test = serializar_diccionario({"1": [1, 5], "2": "aei"})
        res = bytearray(b'{"1": [1, 5], "2": "aei"}')

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)
        self.assertEqual(test, res)

    def test_serializar_diccionario_excepcion(self):
        # Verificar que lavanta excepcion
        no_serializable = {"anya": set()}
        self.assertRaises(JsonError, serializar_diccionario, no_serializable)

        # Verificar que no levanta excepcion
        serializable = {"anya": "as"}
        try:
            serializar_diccionario(serializable)
        except:
            self.fail(
                "Se levantó una excepción con un input que si se puede serializar")

    def test_verificar_secuencia_None(self):
        mensaje = bytearray(b'\x00\x01\x02\x09')
        self.assertIsNone(verificar_secuencia(mensaje, [1, 2]))
    
    def test_verificar_secuencia_maximo(self):
        mensaje = bytearray(b'\x00\x01\x02\x09')
        self.assertRaises(SequenceError, verificar_secuencia, mensaje, [2000])
        
    def test_verificar_secuencia_repetidos(self):
        mensaje = bytearray(b'\x00\x01\x02\x09')
        self.assertRaises(SequenceError, verificar_secuencia, mensaje, [1, 1])
        
    def test_codificar_secuencia(self):
        test_1 = codificar_secuencia([1, 2, 3])
        res_1 = bytearray(b'\x00\x01\x00\x02\x00\x03')
        self.assertEqual(test_1, res_1)

    def test_codificar_secuencia_2(self):
        test_2 = codificar_secuencia([11, 4242, 12])
        res_2 = bytearray(b'\x00\x0b\x10\x92\x00\x0c')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_2, bytearray)
        # Verificar resultados
        self.assertEqual(test_2, res_2)
    
    def test_codificar_secuencia_3(self):
        test_2 = codificar_secuencia([4, 4444, 44])
        res_2 = bytearray(b'\x00\x04\x11\\\x00,')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_2, bytearray)
        # Verificar resultados
        self.assertEqual(test_2, res_2)

    def test_codificar_largo(self):
        test_1 = codificar_largo(7)
        res_1 = bytearray(b'\x00\x00\x00\x07')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)

    def test_codificar_largo_2(self):
        test_2 = codificar_largo(4241)
        res_2 = bytearray(b'\x00\x00\x10\x91')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_2, bytearray)
        # Verificar resultados
        self.assertEqual(test_2, res_2)

    def test_separar_msg(self):
        test_1 = separar_msg(bytearray(b'\x00\x01\x02\x03'), [1, 3])
        res_1 = [bytearray(b'\x01\x03'), bytearray(b'\x00\x02')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, list)
        # Verificar resultados
        self.assertListEqual(test_1, res_1)

    def test_separar_msg_2(self):
        test_2 = separar_msg(bytearray(b'\x00\x01\x02\x03'), [3, 1])
        res_2 = [bytearray(b'\x03\x01'), bytearray(b'\x00\x02')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_2, list)
        # Verificar resultados
        self.assertListEqual(test_2, res_2)
    
    def test_separar_msg_3(self):
        test_2 = separar_msg(bytearray(b'\x00\x01\x02\x03'), [2, 1])
        res_2 = [bytearray(b'\x02\x01'), bytearray(b'\x00\x03')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_2, list)
        # Verificar resultados
        self.assertListEqual(test_2, res_2)


class TestDesencriptar(unittest.TestCase):
    def test_deserializar_diccionario(self):
        test = deserializar_diccionario(bytearray(b'{"1": [1, 5], "2": "aei"}'))
        res = {"1": [1, 5], "2": "aei"}

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, dict)
        # Verificar resultados
        self.assertDictEqual(test, res)

    def test_deserializar_diccionario_excepcion(self):
        # Verificar que lavanta excepcion
        no_deserializable = b'{123:}'
        self.assertRaises(JsonError, deserializar_diccionario, no_deserializable)

        # Verificar que no levanta excepcion
        desserializable = bytearray(b'{"user": "name"}')
        try:
            deserializar_diccionario(desserializable)
        except:
            self.fail("Se levantó una excepción con un input que si se puede deserializar")

    def test_decodificar_largo(self):
        test_1 = decodificar_largo(bytearray(b'\x00\x00\x00\x04'))
        res_1 = 4
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_1, int)
        # Verificar resultados
        self.assertEqual(test_1, res_1)

    def test_decodificar_largo_2(self):
        test_2 = decodificar_largo(bytearray(b'\x00\x00\x11\x5C'))
        res_2 = 4444
        # Verificar tipo de dato pedido
        self.assertIsInstance(test_2, int)
        # Verificar resultados
        self.assertEqual(test_2, res_2)

    def test_separar_msg_encriptado(self):
        def new_decodificar_largo(*args, **kwargs):
            return 2

        with patch('desencriptar.decodificar_largo', side_effect=new_decodificar_largo):
            test = separar_msg_encriptado(
                bytearray(b'\x00\x00\x00\x02\x01\x03\x00\x02\x08\x00\x01\x00\x03'))
            res = [
                bytearray(b'\x01\x03'), 
                bytearray(b'\x00\x02\x08'), 
                bytearray(b'\x00\x01\x00\x03')
                ]
            # Verificar tipo de dato pedido
            self.assertIsInstance(res, list)
            # Verificar resultados
            self.assertListEqual(test, res)

    def test_separar_msg_encriptado_2(self):
        def decodificar_largo(*args, **kwargs):
            return 1

        with patch('desencriptar.decodificar_largo', side_effect=decodificar_largo):
            test = separar_msg_encriptado(
                bytearray(b'\x00\x00\x00\x01\x05\x00\x01\x02\xAA\x00\x03'))
            res = [
                bytearray(b'\x05'), 
                bytearray(b'\x00\x01\x02\xAA'), 
                bytearray(b'\x00\x03')
                ]
            # Verificar tipo de dato pedido
            self.assertIsInstance(res, list)
            # Verificar resultados
            self.assertListEqual(test, res)

    def test_decodificar_secuencia(self):
        test_1 = decodificar_secuencia(bytearray(b'\x00\x01\x00\x02\x00\x03'))
        res_1 = [1, 2, 3]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, list)
        # Verificar resultados
        self.assertListEqual(test_1, res_1)

    def test_decodificar_secuencia_2(self):
        test_2 = decodificar_secuencia(bytearray(b'\x00\x0b\x10\x92\x00\x0b'))
        res_2 = [11, 4242, 11]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_2, list)
        # Verificar resultados
        self.assertListEqual(test_2, res_2)
    
    def test_decodificar_secuencia_3(self):
        test = decodificar_secuencia(bytearray(b'\x10\x92'))
        res = [4242]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_desencriptar(self):
        def separar_msg_encriptado(*args, **kwargs):
            return [bytearray(b'\x01\x03'), 
                    bytearray(b'\x00\x02\x05'), 
                    bytearray(b'\x00\x01\x00\x03')]
        
        def decodificar_secuencia(*args, **kwargs):
            return [1, 3]
        
        with patch('desencriptar.separar_msg_encriptado', side_effect=separar_msg_encriptado):
            with patch('desencriptar.decodificar_secuencia', side_effect=decodificar_secuencia):
                test_1 = desencriptar(
                    bytearray(b'\x00\x00\x00\x02\x01\x03\x00\x02\x05\x00\x01\x00\x03'))
                res_1 = bytearray(b'\x00\x01\x02\x03\x05')
                # Verificar tipo de dato pedido
                self.assertIsInstance(res_1, bytearray)
                # Verificar resultados
                self.assertEqual(test_1, res_1)

    def test_desencriptar_2(self):
        def separar_msg_encriptado(*args, **kwargs):
            return [bytearray(b'abcd'), 
                    bytearray(b'efghijklmn'), 
                    bytearray(b'\x00\x02\x00\x03\x00\n\x00\x0c')]
        
        def decodificar_secuencia(*args, **kwargs):
            return [2, 3, 10, 12]
        
        with patch('desencriptar.separar_msg_encriptado', side_effect=separar_msg_encriptado):
            with patch('desencriptar.decodificar_secuencia', side_effect=decodificar_secuencia):
                test_1 = desencriptar(
                    bytearray(b'\x00\x00\x00\x04abcdefghijklmn\x00\x02\x00\x03\x00\n\x00\x0c'))
                res_1 = bytearray(b'efabghijklcmdn')
                # Verificar tipo de dato pedido
                self.assertIsInstance(res_1, bytearray)
                # Verificar resultados
                self.assertEqual(test_1, res_1)
    

class TestIntegracion(unittest.TestCase):

    def test_integracion_encriptar(self):
        test_1 = encriptar(bytearray(b'\x00\x01\x02\x03\x05'), [1, 3])
        res_1 = bytearray(b'\x00\x00\x00\x02\x01\x03\x00\x02\x05\x00\x01\x00\x03')
        # Verificar tipo de dato pedido
        self.assertIsInstance(res_1, bytearray)
        # Verificar resultados
        self.assertEqual(test_1, res_1)
    
    def test_integracion_desencriptar(self):
        test = bytearray(b'\x00\x00\x00\x05mata123\x00\x02\x00\x01\x00\x00\x00\x03\x00\x04')
        test = desencriptar(test)
        res = bytearray(b'tama123')
        self.assertIsInstance(res, bytearray)
        self.assertEqual(test, res)

    def test_integracion_todo_proceso(self):
        original = {"tama": 1}
        serializado = serializar_diccionario({"tama": 1})
        encriptado = encriptar(serializado, [1, 5, 10, 3])
        desencriptado = desencriptar(encriptado)
        deserializado = deserializar_diccionario(desencriptado)
        self.assertDictEqual(original, deserializado)

if __name__ == '__main__':
    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=2)
