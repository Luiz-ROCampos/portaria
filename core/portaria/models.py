from PySide6.QtWidgets import QMessageBox

from sqlalchemy import DateTime, Table, create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# Criando o banco de dados
engine = create_engine('sqlite:///db_portaria.db', echo=True)

# Criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# TABELA CADASTRO FORNECEDOR
class CadastroFornecedor(Base):
    __tablename__ = "cadastro_fornecedores"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_fornecedor = Column("nome_fornecedor", String, nullable=True)
    nome_entregador = Column("nome_entregador", String, nullable=True)
    numero_rg = Column("numero_rg", String, nullable=True)
    placa_carro = Column("placa_carro", String, nullable=True)

    def __init__(self, nome_fornecedor, nome_entregador, numero_rg, placa_carro):
        self.nome_fornecedor = nome_fornecedor
        self.nome_entregador = nome_entregador
        self.numero_rg = numero_rg
        self.placa_carro = placa_carro

    def __str__(self):
        return self.nome_fornecedor
    
    @staticmethod
    def checar_fornecedor(fornecedor, entregador, rg): 
        lista_fornecedor = session.query(CadastroFornecedor).filter_by(nome_fornecedor = fornecedor)
        for lista in lista_fornecedor:
            if lista.nome_entregador == entregador and lista.numero_rg == rg:
                return True
            else:
                return False
            
    @staticmethod 
    def cadastrar_fornecedor(fornecedor, entregador, rg, placa):
        if not CadastroFornecedor.checar_fornecedor(fornecedor, entregador, rg):
            try:
                fornecedor = CadastroFornecedor(nome_fornecedor=fornecedor, nome_entregador=entregador, numero_rg=rg, placa_carro=placa)
                session.add(fornecedor)
                session.commit()
                mensagem_sucesso("Cadastro realizado", f"Fornecedor/Visitante {fornecedor.nome_fornecedor} foi registrado com sucesso.")
            except:
                session.rollback()
                mensagem('Cadastro Não Realixado', f'Erro interno no sistema!')
        else:
            mensagem("Cadastro existente!", "Fornecedor/Visitante já está cadastrado no sistema.")
            return None
             
    @staticmethod 
    def carregar_lista_fornecedor():
        lista_fornecedor = session.query(CadastroFornecedor.nome_fornecedor).distinct().all()
        return lista_fornecedor

    @staticmethod
    def listar_cadastro_fornecedor():
        lista = session.query(CadastroFornecedor).all()
        return lista

