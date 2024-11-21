#!/bin/bash

# Ensure that the repository was cloned correctly.
if [ ! -d "website-templates" ]; then
  echo "Repository not found! Make sure you've cloned the correct repository."
  exit 1
fi

# Change to the cloned repository folder
cd website-templates

# Define the HTML popup code (Telegram button)
POPUP_HTML='<div id="telegram-popup" style="position: fixed; bottom: 10px; right: 10px; z-index: 10000; background-color: #25d366; border-radius: 50%; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); cursor: pointer;">
  <a href="https://t.me/RektDevelopers" target="_blank" style="text-decoration: none; color: white; font-size: 30px;">
    <i class="fa fa-telegram"></i>
  </a>
</div>'

# Define the CSS styles for the popup
POPUP_CSS='<style>
  /* Popup Button Style */
  #telegram-popup {
    position: fixed;
    bottom: 10px;
    right: 10px;
    background-color: #25d366;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    cursor: pointer;
  }
  #telegram-popup a {
    text-decoration: none;
    color: white;
    font-size: 30px;
  }
</style>'

# Loop through all HTML files and insert the popup code.
find . -name "*.html" | while read file; do
  echo "Adding Telegram popup to $file..."
  
  # Check if Font Awesome is already included, if not, add it
  if ! grep -q "font-awesome" "$file"; then
    # Add Font Awesome to the <head> section of each HTML file if not already included
    sed -i 's/<head>/<head>\n  <link href="https:\/\/cdnjs.cloudflare.com\/ajax\/libs\/font-awesome\/6.0.0-beta3\/css\/all.min.css" rel="stylesheet">/' "$file"
  fi
  
  # Add the popup HTML and CSS before the closing </body> tag
  sed -i "/<\/body>/i $POPUP_HTML" "$file"
  sed -i "/<\/body>/i $POPUP_CSS" "$file"
done

echo "Popup successfully added to all HTML files in the repository!"
