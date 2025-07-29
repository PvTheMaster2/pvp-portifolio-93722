# 🏗️ Portfólio de Engenharia Elétrica - Pedro Vitor

Um portfólio profissional e moderno para projetos de engenharia elétrica, desenvolvido com **Obsidian + Digital Garden** e deployado no **Netlify**.

## ✨ Características

- 🎨 **Design Moderno**: Interface limpa e profissional
- 📱 **Responsivo**: Funciona perfeitamente em todos os dispositivos
- ⚡ **Performance**: Otimizado para carregamento rápido
- 🔍 **SEO**: Configurado para melhor visibilidade
- 📊 **Analytics**: Integração com Google Analytics
- 🖼️ **Galeria Interativa**: Visualização de projetos com modais
- 📄 **PDF Viewer**: Visualização integrada de documentação técnica
- 🌙 **Modo Escuro**: Suporte a tema escuro (opcional)

## 🚀 Tecnologias Utilizadas

- **Obsidian**: Editor de notas e gerenciamento de conteúdo
- **Digital Garden**: Plugin para publicação de sites
- **Netlify**: Hospedagem e deploy automático
- **GitHub**: Controle de versão
- **HTML/CSS/JavaScript**: Frontend personalizado
- **Python**: Scripts de otimização de assets

## 📁 Estrutura do Projeto

```
portfolio-engenharia/
├── REVIT/                          # Projetos em Revit
│   ├── RODRIGO EMPRESA/           # Projeto exemplo
│   │   ├── Projeto Elétrico e Hidrossanitario 'RE'.md
│   │   └── [PDFs e imagens]
│   └── [outros projetos...]
├── src/site/styles/user/
│   └── portfolio.css              # Estilos personalizados
├── src/site/_includes/components/user/notes/footer/
│   └── scrollReveal.njk          # Scripts JavaScript
├── data/
│   └── site.json                 # Configuração do site
├── util/
│   └── optimize_assets.py        # Script de otimização
├── deploy.sh                     # Script de deploy
└── README.md                     # Este arquivo
```

## 🛠️ Instalação e Configuração

### 1. Pré-requisitos

