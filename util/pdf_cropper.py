#!/usr/bin/env python3
"""
PDF Cropper - Recorta PDFs mantendo qualidade vetorial
=======================================================

Este script permite recortar seções específicas de PDFs (A0, A1, A2, etc.)
mantendo a qualidade vetorial original. Ideal para projetos elétricos e técnicos.

Funcionalidades:
- Interface interativa com seleção visual
- Preserva vetores e textos (não rasteriza)
- Suporte a diferentes tamanhos (A0, A1, A2, etc.)
- Margens personalizáveis
- Tratamento de rotação de páginas

Uso:
    python pdf_cropper.py --input projeto.pdf --page 0 --margin 5
    python pdf_cropper.py --input projeto.pdf --interactive
"""

import argparse
import sys
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import fitz  # PyMuPDF


class PDFCropper:
    """Classe principal para recortar PDFs mantendo qualidade vetorial"""
    
    def __init__(self, pdf_path, page_num=0, margin_mm=0):
        """
        Inicializa o cropper
        
        Args:
            pdf_path (str): Caminho para o PDF
            page_num (int): Número da página (0-indexed)
            margin_mm (float): Margem em milímetros
        """
        self.pdf_path = Path(pdf_path)
        self.page_num = page_num
        self.margin_mm = margin_mm
        self.doc = None
        self.page = None
        self.coords = {}
        
        # Constantes de conversão
        self.MM_TO_PT = 72 / 25.4  # milímetros para pontos
        self.PT_TO_MM = 25.4 / 72  # pontos para milímetros
        
    def open_pdf(self):
        """Abre o PDF e carrega a página especificada"""
        try:
            self.doc = fitz.open(str(self.pdf_path))
            if self.page_num >= len(self.doc):
                raise ValueError(f"Página {self.page_num} não existe. PDF tem {len(self.doc)} páginas.")
            
            self.page = self.doc[self.page_num]
            print(f"✅ PDF aberto: {self.pdf_path}")
            print(f"📄 Página {self.page_num + 1} de {len(self.doc)}")
            print(f"📏 Tamanho: {self.page.rect.width * self.PT_TO_MM:.1f} x {self.page.rect.height * self.PT_TO_MM:.1f} mm")
            print(f"🔄 Rotação: {self.page.rotation}°")
            
        except Exception as e:
            print(f"❌ Erro ao abrir PDF: {e}")
            sys.exit(1)
    
    def get_preview_image(self, dpi=150):
        """
        Gera imagem de pré-visualização para seleção
        
        Args:
            dpi (int): Resolução da pré-visualização
            
        Returns:
            numpy.ndarray: Imagem da página
        """
        zoom = dpi / 72  # 72 pontos por polegada no PDF
        matrix = fitz.Matrix(zoom, zoom)
        
        # Gera pixmap da página
        pix = self.page.get_pixmap(matrix=matrix)
        
        # Converte para array numpy
        img_array = np.frombuffer(pix.samples, dtype=np.uint8)
        img_array = img_array.reshape(pix.height, pix.width, pix.n)
        
        # Converte RGBA para RGB se necessário
        if pix.n == 4:  # RGBA
            img_array = img_array[:, :, :3]
        
        self.preview_dpi = dpi
        self.preview_zoom = zoom
        self.preview_size = (pix.width, pix.height)
        
        return img_array
    
    def img_to_pdf_coords(self, img_rect):
        """
        Converte coordenadas da imagem de pré-visualização para pontos do PDF
        
        Args:
            img_rect (tuple): (x0, y0, x1, y1) em pixels da imagem
            
        Returns:
            fitz.Rect: Retângulo em pontos do PDF
        """
        x0_px, y0_px, x1_px, y1_px = img_rect
        
        # Dimensões da página em pontos
        page_width_pt = self.page.rect.width
        page_height_pt = self.page.rect.height
        
        # Dimensões da pré-visualização em pixels
        preview_width_px, preview_height_px = self.preview_size
        
        # Fatores de conversão
        scale_x = page_width_pt / preview_width_px
        scale_y = page_height_pt / preview_height_px
        
        # Converte coordenadas (inverte Y)
        x0_pt = x0_px * scale_x
        y0_pt = (preview_height_px - y1_px) * scale_y  # Inverte Y
        x1_pt = x1_px * scale_x
        y1_pt = (preview_height_px - y0_px) * scale_y  # Inverte Y
        
        # Trata rotação da página
        if self.page.rotation == 90:
            # Troca coordenadas e ajusta
            x0_pt, y0_pt = y0_pt, page_width_pt - x1_pt
            x1_pt, y1_pt = y1_pt, page_width_pt - x0_pt
        elif self.page.rotation == 180:
            # Inverte ambas as coordenadas
            x0_pt, y0_pt = page_width_pt - x1_pt, page_height_pt - y1_pt
            x1_pt, y1_pt = page_width_pt - x0_pt, page_height_pt - y0_pt
        elif self.page.rotation == 270:
            # Troca coordenadas e ajusta
            x0_pt, y0_pt = page_height_pt - y1_pt, x0_pt
            x1_pt, y1_pt = page_height_pt - y0_pt, x1_pt
        
        # Aplica margem se especificada
        if self.margin_mm > 0:
            margin_pt = self.margin_mm * self.MM_TO_PT
            x0_pt -= margin_pt
            y0_pt -= margin_pt
            x1_pt += margin_pt
            y1_pt += margin_pt
        
        # Garante que as coordenadas estão dentro dos limites da página
        x0_pt = max(0, min(x0_pt, page_width_pt))
        y0_pt = max(0, min(y0_pt, page_height_pt))
        x1_pt = max(0, min(x1_pt, page_width_pt))
        y1_pt = max(0, min(y1_pt, page_height_pt))
        
        return fitz.Rect(x0_pt, y0_pt, x1_pt, y1_pt)
    
    def interactive_selection(self):
        """
        Interface interativa para seleção da área
        
        Returns:
            fitz.Rect: Retângulo selecionado em pontos do PDF
        """
        # Gera pré-visualização
        img = self.get_preview_image()
        
        # Configura interface matplotlib
        plt.ion()  # Modo interativo
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.imshow(img)
        ax.set_title(f"Selecione a área para recortar\nPDF: {self.pdf_path.name} | Página {self.page_num + 1}")
        ax.set_xlabel("Clique e arraste para selecionar. Pressione 'Enter' para confirmar.")
        
        # Variável para armazenar seleção
        self.coords = {}
        
        def onselect(eclick, erelease):
            """Callback para seleção do retângulo"""
            x0, y0 = eclick.xdata, eclick.ydata
            x1, y1 = erelease.xdata, erelease.ydata
            
            # Garante que x0,y0 é o canto superior esquerdo
            x0, x1 = min(x0, x1), max(x0, x1)
            y0, y1 = min(y0, y1), max(y0, y1)
            
            self.coords["img_rect"] = (x0, y0, x1, y1)
            
            # Mostra informações da seleção
            width_px = x1 - x0
            height_px = y1 - y0
            print(f"📐 Seleção: {width_px:.0f} x {height_px:.0f} pixels")
        
        def on_key(event):
            """Callback para teclas"""
            if event.key == 'enter':
                if "img_rect" in self.coords:
                    plt.close()
                else:
                    print("⚠️ Selecione uma área primeiro!")
            elif event.key == 'escape':
                print("❌ Seleção cancelada")
                plt.close()
                sys.exit(0)
        
        # Configura seletores
        selector = RectangleSelector(
            ax, onselect, useblit=True, interactive=True,
            button=[1],  # Apenas botão esquerdo do mouse
            minspanx=5, minspany=5,  # Tamanho mínimo da seleção
            spancoords='pixels'  # Coordenadas em pixels
        )
        
        fig.canvas.mpl_connect('key_press_event', on_key)
        
        print("🎯 Selecione a área com o mouse e pressione ENTER para confirmar")
        print("   Pressione ESC para cancelar")
        
        plt.show(block=True)
        
        if "img_rect" not in self.coords:
            print("❌ Nenhuma área selecionada")
            sys.exit(1)
        
        # Converte para coordenadas do PDF
        pdf_rect = self.img_to_pdf_coords(self.coords["img_rect"])
        
        # Mostra informações do recorte
        width_mm = pdf_rect.width * self.PT_TO_MM
        height_mm = pdf_rect.height * self.PT_TO_MM
        print(f"✅ Área selecionada: {width_mm:.1f} x {height_mm:.1f} mm")
        
        return pdf_rect
    
    def crop_pdf(self, rect, output_path=None):
        """
        Recorta o PDF usando o retângulo especificado
        
        Args:
            rect (fitz.Rect): Retângulo em pontos do PDF
            output_path (str): Caminho de saída (opcional)
            
        Returns:
            str: Caminho do arquivo de saída
        """
        if output_path is None:
            # Gera nome de saída automático
            stem = self.pdf_path.stem
            output_path = self.pdf_path.parent / f"{stem}_recorte_p{self.page_num + 1}.pdf"
        
        try:
            # Cria novo documento
            out_doc = fitz.open()
            
            # Cria nova página com tamanho do recorte
            new_page = out_doc.new_page(width=rect.width, height=rect.height)
            
            # Desenha a página original clippada na nova página
            new_page.show_pdf_page(
                new_page.rect,  # Área de destino
                self.doc,       # Documento fonte
                self.page_num,  # Página fonte
                clip=rect       # Área de recorte
            )
            
            # Salva o documento
            out_doc.save(str(output_path))
            out_doc.close()
            
            print(f"💾 PDF recortado salvo: {output_path}")
            
            # Mostra informações do arquivo de saída
            file_size = Path(output_path).stat().st_size / 1024  # KB
            print(f"📊 Tamanho do arquivo: {file_size:.1f} KB")
            
            return str(output_path)
            
        except Exception as e:
            print(f"❌ Erro ao salvar PDF: {e}")
            sys.exit(1)
    
    def close(self):
        """Fecha o documento PDF"""
        if self.doc:
            self.doc.close()


