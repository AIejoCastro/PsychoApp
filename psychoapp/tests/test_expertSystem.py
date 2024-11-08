from django.test import TestCase
from psychoapp.expertSystem import start, PsychologicalEmergencyExpert

class BayesianSystemTest(TestCase):

    def setUp(self):
        self.engine = PsychologicalEmergencyExpert()
    
    def test_infer_diagnosis_1(self):
        result = start(hiper=1, llanto=0, agresividad=1, abuso=0, distorsion=1, ideas=1,
                       temblores=1, sudoracion=0, pitido=0, nubla=1, palpitaciones=0, vomito=0, 
                       abstinencia=0, agresion=0)
        expected_psicotic_advice = "Debes llamar a un numero de emergencia o a alguien de tu entera confianza"
        self.assertIn(expected_psicotic_advice, result['resultado'])
    
    def test_infer_diagnosis_2(self):
        result = start(hiper=1, llanto=1, agresividad=1, abuso=0, distorsion=1, ideas=0,
                       temblores=1, sudoracion=0, pitido=0, nubla=0, palpitaciones=1, vomito=0, 
                       abstinencia=1, agresion=1)
        expected_anxiety_advice = "Si te sientes abrumado, busca un lugar tranquilo y observa 5 cosas a tu alrededor"
        self.assertIn(expected_anxiety_advice, result['resultado'])
    
    def test_infer_diagnosis_3(self):
        result = start(hiper=1, llanto=0, agresividad=0, abuso=0, distorsion=0, ideas=0,
                       temblores=0, sudoracion=0, pitido=0, nubla=0, palpitaciones=0, vomito=0, 
                       abstinencia=0, agresion=0)
        expected_anxiety_advice = "Si te sientes abrumado, busca un lugar tranquilo"
        self.assertIn(expected_anxiety_advice, result['resultado'])

    def test_infer_diagnosis_4(self):
        result = start(hiper=1, llanto=1, agresividad=0, abuso=1, distorsion=0, ideas=1,
                       temblores=0, sudoracion=0, pitido=0, nubla=0, palpitaciones=0, vomito=0, 
                       abstinencia=0, agresion=0)
        expected_panic_advice = "Debes respirar conscientemente, intenta contar hasta 10"
        self.assertIn(expected_panic_advice, result['resultado'])