#!/usr/bin/env python3
"""
Script para otimização de assets do portfólio
Autor: Pedro Vitor
Data: 2024
"""

import os
import shutil
from pathlib import Path
from PIL import Image
import argparse

class PortfolioAssetOptimizer:
    def __init__(self, source_dir, output_dir):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.setup_directories()
    
    def setup_directories(self):
        """Cria a estrutura de diretórios necessária"""
        directories = [
            'assets/imagens',
            'assets/pdfs',
            'assets/imagens/rodrigo-empresa',
            'assets/pdfs/rodrigo-empresa'
        ]
        
        for dir_path in directories:
            full_path = self.output_dir / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Diretório criado: {full_path}")
    
    def optimize_image(self, input_path, output_path, max_size=(800, 600), quality=85):
        """Otimiza uma imagem para web"""
        try:
            with Image.open(input_path) as img:
                # Converter para RGB se necessário
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                # Redimensionar mantendo proporção
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                # Salvar otimizado
                img.save(output_path, 'JPEG', quality=quality, optimize=True)
                print(f"✅ Imagem otimizada: {output_path}")
                
        except Exception as e:
            print(f"❌ Erro ao otimizar {input_path}: {e}")
    
    def create_thumbnail(self, input_path, output_path, size=(400, 300)):
        """Cria thumbnail de uma imagem"""
        try:
            with Image.open(input_path) as img:
                # Converter para RGB se necessário
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                # Redimensionar para thumbnail
                img.thumbnail(size, Image.Resampling.LANCZOS)
                
                # Salvar thumbnail
                img.save(output_path, 'JPEG', quality=80, optimize=True)
                print(f"✅ Thumbnail criado: {output_path}")
                
        except Exception as e:
            print(f"❌ Erro ao criar thumbnail {input_path}: {e}")
    
    def process_rodrigo_empresa_images(self):
        """Processa imagens do projeto Rodrigo Empresa"""
        print("\n🖼️ Processando imagens do projeto Rodrigo Empresa...")
        
        # Mapeamento de imagens
        image_mapping = {
            'Rodrigo empresa.png': {
                'thumb': '3d_render_thumb.jpg',
                'full': '3d_render.jpg',
                'pdf_preview': 'pdf_terreo.jpg'
            }
        }
        
        source_images_dir = self.source_dir / 'REVIT' / 'RODRIGO EMPRESA'
        
        for original_name, new_names in image_mapping.items():
            original_path = source_images_dir / original_name
            
            if original_path.exists():
                # Criar versões otimizadas
                for version, new_name in new_names.items():
                    output_path = self.output_dir / 'assets' / 'imagens' / 'rodrigo-empresa' / new_name
                    
                    if version == 'thumb':
                        self.create_thumbnail(original_path, output_path, (400, 300))
                    elif version == 'full':
                        self.optimize_image(original_path, output_path, (1200, 800))
                    elif version == 'pdf_preview':
                        self.create_thumbnail(original_path, output_path, (300, 200))
            else:
                print(f"⚠️ Imagem não encontrada: {original_path}")
    
    def process_pdfs(self):
        """Processa PDFs do projeto"""
        print("\n📄 Processando PDFs do projeto...")
        
        pdf_mapping = {
            'PVP-A02-E101-R03 - TERREO_recorte_p1.pdf': 'PVP-A02-E101-R03 - TERREO_recorte_p1.pdf',
            'PVP-A02-E201-R02 - 2PAV_recorte_p1.pdf': 'PVP-A02-E201-R02 - 2PAV_recorte_p1.pdf',
            'PVP-A02-E301-R02 - 3PAV_recorte_p1.pdf': 'PVP-A02-E301-R02 - 3PAV_recorte_p1.pdf',
            'PVP-A02-E401-R00 - VERTICAL_recorte_p1.pdf': 'PVP-A02-E401-R00 - VERTICAL_recorte_p1.pdf'
        }
        
        source_pdfs_dir = self.source_dir / 'REVIT' / 'RODRIGO EMPRESA'
        
        for original_name, new_name in pdf_mapping.items():
            original_path = source_pdfs_dir / original_name
            
            if original_path.exists():
                output_path = self.output_dir / 'assets' / 'pdfs' / 'rodrigo-empresa' / new_name
                shutil.copy2(original_path, output_path)
                print(f"✅ PDF copiado: {new_name}")
            else:
                print(f"⚠️ PDF não encontrado: {original_path}")
    
    def create_pdf_previews(self):
        """Cria previews dos PDFs (placeholder)"""
        print("\n🖼️ Criando previews dos PDFs...")
        
        # Por enquanto, vamos criar placeholders
        # Em produção, você pode usar ferramentas como pdf2image
        preview_names = [
            'pdf_terreo.jpg',
            'pdf_2pav.jpg', 
            'pdf_3pav.jpg',
            'pdf_vertical.jpg'
        ]
        
        for preview_name in preview_names:
            # Criar uma imagem placeholder simples
            placeholder_path = self.output_dir / 'assets' / 'imagens' / 'rodrigo-empresa' / preview_name
            
            # Usar a imagem 3D como placeholder por enquanto
            source_image = self.output_dir / 'assets' / 'imagens' / 'rodrigo-empresa' / '3d_render.jpg'
            
            if source_image.exists():
                self.create_thumbnail(source_image, placeholder_path, (300, 200))
                print(f"✅ Preview criado: {preview_name}")
    
    def generate_image_placeholders(self):
        """Gera imagens placeholder para projetos sem imagens"""
        print("\n🎨 Gerando imagens placeholder...")
        
        placeholder_images = [
            'planta_terreo.jpg',
            'planta_2pav.jpg',
            'planta_3pav.jpg'
        ]
        
        for img_name in placeholder_images:
            output_path = self.output_dir / 'assets' / 'imagens' / 'rodrigo-empresa' / img_name
            
            # Criar uma imagem placeholder simples
            with Image.new('RGB', (400, 300), color='#f0f0f0') as img:
                # Adicionar texto placeholder
                from PIL import ImageDraw, ImageFont
                draw = ImageDraw.Draw(img)
                
                # Tentar usar uma fonte padrão
                try:
                    font = ImageFont.load_default()
                except:
                    font = None
                
                text = "Planta Técnica"
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                
                x = (400 - text_width) // 2
                y = (300 - text_height) // 2
                
                draw.text((x, y), text, fill='#666666', font=font)
                img.save(output_path, 'JPEG', quality=85)
                
            print(f"✅ Placeholder criado: {img_name}")
    
    def run_optimization(self):
        """Executa todo o processo de otimização"""
        print("🚀 Iniciando otimização de assets do portfólio...")
        
        self.process_rodrigo_empresa_images()
        self.process_pdfs()
        self.create_pdf_previews()
        self.generate_image_placeholders()
        
        print("\n✅ Otimização concluída!")
        print(f"📁 Assets organizados em: {self.output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Otimiza assets para o portfólio')
    parser.add_argument('--source', default='.', help='Diretório fonte')
    parser.add_argument('--output', default='./portfolio-build', help='Diretório de saída')
    
    args = parser.parse_args()
    
    optimizer = PortfolioAssetOptimizer(args.source, args.output)
    optimizer.run_optimization()

if __name__ == "__main__":
    main() 