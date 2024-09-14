# SOE2P
# Para executar o programa, baixe os 2 arquivos e coloqueos na mesma pasta.
# Após isso abra o x64 Native Tools Command Prompt for VS
# Uma vez aberto, use o comando cd para abrir a pasta onde os 2 arquivos estão
# Uma vez na pasta com os arquivos digite o comando: cl/LD [nome do arquivo] /Fe:[nome da DLL]
# Isso vai gerar a dll para windows 64 bits
# Abra o arquivo .py e garanta que ele está importando o CDLL da biblioteca ctypes
# Faça com que a variável dll esteja referenciando a dll recém criada [ dll = CDLL("./[nome da DLL].dll") ]
# Rode o programa
