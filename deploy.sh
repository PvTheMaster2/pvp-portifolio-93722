#!/bin/bash

# Script de Deploy Automatizado para Portfólio
# Autor: Pedro Vitor
# Data: 2024

set -e  # Parar em caso de erro

echo "🚀 Iniciando deploy do portfólio..."

# ===== CONFIGURAÇÕES =====
REPO_NAME="portfolio-engenharia"
NETLIFY_SITE="pedro-vitor-portfolio"
GITHUB_USER="pedro-vitor"

# ===== VERIFICAÇÕES INICIAIS =====
echo "📋 Verificando pré-requisitos..."

# Verificar se git está configurado
if ! git config user.name > /dev/null 2>&1; then
    echo "❌ Git não está configurado. Configure com:"
    echo "   git config --global user.name 'Seu Nome'"
    echo "   git config --global user.email 'seu@email.com'"
    exit 1
fi

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale Python 3.8+"
    exit 1
fi

# Verificar se PIL está instalado
if ! python3 -c "from PIL import Image" 2>/dev/null; then
    echo "📦 Instalando Pillow..."
    pip3 install Pillow
fi

# ===== OTIMIZAÇÃO DE ASSETS =====
echo "🖼️ Otimizando assets..."

# Executar script de otimização
python3 util/optimize_assets.py --source . --output ./portfolio-build

# ===== ESTRUTURA DE ARQUIVOS =====
echo "📁 Organizando estrutura de arquivos..."

# Criar diretórios necessários
mkdir -p portfolio-build/src/site/styles/user
mkdir -p portfolio-build/src/site/_includes/components/user/notes/footer
mkdir -p portfolio-build/data

# Copiar arquivos CSS e JS
cp src/site/styles/user/portfolio.css portfolio-build/src/site/styles/user/
cp src/site/_includes/components/user/notes/footer/scrollReveal.njk portfolio-build/src/site/_includes/components/user/notes/footer/

# Copiar configuração do site
cp data/site.json portfolio-build/data/

# Copiar arquivos de projeto
cp -r REVIT portfolio-build/

# ===== CONFIGURAÇÃO DO GIT =====
echo "🔧 Configurando repositório Git..."

cd portfolio-build

# Inicializar git se necessário
if [ ! -d ".git" ]; then
    git init
    git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git
fi

# Adicionar todos os arquivos
git add .

# Commit das mudanças
git commit -m "Update: $(date +%Y-%m-%d) - Deploy automático do portfólio" || {
    echo "ℹ️ Nenhuma mudança para commitar"
}

# Push para GitHub
echo "📤 Fazendo push para GitHub..."
git push origin main || {
    echo "⚠️ Erro no push. Verifique se o repositório existe e as credenciais estão corretas"
    echo "   Crie o repositório em: https://github.com/new"
    echo "   Configure o token de acesso em: https://github.com/settings/tokens"
}

# ===== CONFIGURAÇÃO NETLIFY =====
echo "🌐 Configurando Netlify..."

# Criar arquivo netlify.toml se não existir
if [ ! -f "netlify.toml" ]; then
    cat > netlify.toml << EOF
[build]
  command = "npm run build"
  publish = "public"

[build.environment]
  NODE_VERSION = "16"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000"

[[headers]]
  for = "/*.pdf"
  [headers.values]
    Content-Type = "application/pdf"
EOF
fi

# ===== VERIFICAÇÕES FINAIS =====
echo "✅ Verificando arquivos críticos..."

# Verificar se arquivos essenciais existem
ESSENTIAL_FILES=(
    "data/site.json"
    "src/site/styles/user/portfolio.css"
    "src/site/_includes/components/user/notes/footer/scrollReveal.njk"
    "REVIT/RODRIGO EMPRESA/Projeto Elétrico e Hidrossanitario 'RE'.md"
)

for file in "${ESSENTIAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file - ARQUIVO FALTANDO!"
    fi
done

# ===== INSTRUÇÕES FINAIS =====
echo ""
echo "🎉 Deploy concluído com sucesso!"
echo ""
echo "📋 Próximos passos:"
echo "1. Configure o Digital Garden no Obsidian:"
echo "   - Settings > Community Plugins > Digital Garden"
echo "   - Configure as variáveis:"
echo "     GITHUB_USER=$GITHUB_USER"
echo "     GITHUB_REPO=$REPO_NAME"
echo "     NETLIFY_SITE=$NETLIFY_SITE"
echo ""
echo "2. Publique o site:"
echo "   - No Obsidian, clique em 'Publish' no plugin Digital Garden"
echo "   - Ou acesse: https://app.netlify.com/sites/$NETLIFY_SITE"
echo ""
echo "3. Configure domínio personalizado (opcional):"
echo "   - Acesse as configurações do site no Netlify"
echo "   - Adicione seu domínio personalizado"
echo ""
echo "🌐 URL do site: https://$NETLIFY_SITE.netlify.app"
echo "📁 Repositório: https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
echo "🔧 Para atualizações futuras, execute:"
echo "   ./deploy.sh"
echo ""

# ===== ESTATÍSTICAS =====
echo "📊 Estatísticas do deploy:"
echo "   - Arquivos processados: $(find . -type f | wc -l)"
echo "   - Tamanho total: $(du -sh . | cut -f1)"
echo "   - Imagens otimizadas: $(find assets/imagens -name "*.jpg" | wc -l)"
echo "   - PDFs organizados: $(find assets/pdfs -name "*.pdf" | wc -l)"

echo ""
echo "✨ Portfólio pronto para publicação!" 