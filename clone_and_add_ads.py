#!/usr/bin/env python3
import os
import sys
import logging
import shutil
from pathlib import Path
from bs4 import BeautifulSoup
from typing import List, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_ad_container() -> str:
    """Returns the HTML for a responsive advertisement container."""
    return """
    <!-- Advertisement Container -->
    <div class="ad-container" style="
        width: 100%;
        max-width: 728px;
        margin: 20px auto;
        min-height: 90px;
        background-color: #f8f9fa;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #dee2e6;
        border-radius: 4px;
        padding: 10px;
        box-sizing: border-box;
        text-align: center;
    ">
        <p style="color: #6c757d; margin: 0;">Advertisement Space</p>
    </div>
    """

def modify_html_file(file_path: Path) -> bool:
    """
    Modifies a single HTML file to add advertisement containers.
    
    Args:
        file_path: Path to the HTML file
        
    Returns:
        bool: True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        body = soup.find('body')
        
        if not body:
            logger.warning(f"No body tag found in {file_path}")
            return False
            
        # Create the ad container element
        ad_container = BeautifulSoup(setup_ad_container(), 'html.parser')
        
        # Add ad container after opening body tag
        body.insert(0, ad_container)
        
        # Add another ad container before closing body tag
        body.append(BeautifulSoup(setup_ad_container(), 'html.parser'))
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        logger.info(f"Successfully modified {file_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error modifying {file_path}: {str(e)}")
        return False

def process_directory(directory_path: Path) -> tuple[int, int]:
    """
    Recursively processes all HTML files in the given directory.
    
    Args:
        directory_path: Path to the directory to process
        
    Returns:
        tuple[int, int]: (number of files processed, number of files modified)
    """
    processed = 0
    modified = 0
    
    try:
        for file_path in directory_path.rglob('*.html'):
            processed += 1
            if modify_html_file(file_path):
                modified += 1
                
    except Exception as e:
        logger.error(f"Error processing directory {directory_path}: {str(e)}")
        
    return processed, modified

def main():
    """Main function to process website templates."""
    if len(sys.argv) != 2:
        logger.error("Usage: python clone_and_add_ads.py <templates_directory>")
        sys.exit(1)
        
    templates_dir = Path(sys.argv[1])
    
    if not templates_dir.exists():
        logger.error(f"Directory does not exist: {templates_dir}")
        sys.exit(1)
        
    logger.info("Starting template modification process...")
    
    processed, modified = process_directory(templates_dir)
    
    logger.info(f"Process completed. Processed {processed} files, modified {modified} files.")
    
    if processed == 0:
        logger.warning("No HTML files were found to process")
        sys.exit(1)
    
    if modified == 0:
        logger.warning("No files were modified")
        sys.exit(1)
        
    logger.info("Template modification completed successfully")

if __name__ == "__main__":
    main()
