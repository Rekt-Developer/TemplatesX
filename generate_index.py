import os
import shutil
import requests
from PIL import Image
from pathlib import Path

# Define paths
TEMPLATES_DIR = 'website-templates'
OUTPUT_DIR = 'generated_html'
SCREENSHOTS_DIR = os.path.join(OUTPUT_DIR, 'screenshots')
INDEX_FILE_PATH = os.path.join(OUTPUT_DIR, 'index.html')

# Ensure output directories exist
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Function to take screenshots (mock-up for the actual implementation)
def create_screenshot(template_path, screenshot_name):
    # Here, you would need to use a headless browser or tool to create real screenshots, like Selenium or Puppeteer.
    # For simplicity, we'll generate a placeholder screenshot using PIL (Python Imaging Library).
    img = Image.new('RGB', (300, 200), color = (73, 109, 137))
    img.save(os.path.join(SCREENSHOTS_DIR, screenshot_name))

# Function to generate the HTML content
def generate_html(templates):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Explore 150+ HTML5 templates and UI kits for your website projects.">
        <meta property="og:title" content="150+ HTML5 Website Templates">
        <meta property="og:description" content="Discover and download free HTML5 website templates and UI kits.">
        <meta property="og:image" content="generated_html/screenshots/preview.jpg">
        <meta property="og:url" content="https://github.com/Rekt-Developer/TemplatesX">
        <title>150+ HTML5 Website Templates</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f0f0f0; }
            header { background-color: #2b2d42; color: white; text-align: center; padding: 30px 0; }
            header h1 { margin: 0; }
            .template-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; padding: 20px; }
            .template-card { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); text-align: center; }
            .template-card img { width: 100%; height: auto; border-radius: 10px; }
            .template-card h3 { font-size: 1.25rem; margin: 15px 0 10px; }
            .template-card p { font-size: 1rem; margin: 10px 0; }
            .button { padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px; }
            .popup { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); justify-content: center; align-items: center; }
            .popup-content { background-color: white; padding: 20px; border-radius: 10px; text-align: center; }
            .popup-content a { color: #4CAF50; font-weight: bold; text-decoration: none; }
        </style>
    </head>
    <body>
    <header>
        <h1>150+ HTML5 Website Templates</h1>
    </header>
    <div class="template-container">
    """

    # Generate each template card in the grid
    for template in templates:
        template_name = template['name']
        template_path = template['path']
        screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{template_name}.jpg")
        
        # Generate the screenshot for the template
        create_screenshot(template_path, f"{template_name}.jpg")
        
        html_content += f"""
        <div class="template-card">
            <img src="{screenshot_path}" alt="{template_name}">
            <h3>{template_name}</h3>
            <p>Preview and Download this template.</p>
            <a href="https://github.com/learning-zone/website-templates/tree/main/{template_name}" class="button" target="_blank">Fork this Template</a>
        </div>
        """

    # Close the HTML content
    html_content += """
    </div>

    <!-- Popup for Telegram -->
    <div id="popup" class="popup">
        <div class="popup-content">
            <p>Join our community on <a href="https://t.me/RektDevelopers" target="_blank">Telegram</a>!</p>
            <button onclick="document.getElementById('popup').style.display='none'">Close</button>
        </div>
    </div>

    <script>
        // Show popup after 3 seconds
        setTimeout(function() {
            document.getElementById('popup').style.display = 'flex';
        }, 3000);
    </script>
    </body>
    </html>
    """
    
    # Write to the output file
    with open(INDEX_FILE_PATH, 'w') as f:
        f.write(html_content)
    print(f"Generated HTML file at {INDEX_FILE_PATH}")

# Main execution
if __name__ == "__main__":
    # Get the list of template folders in the cloned repo
    templates = []
    for template in os.listdir(TEMPLATES_DIR):
        template_path = os.path.join(TEMPLATES_DIR, template)
        if os.path.isdir(template_path):
            templates.append({'name': template, 'path': template_path})
    
    # Generate the index HTML
    generate_html(templates)
