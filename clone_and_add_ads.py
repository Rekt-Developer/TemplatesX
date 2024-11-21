#!/usr/bin/env python3
import os
import sys
import git
from bs4 import BeautifulSoup
import glob
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WebsiteTemplateModifier:
    def __init__(self, git_url: Optional[str] = None):
        self.git_url = git_url or "https://github.com/learning-zone/website-templates.git"
        self.repo_path = None
        
        # Advertisement HTML template with responsive design
        self.ad_template = """
        <!-- Responsive Advertisement Section -->
        <div class="ad-container" style="
            text-align: center;
            margin: 20px auto;
            padding: 15px;
            background: #f8f9fa;
            max-width: 100%;
            box-sizing: border-box;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <div class="ad-placeholder" style="
                min-height: 250px;
                background: linear-gradient(45deg, #e9ecef, #dee2e6);
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 4px;
                margin: 0 auto;
                max-width: 728px;">
                <p style="color: #6c757d; font-family: Arial, sans-serif;">Advertisement Space</p>
            </div>
        </div>
        """
    
    def clone_repository(self) -> str:
        """Clone the repository to a local directory."""
        try:
            repo_name = self.git_url.split('/')[-1].replace('.git', '')
            self.repo_path = os.path.join(os.getcwd(), repo_name)
            
            if os.path.exists(self.repo_path):
                logger.info(f"Removing existing directory: {self.repo_path}")
                import shutil
                shutil.rmtree(self.repo_path)
            
            logger.info(f"Cloning repository from {self.git_url}")
            git.Repo.clone_from(self.git_url, self.repo_path)
            return self.repo_path
            
        except Exception as e:
            logger.error(f"Failed to clone repository: {str(e)}")
            raise
    
    def process_html_file(self, html_file: str) -> Tuple[bool, str]:
        """Process a single HTML file to add advertisements."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            body = soup.find('body')
            if not body:
                return False, f"No body tag found in {html_file}"
            
            # Add ads at the top and bottom of body
            top_ad = BeautifulSoup(self.ad_template, 'html.parser')
            bottom_ad = BeautifulSoup(self.ad_template, 'html.parser')
            
            body.insert(0, top_ad)
            body.append(bottom_ad)
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return True, html_file
            
        except Exception as e:
            return False, f"Error processing {html_file}: {str(e)}"
    
    def add_ads_to_html_files(self) -> List[str]:
        """Add advertisement placeholders to all HTML files in parallel."""
        if not self.repo_path:
            raise ValueError("Repository path not set. Run clone_repository() first.")
        
        html_files = glob.glob(f"{self.repo_path}/**/*.html", recursive=True)
        modified_files = []
        
        if not html_files:
            logger.warning("No HTML files found in repository")
            return modified_files
        
        logger.info(f"Found {len(html_files)} HTML files to process")
        
        # Process files in parallel using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            results = list(executor.map(self.process_html_file, html_files))
        
        # Process results
        for success, result in results:
            if success:
                modified_files.append(result)
                logger.info(f"Successfully modified: {result}")
            else:
                logger.error(result)
        
        logger.info(f"Modified {len(modified_files)} out of {len(html_files)} files")
        return modified_files

def main():
    """Main execution function."""
    try:
        # Get repository URL from command line argument
        git_url = sys.argv[1] if len(sys.argv) > 1 else None
        
        # Initialize and run the modifier
        modifier = WebsiteTemplateModifier(git_url)
        
        logger.info("Starting website template modification process")
        
        # Clone repository
        repo_path = modifier.clone_repository()
        logger.info(f"Repository cloned to: {repo_path}")
        
        # Add ads to HTML files
        modified_files = modifier.add_ads_to_html_files()
        
        if not modified_files:
            logger.error("No files were modified")
            sys.exit(1)
        
        logger.info("Process completed successfully!")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Process failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