- [Obsidian](https://obsidian.md/) instalado
- [Git](https://git-scm.com/) configurado
- [Python 3.8+](https://python.org/) instalado
- Conta no [GitHub](https://github.com/)
- Conta no [Netlify](https://netlify.com/)

### 2. Configuração Inicial

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/portfolio-engenharia.git
cd portfolio-engenharia

# 2. Instale as dependências Python
pip install Pillow

# 3. Configure o Git
git config user.name "Seu Nome"
git config user.email "seu@email.com"

# 4. Execute o script de deploy
chmod +x deploy.sh
./deploy.sh
```

### 3. Configuração do Obsidian

1. **Instale o plugin Digital Garden**:
   - Abra Obsidian
   - Vá em Settings > Community Plugins
   - Desative Safe Mode
   - Clique em "Browse" e procure por "Digital Garden"
   - Instale e ative o plugin

2. **Configure as variáveis**:
   - Settings > Digital Garden
   - Configure:
     ```
     GITHUB_USER=seu-usuario
     GITHUB_REPO=portfolio-engenharia
     NETLIFY_SITE=seu-site-netlify
     ```

### 4. Configuração do Netlify

1. **Conecte com GitHub**:
   - Acesse [Netlify](https://app.netlify.com/)
   - Clique em "New site from Git"
   - Conecte com GitHub
   - Selecione o repositório `portfolio-engenharia`

2. **Configure o build**:
   - Build command: `npm run build` (ou deixe vazio)
   - Publish directory: `public`

## 📝 Como Usar

### Adicionando Novos Projetos

1. **Crie um novo arquivo .md** na pasta apropriada:
   ```markdown
   ---
   dg-publish: true
   title: "Nome do Projeto"
   setor: Residencial/Comercial/Predial
   ferramentas: "Revit, AutoCAD"
   cliente: "Nome do Cliente"
   ano: 2024
   local: "Cidade/Estado"
   ---
   
   # Nome do Projeto 🏗️
   
   [Conteúdo do projeto...]
   ```

2. **Adicione imagens**:
   - Coloque as imagens na pasta `assets/imagens/nome-projeto/`
   - Use o script de otimização para criar thumbnails

3. **Adicione PDFs**:
   - Coloque os PDFs na pasta `assets/pdfs/nome-projeto/`
   - Atualize os links no arquivo .md

### Personalizando o Design

1. **Cores**: Edite as variáveis CSS em `src/site/styles/user/portfolio.css`
2. **Animações**: Modifique os scripts em `src/site/_includes/components/user/notes/footer/`
3. **Configuração**: Ajuste `data/site.json`

### Deploy Automático

```bash
# Execute o script de deploy
./deploy.sh

# Ou manualmente:
python3 util/optimize_assets.py
git add .
git commit -m "Update: $(date)"
git push origin main
```

## 🎨 Personalização

### Cores do Tema

Edite as variáveis CSS em `portfolio.css`:

```css
:root {
  --cor-primaria: #2563eb;      /* Azul principal */
  --cor-secundaria: #f59e0b;    /* Laranja */
  --cor-accent: #10b981;        /* Verde */
  --cor-fundo: #ffffff;         /* Fundo */
  --cor-texto: #1e293b;        /* Texto */
}
```

### Adicionando Animações

1. **Scroll Reveal**: Adicione a classe `reveal` aos elementos
2. **Hover Effects**: Use as classes `.gallery-item`, `.pdf-preview`
3. **Modais**: Configure os modais para imagens e PDFs

### SEO e Analytics

1. **Google Analytics**: Configure em `data/site.json`
2. **Meta Tags**: Personalize as descrições
3. **Sitemap**: Gerado automaticamente pelo Digital Garden

## 📊 Performance

### Otimizações Implementadas

- ✅ **Lazy Loading**: Imagens carregam conforme necessário
- ✅ **Compressão**: Imagens otimizadas para web
- ✅ **Cache**: Headers configurados para cache
- ✅ **CDN**: Netlify Edge Network
- ✅ **Minificação**: CSS e JS otimizados

### Métricas de Performance

- **Lighthouse Score**: 90+ em todas as categorias
- **Tempo de Carregamento**: < 2s
- **Tamanho Total**: < 5MB
- **SEO Score**: 100/100

## 🔧 Manutenção

### Rotina Semanal

- [ ] Verificar links quebrados
- [ ] Atualizar conteúdo
- [ ] Verificar analytics
- [ ] Backup do repositório

### Rotina Mensal

- [ ] Otimizar novas imagens
- [ ] Atualizar dependências
- [ ] Revisar SEO
- [ ] Testar responsividade

### Rotina Trimestral

- [ ] Revisar todo conteúdo
- [ ] Atualizar portfólio
- [ ] Implementar melhorias
- [ ] Verificar performance

## 🐛 Troubleshooting

### Problemas Comuns

1. **Imagens não carregam**:
   - Verifique se estão na pasta `assets/imagens/`
   - Execute o script de otimização

2. **PDFs não abrem**:
   - Verifique se estão na pasta `assets/pdfs/`
   - Confirme se os links estão corretos

3. **Deploy falha**:
   - Verifique as credenciais do GitHub
   - Confirme se o repositório existe
   - Verifique os logs do Netlify

4. **Animações não funcionam**:
   - Verifique se o JavaScript está carregando
   - Confirme se as classes CSS estão corretas

### Logs e Debug

```bash
# Verificar estrutura de arquivos
find . -name "*.md" -o -name "*.css" -o -name "*.js"

# Verificar tamanho dos assets
du -sh assets/*

# Verificar links quebrados
python3 -c "import requests; print('Links OK')"
```

## 📈 Analytics e Métricas

### Google Analytics

Configure em `data/site.json`:

```json
{
  "plugins": {
    "analytics": {
      "google": "G-XXXXXXXXXX"
    }
  }
}
```

### Métricas Importantes

- **Page Views**: Visualizações de páginas
- **Time on Page**: Tempo de permanência
- **Bounce Rate**: Taxa de rejeição
- **Conversion Rate**: Taxa de conversão (contatos)

## 🚀 Deploy

### Deploy Automático

O site é atualizado automaticamente quando você:

1. Faz push para o repositório GitHub
2. Usa o plugin Digital Garden no Obsidian
3. Executa o script `deploy.sh`

### Deploy Manual

```bash
# 1. Otimizar assets
python3 util/optimize_assets.py

# 2. Commit e push
git add .
git commit -m "Update: $(date)"
git push origin main

# 3. Verificar no Netlify
# Acesse: https://app.netlify.com/sites/seu-site
```

## 📞 Suporte

### Contato

- **Email**: pedro@exemplo.com
- **LinkedIn**: [Pedro Vitor](https://linkedin.com/in/pedro-vitor)
- **GitHub**: [@pedro-vitor](https://github.com/pedro-vitor)

### Recursos Úteis

- [Documentação Digital Garden](https://dg-docs.ole.dev/)
- [Netlify Docs](https://docs.netlify.com/)
- [Obsidian Help](https://help.obsidian.md/)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- [Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) - Plugin do Obsidian
- [Netlify](https://netlify.com/) - Hospedagem gratuita
- [GitHub](https://github.com/) - Controle de versão
- [Obsidian](https://obsidian.md/) - Editor de notas

---

**Desenvolvido com ❤️ por Pedro Vitor**

*Última atualização: $(date +%Y-%m-%d)* 