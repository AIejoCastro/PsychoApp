import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('Panico', 'hiperventilacion'),
    ('Panico', 'llanto_incontenible'),
    ('Panico', 'agresividad'),
    ('Panico', 'abuso_de_sustancias'),
    ('Panico', 'distorsion_de_la_realidad'),
    ('Panico', 'ideas_de_autolesion'),
    ('Panico', 'temblores'),
    ('Panico', 'sudoracion'),
    ('Panico', 'pitido'),
    ('Panico', 'nubla_de_vision'),
    ('Panico', 'palpitaciones_rapidas'),
    ('Panico', 'vomito'),
    ('Panico', 'abstinencia'),
    ('Panico', 'agresion_a_otros'),
    ('Ansiedad', 'hiperventilacion'),
    ('Ansiedad', 'llanto_incontenible'),
    ('Ansiedad', 'agresividad'),
    ('Ansiedad', 'abuso_de_sustancias'),
    ('Ansiedad', 'distorsion_de_la_realidad'),
    ('Ansiedad', 'ideas_de_autolesion'),
    ('Ansiedad', 'temblores'),
    ('Ansiedad', 'sudoracion'),
    ('Ansiedad', 'pitido'),
    ('Ansiedad', 'nubla_de_vision'),
    ('Ansiedad', 'palpitaciones_rapidas'),
    ('Ansiedad', 'vomito'),
    ('Ansiedad', 'abstinencia'),
    ('Ansiedad', 'agresion_a_otros'),
    ('Psicotico', 'hiperventilacion'),
    ('Psicotico', 'llanto_incontenible'),
    ('Psicotico', 'agresividad'),
    ('Psicotico', 'abuso_de_sustancias'),
    ('Psicotico', 'distorsion_de_la_realidad'),
    ('Psicotico', 'ideas_de_autolesion'),
    ('Psicotico', 'temblores'),
    ('Psicotico', 'sudoracion'),
    ('Psicotico', 'pitido'),
    ('Psicotico', 'nubla_de_vision'),
    ('Psicotico', 'palpitaciones_rapidas'),
    ('Psicotico', 'vomito'),
    ('Psicotico', 'abstinencia'),
    ('Psicotico', 'agresion_a_otros')
])

cpd_panico = TabularCPD(variable='Panico', variable_card=2, values=[[0.7], [0.3]])
cpd_ansiedad = TabularCPD(variable='Ansiedad', variable_card=2, values=[[0.6], [0.4]])
cpd_psicotico = TabularCPD(variable='Psicotico', variable_card=2, values=[[0.8], [0.2]])

cpd_hiperventilacion = TabularCPD(variable='hiperventilacion', variable_card=2,
                                  values=[[0.7, 0.4, 0.6, 0.3, 0.5, 0.8, 0.4, 0.3],
                                          [0.3, 0.6, 0.4, 0.7, 0.5, 0.2, 0.6, 0.7]],
                                  evidence=['Panico', 'Ansiedad', 'Psicotico'],
                                  evidence_card=[2, 2, 2])

cpd_llanto = TabularCPD(variable='llanto_incontenible', variable_card=2,
                        values=[[0.8, 0.6, 0.7, 0.4, 0.5, 0.7, 0.4, 0.2],
                                [0.2, 0.4, 0.3, 0.6, 0.5, 0.3, 0.6, 0.8]],
                        evidence=['Panico', 'Ansiedad', 'Psicotico'],
                        evidence_card=[2, 2, 2])

cpd_agresividad = TabularCPD(variable='agresividad', variable_card=2,
                              values=[[0.4, 0.3, 0.6, 0.5, 0.4, 0.6, 0.5, 0.3],
                                      [0.6, 0.7, 0.4, 0.5, 0.6, 0.4, 0.5, 0.7]],
                              evidence=['Panico', 'Ansiedad', 'Psicotico'],
                              evidence_card=[2, 2, 2])

cpd_abuso_sustancias = TabularCPD(variable='abuso_de_sustancias', variable_card=2,
                                  values=[[0.5, 0.3, 0.7, 0.4, 0.5, 0.6, 0.3, 0.2],
                                          [0.5, 0.7, 0.3, 0.6, 0.5, 0.4, 0.7, 0.8]],
                                  evidence=['Panico', 'Ansiedad', 'Psicotico'],
                                  evidence_card=[2, 2, 2])

cpd_distorsion_realidad = TabularCPD(variable='distorsion_de_la_realidad', variable_card=2,
                                     values=[[0.6, 0.4, 0.7, 0.3, 0.4, 0.8, 0.4, 0.2],
                                             [0.4, 0.6, 0.3, 0.7, 0.6, 0.2, 0.6, 0.8]],
                                     evidence=['Panico', 'Ansiedad', 'Psicotico'],
                                     evidence_card=[2, 2, 2])

