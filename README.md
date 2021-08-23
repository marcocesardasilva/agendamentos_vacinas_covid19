# Sistema de Agendamentos de Vacinas para o COVID-19

Sistema desenvolvido na disciplina de Desenvolvimento de Sistemas Orientados à Objetos no curso de Sistemas de Informação da UFSC no ano de 2021.

ESCOPO DO DESENVOLVIMENTO:

Cada posto de vacinação possui um estoque de vacinas de variados fabricantes, enfermeiros e enfermeiras responsáveis pela aplicação das vacinas, e pacientes a serem vacinados.
Um sistema de vacinação deve ser configurado para um determinado posto de vacinação em um município. Nele devem ser cadastrados os enfermeiros e enfermeiras que trabalham naquele posto, as doses de vacinas disponíveis com quantidade e fabricante, assim como os pacientes que serão atendidos por aquele posto de vacinação.
Cada paciente atendido pelo posto de vacinação deve marcar um horário de atendimento para ser vacinado por um enfermeiro(a) em horário comercial (08:00 às 18:00). Esse paciente deve tomar duas doses da vacina, com um intervalo de no mínimo 20 dias entre elas, e ambas devem ser fabricadas pelo mesmo fabricante. Os horários disponíveis dependem das doses de vacinas disponíveis.
Para um determinado posto de vacinação, deve ser possível listar as doses disponíveis e aplicadas, os pacientes que já foram vacinados (primeira e segunda doses), os pacientes com vacinação agendada, e a quantidade de pacientes cadastrados naquele posto que ainda estão esperando na fila (sem atendimento agendado ainda).

Considere algumas regras:
1. No cadastro de pacientes, deve ser informada a idade com números de 0 até 150. Valores de idade fora desses limites devem ser tratados pelo sistema.
2. O cadastro de um horário de atendimento só deve ser realizado com sucesso se houver doses de vacina disponíveis para vacinar aquele paciente.
3. Caso o paciente esteja agendando atendimento para a segunda dose da vacina, deve-se verificar se o paciente já tomou a primeira dose e certificar que as doses disponíveis são compatíveis com a sua primeira dose (do mesmo fabricante).
4. A qualquer momento, deve ser possível gerar um relatório com o número de doses já aplicadas e número de doses disponíveis; os pacientes já vacinados (com distinção entre apenas primeira dose e primeira + segunda doses); os pacientes com vacinação agendada e os pacientes que ainda não agendaram atendimento.
5. Deve ser possível listar todos os pacientes que foram atendidos por um determinado enfermeiro.

RESTRIÇÕES DE ESCOPO:

Para simplificar esse trabalho, o sistema não precisa levar em consideração os grupos de prioridade na vacinação. Além disso, caso uma vacina específica seja necessária para a segunda dose, assume-se que o posto de vacinação pode conseguir as doses com o
UNIVERSIDADE FEDERAL DE SANTA CATARINA
Disciplina: INE5605 – Desenvolvimento de Sistemas Orientados a Objetos I
Professores: Jean Hauck, Dr. e Thaís Bardini Idalino, Dr.
município e adicioná-las no seu estoque a qualquer momento. Também não é necessário manter uma agenda com horários disponíveis dos enfermeiros e enfermeiras.
