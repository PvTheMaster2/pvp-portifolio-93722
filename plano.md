# Plano de Implementação: Portfólio Online de Engenharia Elétrica

## 1. Setup Inicial

### 1.1 Configuração do Digital Garden
```bash
# 1. Acessar https://github.com/oleeskild/obsidian-digital-garden
# 2. Clicar no botão "Deploy to Netlify"
# 3. Seguir as instruções para criar o repositório e site Netlify
```

### 1.2 Configuração de Variáveis
```bash
# Definir estas variáveis no Obsidian (Settings > Digital Garden)
GITHUB_USER="seu-usuario-github"
GITHUB_REPO="seu-repositorio"
GH_TOKEN="seu-token-github"
NETLIFY_SITE="seu-site-netlify"
```

## 2. Estrutura de Pastas e Arquivos

```
/Projetos/
  /Residencial/ (8 arquivos .md)
  /Comercial/ (4 arquivos .md)
  /Predial/ (4 arquivos .md)
/assets/
  /imagens/<projeto>/
  /pdfs/<projeto>/
Home.md
src/site/styles/user/portfolio.css
src/site/_includes/components/
  user/common/head/anime.njk
  user/notes/footer/galleryModal.njk
  user/notes/footer/scrollReveal.njk
```

## 3. Arquivos Base

### 3.1 Home.md
```markdown
---
dg-publish: true
dg-home: true
title: "Portfólio de Engenharia Elétrica"
---

# Portfólio de Engenharia Elétrica

Bem-vindo ao meu portfólio profissional de projetos elétricos. Aqui você encontrará uma seleção dos meus trabalhos em diferentes segmentos:

## Categorias de Projetos

<div class="category-cards reveal">
  <a href="/Projetos/Residencial" class="category-card">
    <h3>Residencial 🏡</h3>
    <p>8 projetos em Revit e AutoCAD</p>
  </a>
  
  <a href="/Projetos/Comercial" class="category-card">
    <h3>Comercial 🏢</h3>
    <p>4 projetos em Revit e AutoCAD</p>
  </a>
  
  <a href="/Projetos/Predial" class="category-card">
    <h3>Predial 🏙️</h3>
    <p>4 projetos em Revit e AutoCAD</p>
  </a>
</div>

## Sobre Mim

Engenheiro eletricista com experiência em projetos residenciais, comerciais e prediais. Especializado em:

- Projetos elétricos completos
- Modelagem BIM (Revit)
- Documentação técnica (AutoCAD)
- Iluminação técnica (Dialux)

[Ver Currículo](/assets/pdfs/curriculo.pdf){:target="_blank" .reveal}

<div class="contact-section reveal">
  <h2>Contato</h2>
  <p>📧 email@exemplo.com</p>
  <p>📱 (00) 00000-0000</p>
</div>
```

### 3.2 Template de Projeto (exemplo-projeto.md)
```markdown
---
dg-publish: true
title: "Nome do Projeto"
setor: Residencial
ferramentas: "Revit, AutoCAD"
---
# Nome do Projeto 🏡

**Projeto residencial completo** — Instalações elétricas para residência de alto padrão com automação e iluminação técnica.

- **Local:** Porto Alegre, RS  
- **Ano:** 2023  
- **Ferramentas:** Revit, AutoCAD, Dialux

<div class="project-gallery reveal">
  <img src="/assets/imagens/projeto-exemplo/capa_thumb.jpg" alt="Visão geral" class="gallery-thumb" loading="lazy">
  <img src="/assets/imagens/projeto-exemplo/planta_thumb.jpg" alt="Planta baixa" class="gallery-thumb" loading="lazy">
  <img src="/assets/imagens/projeto-exemplo/detalhe_thumb.jpg" alt="Detalhe técnico" class="gallery-thumb" loading="lazy">
  <img src="/assets/imagens/projeto-exemplo/render_thumb.jpg" alt="Renderização 3D" class="gallery-thumb" loading="lazy">
</div>

## Descrição do Projeto

Este projeto contemplou o desenvolvimento completo das instalações elétricas de uma residência de 250m². O escopo incluiu:

- Entrada de energia e quadros de distribuição
- Circuitos de iluminação com controle automatizado
- Tomadas e pontos de força
- Infraestrutura para sistemas de segurança
- Projeto luminotécnico para áreas sociais

## Documentação

[📄 **Ver Planta Elétrica**](/assets/pdfs/projeto-exemplo_planta.pdf){:target="_blank" .reveal}

<div class="pdf-container reveal">
  <object data="/assets/pdfs/projeto-exemplo_planta.pdf#toolbar=0"
          type="application/pdf" width="100%" height="500">
    <p>PDF indisponível — <a href="/assets/pdfs/projeto-exemplo_planta.pdf" target="_blank">baixar</a>.</p>
  </object>
</div>

<!-- Modal (não editar id/classes) -->
<div id="img-modal" class="modal">
  <div class="modal-content">
    <img id="modal-img" src="" alt="Imagem Ampliada">
    <span id="modal-close">&#x2715;</span>
  </div>
</div>
```

