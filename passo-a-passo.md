# Passo a Passo: Implementação do Portfólio Online

## Fase 1: Preparação do Ambiente (30 minutos)

1. **Instalar Obsidian**
   - Baixar Obsidian em https://obsidian.md
   - Criar novo vault chamado "portfolio-engenharia"
   - Instalar plugin "Digital Garden"

2. **Configurar GitHub**
   - Criar novo repositório "portfolio-engenharia"
   - Gerar token de acesso (Settings > Developer settings > Personal access tokens)
   - Salvar token em local seguro

3. **Configurar Netlify**
   - Acessar https://www.netlify.com
   - Conectar com GitHub
   - Clicar em "New site from Git"
   - Selecionar repositório "portfolio-engenharia"

## Fase 2: Estrutura de Arquivos (1 hora)

1. **Criar Estrutura Base**
```bash
mkdir -p Projetos/{Residencial,Comercial,Predial}
mkdir -p assets/{imagens,pdfs}
mkdir -p src/site/styles/user
mkdir -p src/site/_includes/components/user/{common/head,notes/footer}
```

2. **Criar Arquivos Base**
```bash
touch Home.md
touch src/site/styles/user/portfolio.css
touch src/site/_includes/components/user/common/head/anime.njk
touch src/site/_includes/components/user/notes/footer/{galleryModal,scrollReveal}.njk
```

3. **Organizar Projetos**
   - Copiar PDFs para `/assets/pdfs/<projeto>/`
   - Otimizar e copiar imagens para `/assets/imagens/<projeto>/`
   - Criar arquivo .md para cada projeto

## Fase 3: Configuração do Digital Garden (30 minutos)

1. **Configurar Plugin**
   - Abrir Obsidian > Settings > Community Plugins
   - Procurar e instalar "Digital Garden"
   - Em Settings > Digital Garden, configurar:
     ```
     GITHUB_USER=seu-usuario
     GITHUB_REPO=portfolio-engenharia
     GH_TOKEN=seu-token
     NETLIFY_SITE=seu-site-netlify
     ```

2. **Configurar Site Settings**
   - Criar arquivo `data/site.json`:
     ```json
     {
       "name": "Portfólio de Engenharia Elétrica",
       "baseUrl": "https://seu-site-netlify.netlify.app",
       "authorName": "Seu Nome",
       "authorEmail": "seu@email.com"
     }
     ```

## Fase 4: Implementação do Conteúdo (2-3 horas)

1. **Criar Home.md**
   - Copiar template do plano.md
   - Personalizar informações
   - Adicionar suas fotos e descrições

2. **Criar Projetos**
   - Para cada projeto:
     1. Criar arquivo .md na pasta apropriada
     2. Usar template do plano.md
     3. Adicionar imagens e PDFs
     4. Personalizar descrições
     5. Testar links e visualização

3. **Organizar Imagens**
   - Redimensionar para tamanhos adequados:
     - Thumbnails: 400x300px
     - Imagens completas: max 1920x1080px
   - Comprimir usando TinyPNG
   - Nomear consistentemente: `projeto_tipo_numero.jpg`

## Fase 5: Estilização e Interatividade (2 horas)

1. **Implementar CSS**
   - Copiar `portfolio.css` do plano.md
   - Ajustar cores se necessário
   - Testar responsividade

2. **Adicionar JavaScript**
   - Implementar `anime.njk`
   - Implementar `galleryModal.njk`
   - Implementar `scrollReveal.njk`
   - Testar todas as animações

3. **Configurar Proteção**
   - Identificar páginas que precisam de proteção
   - Implementar Staticrypt conforme plano.md
   - Testar acesso protegido

## Fase 6: Teste e Otimização (1-2 horas)

1. **Checklist de Qualidade**
   ```markdown
   - [ ] Todas as imagens têm alt text
   - [ ] PDFs estão acessíveis
   - [ ] Links funcionam
   - [ ] Animações são suaves
   - [ ] Site é responsivo
   - [ ] Páginas protegidas funcionam
   ```

2. **Otimização de Performance**
   - Verificar tamanho das imagens
   - Testar tempo de carregamento
   - Validar HTML/CSS
   - Testar em diferentes navegadores

3. **SEO Básico**
   - Adicionar meta descrições
   - Verificar títulos das páginas
   - Confirmar estrutura de URLs
   - Testar compartilhamento social

## Fase 7: Deploy (1 hora)

1. **Preparação Final**
   ```bash
   # Verificar arquivos
   git status
   
   # Commit inicial
   git add .
   git commit -m "Versão inicial do portfólio"
   git push origin main
   ```

2. **Deploy no Netlify**
   - Verificar build no Netlify
   - Testar site publicado
   - Configurar domínio personalizado (opcional)

3. **Testes Pós-Deploy**
   - Verificar todos os links
   - Testar formulários
   - Confirmar proteção de páginas
   - Validar SSL/HTTPS

## Fase 8: Manutenção (Contínuo)

1. **Rotina Semanal**
   - Verificar analytics
   - Testar links quebrados
   - Backup do repositório

2. **Rotina Mensal**
   - Atualizar conteúdo
   - Verificar plugins
   - Otimizar imagens novas
   - Atualizar dependências

3. **Rotina Trimestral**
   - Revisar todo conteúdo
   - Atualizar portfólio
   - Implementar melhorias
   - Verificar SEO

## Tempo Total Estimado: 8-10 horas

### Dicas Importantes

1. **Backup**
   - Manter backup local do vault Obsidian
   - Usar .gitignore apropriado
   - Backup regular dos arquivos originais

2. **Organização**
   - Manter nomenclatura consistente
   - Documentar alterações importantes
   - Usar branches para mudanças grandes

3. **Performance**
   - Não ultrapassar 100MB por arquivo
   - Otimizar todas as imagens
   - Usar lazy loading
   - Minimizar uso de JavaScript

4. **Segurança**
   - Não compartilhar tokens
   - Usar senhas fortes
   - Manter backups seguros
   - Atualizar regularmente

### Próximos Passos Sugeridos

1. **Expansão**
   - Adicionar blog técnico
   - Implementar sistema de tags
   - Criar área de depoimentos
   - Adicionar mais interatividade

2. **Marketing**
   - Compartilhar em redes profissionais
   - Otimizar para SEO
   - Criar conteúdo regular
   - Coletar feedback

3. **Melhorias Técnicas**
   - Implementar PWA
   - Adicionar modo escuro
   - Melhorar acessibilidade
   - Otimizar performance 