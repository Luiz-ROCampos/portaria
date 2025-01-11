from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QMenu, QWidget, QMessageBox, QTreeWidget, QTableWidgetItem, 
                               QPushButton, QVBoxLayout, QButtonGroup, QRadioButton)
from PySide6.QtGui import QAction, QFont
import core
from ui_login_ui import Ui_login
from ui_main_ui import Ui_MainPortaria
from core.users.models import check_user
from core.portaria.models import (CadastroColaboradores, CadastroFornecedor, CadastroTeiceiro, Departamento, RegistroManutencao, RegistroMateriais, RegistroChaves, RegistroColaboradores, RegistroFornecedor, RegistroTeiceiro, Vigilantes, Chaves)

class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do sistema.")

        self.btn_logar.clicked.connect(self.logar)
        
    def logar(self):
        usuario = self.txt_usuario.text()
        senha = self.txt_senha.text()
        print(usuario, senha)
        print(check_user(usuario, senha))
        if usuario == "" or senha == "":
            #utils.mensagem("Usuario ou senha não preenchidos.", "Você deve informar um usuário e uma senha.")
            return None
    
        if check_user(usuario, senha):
            self.w = MainPortaria()
            self.w.show()
            self.close()   
        else:
            #utils.mensagem("Usuário ou senha inválidos!", "Digite novamente, um usuário e senha válidos.")
            self.txt_usuario.setText("")
            self.txt_senha.setText("")      

