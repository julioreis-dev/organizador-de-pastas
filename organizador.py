import os


def definir_extensao(arq):
    index = arq.rfind('.')
    extensao = arq[index:]
    return extensao


def catalogar_arquivos(pasta_atual):
    lista_arquivos = os.listdir(pasta_atual)
    return lista_arquivos


def enderecar_arquivo(pasta):
    pasta_audio = os.path.join(pasta, 'audios')
    pasta_videos = os.path.join(pasta, 'videos')
    pasta_imagem = os.path.join(pasta, 'fotos')
    pasta_documento = os.path.join(pasta, 'documentos')
    pasta_diversos = os.path.join(pasta, 'geral')
    pasta_executavel = os.path.join(pasta, 'drives')
    tupla_enderecos = (pasta_audio, pasta_videos, pasta_imagem, pasta_documento, pasta_diversos, pasta_executavel)
    return tupla_enderecos


def listar_extensao(arquivos):
    lista_extensao = []
    extensao_extraida = str.lower(definir_extensao(arquivos))
    lista_extensao.append(arquivo)
    lista_extensao.append(extensao_extraida)
    return lista_extensao


def criar_pastas(tupla):
    for n in tupla:
        if not os.path.isdir(n):
            os.mkdir(n)


def mover_pasta(origem, destino, ext):
    try:
        ext_audio = ['.mp3', '.wav']
        ext_video = ['.mp4', '.mov', '.avi']
        ext_imagem = ['.jpg', '.jpeg', '.png']
        ext_doc = ['.txt', '.log', '.pdf']
        ext_executavel = ['.exe']
        enderecos = enderecar_arquivo(destino)
        if ext[1] in ext_audio:
            os.rename(os.path.join(origem, ext[0]), os.path.join(enderecos[0], ext[0]))
        elif ext[1] in ext_video:
            os.rename(os.path.join(origem, ext[0]), os.path.join(enderecos[1], ext[0]))
        elif ext[1] in ext_imagem:
            os.rename(os.path.join(origem, ext[0]), os.path.join(enderecos[2], ext[0]))
        elif ext[1] in ext_doc:
            os.rename(os.path.join(origem, ext[0]), os.path.join(enderecos[3], ext[0]))
        elif ext[1] in ext_executavel:
            os.rename(os.path.join(origem, ext[0]), os.path.join(enderecos[5], ext[0]))
        else:
            os.rename(os.path.join(origem, ext[0]), os.path.join(enderecos[4], ext[0]))
    except FileExistsError:
        file_remove = os.path.join(origem, ext[0])
        os.remove(file_remove)
        print('Arquivo existente!!!')


pasta_origem = 'Downloads'
pasta_destino = r'C:\Users\ay4m\Desktop\outros'
criar_pastas(enderecar_arquivo(pasta_destino))
arquivos_pasta = catalogar_arquivos(pasta_origem)
for arquivo in arquivos_pasta:
    status_arquivo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(status_arquivo):
        lista_dados = listar_extensao(arquivo)
        mover_pasta(pasta_origem, pasta_destino, lista_dados)
print('Processo realizado com sucesso!!!')