## 4. Arquivos de Estilo e Script

### 4.1 portfolio.css
```css
:root {
  --cor-primaria: #0055AA;
  --cor-secundaria: #FFCC00;
  --cor-fundo: #FFFFFF;
  --cor-texto: #333333;
  --cor-texto-claro: #666666;
  --sombra: 0 4px 6px rgba(0, 0, 0, 0.1);
  --transicao: all 0.3s ease;
  --borda-raio: 8px;
}

body {
  font-family: 'Segoe UI', sans-serif;
  background-color: var(--cor-fundo);
  color: var(--cor-texto);
  line-height: 1.6;
}

/* Links */
a {
  color: var(--cor-primaria);
  text-decoration: none;
  transition: var(--transicao);
}

a:hover {
  color: var(--cor-secundaria);
}

/* Cabeçalhos */
h1, h2, h3, h4 {
  color: var(--cor-primaria);
}

/* Cards de Categoria */
.category-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin: 30px 0;
}

.category-card {
  background-color: var(--cor-fundo);
  border: 2px solid var(--cor-primaria);
  border-radius: var(--borda-raio);
  padding: 20px;
  box-shadow: var(--sombra);
  transition: var(--transicao);
  display: block;
  text-decoration: none;
  color: var(--cor-texto);
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  border-color: var(--cor-secundaria);
}

.category-card h3 {
  margin-top: 0;
  color: var(--cor-primaria);
}

/* Galeria de Projetos */
.project-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
  margin: 30px 0;
}

.gallery-thumb {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: var(--borda-raio);
  cursor: pointer;
  box-shadow: var(--sombra);
  transition: var(--transicao);
}

.gallery-thumb:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

/* Modal de Imagem */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  overflow: auto;
}

.modal-content {
  position: relative;
  margin: auto;
  padding: 0;
  width: 90%;
  max-width: 1200px;
  top: 50%;
  transform: translateY(-50%);
}

#modal-img {
  width: 100%;
  max-height: 90vh;
  object-fit: contain;
}

#modal-close {
  position: absolute;
  top: -40px;
  right: 0;
  color: white;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

/* Container de PDF */
.pdf-container {
  margin: 30px 0;
  border-radius: var(--borda-raio);
  overflow: hidden;
  box-shadow: var(--sombra);
}

.pdf-container object {
  width: 100%;
  border: none;
}

/* Animações Reveal */
.reveal {
  opacity: 0;
  transform: translateY(20px);
}

/* Responsividade */
@media (max-width: 768px) {
  .project-gallery {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .category-cards {
    grid-template-columns: 1fr;
  }
  
  .pdf-container object {
    height: 400px;
  }
}

@media (max-width: 480px) {
  .project-gallery {
    grid-template-columns: 1fr;
  }
  
  .pdf-container object {
    height: 300px;
  }
}

/* Seção de Contato */
.contact-section {
  background-color: var(--cor-primaria);
  color: var(--cor-fundo);
  padding: 20px;
  border-radius: var(--borda-raio);
  margin-top: 40px;
}

.contact-section h2 {
  color: var(--cor-secundaria);
}

/* Botões */
.btn {
  display: inline-block;
  background-color: var(--cor-primaria);
  color: var(--cor-fundo);
  padding: 10px 20px;
  border-radius: var(--borda-raio);
  transition: var(--transicao);
  margin: 10px 0;
  border: none;
  cursor: pointer;
}

.btn:hover {
  background-color: var(--cor-secundaria);
  color: var(--cor-texto);
}
```

### 4.2 anime.njk
```html
<script src="https://cdn.jsdelivr.net/npm/animejs@3.2.1/lib/anime.min.js"></script>
```

### 4.3 galleryModal.njk
```html
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Selecionar elementos
  const galleryThumbs = document.querySelectorAll('.gallery-thumb');
  const modal = document.getElementById('img-modal');
  const modalImg = document.getElementById('modal-img');
  const modalClose = document.getElementById('modal-close');
  
  // Abrir modal ao clicar na miniatura
  galleryThumbs.forEach(thumb => {
    thumb.addEventListener('click', function() {
      modal.style.display = 'block';
      modalImg.src = this.src.replace('_thumb', '');
      modalImg.alt = this.alt;
      
      // Animar a imagem do modal
      anime({
        targets: '#modal-img',
        opacity: [0, 1],
        scale: [0.8, 1],
        duration: 400,
        easing: 'easeOutCubic'
      });
    });
  });
  
  // Fechar modal
  modalClose.addEventListener('click', function() {
    anime({
      targets: '#modal-img',
      opacity: [1, 0],
      scale: [1, 0.8],
      duration: 300,
      easing: 'easeInCubic',
      complete: function() {
        modal.style.display = 'none';
      }
    });
  });
  
  // Fechar modal clicando fora da imagem
  window.addEventListener('click', function(event) {
    if (event.target === modal) {
      anime({
        targets: '#modal-img',
        opacity: [1, 0],
        scale: [1, 0.8],
        duration: 300,
        easing: 'easeInCubic',
        complete: function() {
          modal.style.display = 'none';
        }
      });
    }
  });
});
</script>
```