# TABELA REGISTRO FORNECEDOR
class RegistroFornecedor(Base):
    __tablename__ = "registro_fornecedores"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    fornecedor = Column("fornecedor", String, nullable=True)
    entregador = Column("entregador", String, nullable=True)
    rg = Column("rg", String, nullable=True)
    placa = Column("placa", String, nullable=True)
    cracha = Column("cracha", Integer, nullable=False)
    departamento = Column("departamento", String, nullable=True)
    autorizadopor = Column("autorizadopor", String, nullable=True)
    hora_entrada = Column("hora_entrada", DateTime, nullable=True)
    hora_saida = Column("hora_saida", DateTime, default=None)

    def __init__(self, fornecedor, entregador, rg, placa, cracha, departamento, autorizadopor, hora_entrada, hora_saida):
        self.fornecedor = fornecedor
        self.entregador = entregador
        self.rg = rg
        self.placa = placa
        self.cracha = cracha
        self.departamento = departamento
        self.autorizadopor = autorizadopor
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida

    def __str__(self):
        return self.fornecedor
    
    @staticmethod
    def listar_entrada_fornecedor():
        lista_fornecedor = session.query(RegistroFornecedor).filter(RegistroFornecedor.hora_saida.is_(None)).all()
        return lista_fornecedor
    
    @staticmethod
    def registrar_fornecedor(entregador_id, placa, cracha, departamento, autorizadopor):
        entregador = session.query(CadastroFornecedor).filter_by(id=entregador_id).first()
        data = datetime.now()

        try:
            registro_fornecedor = RegistroFornecedor(
                fornecedor=entregador.nome_fornecedor, 
                entregador=entregador.nome_entregador, 
                rg=entregador.numero_rg, 
                placa=placa, 
                cracha=cracha, 
                departamento= departamento, 
                autorizadopor=autorizadopor, 
                hora_entrada=data, 
                hora_saida=None
                )
            session.add(registro_fornecedor)
            session.commit()
            mensagem_sucesso('Registro realizado', f'A entrada do fornecedor/Visitante: {entregador.nome_fornecedor} foi registrada com sucesso.')
        except:
            session.rollback()
            mensagem('Registro Não realizado', f'Erro interno no sistema!')

    @staticmethod
    def registrar_saida_fornecedor(fornecedor_id):
        data = datetime.now()
        fornecedor = session.query(RegistroFornecedor).filter(RegistroFornecedor.id == fornecedor_id).first()
        if fornecedor:
            try:
                fornecedor.hora_saida = data
                session.commit()
                mensagem_sucesso('Registro Realizado.', f'A saída do fornecedor/Visitante: {fornecedor.fornecedor}, foi registrada com sucesso.')
            except:
                session.rollback()
                mensagem('Registro Não Realizado', f'Erro interno no sistema!')
        else:
            mensagem('Registro não existente', f'Não Existe a entrada do fornecedor/Visitante: {fornecedor.fornecedor}, saída não registrada.')
            return None
        
# TABELA CADASTRO DE TERCEIROS
class CadastroTeiceiro(Base):
    __tablename__ = "cadastro_terceiros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=True)
    total = Column("total", Integer, nullable=True)
    quantidade = Column("quantidade", Integer, nullable=True, default=0)

    def __init__(self, nome, total, quantidade):
        self.nome = nome
        self.total = total
        self.quantidade = quantidade

    def __str__(self):
        return self.nome
    
    @staticmethod
    def cadastrar_terceiro(nome, total):
        try:
            novo_cadastro = CadastroTeiceiro(
                nome=nome,
                total=total,
                quantidade=0
            )
            session.add(novo_cadastro)
            session.commit()
            mensagem_sucesso('Cadastro Realizado.', f'O {nome} foi cadastrado com sucesso.')
        except:
            session.rollback()
            mensagem('Cadastro Não Realizado.', 'Erro: não foi possivél realizar o cadastro.')
              
    @staticmethod
    def listar_terceiros():
        lista_terceiro = session.query(CadastroTeiceiro).all()
        return lista_terceiro

