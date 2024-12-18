import os
import requests

# GitHub repository URL
REPO_URL = 'https://api.github.com/repos/Rekt-Developer/TemplatesX/contents/website-templates'
INDEX_FILE = 'index.html'

# Function to generate the HTML index file
def generate_index():
    # Fetch data from GitHub repository (list of subfolders in website-templates)
    response = requests.get(REPO_URL)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return
    
    templates = response.json()

    # Debugging: Print the fetched templates to understand the structure
    print(f"Fetched templates: {templates}")
    
    # HTML structure for the header
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Discover the best HTML5 templates, themes, and UI kits. Fork and contribute to awesome projects.">
        <meta name="author" content="Rekt-Developer">
        <meta property="og:title" content="Git Templates Marketplace">
        <meta property="og:description" content="Browse trending HTML5 templates, themes, UI kits, and more. Fork repositories directly from this page.">
        <meta property="og:image" content="https://placehold.it/1200x630">
        <meta property="og:url" content="https://github.com/Rekt-Developer/TemplatesX">
        <title>Git Templates Marketplace</title>
        <link rel="icon" href="favicon.ico" type="image/x-icon">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
        <style>
            body { font-family: 'Arial', sans-serif; background-color: #f4f4f9; margin: 0; padding: 0; }
            header { background-color: #2b2d42; color: white; text-align: center; padding: 30px 20px; }
            header h1 { margin: 0; font-size: 3rem; text-transform: uppercase; }
            header p { font-size: 1.1rem; margin-top: 10px; }
            .repo-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; padding: 20px; margin-top: 30px; }
            .repo-card { background: white; border-radius: 8px; box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1); overflow: hidden; transition: transform 0.3s ease; }
            .repo-card:hover { transform: scale(1.05); }
            .repo-card img { width: 100%; height: 200px; object-fit: cover; transition: opacity 0.3s ease-in-out; }
            .repo-card:hover img { opacity: 0.8; }
            .repo-info { padding: 15px; }
            .repo-info h3 { margin: 0; font-size: 1.5rem; color: #333; }
            .repo-info p { font-size: 1rem; color: #555; margin-top: 10px; }
            .repo-card button { background-color: #4CAF50; color: white; border: none; padding: 12px; width: 100%; font-size: 1.2rem; cursor: pointer; border-radius: 5px; margin-top: 15px; transition: background-color 0.3s ease; }
            .repo-card button:hover { background-color: #45a049; }
            footer { background-color: #2b2d42; color: white; padding: 15px; text-align: center; margin-top: 30px; }
            footer a { color: #FFB703; text-decoration: none; }
            /* Floating Telegram Popup */
            #telegram-popup { position: fixed; bottom: 10px; right: 10px; background-color: #25d366; border-radius: 50%; padding: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); cursor: pointer; z-index: 10000; }
            #telegram-popup a { color: white; font-size: 30px; text-decoration: none; }
        </style>
    </head>
    <body>
        <header>
            <h1>Git Templates Marketplace</h1>
            <p>Discover the best HTML5 templates, themes, and UI kits. Fork and contribute to the coolest projects!</p>
        </header>
        <div class="repo-container">
    '''

    # Loop through all subfolders (templates) and create cards for each one
    for template in templates:
        if isinstance(template, dict) and template.get('type') == 'dir':  # Filter only folders (not files)
            folder_name = template['name']
            folder_url = f"https://rekt-developer.github.io/TemplatesX/{folder_name}"
            # Placeholder for screenshot (you can add logic to fetch the screenshot if available)
            template_preview = f"https://rekt-developer.github.io/TemplatesX/{folder_name}/screenshot.jpg"
            
            html_content += f'''
            <div class="repo-card">
                <img src="{template_preview}" alt="{folder_name} Screenshot">
                <div class="repo-info">
                    <h3><a href="{folder_url}" target="_blank">{folder_name}</a></h3>
                    <p>Explore the HTML5 template {folder_name} for your next project!</p>
                    <button onclick="window.location.href='{folder_url}/fork'">Fork</button>
                </div>
            </div>
            '''

    # HTML footer and close tags
    html_content += '''
        </div>
        <div id="telegram-popup">
            <a href="https://t.me/RektDevelopers" target="_blank">
                <i class="fa fa-telegram"></i>
            </a>
        </div>
        <footer>
            <p>Managed by <a href="https://t.me/RektDevelopers" target="_blank">Rekt-Developers</a> | Join us on Telegram!</p>
        </footer>
    </body>
    </html>
    '''
    
    # Write the generated HTML to the index file
    with open(INDEX_FILE, 'w') as file:
        file.write(html_content)
    print("Index file generated successfully.")

if __name__ == '__main__':
    generate_index()
