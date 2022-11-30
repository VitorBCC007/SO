#AULA 4 SO
#ATIVIDADE MUDA ESTADO 
class Processo:

    def __init__(self, pid, te):  
        self.pid = pid  # Identificador de Processo
        self.tp = 0  # Tempo de Processamento
        self.cp = self.tp + 1  # Contador de Programa / / identifica qual a proxima instrução // Tempo de proc
        self.ep = 'PRONTO'  # Estado do Processo
        self.nes = 0  # Número de vezes que realizou uma operação de E/S
        self.n_cpu = 0  # Número de vezes que usou a CPU
        self.te = te  # Tempo de Execução para terminar a execução

#ESTADOS EXECUTANDO, BLOQUEADO, PRONTO E FINALIZADO
    def executando(self):
        print(f'{self.ep} >>> EXECUTANDO')
        self.ep = 'EXECUTANDO'

    def bloqueado(self):
        print(f'{self.ep} >>> BLOQUEADO')
        self.ep = 'BLOQUEADO'

    def pronto(self):
        print(f'{self.ep} >>> PRONTO')
        self.ep = 'PRONTO'

    def finalizado(self):
        print(f'{self.ep} >>> FINALIZADO')
        self.ep = 'FINALIZADO'

        
    def ep(self): #ESTADO DE PROCESSO
        return self.ep

      
    def add__nes(self): #ADICIONANDO NUM OPERAÇÕES
        self.nes += 1

    def reset__nes(self): #RESETANDO AS MESMAS
        self.nes = 0

    def nes(self): #NUM DE VEZES QUE REALIZOU AS OPERAÇÕES
        return self.nes

    def add__tp(self): #ADICIONANDO AO TEMPO DE PROCESSAMENTO
        self.tp += 1

    def pid(self): #IDENTIFICANDO PROCESSOS(PID)
        return self.pid

    def cp(self): #CONTADOR DO PROGRAMA
        return self.cp

    def set_cp(self): #DEFININDO CONTADOR
        self.cp = self.tp + 1

    def add_ncpu(self): #ADICIONANDO NUM DE VEZES QUE USOU A CPU
        self.n_cpu += 1

        
    def tp(self): #TEMPO DE PROCESSAMENTO
        return self.tp

      
    def te(self): #TEMPO DE EXECUÇÃO
        return self.te

    def print(self): #MOSTRANDO TUDO PARA O USUÁRIO
        print(f'PID: {self.pid}\nTP: {self.tp}\nCP: {self.cp}\nEP: {self.ep}\nNES: {self.nes}\nNCPU: {self.n_cpu}\nTE: {self.te}')