# TABELA REGISTRO DE TERCEIROS
class RegistroTeiceiro(Base):
    __tablename__ = "registro_terceiros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    viacao = Column("viacao", String, nullable=False)
    prefixo = Column("prefixo", Integer, nullable=False)
    hora_entrada = Column("hora_entrada", DateTime, default=None)
    hora_saida = Column("hora_saida", DateTime, default=None)

    def __init__(self, viacao, prefixo, hora_entrada, hora_saida):
        self.viacao = viacao
        self.prefixo = prefixo
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida

    def __str__(self):
        return self.viacao
    
    @staticmethod
    def listar_terceiros_entrada(prefixo):
        lista_terceiros = session.query(RegistroTeiceiro).filter(RegistroTeiceiro.prefixo == prefixo).filter(RegistroTeiceiro.hora_saida.is_(None)).first()
        return lista_terceiros

    @staticmethod
    def resgitrar_terceiro_entrada(viacao, prefixo):
        data = datetime.now()
        try:
            registro_terceiro = RegistroTeiceiro(viacao=viacao, prefixo=prefixo, hora_entrada=data, hora_saida=None)
            session.add(registro_terceiro)
            cadastro_terceiro = session.query(CadastroTeiceiro).filter(CadastroTeiceiro.nome == registro_terceiro.viacao).first()
            if cadastro_terceiro:
                cadastro_terceiro.quantidade = (cadastro_terceiro.quantidade or 0) + 1
                session.add(cadastro_terceiro)
            session.commit()
            mensagem_sucesso('Registro realizado', f'A entrada do {registro_terceiro.viacao} foi registrada com sucesso.')
        except:
            session.rollback()
            mensagem('Registro não realizado', f'A entrada do {registro_terceiro.viacao} não foi registrada.')

    @staticmethod
    def resgitrar_terceiro_saida(prefixo):
        data = datetime.now()
        lista_terceiro = RegistroTeiceiro.listar_terceiros_entrada(prefixo)
        try:
            registro_terceiro = session.query(RegistroTeiceiro).filter(RegistroTeiceiro.prefixo==lista_terceiro.prefixo).filter(RegistroTeiceiro.hora_entrada==lista_terceiro.hora_entrada).first()
            registro_terceiro.hora_saida = data
            session.add(registro_terceiro)

            cadastro_terceiro = session.query(CadastroTeiceiro).filter(CadastroTeiceiro.nome == lista_terceiro.viacao).first()
            
            if cadastro_terceiro:
                cadastro_terceiro.quantidade = (cadastro_terceiro.quantidade or 0) - 1
                session.add(cadastro_terceiro)
            
            session.commit()
            mensagem_sucesso('Registro realizado', f'A saída do {registro_terceiro.viacao} foi registrada com sucesso.')
        except:
            session.rollback()
            mensagem('Registro não realizado', f'A saída do {registro_terceiro.viacao} não foi registrada.')

# TABELA DE DEPARTAMENTOS
class Departamento(Base):
    __tablename__ = "cadastro_departamento"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
    
    @staticmethod
    def registrar_departamento(nome):
            novo_departamento = Departamento(
                nome=nome
                )
            session.add(novo_departamento)
            session.commit()
            mensagem_sucesso('Registro realizado', f'Departamento {novo_departamento.nome} registrado com sucesso.')
            return novo_departamento
       
    @staticmethod
    def deletar_departamento(id):
        departamento = session.query(Departamento).filter(Departamento.id == id).first()
        if departamento:
            try:
                session.delete(departamento)
                session.commit()
                mensagem_sucesso('Registro realizado', f'Departamento {departamento.nome} excluido com sucesso.')
                return departamento.nome
            except:
                session.rollback()
                mensagem('Registro não realizado', f'Erro: Departamento {departamento.nome} não foi excluido.')
        else:
            return mensagem('Registro não realizado', f'Erro: Departamento não foi encontrado.')
        
    @staticmethod
    def atualizar_departamento(novo_nome):
        departamento = session.query(Departamento).filter(Departamento.nome == novo_nome).first()
        if departamento:
            try:
                departamento.nome = novo_nome
                session.commit()
                mensagem_sucesso('Registro realizado', f'Departamento {departamento.nome} atualizado com sucesso.')
                return departamento.nome
            except:
                session.rollback()
                mensagem('Registro não realizado', f'Erro: Departamento {departamento.nome} não foi atualizado.')
        else:
            return mensagem('Registro não realizado', f'Erro: Departamento não foi encontrado.')
    
    @staticmethod
    def lista_departamento():
        departamento = session.query(Departamento).all()
        return departamento