def main():
    """Função principal"""
    parser = argparse.ArgumentParser(
        description="Recorta PDFs mantendo qualidade vetorial",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python pdf_cropper.py --input projeto.pdf --interactive
  python pdf_cropper.py --input projeto.pdf --page 0 --margin 5
  python pdf_cropper.py --input projeto.pdf --coords 100 100 300 400
        """
    )
    
    parser.add_argument("--input", "-i", required=True,
                       help="Caminho para o PDF de entrada")
    parser.add_argument("--page", "-p", type=int, default=0,
                       help="Número da página (0-indexed, padrão: 0)")
    parser.add_argument("--margin", "-m", type=float, default=0,
                       help="Margem em milímetros (padrão: 0)")
    parser.add_argument("--output", "-o",
                       help="Caminho de saída (padrão: auto-gerado)")
    parser.add_argument("--interactive", "-I", action="store_true",
                       help="Modo interativo com seleção visual")
    parser.add_argument("--coords", "-c", nargs=4, type=float,
                       help="Coordenadas em milímetros: x0 y0 x1 y1")
    
    args = parser.parse_args()
    
    # Verifica se arquivo existe
    if not Path(args.input).exists():
        print(f"❌ Arquivo não encontrado: {args.input}")
        sys.exit(1)
    
    # Cria cropper
    cropper = PDFCropper(args.input, args.page, args.margin)
    cropper.open_pdf()
    
    try:
        if args.interactive:
            # Modo interativo
            rect = cropper.interactive_selection()
        elif args.coords:
            # Modo com coordenadas especificadas
            x0_mm, y0_mm, x1_mm, y1_mm = args.coords
            
            # Converte milímetros para pontos
            x0_pt = x0_mm * cropper.MM_TO_PT
            y0_pt = y0_mm * cropper.MM_TO_PT
            x1_pt = x1_mm * cropper.MM_TO_PT
            y1_pt = y1_mm * cropper.MM_TO_PT
            
            rect = fitz.Rect(x0_pt, y0_pt, x1_pt, y1_pt)
            print(f"📐 Usando coordenadas: {x0_mm:.1f} {y0_mm:.1f} {x1_mm:.1f} {y1_mm:.1f} mm")
        else:
            print("❌ Especifique --interactive ou --coords")
            sys.exit(1)
        
        # Recorta o PDF
        output_path = cropper.crop_pdf(rect, args.output)
        
        print(f"✅ Recorte concluído: {output_path}")
        
    finally:
        cropper.close()


if __name__ == "__main__":
    main() 