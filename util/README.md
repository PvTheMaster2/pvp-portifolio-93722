# PDF Cropper - Recorta PDFs mantendo qualidade vetorial

Este script Python permite recortar seções específicas de PDFs (A0, A1, A2, etc.) mantendo a qualidade vetorial original. Ideal para projetos elétricos e técnicos.

## 🎯 Funcionalidades

- ✅ **Interface interativa** com seleção visual
- ✅ **Preserva vetores e textos** (não rasteriza)
- ✅ **Suporte universal** a diferentes tamanhos (A0, A1, A2, etc.)
- ✅ **Margens personalizáveis** em milímetros
- ✅ **Tratamento de rotação** de páginas
- ✅ **Conversão automática** de coordenadas
- ✅ **Qualidade vetorial mantida** mesmo com zoom

## 📦 Instalação

### 1. Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### 2. Instalar dependências
```bash
# Navegue até a pasta util
cd util

# Instale as dependências
pip install -r requirements.txt
```

### 3. Verificar instalação
```bash
python pdf_cropper.py --help
```

## 🚀 Como usar

### Modo Interativo (Recomendado)
```bash
# Abre interface visual para seleção
python pdf_cropper.py --input "caminho/para/projeto.pdf" --interactive
```

### Modo com Coordenadas Específicas
```bash
# Recorta área específica (coordenadas em milímetros)
python pdf_cropper.py --input "projeto.pdf" --coords 100 100 300 400
```

### Com Margem
```bash
# Adiciona margem de 5mm ao redor da seleção
python pdf_cropper.py --input "projeto.pdf" --interactive --margin 5
```

### Página Específica
```bash
# Trabalha com página específica (0-indexed)
python pdf_cropper.py --input "projeto.pdf" --page 1 --interactive
```

### Saída Personalizada
```bash
# Define nome do arquivo de saída
python pdf_cropper.py --input "projeto.pdf" --interactive --output "recorte_final.pdf"
```

## 📋 Parâmetros

| Parâmetro | Descrição | Padrão |
|-----------|-----------|--------|
| `--input, -i` | Caminho do PDF de entrada | **Obrigatório** |
| `--page, -p` | Número da página (0-indexed) | 0 |
| `--margin, -m` | Margem em milímetros | 0 |
| `--output, -o` | Caminho de saída | Auto-gerado |
| `--interactive, -I` | Modo interativo | False |
| `--coords, -c` | Coordenadas em mm: x0 y0 x1 y1 | - |

## 🎮 Interface Interativa

1. **Execute o script** com `--interactive`
2. **Uma janela abrirá** mostrando o PDF
3. **Clique e arraste** para selecionar a área
4. **Pressione ENTER** para confirmar
5. **Pressione ESC** para cancelar

### Dicas da Interface
- A área selecionada aparece em **vermelho**
- Use **zoom do mouse** para precisão
- As coordenadas são mostradas em **tempo real**
- O arquivo de saída é gerado automaticamente

## 📐 Coordenadas e Tamanhos

### Sistema de Coordenadas
- **Origem**: Canto superior esquerdo
- **Unidade**: Milímetros (mm)
- **Formato**: `x0 y0 x1 y1` (canto superior esquerdo → canto inferior direito)

### Tamanhos Padrão
| Formato | Dimensões (mm) |
|---------|----------------|
| A0 | 841 × 1189 |
| A1 | 594 × 841 |
| A2 | 420 × 594 |
| A3 | 297 × 420 |
| A4 | 210 × 297 |

## 🔧 Exemplos Práticos

### Recortar Detalhe de Projeto Elétrico
```bash
python pdf_cropper.py --input "projeto_eletrico.pdf" --interactive --margin 10
```

### Recortar Área Específica (100x150mm)
```bash
python pdf_cropper.py --input "projeto.pdf" --coords 50 50 150 200
```

### Recortar Múltiplas Páginas
```bash
# Página 1
python pdf_cropper.py --input "projeto.pdf" --page 0 --interactive --output "recorte_p1.pdf"

# Página 2  
python pdf_cropper.py --input "projeto.pdf" --page 1 --interactive --output "recorte_p2.pdf"
```

## ⚠️ Limitações e Soluções

### PDFs Rasterizados (Escaneados)
- **Problema**: Não há vetores para preservar
- **Solução**: O script mantém a resolução original, mas não pode "criar" vetores

### PDFs Protegidos
- **Problema**: PDFs com senha ou proteção
- **Solução**: Remova a proteção antes de usar o script

### Arquivos Muito Grandes
- **Problema**: PDFs com muitas páginas podem ser lentos
- **Solução**: Use `--page` para trabalhar com páginas específicas

## 🛠️ Troubleshooting

### Erro: "Arquivo não encontrado"
```bash
# Verifique o caminho do arquivo
ls -la "caminho/para/arquivo.pdf"
```

### Erro: "Página não existe"
```bash
# Liste as páginas disponíveis
python pdf_cropper.py --input "arquivo.pdf" --page 0 --interactive
```

### Interface não abre
```bash
# Verifique se matplotlib está instalado
pip install matplotlib
```

### Qualidade baixa no resultado
- ✅ O script preserva vetores - a qualidade deve ser idêntica ao original
- ⚠️ Se a qualidade está baixa, verifique se o PDF original tem vetores

## 📁 Estrutura de Arquivos

```
util/
├── pdf_cropper.py      # Script principal
├── requirements.txt     # Dependências
└── README.md          # Este arquivo
```

## 🔄 Atualizações

### Versão 1.0
- ✅ Interface interativa
- ✅ Preservação de vetores
- ✅ Suporte a rotação
- ✅ Margens personalizáveis
- ✅ Conversão automática de coordenadas

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Teste com um PDF simples primeiro
3. Verifique os logs de erro no terminal

---

**Desenvolvido para projetos elétricos e técnicos** ⚡📐 