# TABELA DE CADASTRO DE COLABORADORES
class CadastroColaboradores(Base):
    __tablename__ = "cadastro_colaborador"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    departamento_id = Column("departamento_id", Integer, ForeignKey("cadastro_departamento.id"))
    setor = Column("setor", String, nullable=False)
    status = Column("status", Boolean, default=True)

    departamento = relationship("Departamento", backref="colaboradores")

    def __init__(self, nome, departamento_id, setor, status):
        self.nome = nome
        self.departamento_id = departamento_id
        self.setor = setor
        self.status = status
    
    def __str__(self):
        return self.nome

    @staticmethod
    def adicionar_colaborador(nome, departamento_id, setor, status=True):
        try:
            novo_colaborador = CadastroColaboradores(
            nome=nome,
            departamento_id=departamento_id,
            setor=setor,
            status=status
            )
            session.add(novo_colaborador)
            session.commit()
            mensagem_sucesso("Cadatro Realizado", f"Colaborador '{nome}' adicionado com sucesso!")

            return novo_colaborador
        except:
            session.rollback()
            mensagem("Cadatro Não Realizado", f"Colaborador '{nome}' não foi adicionado!")
            return None

    @staticmethod
    def listar_colaborador():
            lista_colaborador = session.query(CadastroColaboradores).all()
            return lista_colaborador

    @staticmethod
    def listar_colaborador_por_departamento(departamento_id):
        colaboradores = session.query(CadastroColaboradores).filter_by(departamento_id=departamento_id).all()    
        return colaboradores