cpd_ideas_autolesion = TabularCPD(variable='ideas_de_autolesion', variable_card=2,
                                  values=[[0.5, 0.3, 0.6, 0.4, 0.3, 0.7, 0.4, 0.2],
                                          [0.5, 0.7, 0.4, 0.6, 0.7, 0.3, 0.6, 0.8]],
                                  evidence=['Panico', 'Ansiedad', 'Psicotico'],
                                  evidence_card=[2, 2, 2])

cpd_temblores = TabularCPD(variable='temblores', variable_card=2,
                           values=[[0.6, 0.4, 0.7, 0.3, 0.5, 0.7, 0.3, 0.2],
                                   [0.4, 0.6, 0.3, 0.7, 0.5, 0.3, 0.7, 0.8]],
                           evidence=['Panico', 'Ansiedad', 'Psicotico'],
                           evidence_card=[2, 2, 2])

cpd_sudoracion = TabularCPD(variable='sudoracion', variable_card=2,
                            values=[[0.7, 0.5, 0.8, 0.4, 0.6, 0.9, 0.5, 0.3],
                                    [0.3, 0.5, 0.2, 0.6, 0.4, 0.1, 0.5, 0.7]],
                            evidence=['Panico', 'Ansiedad', 'Psicotico'],
                            evidence_card=[2, 2, 2])

cpd_pitido = TabularCPD(variable='pitido', variable_card=2,
                         values=[[0.5, 0.3, 0.6, 0.4, 0.4, 0.7, 0.3, 0.2],
                                 [0.5, 0.7, 0.4, 0.6, 0.6, 0.3, 0.7, 0.8]],
                         evidence=['Panico', 'Ansiedad', 'Psicotico'],
                         evidence_card=[2, 2, 2])

cpd_nubla_vision = TabularCPD(variable='nubla_de_vision', variable_card=2,
                               values=[[0.6, 0.4, 0.7, 0.3, 0.5, 0.8, 0.4, 0.2],
                                       [0.4, 0.6, 0.3, 0.7, 0.5, 0.2, 0.6, 0.8]],
                               evidence=['Panico', 'Ansiedad', 'Psicotico'],
                               evidence_card=[2, 2, 2])

cpd_palpitaciones = TabularCPD(variable='palpitaciones_rapidas', variable_card=2,
                               values=[[0.7, 0.5, 0.8, 0.4, 0.6, 0.9, 0.5, 0.3],
                                       [0.3, 0.5, 0.2, 0.6, 0.4, 0.1, 0.5, 0.7]],
                               evidence=['Panico', 'Ansiedad', 'Psicotico'],
                               evidence_card=[2, 2, 2])

cpd_vomito = TabularCPD(variable='vomito', variable_card=2,
                         values=[[0.5, 0.3, 0.6, 0.4, 0.4, 0.7, 0.3, 0.2],
                                 [0.5, 0.7, 0.4, 0.6, 0.6, 0.3, 0.7, 0.8]],
                         evidence=['Panico', 'Ansiedad', 'Psicotico'],
                         evidence_card=[2, 2, 2])

cpd_abstinencia = TabularCPD(variable='abstinencia', variable_card=2,
                              values=[[0.6, 0.4, 0.7, 0.3, 0.5, 0.8, 0.4, 0.2],
                                      [0.4, 0.6, 0.3, 0.7, 0.5, 0.2, 0.6, 0.8]],
                              evidence=['Panico', 'Ansiedad', 'Psicotico'],
                              evidence_card=[2, 2, 2])

cpd_agresion_otros = TabularCPD(variable='agresion_a_otros', variable_card=2,
                                values=[[0.7, 0.5, 0.8, 0.4, 0.6, 0.9, 0.5, 0.3],
                                        [0.3, 0.5, 0.2, 0.6, 0.4, 0.1, 0.5, 0.7]],
                                evidence=['Panico', 'Ansiedad', 'Psicotico'],
                                evidence_card=[2, 2, 2])

model.add_cpds(cpd_hiperventilacion, cpd_llanto, cpd_agresividad, cpd_abuso_sustancias,
               cpd_distorsion_realidad, cpd_ideas_autolesion, cpd_temblores, cpd_sudoracion,
               cpd_pitido, cpd_nubla_vision, cpd_palpitaciones, cpd_vomito, cpd_abstinencia,
               cpd_agresion_otros, cpd_panico, cpd_ansiedad, cpd_psicotico)

assert model.check_model()

inference = VariableElimination(model)

from experta import *

class Symptom(Fact):
    hiperventilacion = Field(int, default=0)
    llanto_incontenible = Field(int, default=0)
    agresividad = Field(int, default=0)
    abuso_de_sustancias = Field(int, default=0)
    distorsion_de_la_realidad = Field(int, default=0)
    ideas_de_autolesion = Field(int, default=0)
    temblores = Field(int, default=0)
    sudoracion = Field(int, default=0)
    pitido = Field(int, default=0)
    nubla_de_vision = Field(int, default=0)
    palpitaciones_rapidas = Field(int, default=0)
    vomito = Field(int, default=0)
    abstinencia = Field(int, default=0)
    agresion_a_otros = Field(int, default=0)

