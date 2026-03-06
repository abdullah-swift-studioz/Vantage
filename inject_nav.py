import os
import re

# Configuration
ROOT_DIR = '/Users/abdullah/Downloads/vantage'
EXCLUDE_DIRS = ['.git', '.gemini', 'images', 'css', 'js']

def get_relative_path(current_file, target_path):
    """Calculates relative path from current_file to target_path."""
    curr_dir = os.path.dirname(current_file)
    return os.path.relpath(target_path, curr_dir)

def generate_nav_html(root_rel):
    """Generates the HTML string for the navigation bar."""
    
    # helper for clean paths
    def link(path):
        return os.path.join(root_rel, path)

    # Dynamic Lists (Hardcoded based on requirements/knowledge to ensure correct ordering/naming if needed, 
    # but script logic below could scan folders too. For reliability in this specific task, scanning is better 
    # to catch 'ALL' files as requested.)
    
    # Scan for Services
    services_dir = os.path.join(ROOT_DIR, 'services')
    services_links = []
    if os.path.exists(services_dir):
        for f in sorted(os.listdir(services_dir)):
            if f.endswith('.html'):
                name = f.replace('.html', '').replace('-', ' ').title()
                # Special casing names if needed
                if name == "Fao Review": name = "FAO Review"
                services_links.append(f'<a href="{link(f"services/{f}")}" class="dropdown-link">{name}</a>')
                
    # Scan for Countries
    countries_dir = os.path.join(ROOT_DIR, 'countries')
    countries_links = []
    if os.path.exists(countries_dir):
        for f in sorted(os.listdir(countries_dir)):
            if f.endswith('.html'):
                name = f.replace('.html', '').replace('-', ' ').title()
                # Special casing
                if name == "Uae": name = "UAE"
                if name == "Uk": name = "UK"
                if name == "Usa": name = "USA"
                countries_links.append(f'<a href="{link(f"countries/{f}")}" class="dropdown-link">{name}</a>')

    service_items_html = '\n'.join(services_links)
    country_items_html = '\n'.join(countries_links)
    
    # Mobile versions
    service_items_mobile = service_items_html.replace('dropdown-link', 'mobile-sub-link')
    country_items_mobile = country_items_html.replace('dropdown-link', 'mobile-sub-link')

    html = f'''
    <!-- NAVIGATION START -->
    <nav class="vantage-navbar">
        <div class="nav-wrapper">
            <a href="{link('index.html')}" class="nav-brand">Vantage Education</a>
            
            <!-- Desktop Menu -->
            <ul class="desktop-nav">
                <li class="nav-item">
                    <a href="{link('index.html')}" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">Services <span class="nav-arrow">▼</span></a>
                    <div class="dropdown-menu">
                        {service_items_html}
                    </div>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">Countries <span class="nav-arrow">▼</span></a>
                    <div class="dropdown-menu">
                        {country_items_html}
                    </div>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">About <span class="nav-arrow">▼</span></a>
                    <div class="dropdown-menu">
                        <a href="{link('about.html')}" class="dropdown-link">About Us</a>
                        <a href="{link('mission-vision.html')}" class="dropdown-link">Mission & Vision</a>
                    </div>
                </li>
                <li>
                    <a href="{link('contact.html')}" class="nav-cta-btn">Contact</a>
                </li>
            </ul>

            <!-- Mobile Trigger -->
            <button class="mobile-toggle" onclick="toggleMobileMenu()">
                <div class="hamburger"></div>
            </button>
        </div>
    </nav>

    <!-- Mobile Menu Overlay -->
    <div class="mobile-menu-container" id="mobileMenu">
        <div class="mobile-menu-header">
            <a href="{link('index.html')}" class="mobile-menu-logo">
                <span>Vantage</span>
                <span>Education</span>
            </a>
            <button class="mobile-toggle" onclick="toggleMobileMenu()">
                <div class="hamburger"></div>
            </button>
        </div>
        
        <ul class="mobile-nav-list">
            <li class="mobile-nav-item">
                <a href="{link('index.html')}" class="mobile-link">Home</a>
            </li>
            <li class="mobile-nav-item">
                <button class="mobile-dropdown-trigger mobile-link" onclick="toggleAccordion('mobileServices')">
                    Services <span class="mobile-arrow">▼</span>
                </button>
                <div id="mobileServices" class="mobile-dropdown-content">
                    {service_items_mobile}
                </div>
            </li>
             <li class="mobile-nav-item">
                <button class="mobile-dropdown-trigger mobile-link" onclick="toggleAccordion('mobileCountries')">
                    Countries <span class="mobile-arrow">▼</span>
                </button>
                <div id="mobileCountries" class="mobile-dropdown-content">
                    {country_items_mobile}
                </div>
            </li>
            <li class="mobile-nav-item">
                <button class="mobile-dropdown-trigger mobile-link" onclick="toggleAccordion('mobileAbout')">
                    About <span class="mobile-arrow">▼</span>
                </button>
                <div id="mobileAbout" class="mobile-dropdown-content">
                    <a href="{link('about.html')}" class="mobile-sub-link">About Us</a>
                    <a href="{link('mission-vision.html')}" class="mobile-sub-link">Mission & Vision</a>
                </div>
            </li>
            <li class="mobile-nav-item">
                <a href="{link('contact.html')}" class="mobile-link">Contact</a>
            </li>
        </ul>
    </div>
    <!-- NAVIGATION END -->
    '''
    return html

def inject_nav():
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                # Calculate relative path to root for links
                rel_to_root = os.path.relpath(ROOT_DIR, root)
                if rel_to_root == '.':
                    rel_to_root = ''
                else:
                    rel_to_root += '/'
                
                # Generate Nav HTML
                nav_html = generate_nav_html(rel_to_root)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove existing nav if present (simple regex heuristic or just ensure we don't duplicate)
                # "The previous navigation bar has been completely removed" - user said this.
                # However, to be safe against re-runs, let's remove our own marker if it exists.
                content = re.sub(r'<!-- NAVIGATION START -->.*?<!-- NAVIGATION END -->', '', content, flags=re.DOTALL)
                
                # Inject at start of body
                if '<body>' in content:
                    new_content = content.replace('<body>', '<body>' + nav_html, 1)
                else:
                    # Fallback if no body tag found (unlikely)
                    new_content = nav_html + content
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"Injected nav into: {file}")
                count += 1
                
    print(f"Total files updated: {count}")

if __name__ == '__main__':
    inject_nav()
