import sys
import os
import git
from git.exc import GitCommandError
import subprocess

# Function to install required Python modules
def install_modules():
    try:
        print("Installing required Python modules...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gitpython"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing required modules: {e}")
        sys.exit(1)

# Function to remove old 'website-templates' folder and create a new one
def remove_and_create_folder(clone_dir='website-templates'):
    if os.path.exists(clone_dir):
        try:
            print(f"Removing old folder '{clone_dir}'...")
            # Remove the folder if it exists
            for root, dirs, files in os.walk(clone_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(clone_dir)  # Finally, remove the main directory
            print(f"Folder '{clone_dir}' removed successfully.")
        except OSError as e:
            print(f"Error removing folder: {e}")
            sys.exit(1)
    
    # Create the new folder
    try:
        print(f"Creating new folder '{clone_dir}'...")
        os.makedirs(clone_dir)  # Create the folder
        print(f"Folder '{clone_dir}' created successfully.")
    except OSError as e:
        print(f"Error creating folder: {e}")
        sys.exit(1)

# Function to clone the repository
def clone_repo(git_url, clone_dir='website-templates'):
    try:
        print(f"Cloning repository from {git_url} into '{clone_dir}'...")
        git.Repo.clone_from(git_url, clone_dir)
        print(f"Repository successfully cloned into '{clone_dir}'")
    except GitCommandError as e:
        print(f"Failed to clone repository: {e}")
        sys.exit(1)

# Function to add ads in all HTML files
def add_ads_to_html(clone_dir='website-templates'):
    ad_code = '''<script type="text/javascript" src="//pl25013478.profitablecpmrate.com/66/17/d7/6617d7163a895c776c2db7800c9d3306.js"></script>'''
    ad_code_2 = '''<a href="https://www.profitablecpmrate.com/tgzx4x7534?key=6ef5bb925723a00f5a280cee80cfc569" target="_blank">Direct Ad Link</a>'''
    ad_code_3 = '''<script type="text/javascript" src="//pl25032294.profitablecpmrate.com/0f/9f/9c/0f9f9c5c85bb14b4da3ce62b002175ec.js"></script>'''

    popup_ad_code = '''<script type="text/javascript">
        window.onload = function() {
            setTimeout(function() {
                var popup = window.open("https://t.me/RektDevelopers", "_blank", "width=600,height=400");
            }, 3000);  // Popup will show after 3 seconds
        };
    </script>'''

    # Add ads in HTML files
    for root, dirs, files in os.walk(clone_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    # Attempt to read the file with different encodings if necessary
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    # Insert the ad code before the closing </body> tag
                    if '</body>' in content:
                        content = content.replace('</body>', f'<!-- Ads Section -->\n{ad_code}\n{ad_code_2}\n{ad_code_3}\n{popup_ad_code}\n</body>')

                    # Write the modified content back to the file
                    with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
                        f.write(content)
                    print(f"Ads added to {file_path}")

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

# Main function to handle the full process
def main():
    # Git URL is passed from the GitHub Actions input or provided by the user
    git_url = sys.argv[1] if len(sys.argv) > 1 else "https://github.com/learning-zone/website-templates.git"
    
    # Step 1: Install required Python modules
    install_modules()

    # Step 2: Remove old folder (if exists) and create a new one
    remove_and_create_folder()

    # Step 3: Clone the repository
    clone_repo(git_url)

    # Step 4: Add ads to the HTML files
    add_ads_to_html()

if __name__ == "__main__":
    main()