class Diagnosis(Fact):
    """Diagnóstico basado en síntomas"""
    pass

class PsychologicalEmergencyExpert(KnowledgeEngine):

    def __init__(self):
       super().__init__()
       self.result = ""

    def infer_diagnosis_generic(self, f):
        symptoms = {
            'hiperventilacion': f['hiperventilacion'], 'llanto_incontenible': f['llanto_incontenible'],
            'agresividad': f['agresividad'], 'abuso_de_sustancias': f['abuso_de_sustancias'],
            'distorsion_de_la_realidad': f['distorsion_de_la_realidad'], 'ideas_de_autolesion': f['ideas_de_autolesion'],
            'temblores': f['temblores'], 'sudoracion': f['sudoracion'], 'pitido': f['pitido'],
            'nubla_de_vision': f['nubla_de_vision'], 'palpitaciones_rapidas': f['palpitaciones_rapidas'],
            'vomito': f['vomito'], 'abstinencia': f['abstinencia'], 'agresion_a_otros': f['agresion_a_otros']
        }

        evidence = {key: value for key, value in symptoms.items() if value == 1}

        result_anxiety = inference.query(variables=['Ansiedad'], evidence=evidence)
        result_panic = inference.query(variables=['Panico'], evidence=evidence)
        result_psicotic = inference.query(variables=['Psicotico'], evidence=evidence)

        results = [result_anxiety.values[1], result_panic.values[1], result_psicotic.values[1]]
        disease_results = [result_anxiety.variables, result_panic.variables, result_psicotic.variables]

        disease_probability = encontrar_maximo(results)
        disease = disease_results[results.index(disease_probability)]

        self.declare(Diagnosis(name=disease[0]))

    @Rule(AS.f << Symptom(hiperventilacion=MATCH.hiperventilacion,
        llanto_incontenible=MATCH.llanto_incontenible,
        agresividad=MATCH.agresividad,
        abuso_de_sustancias=MATCH.abuso_de_sustancias,
        distorsion_de_la_realidad=MATCH.distorsion_de_la_realidad,
        ideas_de_autolesion=MATCH.ideas_de_autolesion,
        temblores=MATCH.temblores,
        sudoracion=MATCH.sudoracion,
        pitido=MATCH.pitido,
        nubla_de_vision=MATCH.nubla_de_vision,
        palpitaciones_rapidas=MATCH.palpitaciones_rapidas,
        vomito=MATCH.vomito,
        abstinencia=MATCH.abstinencia,
        agresion_a_otros=MATCH.agresion_a_otros))
    def infer_diagnosis_4(self, f):
        self.infer_diagnosis_generic(f)

    @Rule(Diagnosis(name = "Ansiedad"))
    def anxiety(self):
      self.result += f"Si te sientes abrumado, busca un lugar tranquilo y observa 5 cosas a tu alrededor, enfocándote en los detalles. Cierra los ojos (si te sientes cómodo) y escucha 4 sonidos distintos. Toca 3 objetos cercanos, sintiendo su textura, temperatura y forma. Respira hondo por la nariz (4 segundos), retén (4 segundos) y exhala por la boca (6 segundos). Repite 5 veces. Presta atención mientras respiras a lo que ves, oyes y tocas, manteniéndote presente. Recuerda, está bien tomarte un tiempo para ti. Este ejercicio te ayuda a encontrar paz y claridad. Respira y tómate tu tiempo."

    @Rule(Diagnosis(name = "Panico"))
    def panic(self):
      self.result += f"Debes respirar conscientemente, intenta contar hasta 10 y luego regresa a contar hacia atras, busca un lugar tranquilo y seguro. Trata de no estar solo, llama a alguien de confianza."

    @Rule(Diagnosis(name = "Psicotico"))
    def suicidal(self):
      self.result += f"Debes llamar a un numero de emergencia o a alguien de tu entera confianza, entiende que tu vida vale mucho"

engine = PsychologicalEmergencyExpert()

def encontrar_maximo(array):
  maximo = array[0]
  for elemento in array:
    if elemento > maximo:
      maximo = elemento
  return maximo

def start(hiper, llanto, agresividad, abuso, distorsion, ideas, temblores, sudoracion, pitido, nubla, palpitaciones, vomito, abstinencia, agresion):
    symptoms_values = {
        'hiperventilacion': hiper,
        'llanto_incontenible': llanto,
        'agresividad': agresividad,
        'abuso_de_sustancias': abuso,
        'distorsion_de_la_realidad': distorsion,
        'ideas_de_autolesion': ideas,
        'temblores': temblores,
        'sudoracion': sudoracion,
        'pitido': pitido,
        'nubla_de_vision': nubla,
        'palpitaciones_rapidas': palpitaciones,
        'vomito': vomito,
        'abstinencia': abstinencia,
        'agresion_a_otros': agresion
    }
    engine.reset()
    engine.result = ""
    engine.declare(Symptom(**symptoms_values))
    engine.run()

    return {'resultado': engine.result}