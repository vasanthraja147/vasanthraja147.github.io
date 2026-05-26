import os
import shutil

# Directories
os.makedirs('assets/images/projects', exist_ok=True)
os.makedirs('assets/images/brand', exist_ok=True)
os.makedirs('assets/docs', exist_ok=True)

# Define moves
moves = {
    'Vasanthkumar_R_Resume.pdf': 'assets/docs/Vasanthkumar_R_Resume.pdf',
    'about-photo.png': 'assets/images/brand/about-photo.png',
    'profile.png': 'assets/images/brand/profile.png',
    'favicon.png': 'assets/images/brand/favicon.png',
    'og-preview.png': 'assets/images/brand/og-preview.png',
    'freelance-icon.png': 'assets/images/brand/freelance-icon.png',
    'github-avatar.png': 'assets/images/brand/github-avatar.png',
    'infosys-logo.png': 'assets/images/brand/infosys-logo.png',
}

project_folders = [
    'Crop-Yield-optimization-',
    'E-Commerce-platform-for-Home-cleaning-Product',
    'Face Recognition Attendance System using faceNet',
    'Face recognition attendance system using opencv',
    'Intrusion-Detection-system for Home',
    'Personal-Healthcare-Records-with-Medication-Tracker',
    'Quantum-based-Satellite-Land-Monitoring-System'
]

for folder in project_folders:
    if os.path.exists(folder):
        shutil.move(folder, f'assets/images/projects/{folder}')

for src, dst in moves.items():
    if os.path.exists(src):
        shutil.move(src, dst)

# Update HTML files
def update_html(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace simple image/pdf paths
    for src, dst in moves.items():
        content = content.replace(f'href="{src}"', f'href="{dst}"')
        content = content.replace(f'src="{src}"', f'src="{dst}"')
        content = content.replace(f'content="{src}"', f'content="{dst}"')
        
    # Replace project folder paths
    for folder in project_folders:
        content = content.replace(f'src="{folder}/', f'src="assets/images/projects/{folder}/')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_html('index.html')
update_html('404.html')

# Update robots.txt (if it has project paths)
if os.path.exists('robots.txt'):
    with open('robots.txt', 'r', encoding='utf-8') as f:
        r = f.read()
    for folder in project_folders:
        r = r.replace(f'/{folder}/', f'/assets/images/projects/{folder}/')
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(r)