class MainPortaria(QMainWindow, Ui_MainPortaria):
    def __init__(self):
        super(MainPortaria, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controle Fluxo da Portaria')
        self.paginas.setCurrentWidget(self.pg_home)

        #******************** Paginas do Sistema ********************
        self.btn_pg_home.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_home))
        self.btn_pg_fornecedor.clicked.connect(self.listar_fornecedor)
        self.btn_pg_terceiros.clicked.connect(self.listar_terceiro)
        self.btn_pg_colaboradores.clicked.connect(self.listar_departamento_colaborador)
        self.btn_pg_chave.clicked.connect(self.listar_setores)
        self.btn_pg_materiais.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_materiais))

        fonte = QFont("Arial", 12)

        #******************** Pagina Novo Fornecedor ********************
        self.btn_pg_novo_fornecedor.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_novo_fornecedor))

        #******************** Cadastro Novo Fornecedor ********************
        self.btn_novo_fornecedor.clicked.connect(self.cadastro_fornecedor)
        self.btn_limpar_cadastro_fornecedor.clicked.connect(self.limpar_cadastro_fornecedor)
        self.btn_voltar_fornecedor.clicked.connect(self.listar_fornecedor)

        #******************** Registro Fornecedor ********************
        self.cmb_registro_fornecedor.setPlaceholderText("Escolha o fornecedor.")

        self.cmb_registro_nome.setPlaceholderText("Escolha o entregador.")

        self.cmb_registro_departamento.setPlaceholderText("Escolha o departamento.")
        self.cmb_registro_autorizadopor.setPlaceholderText("Escolha quem autorizou.")

        self.cmb_registro_fornecedor.currentIndexChanged.connect(self.listar_entregador)
        
        self.cmb_registro_nome.currentIndexChanged.connect(self.listar_rg)

        self.cmb_registro_departamento.currentIndexChanged.connect(self.listar_autorizadopor)

        self.btn_registrar_fornecedor.clicked.connect(self.registro_fornecedor)
        self.btn_f_limpar.clicked.connect(self.limpar_registro_fornecedor)

        

        #******************** Cadastro e Registro de Terceiros ********************
        self.cmb_reg_terceiros_viacao.setPlaceholderText("Escolha a viação ou digite o motorista.")

        self.btn_reg_terceiros_entrada.clicked.connect(self.registro_terceiro_entrada)
        self.btn_reg_terceiros_saida.clicked.connect(self.registro_terceiro_saida)

        #******************** Registro de Colaboradores ********************
        self.cmb_colaboradores_departamento.setPlaceholderText("Escolha o departamento")
        self.cmb_colaboradores_funcionario.setPlaceholderText("Escolha o funcionário")
        
        self.cmb_colaboradores_departamento.currentIndexChanged.connect(self.listar_colaborador)

        self.btn_colaboradores_salvar.clicked.connect(self.registro_colaborador)

        #******************** Registro de Chaves ********************
        self.cmb_chave_setor.setPlaceholderText('Escolha o setor.')
        self.cmb_chave_vigilante.setPlaceholderText('Escolha o vigilante.')

        self.cmb_chave_setor.currentIndexChanged.connect(self.listar_numero_chave)

        self.btn_ch_salvar.clicked.connect(self.registrar_chave)

        #******************** Registro de Materiais ********************
        self.btn_m_salvar.clicked.connect(self.registrar_materiais)

        self.btn_ma_salvar.clicked.connect(self.registrar_manutencao)


    #******************** Cadastro e Registro de Fornecedores ********************

    def listar_fornecedor(self):
        self.paginas.setCurrentWidget(self.pg_fonecedor)

        self.cmb_registro_fornecedor.clear()
        self.cmb_registro_departamento.clear()
        
        for fornecedor in CadastroFornecedor.carregar_lista_fornecedor():
            self.cmb_registro_fornecedor.addItem(fornecedor.nome_fornecedor)

        for departamento  in Departamento.lista_departamento():
            self.cmb_registro_departamento.addItem(departamento.nome, departamento.id)

        self.adicionar_fornecedor_tabela()

    def limpar_registro_fornecedor(self):
        
        self.cmb_registro_fornecedor.clear()
        self.cmb_registro_nome.clear()
        self.txt_registro_rg.clear()
        self.txt_registro_placa.clear()
        self.txt_registro_cracha.clear()
        self.cmb_registro_departamento.clear()
        self.cmb_registro_autorizadopor.clear()

        self.adicionar_fornecedor_tabela()
            
    def listar_entregador(self):
        fornecedor = self.cmb_registro_fornecedor.currentText()

        self.cmb_registro_nome.clear()

        for lista in CadastroFornecedor.listar_cadastro_fornecedor():
            if lista.nome_fornecedor == fornecedor:
                self.cmb_registro_nome.addItem(lista.nome_entregador, lista.id)
                    
    def listar_rg(self):
        entregador_id = self.cmb_registro_nome.currentData()
        print(entregador_id)
        self.txt_registro_rg.clear()
        self.txt_registro_placa.clear()

        for lista in CadastroFornecedor.listar_cadastro_fornecedor():
            if lista.id == entregador_id:
                self.txt_registro_rg.setText(lista.numero_rg)
                self.txt_registro_placa.setText(lista.placa_carro)
    
    def listar_departamento(self):
        departamentos = Departamento.lista_departamento()

        self.cmb_registro_departamento.clear()

        for departamento  in departamentos:
            self.cmb_registro_departamento.addItem(departamento.nome, departamento.id)

    def listar_autorizadopor(self):

        departamento_id = self.cmb_registro_departamento.currentData()

        self.cmb_registro_autorizadopor.clear()
        
        if departamento_id:
            colaboradores = CadastroColaboradores.listar_colaborador_por_departamento(departamento_id)
            for colaborador in colaboradores:
                self.cmb_registro_autorizadopor.addItem(colaborador.nome)

    def registro_fornecedor(self):
        entregador = self.cmb_registro_nome.currentData()
        placa = self.txt_registro_placa.text()
        cracha = self.txt_registro_cracha.text()
        departamento = self.cmb_registro_departamento.currentText()
        autorizadopor = self.cmb_registro_autorizadopor.currentText()

        RegistroFornecedor.registrar_fornecedor(entregador, placa, cracha, departamento, autorizadopor)
        
        self.listar_fornecedor()

    def registrar_saida(self, row):
        # Obter o ID do fornecedor associado à linha
        item = self.tabela_fornecedor.item(row, 0)
        print(item)
        if item:
            fornecedor_id = item.data(Qt.UserRole)
            print(fornecedor_id)
            RegistroFornecedor.registrar_saida_fornecedor(fornecedor_id)
    
        self.listar_fornecedor()
    
    def adicionar_fornecedor_tabela(self):
        self.tabela_fornecedor.clearContents()
        listar_fornecedor = RegistroFornecedor.listar_entrada_fornecedor()
        if listar_fornecedor:
            self.tabela_fornecedor.clearContents()
            self.tabela_fornecedor.setColumnCount(4)
            self.tabela_fornecedor.setRowCount(len(listar_fornecedor))
            
            for row_index, lista in enumerate(listar_fornecedor):

                item_fornecedor = QTableWidgetItem(lista.fornecedor)
                item_fornecedor.setTextAlignment(Qt.AlignCenter)
                item_placa = QTableWidgetItem(lista.placa)
                item_placa.setTextAlignment(Qt.AlignCenter)
                item_fornecedor.setData(Qt.UserRole, lista.id)

                self.tabela_fornecedor.setItem(row_index, 0, QTableWidgetItem(item_fornecedor))
                self.tabela_fornecedor.setItem(row_index, 1, QTableWidgetItem(item_placa))

                mascara_data = datetime.strftime(lista.hora_entrada, "%d/%m/%Y - %H:%M")
                self.tabela_fornecedor.setItem(row_index, 2, QTableWidgetItem(mascara_data))

                btn_fornecedor_saida = QPushButton('Registrar saída')
                btn_fornecedor_saida.clicked.connect(lambda _, row=row_index: self.registrar_saida(row))
                self.tabela_fornecedor.setCellWidget(row_index, 3, btn_fornecedor_saida)

            self.layout = QVBoxLayout()
            self.layout.addWidget(self.tabela_fornecedor)
            self.setLayout(self.layout)

            self.tabela_fornecedor.setColumnWidth(0, 155)
            self.tabela_fornecedor.setColumnWidth(1, 90)
            self.tabela_fornecedor.setColumnWidth(2, 120)
            self.tabela_fornecedor.setColumnWidth(3, 99)
            self.tabela_fornecedor.sortItems(2, Qt.AscendingOrder)

    def limpar_cadastro_fornecedor(self):
        self.txt_novo_fornecedor.setText("")
        self.txt_novo_entregador.setText("")
        self.txt_novo_rg.setText("")
        self.txt_novo_placa.setText("")

    def cadastro_fornecedor(self):
        fornecedor = self.txt_novo_fornecedor.text()
        entregador = self.txt_novo_entregador.text()
        rg = self.txt_novo_rg.text()
        placa = self.txt_novo_placa.text()

        CadastroFornecedor.cadastrar_fornecedor(fornecedor, entregador, rg, placa)

        self.txt_novo_fornecedor.setText("")
        self.txt_novo_entregador.setText("")
        self.txt_novo_rg.setText("")
        self.txt_novo_placa.setText("")

    #******************** Registro de Terceiros ********************
    def listar_terceiro(self):
        self.paginas.setCurrentWidget(self.pg_terceiros)
        self.cmb_reg_terceiros_viacao.clear()
        
        for lista in CadastroTeiceiro.listar_terceiros():
            print(lista.nome)
            self.cmb_reg_terceiros_viacao.addItem(lista.nome)
        
        self.adicionar_terceiros_tabela()

    def registro_terceiro_entrada(self):
        prefixo = self.txt_reg_terceiros_prefixo.text()
        viacao = self.cmb_reg_terceiros_viacao.currentText()
        
        RegistroTeiceiro.resgitrar_terceiro_entrada(viacao, prefixo)
        
        self.txt_reg_terceiros_prefixo.clear()
        self.cmb_reg_terceiros_viacao.clear()
        self.listar_terceiro()
        
    def registro_terceiro_saida(self):
        prefixo = self.txt_reg_terceiros_prefixo.text()
        
        RegistroTeiceiro.resgitrar_terceiro_saida(prefixo)
        
        self.listar_terceiro()
        
    def adicionar_terceiros_tabela(self):
        lista_terceiros = CadastroTeiceiro.listar_terceiros()
        if lista_terceiros:
            self.tabela_terceiros.clearContents()
            self.tabela_terceiros.setColumnCount(3)
            self.tabela_terceiros.setRowCount(len(lista_terceiros))

            for row_index, lista in enumerate(lista_terceiros):
                item_nome = QTableWidgetItem(lista.nome)
                item_total = QTableWidgetItem(str(lista.total))
                if lista.quantidade == None:
                    item_quantidade = QTableWidgetItem(str(0))
                else:
                    item_quantidade = QTableWidgetItem(str(lista.quantidade))

                self.tabela_terceiros.setItem(row_index, 0, item_nome)
                self.tabela_terceiros.setItem(row_index, 1, item_total)
                self.tabela_terceiros.setItem(row_index, 2, item_quantidade)

            self.layout = QVBoxLayout()
            self.layout.addWidget(self.tabela_terceiros)
            self.setLayout(self.layout)

            self.tabela_terceiros.setColumnWidth(0, 160)
            self.tabela_terceiros.setColumnWidth(1, 116)
            self.tabela_terceiros.setColumnWidth(2, 120)

    #******************** Registro de colaboradores ********************
    def listar_departamento_colaborador(self):
        
        self.paginas.setCurrentWidget(self.pg_colaboradores)

        self.cmb_colaboradores_departamento.clear()

        departamentos = Departamento.lista_departamento()

        if departamentos:
            for departamento in departamentos:
                self.cmb_colaboradores_departamento.addItem(departamento.nome, departamento.id)
        
    def listar_colaborador(self):
        # Obtenha o ID do departamento selecionado
        departamento_id = self.cmb_colaboradores_departamento.currentData()

        print(f"Departamento ID selecionado: {departamento_id}")
        # Limpe o combobox de funcionários
        self.cmb_colaboradores_funcionario.clear()
        
        if departamento_id:
            # Busque os colaboradores associados ao departamento
            colaboradores = CadastroColaboradores.listar_colaborador_por_departamento(departamento_id)
            for colaborador in colaboradores:
                self.cmb_colaboradores_funcionario.addItem(colaborador.nome)
                      
    def registro_colaborador(self):
        departamento_id = self.cmb_colaboradores_departamento.currentData()
        colaborador = self.cmb_colaboradores_funcionario.currentText()
        

        if self.ob_colaboradores_entrada.isChecked():
            RegistroColaboradores.registrar_colaborador_entrada(departamento_id, colaborador)
        elif self.ob_colaboradores_saidaA.isChecked():
            RegistroColaboradores.registrar_colaborador_saida_a(departamento_id, colaborador)
        elif self.ob_colaboradores_entradaA.isChecked():
            RegistroColaboradores.registrar_colaborador_entrada_a(departamento_id, colaborador)
        elif self.ob_colaboradores_saida.isChecked():
            RegistroColaboradores.registrar_colaborador_saida(departamento_id, colaborador)
        else:
            core.portaria.mensagem('Registro não realizado', 'Erro: preencha todos os campos e selecione uma opção!')
            return None

        self.listar_departamento_colaborador()

    #******************** Registro de chaves ********************
    def listar_setores(self):
        self.cmb_chave_setor.clear()
        self.cmb_chave_vigilante.clear()
        self.paginas.setCurrentWidget(self.pg_chave)

        for chave in Chaves.listar_chave():
            self.cmb_chave_setor.addItem(chave.setor)


        for vigilante in Vigilantes.listar_vigilante():
            self.cmb_chave_vigilante.addItem(vigilante.nome)

        self.adicionar_chave_tabela()

    def registrar_chave(self):
        colaborador = self.txt_chave_nome.text()
        chave_setor = self.cmb_chave_setor.currentText()
        vigilante = self.cmb_chave_vigilante.currentText()

        RegistroChaves.registro_chave(colaborador, chave_setor, vigilante)

        self.listar_setores()

    def adicionar_chave_tabela(self):
        lista_entrada = RegistroChaves.listar_chave_entrada()
        chaves = Chaves.listar_chave()
        self.tabela_chaves.clearContents()
        self.tabela_chaves.setColumnCount(5)
        self.tabela_chaves.setRowCount(len(lista_entrada))

        for row_index, lista in enumerate(lista_entrada):
            numero = ""
            setor = ""

            for chave in chaves:
                if chave.id == lista.chave_setor_id:
                    setor = chave.setor
                    numero = str(chave.numero)

            # Criando os itens com centralização
            item_numero = QTableWidgetItem(numero)
            item_numero.setTextAlignment(Qt.AlignCenter)
            
            item_setor = QTableWidgetItem(setor)
            item_setor.setTextAlignment(Qt.AlignCenter)
            
            item_colaborador = QTableWidgetItem(lista.colaborador)
            item_colaborador.setTextAlignment(Qt.AlignCenter)

            item_colaborador.setData(Qt.UserRole, lista.id)

            mascara_data = datetime.strftime(lista.retirada, "%d/%m/%Y - %H:%M")
            item_data = QTableWidgetItem(mascara_data)
            item_data.setTextAlignment(Qt.AlignCenter)

            # Adicionando os itens à tabela
            self.tabela_chaves.setItem(row_index, 0, item_numero)
            self.tabela_chaves.setItem(row_index, 1, item_setor)
            self.tabela_chaves.setItem(row_index, 2, item_data)
            self.tabela_chaves.setItem(row_index, 3, item_colaborador)

            # Configurando o botão na última coluna
            btn_fornecedor_saida = QPushButton('Devolvida')
            btn_fornecedor_saida.clicked.connect(lambda _, row=row_index: self.registrar_chave_saida(row))
            self.tabela_chaves.setCellWidget(row_index, 4, btn_fornecedor_saida)

        # Configurando as larguras e ordenação
        self.tabela_chaves.setColumnWidth(0, 80)
        self.tabela_chaves.setColumnWidth(1, 120)
        self.tabela_chaves.setColumnWidth(2, 120)
        self.tabela_chaves.setColumnWidth(3, 120)
        self.tabela_chaves.setColumnWidth(4, 98)
        self.tabela_chaves.sortItems(2, Qt.AscendingOrder)

    def listar_numero_chave(self):
        self.txt_ch_chave.clear()

        setor = self.cmb_chave_setor.currentText()

        for lista in Chaves.listar_chave():
            if lista.setor == setor:
                self.txt_ch_chave.setText(str(lista.numero))
                
    def registrar_chave_saida(self, row):
        # Obter o ID da chave associado à linha
        item = self.tabela_chaves.item(row, 3)
        if item:
            chave_id = item.data(Qt.UserRole)
            RegistroChaves.registro_chave_saida(chave_id)
    
        self.adicionar_chave_tabela()

    #******************** Registro de materiais ********************
    def registrar_materiais(self):
        prefixo = self.txt_m_carro.text()
        motorista = self.txt_m_motorista.text()
        material = []

        if self.ob_m_vassoura.isChecked():
            material.append('Vassoura')

        if self.ob_m_marreta.isChecked():
            material.append('Marreta')

        RegistroMateriais.registro_material(prefixo, motorista, material)

        self.txt_m_carro.clear()
        self.txt_m_motorista.clear()
        self.ob_m_vassoura.setChecked(False)
        self.ob_m_marreta.setChecked(False)

    def registrar_manutencao(self):
        prefixo = self.txt_ma_carro.text()
        manutencao = []

        if self.ob_ma_lavagem.isChecked():
            manutencao.append('LAVAGEM INTERNA')
            

        if self.ob_ma_manutencao.isChecked():
            manutencao.append('MANUTENÇÃO')
            

        if self.ob_ma_mecanica.isChecked():
            manutencao.append('MECÂNICA')
            

        if self.ob_ma_eletrica.isChecked():
            manutencao.append('ELÉTRICA')
            

        if self.ob_ma_borracharia.isChecked():
            manutencao.append('BORRACHARIA')

        if self.ob_ma_funilaria.isChecked():
            manutencao.append('FUNILÁRIA') 
        
        RegistroManutencao.registro_manutencao(prefixo, manutencao)

        self.txt_m_carro.clear()
        self.ob_ma_lavagem.setChecked(False)
        self.ob_ma_manutencao.setChecked(False)
        self.ob_ma_mecanica.setChecked(False)
        self.ob_ma_eletrica.setChecked(False)
        self.ob_ma_borracharia.setChecked(False)
        self.ob_ma_funilaria.setChecked(False)
