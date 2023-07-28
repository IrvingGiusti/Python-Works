# TreinamentoDIO

## Comandos do Git

git config (Mostra as informações de comandos do Git)

CTRL + L (Limpa a tela)

git config --global user.name "Nome" (Configura o nome do usuário)

git config --global user.email E-mail
(Configurar o e-mail do usuário)

git config init.defaultBranch (Mostra o repositorio padrão)

git config --global init.defaultBranch main (Altera o nome do repositório padrão)

git config --global --list (lista as informação)

git clone "inserir caminho" (conecta ao repositorio do Github)

git config --global credential.helper cache (armazena a chave de acesso ao github teporariamente)

git config --global credential.helper store (armazena a chave de acesso ao github)

cat .gitconfig (mostra as informações configuradas)

cat .git-credentials (mostra a senha do token de acesso ao github)

git config --global --show-origin credential.helper (mostra o local de armazenamento do arquivo de configuração)

ls -a ~/.ssh (Verifica se existem chaves ssh salvas)

ssh-keygen -t ed25519 -C "insreir e-mail do Github" (gerar uma chave ssh)

eval "$(ssh-agent -s)" (valida a chave gerada)

ssh-add ~/.ssh/id_ed25519 (adiciona a chave gerada)

cd ~/.ssh (acessar o diretório onde está armazenada a chave)

ls (lista as informações)

cat id_ed25519.pub (exiber a chave ssh pública)

mkdir repo-local (criar diretório)

git init (inicializa o git no repositório informado)

git remote add origin +link do repositório do Github (conecta com o repositório remoto)

git clone +URL do repositório do Github +nome do repositório (adiciona o repositório com o nome escolhido)

touch (usado para criar um arquivo dentro do diretório)
git status (informa os status do diretório)

git add +nome do arquivo (Prepara o arquivo para ser comitado)

git add . (prepara todos os arquvis di diretório para serem commitados)

git commit -m”+texto de sua escolha” (comita o arquivo junto com uma mensagem)

echo +nome do diretório/ > .gitignore (ignora o diretório)

touch +nome do diretório/ .gitkeep (reconhecer diretórios vazios)

git log (mostra histórico de comits)

rm -rf .git (desfaz o git init)

git restore +nome do arquivo (restaura um arquivo que tenha sido alterado erroneamente)

git commit –amend -m”+texto de sua preferência” (altera o texto que foi usado no último comit)

git commint –amend (abre o editor para que seja alterado texto do último commit)

git reset –soft +hash do commit (desfaz o último commit)

git reset –mixed +hash do commit (desfaz todos os commint já realizados)

git reset –hard +hash do commint (limpa todo o repositório)

git reflog (apresenta um log de todos os commit realizados)

git remot add origin +URL do diretório no Github (adiciona o repositório do Github para o repositório local)

git push -u origin main (envia os arquivos do repositório local para o repositório remoto)

git pull (busca os arquivos do repositório remoto e atualiza no repositório local)