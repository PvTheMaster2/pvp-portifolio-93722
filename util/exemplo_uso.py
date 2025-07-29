#!/usr/bin/env python3
"""
Exemplo de uso do PDF Cropper
==============================

Este script demonstra como usar o PDF Cropper programaticamente
para automatizar recortes de PDFs.
"""

import sys
from pathlib import Path
import fitz

# Adiciona o diretório atual ao path para importar o módulo
sys.path.append(str(Path(__file__).parent))

from pdf_cropper import PDFCropper


def exemplo_recorte_interativo():
    """Exemplo de recorte usando interface interativa"""
    print("🎯 Exemplo: Recorte Interativo")
    print("=" * 50)
    
    # Substitua pelo caminho do seu PDF
    pdf_path = "caminho/para/seu/projeto.pdf"
    
    if not Path(pdf_path).exists():
        print(f"❌ PDF não encontrado: {pdf_path}")
        print("   Edite o script e defina o caminho correto")
        return
    
    # Cria cropper
    cropper = PDFCropper(pdf_path, page_num=0, margin_mm=5)
    cropper.open_pdf()
    
    try:
        # Seleção interativa
        rect = cropper.interactive_selection()
        
        # Recorta o PDF
        output_path = cropper.crop_pdf(rect)
        
        print(f"✅ Recorte salvo em: {output_path}")
        
    finally:
        cropper.close()


def exemplo_recorte_coordenadas():
    """Exemplo de recorte usando coordenadas específicas"""
    print("📐 Exemplo: Recorte com Coordenadas")
    print("=" * 50)
    
    # Substitua pelo caminho do seu PDF
    pdf_path = "caminho/para/seu/projeto.pdf"
    
    if not Path(pdf_path).exists():
        print(f"❌ PDF não encontrado: {pdf_path}")
        print("   Edite o script e defina o caminho correto")
        return
    
    # Cria cropper
    cropper = PDFCropper(pdf_path, page_num=0, margin_mm=10)
    cropper.open_pdf()
    
    try:
        # Coordenadas em milímetros (x0, y0, x1, y1)
        # Exemplo: recorta área de 100x150mm a partir de (50, 50)
        coords_mm = (50, 50, 150, 200)
        
        # Converte para pontos
        x0_pt = coords_mm[0] * cropper.MM_TO_PT
        y0_pt = coords_mm[1] * cropper.MM_TO_PT
        x1_pt = coords_mm[2] * cropper.MM_TO_PT
        y1_pt = coords_mm[3] * cropper.MM_TO_PT
        
        rect = fitz.Rect(x0_pt, y0_pt, x1_pt, y1_pt)
        
        print(f"📐 Recortando área: {coords_mm[0]}x{coords_mm[1]} a {coords_mm[2]}x{coords_mm[3]} mm")
        
        # Recorta o PDF
        output_path = cropper.crop_pdf(rect, "recorte_exemplo.pdf")
        
        print(f"✅ Recorte salvo em: {output_path}")
        
    finally:
        cropper.close()


def exemplo_recorte_multiplas_paginas():
    """Exemplo de recorte em múltiplas páginas"""
    print("📄 Exemplo: Recorte Múltiplas Páginas")
    print("=" * 50)
    
    # Substitua pelo caminho do seu PDF
    pdf_path = "caminho/para/seu/projeto.pdf"
    
    if not Path(pdf_path).exists():
        print(f"❌ PDF não encontrado: {pdf_path}")
        print("   Edite o script e defina o caminho correto")
        return
    
    # Abre PDF para verificar número de páginas
    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    doc.close()
    
    print(f"📄 PDF tem {num_pages} páginas")
    
    # Recorta cada página
    for page_num in range(min(3, num_pages)):  # Máximo 3 páginas para exemplo
        print(f"\n🔄 Processando página {page_num + 1}...")
        
        cropper = PDFCropper(pdf_path, page_num=page_num, margin_mm=5)
        cropper.open_pdf()
        
        try:
            # Seleção interativa
            rect = cropper.interactive_selection()
            
            # Recorta com nome personalizado
            output_path = cropper.crop_pdf(rect, f"recorte_pagina_{page_num + 1}.pdf")
            
            print(f"✅ Página {page_num + 1} salva em: {output_path}")
            
        finally:
            cropper.close()


def exemplo_recorte_area_especifica():
    """Exemplo de recorte de área específica (útil para detalhes técnicos)"""
    print("🔧 Exemplo: Recorte Área Específica")
    print("=" * 50)
    
    # Substitua pelo caminho do seu PDF
    pdf_path = "caminho/para/seu/projeto.pdf"
    
    if not Path(pdf_path).exists():
        print(f"❌ PDF não encontrado: {pdf_path}")
        print("   Edite o script e defina o caminho correto")
        return
    
    # Cria cropper
    cropper = PDFCropper(pdf_path, page_num=0, margin_mm=0)
    cropper.open_pdf()
    
    try:
        # Áreas comuns em projetos elétricos (em mm)
        areas = {
            "quadro_eletrico": (100, 100, 300, 400),
            "detalhe_instalacao": (50, 200, 250, 350),
            "esquema_unifilar": (200, 50, 600, 200),
        }
        
        for nome, coords in areas.items():
            print(f"\n📐 Recortando {nome}...")
            
            # Converte para pontos
            x0_pt = coords[0] * cropper.MM_TO_PT
            y0_pt = coords[1] * cropper.MM_TO_PT
            x1_pt = coords[2] * cropper.MM_TO_PT
            y1_pt = coords[3] * cropper.MM_TO_PT
            
            rect = fitz.Rect(x0_pt, y0_pt, x1_pt, y1_pt)
            
            # Recorta o PDF
            output_path = cropper.crop_pdf(rect, f"recorte_{nome}.pdf")
            
            print(f"✅ {nome} salvo em: {output_path}")
        
    finally:
        cropper.close()


def main():
    """Função principal com menu de exemplos"""
    print("🔧 PDF Cropper - Exemplos de Uso")
    print("=" * 50)
    print()
    
    exemplos = {
        "1": ("Recorte Interativo", exemplo_recorte_interativo),
        "2": ("Recorte com Coordenadas", exemplo_recorte_coordenadas),
        "3": ("Recorte Múltiplas Páginas", exemplo_recorte_multiplas_paginas),
        "4": ("Recorte Área Específica", exemplo_recorte_area_especifica),
    }
    
    print("Escolha um exemplo:")
    for key, (nome, _) in exemplos.items():
        print(f"  {key}. {nome}")
    print("  0. Sair")
    print()
    
    try:
        escolha = input("Digite sua escolha (0-4): ").strip()
        
        if escolha == "0":
            print("👋 Até logo!")
            return
        
        if escolha in exemplos:
            nome, funcao = exemplos[escolha]
            print(f"\n🚀 Executando: {nome}")
            print("=" * 50)
            funcao()
        else:
            print("❌ Escolha inválida!")
            
    except KeyboardInterrupt:
        print("\n👋 Operação cancelada pelo usuário")
    except Exception as e:
        print(f"❌ Erro: {e}")


if __name__ == "__main__":
    main() 