# TABELA DE REGISTRO DE COLABORADORES
class RegistroColaboradores(Base):
    __tablename__ = "registro_colaborador"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    departamento_id = Column("departamento_id", Integer, ForeignKey("cadastro_departamento.id"))
    setor = Column("setor", String, nullable=False)
    entrada = Column("entrada", DateTime)
    saida_a = Column("saida_a", DateTime, default=None)
    entrada_a = Column("entrada_a", DateTime, default=None)
    saida = Column("saida", DateTime, default=None)

    departamento = relationship("Departamento", backref="registro_colaborador")

    def __init__(self, nome, departamento_id, setor, entrada, saida_a, entrada_a, saida):
        self.nome = nome
        self.departamento_id = departamento_id
        self.setor = setor
        self.entrada = entrada
        self.saida_a = saida_a
        self.entrada_a = entrada_a
        self.saida = saida

    def __str__(self):
        return self.nome
    
    @staticmethod
    def listar_colaborador_departamento(nome, departamento_id):
        colaborador = session.query(RegistroColaboradores).filter(RegistroColaboradores.departamento_id==departamento_id).filter(RegistroColaboradores.nome==nome).first()
        return colaborador
    
    @staticmethod
    def registrar_colaborador_entrada(departamento_id, colaborador):
        
        data = datetime.now()
        lista = session.query(RegistroColaboradores).filter(RegistroColaboradores.departamento_id==departamento_id).filter(RegistroColaboradores.nome==colaborador).first()
        if lista:
            mensagem('Registro Existente', f'Existe a entrada do colaborador {lista.nome}, entrada não registrada.')
            session.rollback()
        else:
            try:
                lista = session.query(CadastroColaboradores).filter(CadastroColaboradores.nome==colaborador).first()
                novo_registro = RegistroColaboradores(
                    nome=colaborador,
                    departamento_id=departamento_id,
                    setor=lista.setor,
                    entrada=data,
                    saida_a=None,
                    entrada_a=None,
                    saida=None
                )
                session.add(novo_registro)
                session.commit()
                mensagem_sucesso('Registro realizado', f'A entrada do {novo_registro.nome} foi registrada com sucesso.')
            except:
                session.rollback()
                mensagem('Registro Não Realixado', f'Erro interno no sistema!')
    
    @staticmethod
    def registrar_colaborador_saida_a(departamento_id, colaborador):
        data = datetime.now()
        
        lista = session.query(RegistroColaboradores).filter(RegistroColaboradores.departamento_id==departamento_id).filter(RegistroColaboradores.nome==colaborador and RegistroColaboradores.saida_a=='').first()
        
        if lista:
            try:
                lista.saida_a = data
                session.commit()
                mensagem_sucesso('Registro realizado', f'A Saída do almoço do {lista.nome} foi registrada com sucesso.')
            except:
                session.rollback()
                mensagem('Registro não encontrado', f'A entrada do {lista.nome} não foi encontrado.')
        else:
            try:      
                lista = session.query(CadastroColaboradores).filter(CadastroColaboradores.nome==colaborador).first()  
                novo_registro = RegistroColaboradores(
                    nome=colaborador,
                    departamento_id=departamento_id,
                    setor=lista.setor,
                    entrada=None,
                    saida_a=data,
                    entrada_a=None,
                    saida=None
                    )
                session.add(novo_registro)
                session.commit()     
                mensagem_sucesso('Registro realizado', f'A retorno do almoço do {novo_registro.nome} foi registrado com sucesso.')
            except:
                session.rollback()
                mensagem('Registro não encontrado', f'A entrada do {novo_registro.nome} não foi encontrado.')
    
    @staticmethod
    def registrar_colaborador_entrada_a(departamento_id, colaborador):
        data = datetime.now()
        
        lista = session.query(RegistroColaboradores).filter(RegistroColaboradores.departamento_id==departamento_id).filter(RegistroColaboradores.nome==colaborador and RegistroColaboradores.entrada_a=='').first()

        if lista:
            try:
                lista.entrada_a = data
                session.commit()
                mensagem_sucesso('Registro realizado', f'A retorno do almoço do {lista.nome} foi registrada com sucesso.')
            except:
                session.rollback()
                mensagem('Registro não encontrado', f'A entrada do {lista.nome} não foi encontrado.')
        else:
            try:        
                lista = session.query(CadastroColaboradores).filter(CadastroColaboradores.nome==colaborador).first()
                novo_registro = RegistroColaboradores(
                    nome=colaborador,
                    departamento_id=departamento_id,
                    setor=lista.setor,
                    entrada=None,
                    saida_a=None,
                    entrada_a=data,
                    saida=None
                    )
                session.add(novo_registro)
                session.commit()     
                mensagem_sucesso('Registro realizado', f'A retorno do almoço do {novo_registro.nome} foi registrado com sucesso.')
            except:
                session.rollback()
                mensagem('Registro não encontrado', f'A entrada do {novo_registro.nome} não foi encontrado.')
    
    @staticmethod
    def registrar_colaborador_saida(departamento_id, colaborador):
        data = datetime.now()
        
        lista = session.query(RegistroColaboradores).filter(RegistroColaboradores.departamento_id==departamento_id).filter(RegistroColaboradores.nome==colaborador and RegistroColaboradores.saida=='').first()
        
        if lista:
            lista.saida = data
            session.commit()
            mensagem_sucesso('Registro realizado', f'A Saída do {lista.nome} foi registrada com sucesso.')
        else:
            try:
                lista = session.query(CadastroColaboradores).filter(CadastroColaboradores.nome==colaborador).first()        
                novo_registro = RegistroColaboradores(
                    nome=colaborador,
                    departamento_id=departamento_id,
                    setor=lista.setor,
                    entrada=None,
                    saida_a=None,
                    entrada_a=None,
                    saida=data
                    )
                session.add(novo_registro)
                session.commit()           
                mensagem_sucesso('Registro realizado', f'A Saída do {novo_registro.nome} foi registrada com sucesso.')
            except:
                session.rollback()
                mensagem('Registro Não Realixado', f'Erro interno no sistema!')
                return None
# TABELA DE CHAVES
class Chaves(Base):
    __tablename__ = 'cadastro_chave'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    numero = Column('numero', Integer, nullable=False, unique=True)
    setor = Column('setor', String, nullable=False, unique=True)

    def __init__(self, numero, setor):
        self.numero = numero
        self.setor = setor

    def __str__(self):
        return self.nome_setor
    
    @staticmethod
    def cadastro_chave(numero, setor):
        try:
            novo_setor = Chaves(
                numero=numero,
                setor=setor
            )
            session.add(novo_setor)
            session.commit()
            mensagem_sucesso('Cadastro relizado', f'Setor {setor} cadastrado com sucesso.')
            return setor
        except:
            session.rollback()
            mensagem('Cadastro não realizado', 'Erro: Cadastro não realiado')

    @staticmethod
    def listar_chave():
        lista_chave = session.query(Chaves).all()
        return lista_chave

