# 🚀 Guia Rápido - PDF Cropper

## Instalação Rápida (Windows)

1. **Execute o instalador:**
   ```bash
   cd util
   install.bat
   ```

2. **Ou instale manualmente:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso Básico

### 1. Recorte Interativo (Recomendado)
```bash
python pdf_cropper.py --input "seu_projeto.pdf" --interactive
```

**Passos:**
1. Uma janela abrirá mostrando seu PDF
2. Clique e arraste para selecionar a área
3. Pressione **ENTER** para confirmar
4. O arquivo recortado será salvo automaticamente

### 2. Recorte com Margem
```bash
python pdf_cropper.py --input "projeto.pdf" --interactive --margin 10
```

### 3. Recorte de Página Específica
```bash
python pdf_cropper.py --input "projeto.pdf" --page 1 --interactive
```

### 4. Recorte com Coordenadas
```bash
python pdf_cropper.py --input "projeto.pdf" --coords 50 50 200 300
```

## Exemplos Práticos

### Recortar Detalhe de Quadro Elétrico
```bash
python pdf_cropper.py --input "projeto_eletrico.pdf" --interactive --margin 5
```

### Recortar Esquema Unifilar
```bash
python pdf_cropper.py --input "projeto.pdf" --coords 100 100 400 200
```

### Recortar Múltiplas Áreas
```bash
# Área 1
python pdf_cropper.py --input "projeto.pdf" --interactive --output "quadro.pdf"

# Área 2  
python pdf_cropper.py --input "projeto.pdf" --interactive --output "detalhes.pdf"
```

## Dicas Importantes

✅ **Qualidade mantida**: O script preserva vetores e textos
✅ **Universal**: Funciona com A0, A1, A2, A3, A4, etc.
✅ **Rápido**: Interface responsiva e processamento otimizado
✅ **Flexível**: Margens, coordenadas e páginas personalizáveis

## Troubleshooting

### Erro: "Arquivo não encontrado"
- Verifique o caminho do arquivo
- Use caminhos completos se necessário

### Interface não abre
- Verifique se matplotlib está instalado: `pip install matplotlib`

### Qualidade baixa
- O script preserva vetores - se a qualidade está baixa, verifique o PDF original

## Comandos Úteis

```bash
# Ajuda
python pdf_cropper.py --help

# Teste com exemplo
python exemplo_uso.py

# Verificar instalação
python pdf_cropper.py --input "teste.pdf" --interactive
```

---

**Desenvolvido para projetos elétricos e técnicos** ⚡📐 