### 4.4 scrollReveal.njk
```html
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Configurar o IntersectionObserver para elementos com classe .reveal
  const revealElements = document.querySelectorAll('.reveal');
  
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Animar o elemento quando ele entra na viewport
        anime({
          targets: entry.target,
          opacity: [0, 1],
          translateY: [20, 0],
          duration: 800,
          easing: 'easeOutCubic',
          delay: anime.stagger(100)
        });
        
        // Parar de observar após a animação
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });
  
  // Começar a observar todos os elementos .reveal
  revealElements.forEach(element => {
    revealObserver.observe(element);
  });
});
</script>
```

## 5. Proteção por Senha (Staticrypt)

### 5.1 Script de Proteção
```bash
#!/bin/bash

# Proteger páginas restritas com Staticrypt
echo "Aplicando proteção por senha às páginas restritas..."

# Instalar Staticrypt se necessário
npm install -g staticrypt

# Proteger a página de projetos confidenciais
npx staticrypt public/projetos-confidenciais/index.html SENHA_SECRETA \
     --output public/projetos-confidenciais/index.html \
     --title "Área Restrita" \
     --instructions "Digite a senha para acessar os projetos confidenciais." \
     --button-label "Acessar" \
     --password-placeholder "Senha" \
     --remember-label "Lembrar senha"

echo "Proteção aplicada com sucesso!"
```

### 5.2 Configuração no netlify.toml
```toml
[build]
  command = "npm run build"
  publish = "public"

# Post-processing: aplicar proteção por senha após o build
[build.environment]
  NODE_VERSION = "16"

[build.processing]
  skip_processing = false

[build.processing.html]
  pretty_urls = true

# Executar script de proteção após o build
[build.lifecycle]
  onPostBuild = "bash ./scripts/protect-pages.sh"
```

## 6. Automação de Deploy

### 6.1 Script de Build e Deploy
```bash
#!/bin/bash

# Script de build e deploy para o portfólio
echo "Iniciando processo de build e deploy..."

# 1. Verificar arquivos
echo "Verificando estrutura de arquivos..."
if [ ! -f "Home.md" ]; then
  echo "ERRO: Home.md não encontrado!"
  exit 1
fi

# 2. Otimizar imagens (requer TinyPNG CLI)
echo "Otimizando imagens..."
find ./assets/imagens -type f \( -name "*.jpg" -o -name "*.png" \) -exec tinypng {} \;

# 3. Executar build local para teste
echo "Executando build local para teste..."
npm run build

# 4. Verificar build
echo "Verificando build..."
if [ ! -d "public" ]; then
  echo "ERRO: Build falhou!"
  exit 1
fi

# 5. Commit e push para GitHub (ativa deploy automático no Netlify)
echo "Realizando commit e push para GitHub..."
git add .
git commit -m "Update: $(date +%Y-%m-%d)"
git push origin main

echo "Deploy iniciado! Verifique o status no painel do Netlify."
```

## 7. Checklist Final

### 7.1 Verificação Pré-Deploy
- [ ] Todas as páginas de projeto têm `dg-publish: true`
- [ ] Home.md tem `dg-home: true`
- [ ] Todas as imagens estão otimizadas e com atributo `loading="lazy"`
- [ ] Todos os PDFs estão na pasta correta e com links funcionando
- [ ] CSS está aplicado corretamente
- [ ] Scripts JS estão funcionando (galeria, scroll reveal)
- [ ] Site é responsivo em dispositivos móveis
- [ ] Páginas restritas estão protegidas por senha
- [ ] Contraste de cores atende aos padrões de acessibilidade

### 7.2 Verificação Pós-Deploy
- [ ] Todas as páginas estão acessíveis
- [ ] Imagens carregam corretamente
- [ ] PDFs podem ser visualizados/baixados
- [ ] Animações funcionam em diferentes navegadores
- [ ] Páginas protegidas solicitam senha corretamente
- [ ] Tempo de carregamento é aceitável
- [ ] Links internos e externos funcionam
- [ ] SEO básico está configurado (títulos, meta descrições)

## 8. Expansão Futura

### 8.1 Ideias para Melhorias
- Adicionar sistema de tags para filtrar projetos
- Implementar modo escuro
- Adicionar formulário de contato (Netlify Forms)
- Integrar Google Analytics
- Adicionar seção de depoimentos de clientes
- Criar página de blog/artigos técnicos
- Implementar pesquisa no site

### 8.2 Manutenção
- Atualizar portfólio trimestralmente
- Verificar links quebrados mensalmente
- Manter plugins e dependências atualizados
- Fazer backup regular do repositório e conteúdo 