# TABELA DE VIGILANTES
class Vigilantes(Base):
    __tablename__ = 'vigilante'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=True, unique=True)

    def __init__(self, nome):
        self.nome=nome

    def __str__(self):
        return self.nome
    
    @staticmethod
    def cadastrar_vigilante(nome):
        try:
            novo_vigilante = Vigilantes(
                nome=nome
            )
            session.add(novo_vigilante)
            session.commit()
            mensagem_sucesso('Cadastro realizado', f'O vigilante {novo_vigilante.nome} foi cadastrado com sucesso.')
        except:
            session.rollback()
            mensagem('Cadastro não realizado', 'Erro: vigilante não cadastrado.')

    @staticmethod
    def listar_vigilante():
        lista_vigilante = session.query(Vigilantes).all()
        return lista_vigilante

# TABELA DE REGISTRO CHAVES
class RegistroChaves(Base):
    __tablename__ = 'registro_chave'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    colaborador = Column('colaborador', String, nullable=False)
    chave_setor_id = Column('chave_setor_id', Integer, ForeignKey('cadastro_chave.id'), nullable=False)
    retirada = Column('retirada', DateTime, nullable=False)
    devolucao = Column('devolucao', DateTime, default=None)
    vigilante_id = Column('vigilante_id', Integer, ForeignKey('vigilante.id'), nullable=False)

    chave = relationship("Chaves", backref="chave_registros")
    vigilante = relationship("Vigilantes", backref="vigilante_registros")

    def __init__(self, colaborador, chave_setor_id, retirada, devolucao, vigilante_id):
        self.colaborador = colaborador
        self.chave_setor_id = chave_setor_id
        self.retirada = retirada
        self.devolucao = devolucao
        self.vigilante_id = vigilante_id

    def __str__(self):
        return f"Registro de Chave #{self.chave_setor_id} - Retirada por colaborador ID {self.colaborador_id}"

    @staticmethod
    def registro_chave(colaborador, chave_setor, nome_vigilante):
        chave = session.query(Chaves).filter(Chaves.setor == chave_setor).first()
        vigilante = session.query(Vigilantes).filter(Vigilantes.nome == nome_vigilante).first()

        if not chave:
            mensagem('Erro', 'Chave não foi encontrada.')
            return None

        if not vigilante:
            mensagem('Erro', 'Vigilante não encontrado.')
            return None

        registro = session.query(RegistroChaves).filter(
            RegistroChaves.chave_setor_id == chave.id,
            RegistroChaves.devolucao == None
        ).first()

        if registro:
            mensagem_sucesso('Registro existente', 'A chave já está registrada e não foi devolvida.')
            return None
        else:
            try:
                data = datetime.now()
                novo_registro = RegistroChaves(
                    colaborador=colaborador,
                    chave_setor_id=chave.id,
                    retirada=data,
                    devolucao=None,
                    vigilante_id=vigilante.id
                )
                session.add(novo_registro)
                session.commit()
                mensagem_sucesso('Registro realizado', f'A chave do setor {chave.setor} foi registrada com sucesso pelo vigilante {vigilante.nome}.')
                return novo_registro
            except Exception as e:
                session.rollback()
                mensagem('Erro', 'Não foi possível registrar a chave.')
                return None
        
    @staticmethod
    def listar_chave_entrada():
        lista_chave = session.query(RegistroChaves).filter(RegistroChaves.devolucao == None).all()
        return lista_chave

    @staticmethod
    def registro_chave_saida(chave_id):
        data = datetime.now()
        chave = session.query(RegistroChaves).filter(RegistroChaves.id == chave_id).first()
        if chave:
            try:
                chave.devolucao = data
                session.commit()
                mensagem_sucesso('Registro Realizado.', 'A Devolução da chave foi registrada com sucesso.')
            except:
                session.rollback()
                mensagem('Registro Não Realixado', 'Erro interno no sistema!')
        else:
            mensagem('Registro não existente', 'Não Existe a retirada da chave, saída não registrada.')
            return None
            
# TABELA DE MATERIAIS
class RegistroMateriais(Base):
    __tablename__ = 'registro_materiais'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    prefixo = Column('prefixo', Integer, nullable=False)
    motorista = Column('motorista', String, nullable=False)
    material = Column('material', String, nullable=False)

    def __init__(self, prefixo, motorista, material):
        self.prefixo = prefixo
        self.motorista = motorista
        self.material = material

    def __str__(self):
        return self.prefixo
    
    @staticmethod
    def registro_material(prefixo, motorista, material):
        
        try:
            material_str = ", ".join(material)
            novo_registro = RegistroMateriais(
                prefixo=prefixo,
                motorista=motorista,
                material=material_str
            )
            session.add(novo_registro)
            session.commit()
            mensagem_sucesso('Registro realizado', f'A retirada do material foi registrada com sucesso.')
        except:
            session.rollback()
            mensagem('Registro não realizado', 'Erro: material não registrado.')

    @staticmethod
    def lista_material():
        lista = session.query(RegistroMateriais).all()
        return lista

# TABELA DE SERVIÇOS
class RegistroManutencao(Base):
    __tablename__ = 'registro_manutencao'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    prefixo = Column('prefixo', Integer, nullable=False)
    servico = Column('servico', String, nullable=False)

    def __init__(self, prefixo, servico):
        self.prefixo = prefixo
        self.servico = servico

    def __str__(self):
        return self.prefixo
    
    @staticmethod
    def registro_manutencao(prefixo, servico):
        try:
            servicos_str = ", ".join(servico)
            novo_registro = RegistroManutencao(
                prefixo=prefixo,
                servico=servicos_str
            )
            session.add(novo_registro)

            session.commit()
            mensagem_sucesso('Registro Realizado.', 'O serviço foi registrado com sucesso.')
        except:
            session.rollback()
            mensagem('Registro Não Realizado', 'Erro: o serviço não foi reagistrado.')

    @staticmethod
    def lista_manutencao(self):
        lista = session.query(RegistroManutencao).all()
        return lista

#CadastroFornecedor.cadastrar_fornecedor('Pneus Bus','Juliano Teixeira', 4567834523, 'FGD-5198')

#RegistroFornecedor.registrar_fornecedor( 1, "QWE-8765", 1, 2, "autorizadopor")

#CadastroTeiceiro.cadastrar_terceiro('Nicolau', 1)
    
#CadastroColaboradores.adicionar_colaborador(nome='Geraldo', departamento_id=13, setor='Gerente Manutenção')
    
#RegistroColaboradores.registrar_colaborador_saida('Tatiane', 13, 'GERENTE TR')
                
#RegistroColaboradores.registrar_colaborador_entrada(nome="José",departamento_id=7,setor="bilhetagem") # Valor obrigatório para 'setor')

#Vigilantes.cadastrar_vigilante('Rafael')

#Departamento.registrar_departamento('GERENCIA')

#Chaves.cadastro_chave(3, 'Almoxarifado')
        
#RegistroChaves.registro_chave('ANA','RH', 'Rafael')

# MENSAGEM DO SISTEMA
def mensagem(titulo, mensagens):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titulo)
    msg.setText(mensagens)
    msg.exec_()

def mensagem_sucesso(titulo, mensagens):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(titulo)
    msg.setText(mensagens)
    msg.exec_()

#Base.metadata.drop_all(engine)
#RegistroFornecedor.__table__.drop(engine)  

#Base.metadata.create_all(engine)
